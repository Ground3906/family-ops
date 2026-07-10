# setup-watcher-tasks.ps1 - Register inbox watcher and watchdog scheduled tasks.
#
# Run from Administrator PowerShell on ThinkPad:
#   Right-click PowerShell -> Run as administrator
#   cd "C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts"
#   .\setup-watcher-tasks.ps1
#
# Registers two tasks as SYSTEM:
#   BayerFamilyOps-InboxWatcher  - starts at boot, runs indefinitely, polls Inbox every 60 sec
#   BayerFamilyOps-Watchdog      - runs at 0800, 1400, 2000 daily
#
# IMPORTANT: Email alerts require Mail.Send on the Graph token.
# If you have not re-authorized since Mail.Send was added, run:
#   .\graph-auth.ps1
# and follow the browser prompt before running this script.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

# Admin check
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host ""
    Write-Host "ERROR: Must run as Administrator."
    Write-Host "Right-click PowerShell -> Run as administrator, then re-run."
    exit 1
}

$ScriptDir    = $PSScriptRoot
$WatcherPath  = Join-Path $ScriptDir "inbox-watcher.ps1"
$WatchdogPath = Join-Path $ScriptDir "watchdog.ps1"

if (-not (Test-Path $WatcherPath))  { Write-Host "ERROR: inbox-watcher.ps1 not found at $WatcherPath"; exit 1 }
if (-not (Test-Path $WatchdogPath)) { Write-Host "ERROR: watchdog.ps1 not found at $WatchdogPath"; exit 1 }

# ---------------------------------------------------------------
# TASK 1: BayerFamilyOps-InboxWatcher
# Boot trigger, 2-minute delay (allows OneDrive client to start first).
# No execution time limit (PT0S). Restarts up to 3 times on failure.
# ---------------------------------------------------------------
$watcherXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>Bayer Family Ops - polls Filing Cabinet Inbox for receipts and files them.</Description>
  </RegistrationInfo>
  <Triggers>
    <BootTrigger>
      <Delay>PT2M</Delay>
      <Enabled>true</Enabled>
    </BootTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-18</UserId>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Enabled>true</Enabled>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <RestartOnFailure>
      <Interval>PT5M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>powershell.exe</Command>
      <Arguments>-NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File &quot;$WatcherPath&quot;</Arguments>
    </Exec>
  </Actions>
</Task>
"@

# ---------------------------------------------------------------
# TASK 2: BayerFamilyOps-Watchdog
# Three daily triggers: 0800, 1400, 2000.
# 5-minute execution time limit. StartWhenAvailable catches a missed run.
# ---------------------------------------------------------------
$today       = (Get-Date).ToString("yyyy-MM-dd")
$watchdogXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>Bayer Family Ops - checks watcher heartbeat, disk space, and filing cabinet file count.</Description>
  </RegistrationInfo>
  <Triggers>
    <CalendarTrigger>
      <StartBoundary>${today}T08:00:00</StartBoundary>
      <ScheduleByDay><DaysInterval>1</DaysInterval></ScheduleByDay>
      <Enabled>true</Enabled>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>${today}T14:00:00</StartBoundary>
      <ScheduleByDay><DaysInterval>1</DaysInterval></ScheduleByDay>
      <Enabled>true</Enabled>
    </CalendarTrigger>
    <CalendarTrigger>
      <StartBoundary>${today}T20:00:00</StartBoundary>
      <ScheduleByDay><DaysInterval>1</DaysInterval></ScheduleByDay>
      <Enabled>true</Enabled>
    </CalendarTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-18</UserId>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <ExecutionTimeLimit>PT5M</ExecutionTimeLimit>
    <Enabled>true</Enabled>
    <StartWhenAvailable>true</StartWhenAvailable>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>powershell.exe</Command>
      <Arguments>-NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File &quot;$WatchdogPath&quot;</Arguments>
    </Exec>
  </Actions>
</Task>
"@

# ---------------------------------------------------------------
# REGISTER
# ---------------------------------------------------------------
Write-Host ""
Write-Host "Registering BayerFamilyOps-InboxWatcher..."
try {
    Register-ScheduledTask -TaskName "BayerFamilyOps-InboxWatcher" -Xml $watcherXml -Force | Out-Null
    Write-Host "  Registered."
} catch {
    Write-Host "  ERROR: $_"
    exit 1
}

Write-Host "Registering BayerFamilyOps-Watchdog..."
try {
    Register-ScheduledTask -TaskName "BayerFamilyOps-Watchdog" -Xml $watchdogXml -Force | Out-Null
    Write-Host "  Registered."
} catch {
    Write-Host "  ERROR: $_"
    exit 1
}

# Start the watcher immediately (does not wait for next boot)
Write-Host "Starting BayerFamilyOps-InboxWatcher..."
try {
    Start-ScheduledTask -TaskName "BayerFamilyOps-InboxWatcher"
    Write-Host "  Started."
} catch {
    Write-Host "  Warning: Could not start immediately. Will start at next boot."
    Write-Host "  Error: $_"
}

# ---------------------------------------------------------------
# RESULT + SMOKE TEST INSTRUCTIONS
# ---------------------------------------------------------------
$repoRoot    = Split-Path $ScriptDir -Parent
$receiptsLog = Join-Path $repoRoot "archive\receipts-log.jsonl"
$heartbeat   = Join-Path $repoRoot "archive\watcher-heartbeat.txt"

Write-Host ""
Write-Host "=== SETUP COMPLETE ==="
Write-Host ""
Write-Host "InboxWatcher: boot trigger, runs indefinitely, restarts up to 3x on failure."
Write-Host "Watchdog:     runs at 0800, 1400, 2000 daily."
Write-Host ""
Write-Host "--- SMOKE TEST ---"
Write-Host "1. Drop a test PDF into:"
Write-Host "   C:\Users\ThinkPad X1 Carbon\OneDrive\Filing Cabinet\Inbox"
Write-Host "2. Wait 60-90 seconds."
Write-Host "3. Verify it moves to Filing Cabinet root (Inbox should be empty)."
Write-Host "4. Check the JSONL log:"
Write-Host "   Get-Content '$receiptsLog' -Tail 5"
Write-Host "5. Check the heartbeat:"
Write-Host "   Get-Content '$heartbeat'"
Write-Host ""
Write-Host "--- VERIFY TASKS ---"
Write-Host "  Get-ScheduledTaskInfo -TaskName 'BayerFamilyOps-InboxWatcher'"
Write-Host "  Get-ScheduledTaskInfo -TaskName 'BayerFamilyOps-Watchdog'"
Write-Host ""
Write-Host "--- MAIL.SEND SCOPE ---"
Write-Host "Email alerts require Mail.Send on the Graph token."
Write-Host "If no alert emails arrive during testing, re-run:"
Write-Host "  .\graph-auth.ps1"
Write-Host "and sign in again when the browser opens. The new token will include Mail.Send."
Write-Host ""
