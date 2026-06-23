# setup-sync-task.ps1 - Register BayerFamilyOps-GraphSync scheduled task on ThinkPad.
# Run once on the ThinkPad. Open PowerShell as Administrator, then:
#   cd "C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts"
#   .\setup-sync-task.ps1
#
# Task runs graph-sync.ps1 every 3 min, hidden, as the current logged-in user.
# Re-run to update (Force flag overwrites existing registration).

$TaskName   = "BayerFamilyOps-GraphSync"
$ScriptPath = Join-Path $PSScriptRoot "graph-sync.ps1"

if (-not (Test-Path $ScriptPath)) {
    Write-Host "ERROR: graph-sync.ps1 not found at $ScriptPath"
    exit 1
}

Write-Host "Registering '$TaskName'..."
Write-Host "Script: $ScriptPath"
Write-Host ""

$Action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptPath`""

# Trigger: once (immediately), repeat every 3 min indefinitely
$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddSeconds(10)
$Trigger.Repetition.Interval = "PT3M"
$Trigger.Repetition.Duration = ""  # empty = indefinite

$Settings = New-ScheduledTaskSettingsSet `
    -MultipleInstances      IgnoreNew `
    -ExecutionTimeLimit     ([timespan]::FromMinutes(2)) `
    -StartWhenAvailable `
    -DontStopIfGoingOnBatteries `
    -RunOnlyIfNetworkAvailable

# Run as current interactive user - no password required on auto-login machine
$Principal = New-ScheduledTaskPrincipal `
    -UserId    "$env:USERDOMAIN\$env:USERNAME" `
    -LogonType Interactive `
    -RunLevel  Highest

Register-ScheduledTask `
    -TaskName   $TaskName `
    -Action     $Action `
    -Trigger    $Trigger `
    -Settings   $Settings `
    -Principal  $Principal `
    -Description "Bayer Family Ops: sync calendars.md to Outlook every 3 min." `
    -Force | Out-Null

Write-Host "Task registered. Firing first run now..."
Start-ScheduledTask -TaskName $TaskName

# Wait and check heartbeat
$hb = Join-Path $PSScriptRoot "graph-sync-heartbeat.txt"
$waited = 0
while (-not (Test-Path $hb) -and $waited -lt 30) {
    Start-Sleep -Seconds 2
    $waited += 2
    Write-Host "  ...waiting ($waited s)"
}

if (Test-Path $hb) {
    Write-Host ""
    Write-Host "=== SUCCESS ==="
    Write-Host "Heartbeat: $(Get-Content $hb)"
} else {
    Write-Host ""
    Write-Host "=== HEARTBEAT NOT YET WRITTEN ==="
    Write-Host "Check: $PSScriptRoot\graph-sync-error.log"
    Write-Host "Or run manually: powershell -File `"$ScriptPath`""
}

Write-Host ""
Write-Host "Verify task: Get-ScheduledTaskInfo -TaskName '$TaskName'"
Write-Host "Heartbeat:   $hb"
Write-Host "Revert log:  $(Join-Path $PSScriptRoot 'graph-sync-revert.log')"
