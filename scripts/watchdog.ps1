# watchdog.ps1 - Health checks for Bayer Family Ops automation layer.
# Runs at 0800, 1400, 2000 daily via BayerFamilyOps-Watchdog scheduled task.
# No in-script time gate: the schedule IS the window.
#
# Checks per run:
#   1. InboxWatcher staleness   - archive\watcher-heartbeat.txt         (6h threshold)
#   2. GraphSync staleness      - scripts\graph-sync-heartbeat.txt       (6h threshold)
#      EMAIL SUPPRESSED 2026-09-01 - see CHECK 2 block. Still logged and
#      still reported in ops\system-health.json. No mail is sent.
#   3. PullJob staleness        - last-pull.json                         (6h threshold)
#   4. NightWatch staleness     - archive\night-watch-heartbeat.txt     (25h threshold)
#   5. Disk free space          - C: drive below 75 GB
#   6. Filing Cabinet count     - root file count dropped
#   7. Pending arrivals count   - logs\receipts-index.jsonl vs logs\arrivals-processed.jsonl
#      (count only, no alert - rides the existing digest per Locked #5,
#      docs\document-pipeline-map.md: no per-arrival notifications)
#
# State persisted in archive\watchdog-state.json.
# Health snapshot written to ops\system-health.json (pushed to repo Sundays by WeeklyPush).
# All alerts via Microsoft Graph sendMail.
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
$OpsDir          = Join-Path $RepoRoot "ops"
$HeartbeatFile   = Join-Path $ArchiveDir "watcher-heartbeat.txt"
$GraphSyncHB     = Join-Path $ScriptDir "graph-sync-heartbeat.txt"
$PullJobSync     = Join-Path $RepoRoot "last-pull.json"
$NightWatchHB    = Join-Path $ArchiveDir "night-watch-heartbeat.txt"
$WatchdogState   = Join-Path $ArchiveDir "watchdog-state.json"
$WatchdogLog     = Join-Path $ArchiveDir "watchdog-log.jsonl"
$HealthFile      = Join-Path $OpsDir "system-health.json"
$ReceiptsIndex   = Join-Path $RepoRoot "logs\receipts-index.jsonl"
$ArrivalsProcessed = Join-Path $RepoRoot "logs\arrivals-processed.jsonl"
$CabinetRoot     = "C:\Users\ThinkPad X1 Carbon\OneDrive\Filing Cabinet"
$AlertTo         = "matthew.bayer@outlook.com"

# Thresholds
$InboxStalenessHours   = 6
$GraphSyncStalenessHours = 6
$PullJobStalenessHours = 6
$NightWatchStalenessHours = 25   # Only runs 21:30-06:00; max gap between nights is ~15.5h
$DiskThresholdGB       = 75

foreach ($d in @($ArchiveDir, $OpsDir)) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d | Out-Null }
}

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
# HEARTBEAT CHECK HELPER
# Returns age in hours, or -1 if file missing, -2 on parse error.
# ---------------------------------------------------------------
function Get-HeartbeatAgeHours {
    param([string]$FilePath)
    if (-not (Test-Path $FilePath)) { return -1 }
    try {
        $content = (Get-Content $FilePath -Raw -ErrorAction Stop).Trim()
        $ts      = [datetime]::Parse($content.Split(' ')[0])
        return ([datetime]::Now - $ts).TotalHours
    } catch { return -2 }
}

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
try {
    Write-Host "[watchdog] $(Get-Date -Format 'HH:mm:ss') Running checks..."

    $state = if (Test-Path $WatchdogState) {
        Get-Content $WatchdogState -Raw | ConvertFrom-Json
    } else {
        [PSCustomObject]@{ last_file_count = -1; last_run = $null }
    }

    $alerts = 0

    # Health snapshot - populated as checks run
    $health = @{
        last_updated = (Get-Date -Format 'o')
        checks       = @{
            inbox_watcher = @{ status = "unknown"; age_hours = $null }
            graph_sync    = @{ status = "unknown"; age_hours = $null }
            pull_job      = @{ status = "unknown"; age_hours = $null }
            night_watch   = @{ status = "unknown"; age_hours = $null }
        }
        disk_free_gb      = $null
        pending_arrivals  = $null
        total_alerts      = 0
    }

    # ------------------------------------------------------------------
    # CHECK 1: InboxWatcher heartbeat
    # ------------------------------------------------------------------
    $inboxAge = Get-HeartbeatAgeHours $HeartbeatFile
    if ($inboxAge -eq -1) {
        $msg = "Heartbeat file not found at $HeartbeatFile. InboxWatcher may never have started or crashed before first write."
        Write-Warning "[watchdog] $msg"
        Send-Alert "[FamilyOps] InboxWatcher: no heartbeat file" $msg
        Write-WatchdogLog "inbox_heartbeat_missing" "File not found"
        $health.checks.inbox_watcher.status = "missing"
        $alerts++
    } elseif ($inboxAge -eq -2) {
        Write-Warning "[watchdog] Could not parse InboxWatcher heartbeat."
        Write-WatchdogLog "inbox_heartbeat_parse_error" "Parse failed"
        $health.checks.inbox_watcher.status = "parse_error"
    } else {
        $health.checks.inbox_watcher.age_hours = [math]::Round($inboxAge, 2)
        Write-Host "[watchdog] InboxWatcher heartbeat age: $([math]::Round($inboxAge, 1))h"
        if ($inboxAge -gt $InboxStalenessHours) {
            $msg = "InboxWatcher heartbeat is $([math]::Round($inboxAge, 1))h old (threshold: $InboxStalenessHours h)."
            Send-Alert "[FamilyOps] InboxWatcher stale: check ThinkPad" $msg
            Write-WatchdogLog "inbox_heartbeat_stale" "Age: $([math]::Round($inboxAge, 2))h"
            $health.checks.inbox_watcher.status = "stale"
            $alerts++
        } else {
            Write-WatchdogLog "inbox_heartbeat_ok" "Age: $([math]::Round($inboxAge, 2))h"
            $health.checks.inbox_watcher.status = "ok"
        }
    }

    # ------------------------------------------------------------------
    # CHECK 2: GraphSync heartbeat
    #
    # EMAIL SUPPRESSED 2026-09-01 by Matt's direction.
    # The GraphSync heartbeat has been stale since 2026-06-24 because the
    # graph-sync.ps1 run does not reach its step 9 write. The alert was
    # correct but carried no new information and fired three times a day.
    # The check still runs, still logs, and still reports into
    # ops\system-health.json. Only the two Send-Alert calls are commented out.
    # Re-enable both lines once the graph-sync.ps1 fault is fixed.
    # ------------------------------------------------------------------
    $graphAge = Get-HeartbeatAgeHours $GraphSyncHB
    if ($graphAge -eq -1) {
        $msg = "GraphSync heartbeat not found at $GraphSyncHB. GraphSync task may not be running."
        Write-Warning "[watchdog] $msg"
        # Send-Alert "[FamilyOps] GraphSync: no heartbeat file" $msg
        Write-WatchdogLog "graph_sync_heartbeat_missing" "File not found (alert suppressed 2026-09-01)"
        $health.checks.graph_sync.status = "missing"
        $alerts++
    } elseif ($graphAge -eq -2) {
        Write-Warning "[watchdog] Could not parse GraphSync heartbeat."
        Write-WatchdogLog "graph_sync_heartbeat_parse_error" "Parse failed"
        $health.checks.graph_sync.status = "parse_error"
    } else {
        $health.checks.graph_sync.age_hours = [math]::Round($graphAge, 2)
        Write-Host "[watchdog] GraphSync heartbeat age: $([math]::Round($graphAge, 1))h"
        if ($graphAge -gt $GraphSyncStalenessHours) {
            $msg = "GraphSync heartbeat is $([math]::Round($graphAge, 1))h old (threshold: $GraphSyncStalenessHours h). Calendar sync may be down."
            Write-Warning "[watchdog] $msg"
            # Send-Alert "[FamilyOps] GraphSync stale: calendar sync may be down" $msg
            Write-WatchdogLog "graph_sync_stale" "Age: $([math]::Round($graphAge, 2))h (alert suppressed 2026-09-01)"
            $health.checks.graph_sync.status = "stale"
            $alerts++
        } else {
            Write-WatchdogLog "graph_sync_ok" "Age: $([math]::Round($graphAge, 2))h"
            $health.checks.graph_sync.status = "ok"
        }
    }

    # ------------------------------------------------------------------
    # CHECK 3: PullJob - reads last-pull.json {"last_ok": "YYYY-MM-DD HH:mm:ss"}
    # ------------------------------------------------------------------
    $pullAge = $null
    if (-not (Test-Path $PullJobSync)) {
        $msg = "last-pull.json not found at $PullJobSync. Pull job may never have succeeded."
        Write-Warning "[watchdog] $msg"
        Send-Alert "[FamilyOps] PullJob: no last-pull.json" $msg
        Write-WatchdogLog "pull_job_missing" "File not found"
        $health.checks.pull_job.status = "missing"
        $alerts++
    } else {
        try {
            $pj      = Get-Content $PullJobSync -Raw | ConvertFrom-Json
            $pjTime  = [datetime]::Parse($pj.last_ok)
            $pullAge = ([datetime]::Now - $pjTime).TotalHours
            $health.checks.pull_job.age_hours = [math]::Round($pullAge, 2)
            Write-Host "[watchdog] PullJob last-ok age: $([math]::Round($pullAge, 1))h"
            if ($pullAge -gt $PullJobStalenessHours) {
                $msg = "Pull job last success was $([math]::Round($pullAge, 1))h ago (threshold: $PullJobStalenessHours h). Cockpit may be serving stale data."
                Send-Alert "[FamilyOps] PullJob stale: Cockpit data may be old" $msg
                Write-WatchdogLog "pull_job_stale" "Age: $([math]::Round($pullAge, 2))h"
                $health.checks.pull_job.status = "stale"
                $alerts++
            } else {
                Write-WatchdogLog "pull_job_ok" "Age: $([math]::Round($pullAge, 2))h"
                $health.checks.pull_job.status = "ok"
            }
        } catch {
            Write-Warning "[watchdog] Could not parse last-pull.json: $_"
            Write-WatchdogLog "pull_job_parse_error" "$_"
            $health.checks.pull_job.status = "parse_error"
        }
    }

    # ------------------------------------------------------------------
    # CHECK 4: NightWatch heartbeat (25h threshold - only runs at night)
    # ------------------------------------------------------------------
    $nwAge = Get-HeartbeatAgeHours $NightWatchHB
    if ($nwAge -eq -1) {
        # FIX 2026-08-27: this case used to log "not_started" and send nothing, on the
        # assumption the task might not be registered yet. NightWatch is registered, so a
        # missing heartbeat now means the task is not running or the file was removed.
        # Alerts like every other check.
        $msg = "NightWatch heartbeat not found at $NightWatchHB. NightWatch task may not be running, or the heartbeat file was removed."
        Write-Warning "[watchdog] $msg"
        Send-Alert "[FamilyOps] NightWatch: no heartbeat file" $msg
        Write-WatchdogLog "night_watch_heartbeat_missing" "File not found"
        $health.checks.night_watch.status = "missing"
        $alerts++
    } elseif ($nwAge -eq -2) {
        Write-Warning "[watchdog] Could not parse NightWatch heartbeat."
        Write-WatchdogLog "night_watch_heartbeat_parse_error" "Parse failed"
        $health.checks.night_watch.status = "parse_error"
    } else {
        $health.checks.night_watch.age_hours = [math]::Round($nwAge, 2)
        Write-Host "[watchdog] NightWatch heartbeat age: $([math]::Round($nwAge, 1))h"
        if ($nwAge -gt $NightWatchStalenessHours) {
            $msg = "NightWatch heartbeat is $([math]::Round($nwAge, 1))h old (threshold: $NightWatchStalenessHours h). NightWatch task may have stopped."
            Send-Alert "[FamilyOps] NightWatch stale: task may be down" $msg
            Write-WatchdogLog "night_watch_stale" "Age: $([math]::Round($nwAge, 2))h"
            $health.checks.night_watch.status = "stale"
            $alerts++
        } else {
            Write-WatchdogLog "night_watch_ok" "Age: $([math]::Round($nwAge, 2))h"
            $health.checks.night_watch.status = "ok"
        }
    }

    # ------------------------------------------------------------------
    # CHECK 5: Disk free space on C:
    # ------------------------------------------------------------------
    try {
        $disk   = Get-PSDrive -Name C -ErrorAction Stop
        $freeGB = [math]::Round($disk.Free / 1GB, 2)
        $health.disk_free_gb = $freeGB
        Write-Host "[watchdog] C: free: $freeGB GB (threshold: $DiskThresholdGB GB)"
        if ($freeGB -lt $DiskThresholdGB) {
            $msg = "C: has $freeGB GB free. Threshold is $DiskThresholdGB GB. Check disk usage on ThinkPad before the archive is impacted."
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

    # ------------------------------------------------------------------
    # CHECK 6: Filing Cabinet root file count
    # ------------------------------------------------------------------
    try {
        $currentCount = (Get-ChildItem -LiteralPath $CabinetRoot -File -ErrorAction Stop).Count
        Write-Host "[watchdog] Filing Cabinet root: $currentCount files (last known: $($state.last_file_count))"
        if ($state.last_file_count -ge 0 -and $currentCount -lt $state.last_file_count) {
            $dropped = $state.last_file_count - $currentCount
            $msg     = "Filing Cabinet root dropped from $($state.last_file_count) to $currentCount files. $dropped file(s) missing. Check OneDrive - use Files Restore at onedrive.com if within 30 days."
            Send-Alert "[FamilyOps] Filing Cabinet: $dropped file(s) disappeared" $msg
            Write-WatchdogLog "file_count_dropped" "Was: $($state.last_file_count)  Now: $currentCount  Dropped: $dropped"
            $alerts++
        } else {
            Write-WatchdogLog "file_count_ok" "Count: $currentCount"
        }
        $state.last_file_count = $currentCount
    } catch {
        Write-Warning "[watchdog] File count check failed: $_"
        Write-WatchdogLog "file_count_error" "$_"
    }

    # ------------------------------------------------------------------
    # CHECK 7: Pending document-pipeline arrivals
    # Count only - no alert, no email of its own. Rides the existing digest.
    # Per docs\document-pipeline-map.md Locked #5, arrivals are caught by the
    # session-open hook, not by watcher/watchdog notification. This check does
    # not add a notification path - it adds visibility to the health snapshot
    # that already goes out three times a day for other reasons.
    # ------------------------------------------------------------------
    try {
        if (-not (Test-Path $ReceiptsIndex)) {
            Write-Host "[watchdog] Pending arrivals: receipts index not found yet."
            Write-WatchdogLog "pending_arrivals_no_index" "File not found: $ReceiptsIndex"
        } else {
            $indexed = @(Get-Content $ReceiptsIndex -ErrorAction Stop |
                Where-Object { $_.Trim() -ne "" } |
                ForEach-Object { (ConvertFrom-Json $_).filename })

            $processed = if (Test-Path $ArrivalsProcessed) {
                @(Get-Content $ArrivalsProcessed -ErrorAction Stop |
                    Where-Object { $_.Trim() -ne "" } |
                    ForEach-Object { (ConvertFrom-Json $_).filename })
            } else { @() }

            $pending = @($indexed | Where-Object { $_ -notin $processed })
            $health.pending_arrivals = $pending.Count
            Write-Host "[watchdog] Pending arrivals: $($pending.Count) (indexed: $($indexed.Count), processed: $($processed.Count))"
            Write-WatchdogLog "pending_arrivals_count" "Pending: $($pending.Count)  Indexed: $($indexed.Count)  Processed: $($processed.Count)"
        }
    } catch {
        Write-Warning "[watchdog] Pending arrivals check failed: $_"
        Write-WatchdogLog "pending_arrivals_error" "$_"
    }

    # ------------------------------------------------------------------
    # WRITE HEALTH SNAPSHOT
    # ------------------------------------------------------------------
    $health.total_alerts = $alerts
    $health | ConvertTo-Json -Depth 4 | Set-Content $HealthFile -Encoding UTF8
    Write-Host "[watchdog] system-health.json written."

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
