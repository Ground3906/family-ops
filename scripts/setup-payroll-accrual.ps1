# setup-payroll-accrual.ps1
# Registers BayerFamilyOps-PayrollAccrual on the ThinkPad. Run once, elevated.
# ASCII only - PowerShell 5.1

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

$trigger = New-ScheduledTaskTrigger -Monthly -DaysOfMonth 1 -At 6am

$principal = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest

# StartWhenAvailable is the point: if the ThinkPad is off or asleep on the
# 1st, the run happens when it next comes up rather than being skipped.
# Skipping is exactly how three months went missing.
$settings = New-ScheduledTaskSettingsSet `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
    -MultipleInstances IgnoreNew `
    -DontStopOnIdleEnd

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger `
    -Principal $principal -Settings $settings | Out-Null

Write-Host "Registered $TaskName" -ForegroundColor Green
Get-ScheduledTask -TaskName $TaskName | Select-Object TaskName, State
Write-Host ""
Write-Host "Dry run (safe - it will skip if this month is already accrued):"
Write-Host "  Start-ScheduledTask -TaskName $TaskName"
Write-Host "Then check:"
Write-Host "  Get-Content 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops\logs\payroll-accrual.log' -Tail 5"
