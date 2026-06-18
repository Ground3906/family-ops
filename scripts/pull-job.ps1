# pull-job.ps1 — Cockpit git pull heartbeat
# Runs via Task Scheduler every 3 min. Pulls family-ops repo. Logs result.
# On success, writes last-pull.json for Cockpit sync footer.

$RepoPath  = "C:\Users\ThinkPad X1 Carbon\Documents\family-ops"
$LogFile   = "$RepoPath\logs\pull-heartbeat.log"
$SyncFile  = "$RepoPath\last-pull.json"
$MaxLines  = 500
$Timestamp = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")

if (-not (Test-Path (Split-Path $LogFile))) {
    New-Item -ItemType Directory -Path (Split-Path $LogFile) | Out-Null
}

$net = Test-Connection -ComputerName github.com -Count 1 -Quiet -ErrorAction SilentlyContinue
if (-not $net) {
    Add-Content -Path $LogFile -Value "[$Timestamp] SKIP - no network"
} else {
    $result = & git -C $RepoPath pull 2>&1
    $exit   = $LASTEXITCODE
    if ($exit -eq 0) {
        Add-Content -Path $LogFile -Value "[$Timestamp] OK"
        Set-Content -Path $SyncFile -Value "{`"last_ok`": `"$Timestamp`"}" -Encoding UTF8
    } else {
        Add-Content -Path $LogFile -Value "[$Timestamp] FAIL (exit $exit) - $($result -join ' | ')"
    }
}

if (Test-Path $LogFile) {
    $lines = Get-Content $LogFile
    if ($lines.Count -gt $MaxLines) {
        $lines | Select-Object -Last $MaxLines | Set-Content $LogFile
    }
}
