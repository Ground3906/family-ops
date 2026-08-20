# weekly-push.ps1 - Weekly NightWatch log push to GitHub
# Runs Sundays 06:05 via BayerFamilyOps-WeeklyPush Task Scheduler task.
#
# Pushes:
#   logs\night-watch.jsonl        - week of LAN activity observations
#   ops\system-health.json        - latest Watchdog health snapshot
#   logs\receipts-index.jsonl     - lean receipt-arrival index, written locally all week
#                                    by inbox-watcher.ps1
#
# This is the mechanism by which Al reads NightWatch and receipt-arrival data for the
# weekly synthesis.
#
# PREREQUISITE: SYSTEM git auth via SSH deploy key, configured machine-wide on this box.
# See repo-write-discipline.md, "ThinkPad SYSTEM git authentication," for the full setup.
# Verify manually:
#   git -C "C:\Users\ThinkPad X1 Carbon\Documents\family-ops" push --dry-run
# before relying on this task.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

$RepoRoot  = "C:\Users\ThinkPad X1 Carbon\Documents\family-ops"
$PushLog   = Join-Path $RepoRoot "logs\push-heartbeat.log"
$Timestamp = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")

function Log { param([string]$msg)
    Add-Content -Path $PushLog -Value "[$Timestamp] $msg" -Encoding UTF8
}

try {
    $net = Test-Connection -ComputerName github.com -Count 1 -Quiet -ErrorAction SilentlyContinue
    if (-not $net) { Log "SKIP - no network"; exit 0 }

    # Pull first to avoid conflicts
    $pull = & git -C $RepoRoot pull 2>&1
    if ($LASTEXITCODE -ne 0) { Log "PULL FAIL: $($pull -join ' | ')"; exit 1 }

    # Stage files if they exist
    $filesToAdd = @(
        "logs\night-watch.jsonl"
        "ops\system-health.json"
        "logs\receipts-index.jsonl"
    )
    $staged = 0
    foreach ($f in $filesToAdd) {
        $full = Join-Path $RepoRoot $f
        if (Test-Path $full) {
            & git -C $RepoRoot add $f 2>&1 | Out-Null
            $staged++
        }
    }

    if ($staged -eq 0) { Log "Nothing to stage."; exit 0 }

    # Bail if nothing actually changed
    $diff = & git -C $RepoRoot diff --cached --stat 2>&1
    if (-not $diff) { Log "No staged changes."; exit 0 }

    # Commit and push
    $week = Get-Date -Format "yyyy-MM-dd"
    & git -C $RepoRoot commit -m "ops: weekly NightWatch push $week" 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) { Log "COMMIT FAIL"; exit 1 }

    $push = & git -C $RepoRoot push 2>&1
    if ($LASTEXITCODE -ne 0) { Log "PUSH FAIL: $($push -join ' | ')"; exit 1 }

    Log "OK - pushed week of $week"
    Write-Host "[weekly-push] Done."

} catch {
    Log "FATAL: $_"
    exit 1
}
