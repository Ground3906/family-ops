# setup-payroll-write.ps1
# Run once on ThinkPad as Administrator to register the payroll write listener.
# ASCII only - PowerShell 5.1

$ScriptPath = 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts\payroll-write.ps1'
$TaskName   = 'BayerFamilyOps-PayrollWrite'

$action  = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NonInteractive -ExecutionPolicy Bypass -File `"$ScriptPath`""

# Startup trigger with 3-minute delay to ensure network is up
$trigger = New-ScheduledTaskTrigger -AtStartup
$trigger.Delay = 'PT3M'

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit ([TimeSpan]::Zero) `
    -RestartCount 5 `
    -RestartInterval (New-TimeSpan -Minutes 2) `
    -StartWhenAvailable

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -RunLevel Highest `
    -User 'SYSTEM' `
    -Force

Write-Host "Task '$TaskName' registered. Starting now..."
Start-ScheduledTask -TaskName $TaskName
Write-Host "Done. Verify with: Get-ScheduledTask -TaskName '$TaskName' | Select State"
