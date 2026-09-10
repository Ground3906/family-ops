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
#
# FIX 2026-08-21: origin was found pointed at HTTPS instead of the documented SSH
# deploy-key remote, which made every push under SYSTEM hang indefinitely rather than
# fail (no session to satisfy a credential prompt). Remote corrected to SSH. Separately,
# this run added ahead-of-origin recovery below: a run that commits successfully but
# then fails to push (as the HTTPS hang did) used to leave that commit stranded forever,
# because a later run with nothing new to stage never checked for it. See
# repo-write-discipline.md for the full incident.
#
# FIX 2026-09-09: every run from 2026-08-23 onward logged "FATAL: To github.com:..."
# and exited 1 while actually committing and pushing successfully. Cause: git writes
# push progress to stderr, `2>&1` turned those lines into error records, and
# $ErrorActionPreference = 'Stop' made the first one terminating. Control jumped to the
# catch block BEFORE the $LASTEXITCODE check on the next line ever ran. The exit-code
# checks in this script were always correct; they were simply unreachable. Git calls now
# route through Invoke-Git, which relaxes the preference for the duration of the call
# only, so cmdlets in this script still fail hard under 'Stop'. Note the first FATAL
# (2026-08-23) is the Sunday immediately after the 2026-08-21 SSH fix: pushes only began
# printing to stderr once they started working.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

$RepoRoot  = "C:\Users\ThinkPad X1 Carbon\Documents\family-ops"
$PushLog   = Join-Path $RepoRoot "logs\push-heartbeat.log"
$Timestamp = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
$GitExit   = 0

function Log { param([string]$msg)
    Add-Content -Path $PushLog -Value "[$Timestamp] $msg" -Encoding UTF8
}

# Run a git command without letting its stderr chatter terminate the script.
# Sets $script:GitExit to the real process exit code. Callers test $GitExit,
# never $LASTEXITCODE, because the pipeline may have moved on by then.
function Invoke-Git {
    param([string[]]$GitArgs)
    $prev = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $out = & git -C $RepoRoot @GitArgs 2>&1
        $script:GitExit = $LASTEXITCODE
        return $out
    } finally {
        $ErrorActionPreference = $prev
    }
}

try {
    $net = Test-Connection -ComputerName github.com -Count 1 -Quiet -ErrorAction SilentlyContinue
    if (-not $net) { Log "SKIP - no network"; exit 0 }

    # Pull first to avoid conflicts
    $pull = Invoke-Git @('pull')
    if ($GitExit -ne 0) { Log "PULL FAIL: $($pull -join ' | ')"; exit 1 }

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
            Invoke-Git @('add', $f) | Out-Null
            $staged++
        }
    }

    if ($staged -eq 0) { Log "Nothing to stage."; exit 0 }

    # Bail if nothing actually changed -- but first check for a stranded commit from a
    # prior run that committed successfully and then failed to push. Without this check,
    # a run with nothing new to stage exits here and a stuck commit sits forever.
    $diff = Invoke-Git @('diff', '--cached', '--stat')
    if (-not $diff) {
        $ahead = Invoke-Git @('rev-list', '--count', 'origin/main..HEAD')
        if ($GitExit -eq 0 -and $ahead -match '^\d+$' -and [int]$ahead -gt 0) {
            Log "No new changes, but $ahead unpushed commit(s) found -- pushing existing commits."
            $recoverPush = Invoke-Git @('push')
            if ($GitExit -ne 0) { Log "PUSH FAIL (recovery): $($recoverPush -join ' | ')"; exit 1 }
            Log "OK - recovered $ahead previously stuck commit(s)"
            exit 0
        }
        Log "No staged changes."
        exit 0
    }

    # Commit and push
    $week = Get-Date -Format "yyyy-MM-dd"
    Invoke-Git @('commit', '-m', "ops: weekly NightWatch push $week") | Out-Null
    if ($GitExit -ne 0) { Log "COMMIT FAIL"; exit 1 }

    $push = Invoke-Git @('push')
    if ($GitExit -ne 0) { Log "PUSH FAIL: $($push -join ' | ')"; exit 1 }

    Log "OK - pushed week of $week"
    Write-Host "[weekly-push] Done."

} catch {
    Log "FATAL (line $($_.InvocationInfo.ScriptLineNumber)): $_"
    exit 1
}
