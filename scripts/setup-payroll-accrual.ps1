# setup-payroll-accrual.ps1
# Registers BayerFamilyOps-PayrollAccrual on the ThinkPad. Run once, elevated.
# ASCII only - PowerShell 5.1
#
# Trigger is DAILY, not monthly, on purpose.
#
# New-ScheduledTaskTrigger has no -Monthly parameter. Monthly schedules
# require raw MSFT_TaskTimeTrigger CIM instances or schtasks.exe, both of
# which are more fragile than the alternative.
#
# The alternative: payroll-accrual.ps1 already refuses to run twice in the
# same month. It checks lastAccrualMonth and exits if the month is done. So
# a daily trigger produces monthly behaviour, and it does something the
# monthly trigger could not: if the ThinkPad was off, asleep, or offline on
# the 1st, the next day it wakes up catches the accrual automatically.
#
# The guard is the schedule. The trigger just has to fire often enough to
# find it. That is one moving part instead of three.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

$TaskName = 'BayerFamilyOps-PayrollAccrual'
$Script   = 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts\payroll-accrual.ps1'

if (-not (Test-Path $Script)) {
    Write-Host "ERROR: $Script not found. Pull the repo first." -ForegroundColor Red
    exit 1
}

$existing = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Task already exists. Removing and re-registering."
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

$action = New-ScheduledTaskAction -Execute 'powershell.exe' `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Script`""

$trigger = New-ScheduledTaskTrigger -Daily -At 6am

$principal = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest

$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
    -MultipleInstances IgnoreNew `
    -DontStopOnIdleEnd

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger `
    -Principal $principal -Settings $settings | Out-Null

Write-Host "Registered $TaskName (daily 06:00, accrues once per month)" -ForegroundColor Green
Get-ScheduledTask -TaskName $TaskName | Select-Object TaskName, State
Write-Host ""
Write-Host "Dry run - safe. September is already accrued, so it should report SKIP:"
Write-Host "  Start-ScheduledTask -TaskName $TaskName"
Write-Host "Then check:"
Write-Host "  Get-Content 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops\logs\payroll-accrual.log' -Tail 5"
