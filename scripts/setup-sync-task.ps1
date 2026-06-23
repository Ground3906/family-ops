# setup-sync-task.ps1 - Register BayerFamilyOps-GraphSync scheduled task.
# Must run from an ADMINISTRATOR PowerShell on the ThinkPad:
#   Right-click PowerShell -> Run as administrator
#   cd "C:\Users\ThinkPad X1 Carbon\Documents\family-ops\scripts"
#   .\setup-sync-task.ps1
#
# Uses schtasks.exe (avoids PS version quirks with Trigger.Repetition).
# Runs as SYSTEM - no password prompt, always available on headless machine.
# Re-run anytime to update the registration.

$TaskName   = "BayerFamilyOps-GraphSync"
$ScriptPath = Join-Path $PSScriptRoot "graph-sync.ps1"

# --- Admin check ---
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host ""
    Write-Host "ERROR: This script must run as Administrator."
    Write-Host "Right-click PowerShell -> Run as administrator, then re-run."
    Write-Host ""
    exit 1
}

if (-not (Test-Path $ScriptPath)) {
    Write-Host "ERROR: graph-sync.ps1 not found at $ScriptPath"
    exit 1
}

Write-Host "Registering '$TaskName'..."
Write-Host "Script: $ScriptPath"
Write-Host ""

# Remove existing registration (ignore errors)
& schtasks /Delete /TN $TaskName /F 2>&1 | Out-Null

# Register: every 3 min, SYSTEM account, highest privilege
$TRCmd = "powershell.exe -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$ScriptPath`""

$out = & schtasks /Create `
    /TN $TaskName `
    /SC MINUTE /MO 3 `
    /TR $TRCmd `
    /RU SYSTEM `
    /RL HIGHEST `
    /F 2>&1

if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: schtasks /Create failed (exit $LASTEXITCODE):"
    Write-Host $out
    exit 1
}
Write-Host $out

# Fire first run immediately
Write-Host "Firing first run..."
& schtasks /Run /TN $TaskName | Out-Null

# Check heartbeat (allow up to 90 sec - first run after cleanup can take a while)
$hb     = Join-Path $PSScriptRoot "graph-sync-heartbeat.txt"
$before = Get-Date
$waited = 0
while ($waited -lt 90) {
    Start-Sleep -Seconds 3
    $waited += 3
    Write-Host "  ...waiting ($waited s)" -NoNewline
    if (Test-Path $hb) {
        $hbTs = [datetime]::Parse((Get-Content $hb -Raw).Split(' ')[0])
        if ($hbTs -gt $before) {
            Write-Host " - heartbeat written!"
            break
        }
    }
    Write-Host ""
}

Write-Host ""
if ((Test-Path $hb) -and ([datetime]::Parse((Get-Content $hb -Raw).Split(' ')[0]) -gt $before)) {
    Write-Host "=== SUCCESS ==="
    Write-Host "Heartbeat: $(Get-Content $hb)"
    Write-Host "Task is live. Runs every 3 min."
} else {
    Write-Host "=== HEARTBEAT NOT WRITTEN IN TIME ==="
    Write-Host "Check: $(Join-Path $PSScriptRoot 'graph-sync-error.log')"
    Write-Host "Or run manually: powershell -File `"$ScriptPath`""
}

Write-Host ""
Write-Host "Query task:  schtasks /Query /TN '$TaskName' /FO LIST"
Write-Host "Heartbeat:   $hb"
Write-Host "Revert log:  $(Join-Path $PSScriptRoot 'graph-sync-revert.log')"
