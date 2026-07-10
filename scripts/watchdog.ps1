# watchdog.ps1 - Health checks for Bayer Family Ops automation layer.
# Runs at 0800, 1400, 2000 daily via BayerFamilyOps-Watchdog scheduled task.
# No in-script time gate: the schedule IS the window.
#
# Three checks per run:
#   1. Watcher staleness: email if watcher-heartbeat.txt is older than 6 hours.
#   2. Disk free space:   email if C: drops below 75 GB free.
#   3. File count:        email if Filing Cabinet root loses files since last check.
#
# State persisted in archive\watchdog-state.json.
# All emails via Microsoft Graph sendMail.
#
# NOTE: Email alerts require Mail.Send scope on the Graph token.
# If alerts are silent, re-run graph-auth.ps1 to re-authorize with Mail.Send.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------
$ClientId        = "eec121fa-f054-4214-af52-aa83371128ac"
$TokenUrl        = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
$ScriptDir       = $PSScriptRoot
$RepoRoot        = Split-Path $ScriptDir -Parent
$TokenFile       = Join-Path $ScriptDir "graph-token.json"
$ArchiveDir      = Join-Path $RepoRoot "archive"
$HeartbeatFile   = Join-Path $ArchiveDir "watcher-heartbeat.txt"
$WatchdogState   = Join-Path $ArchiveDir "watchdog-state.json"
$WatchdogLog     = Join-Path $ArchiveDir "watchdog-log.jsonl"
$CabinetRoot     = "C:\Users\ThinkPad X1 Carbon\OneDrive\Filing Cabinet"
$AlertTo         = "matthew.bayer@outlook.com"
$StalenessHours  = 6
$DiskThresholdGB = 75

# Ensure archive directory exists
if (-not (Test-Path $ArchiveDir)) { New-Item -ItemType Directory -Path $ArchiveDir | Out-Null }

# ---------------------------------------------------------------
# GRAPH TOKEN
# ---------------------------------------------------------------
function Get-AccessToken {
    if (-not (Test-Path $TokenFile)) { throw "No token at $TokenFile. Run graph-auth.ps1." }
    $t = Get-Content $TokenFile -Raw | ConvertFrom-Json
    if ((Get-Date) -ge [datetime]::Parse($t.expires_at).AddMinutes(-5)) {
        $r = Invoke-RestMethod -Method Post -Uri $TokenUrl `
            -ContentType "application/x-www-form-urlencoded" `
            -Body @{
                grant_type    = "refresh_token"
                client_id     = $ClientId
                refresh_token = $t.refresh_token
                scope         = "Calendars.ReadWrite Mail.Send User.Read offline_access"
            }
        $newToken = @{
            access_token  = $r.access_token
            refresh_token = $r.refresh_token
            expires_at    = (Get-Date).AddSeconds([int]$r.expires_in).ToString("o")
        }
        $newToken | ConvertTo-Json | Set-Content $TokenFile -Encoding UTF8
        return $r.access_token
    }
    return $t.access_token
}

# ---------------------------------------------------------------
# GRAPH MAIL ALERT
# ---------------------------------------------------------------
function Send-Alert {
    param([string]$Subject, [string]$Body)
    try {
        $tok     = Get-AccessToken
        $payload = @{
            message = @{
                subject      = $Subject
                body         = @{ contentType = 'Text'; content = $Body }
                toRecipients = @(@{ emailAddress = @{ address = $AlertTo } })
            }
            saveToSentItems = $false
        } | ConvertTo-Json -Depth 6
        Invoke-RestMethod -Method Post `
            -Uri "https://graph.microsoft.com/v1.0/me/sendMail" `
            -Headers @{ Authorization = "Bearer $tok" } `
            -ContentType "application/json" -Body $payload | Out-Null
        Write-Host "[watchdog] Alert sent: $Subject"
    } catch {
        Write-Warning "[watchdog] Alert send failed: $_"
    }
}

# ---------------------------------------------------------------
# LOG HELPER
# ---------------------------------------------------------------
function Write-WatchdogLog {
    param([string]$Event, [string]$Detail)
    @{ ts = (Get-Date -Format 'o'); event = $Event; detail = $Detail } |
        ConvertTo-Json -Compress | Add-Content $WatchdogLog -Encoding UTF8
}

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
try {
    Write-Host "[watchdog] $(Get-Date -Format 'HH:mm:ss') Running checks..."

    # Load state
    $state = if (Test-Path $WatchdogState) {
        Get-Content $WatchdogState -Raw | ConvertFrom-Json
    } else {
        [PSCustomObject]@{ last_file_count = -1; last_run = $null }
    }

    $alerts = 0

    # Check 1: Watcher staleness
    if (-not (Test-Path $HeartbeatFile)) {
        $msg = "Heartbeat file not found at $HeartbeatFile. Watcher may never have started or crashed before first write."
        Write-Warning "[watchdog] $msg"
        Send-Alert "[FamilyOps] Watcher: no heartbeat file" $msg
        Write-WatchdogLog "heartbeat_missing" "File not found"
        $alerts++
    } else {
        try {
            $hbContent = (Get-Content $HeartbeatFile -Raw -ErrorAction Stop).Trim()
            $hbTime    = [datetime]::Parse($hbContent.Split(' ')[0])
            $ageHours  = ([datetime]::UtcNow - $hbTime.ToUniversalTime()).TotalHours
            Write-Host "[watchdog] Heartbeat age: $([math]::Round($ageHours, 1)) hours"
            if ($ageHours -gt $StalenessHours) {
                $msg = "Watcher heartbeat is $([math]::Round($ageHours, 1)) hours old (threshold: $StalenessHours h). Last beat: $hbContent"
                Send-Alert "[FamilyOps] Watcher stale: check ThinkPad" $msg
                Write-WatchdogLog "heartbeat_stale" "Age: $([math]::Round($ageHours, 2)) h"
                $alerts++
            } else {
                Write-WatchdogLog "heartbeat_ok" "Age: $([math]::Round($ageHours, 2)) h"
            }
        } catch {
            Write-Warning "[watchdog] Could not parse heartbeat file: $_"
            Write-WatchdogLog "heartbeat_parse_error" "$_"
        }
    }

    # Check 2: Disk free space on C:
    try {
        $disk   = Get-PSDrive -Name C -ErrorAction Stop
        $freeGB = [math]::Round($disk.Free / 1GB, 2)
        Write-Host "[watchdog] C: free: $freeGB GB (threshold: $DiskThresholdGB GB)"
        if ($freeGB -lt $DiskThresholdGB) {
            $msg = "C: has $freeGB GB free. Threshold is $DiskThresholdGB GB. Check what is consuming disk space on the ThinkPad before the archive is impacted."
            Send-Alert "[FamilyOps] Low disk: $freeGB GB free on ThinkPad" $msg
            Write-WatchdogLog "disk_low" "Free: $freeGB GB"
            $alerts++
        } else {
            Write-WatchdogLog "disk_ok" "Free: $freeGB GB"
        }
    } catch {
        Write-Warning "[watchdog] Disk check failed: $_"
        Write-WatchdogLog "disk_check_error" "$_"
    }

    # Check 3: Filing Cabinet root file count
    try {
        $currentCount = (Get-ChildItem -LiteralPath $CabinetRoot -File -ErrorAction Stop).Count
        Write-Host "[watchdog] Filing Cabinet root: $currentCount files (last known: $($state.last_file_count))"
        if ($state.last_file_count -ge 0 -and $currentCount -lt $state.last_file_count) {
            $dropped = $state.last_file_count - $currentCount
            $msg     = "Filing Cabinet root dropped from $($state.last_file_count) to $currentCount files. $dropped file(s) missing. Check OneDrive for deleted or moved items. If within 30 days, use Files Restore at onedrive.com."
            Send-Alert "[FamilyOps] Filing Cabinet: $dropped file(s) disappeared" $msg
            Write-WatchdogLog "file_count_dropped" "Was: $($state.last_file_count)  Now: $currentCount  Dropped: $dropped"
            $alerts++
        } else {
            Write-WatchdogLog "file_count_ok" "Count: $currentCount"
        }
        # Always update the stored count to current (even after a drop, so we track the new baseline)
        $state.last_file_count = $currentCount
    } catch {
        Write-Warning "[watchdog] File count check failed: $_"
        Write-WatchdogLog "file_count_error" "$_"
    }

    # Save state and log run
    $state.last_run = (Get-Date -Format 'o')
    $state | ConvertTo-Json | Set-Content $WatchdogState -Encoding UTF8
    Write-WatchdogLog "run_complete" "Alerts: $alerts"
    Write-Host "[watchdog] Done. Alerts sent: $alerts"

} catch {
    $fatal = "$(Get-Date -Format 'o') FATAL: $_"
    Write-Warning $fatal
    try { Send-Alert "[FamilyOps] Watchdog FATAL: check ThinkPad" $fatal } catch {}
    exit 1
}
