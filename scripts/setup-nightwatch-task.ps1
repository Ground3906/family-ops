# setup-nightwatch-task.ps1 — Register NightWatch and WeeklyPush tasks
# Run ONCE as Administrator on the ThinkPad.
# Both tasks run as SYSTEM.
#
# After registration, smoke-test:
#   Start-ScheduledTask -TaskName "BayerFamilyOps-NightWatch"
#   # Wait 30 seconds, then check:
#   Get-Content "C:\Users\ThinkPad X1 Carbon\Documents\family-ops\archive\night-watch-heartbeat.txt"
#
# WeeklyPush prerequisite: verify git push credentials first:
#   git -C "C:\Users\ThinkPad X1 Carbon\Documents\family-ops" push --dry-run

$ScriptDir = "C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts"
$TaskUser  = "SYSTEM"

# ---- TASK 1: BayerFamilyOps-NightWatch ----
# Runs every 5 minutes. Time gate (21:30-06:00) enforced inside the script.
$nwAction = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NonInteractive -ExecutionPolicy Bypass -File `"$ScriptDir\night-watch.ps1`""

$nwTrigger = New-ScheduledTaskTrigger `
    -RepetitionInterval (New-TimeSpan -Minutes 5) `
    -Once -At "00:00"

$nwSettings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 4) `
    -MultipleInstances IgnoreNew `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -StartWhenAvailable

Register-ScheduledTask `
    -TaskName "BayerFamilyOps-NightWatch" `
    -Action $nwAction `
    -Trigger $nwTrigger `
    -Settings $nwSettings `
    -RunLevel Highest `
    -User $TaskUser `
    -Force | Out-Null

Write-Host "[setup] BayerFamilyOps-NightWatch registered (every 5 min, time-gated 21:30-06:00)."

# ---- TASK 2: BayerFamilyOps-WeeklyPush ----
# Sundays at 06:05 — 5 minutes after NightWatch window closes at 06:00.
$wpAction = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NonInteractive -ExecutionPolicy Bypass -File `"$ScriptDir\weekly-push.ps1`""

$wpTrigger = New-ScheduledTaskTrigger `
    -Weekly -DaysOfWeek Sunday -At "06:05"

$wpSettings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10) `
    -MultipleInstances IgnoreNew `
    -StartWhenAvailable

Register-ScheduledTask `
    -TaskName "BayerFamilyOps-WeeklyPush" `
    -Action $wpAction `
    -Trigger $wpTrigger `
    -Settings $wpSettings `
    -RunLevel Highest `
    -User $TaskUser `
    -Force | Out-Null

Write-Host "[setup] BayerFamilyOps-WeeklyPush registered (Sundays 06:05)."
Write-Host ""
Write-Host "Smoke test NightWatch:"
Write-Host "  Start-ScheduledTask -TaskName 'BayerFamilyOps-NightWatch'"
Write-Host "  Start-Sleep 30"
Write-Host "  Get-Content '$ScriptDir\..\archive\night-watch-heartbeat.txt'"
