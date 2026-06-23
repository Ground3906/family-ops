# setup-sync-task.ps1 - Register BayerFamilyOps-GraphSync scheduled task.
# Run from Administrator PowerShell on ThinkPad:
#   Right-click PowerShell -> Run as administrator
#   cd "C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts"
#   .\setup-sync-task.ps1
#
# Uses Register-ScheduledTask -Xml to avoid schtasks.exe quoting issues
# with paths that contain spaces. Runs as SYSTEM (no password prompt).

$TaskName   = "BayerFamilyOps-GraphSync"
$ScriptPath = Join-Path $PSScriptRoot "graph-sync.ps1"

# --- Admin check ---
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host ""
    Write-Host "ERROR: Must run as Administrator."
    Write-Host "Right-click PowerShell -> Run as administrator, then re-run."
    exit 1
}

if (-not (Test-Path $ScriptPath)) {
    Write-Host "ERROR: graph-sync.ps1 not found at $ScriptPath"
    exit 1
}

Write-Host "Registering '$TaskName'..."
Write-Host "Script: $ScriptPath"
Write-Host ""

# Build Task XML directly.
# &quot; in XML element content decodes to " for Task Scheduler,
# which correctly quotes the path with spaces for PowerShell.
# S-1-5-18 = SYSTEM account (no password, always available headless).
$startTime = (Get-Date).AddSeconds(30).ToString("yyyy-MM-ddTHH:mm:ss")
$taskXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>Bayer Family Ops - sync calendars.md to Outlook every 3 min.</Description>
  </RegistrationInfo>
  <Triggers>
    <TimeTrigger>
      <Repetition>
        <Interval>PT3M</Interval>
        <StopAtDurationEnd>false</StopAtDurationEnd>
      </Repetition>
      <StartBoundary>$startTime</StartBoundary>
      <Enabled>true</Enabled>
    </TimeTrigger>
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
    <ExecutionTimeLimit>PT2M</ExecutionTimeLimit>
    <Enabled>true</Enabled>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <StartWhenAvailable>true</StartWhenAvailable>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>powershell.exe</Command>
      <Arguments>-NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File &quot;$ScriptPath&quot;</Arguments>
    </Exec>
  </Actions>
</Task>
"@

try {
    Register-ScheduledTask -TaskName $TaskName -Xml $taskXml -Force | Out-Null
    Write-Host "Task registered successfully."
} catch {
    Write-Host "ERROR registering task: $_"
    exit 1
}

Write-Host "Firing first run..."
try {
    Start-ScheduledTask -TaskName $TaskName
} catch {
    Write-Host "Warning: Could not fire immediate run: $_"
    Write-Host "Task is still registered and will fire at next 3-min interval."
}

# Wait for a fresh heartbeat (90 sec max - first run after rebuild takes ~60 sec)
$hb     = Join-Path $PSScriptRoot "graph-sync-heartbeat.txt"
$before = Get-Date
$waited = 0
Write-Host "Waiting for heartbeat..."
while ($waited -lt 90) {
    Start-Sleep -Seconds 3
    $waited += 3
    Write-Host "  ...($waited s)" -NoNewline
    if (Test-Path $hb) {
        try {
            $hbLine = (Get-Content $hb -Raw).Trim()
            $hbTs   = [datetime]::Parse($hbLine.Split(' ')[0])
            if ($hbTs -gt $before) { Write-Host " fresh!"; break }
        } catch { }
    }
    Write-Host ""
}

# Result
$fresh = $false
if (Test-Path $hb) {
    try {
        $hbLine = (Get-Content $hb -Raw).Trim()
        $hbTs   = [datetime]::Parse($hbLine.Split(' ')[0])
        $fresh  = ($hbTs -gt $before)
    } catch { }
}

Write-Host ""
if ($fresh) {
    Write-Host "=== SUCCESS ==="
    Write-Host "Heartbeat: $(Get-Content $hb -Raw)"
    Write-Host "Task is live. Runs every 3 min."
} else {
    Write-Host "=== NO FRESH HEARTBEAT YET ==="
    Write-Host "Task is registered. First SYSTEM run may take a few more minutes."
    Write-Host "Check: Get-Content '$hb'"
    Write-Host "Error: $(Join-Path $PSScriptRoot 'graph-sync-error.log')"
}

Write-Host ""
Write-Host "Query:     Get-ScheduledTaskInfo -TaskName '$TaskName'"
Write-Host "Heartbeat: $hb"
