# night-watch.ps1 — LAN activity monitor, night window 21:30–06:00
# Runs every 5 min via BayerFamilyOps-NightWatch Task Scheduler task.
#
# BASELINE MODE: logs all unknown-device activity. No alerts, no digest.
# Thresholds and digest added after Chromebook baseline week completes.
#
# Observation types written to night-watch.jsonl:
#   blip    — device seen in < 3 consecutive 5-min checks (< 15 min sustained)
#   session — device seen in 3+ consecutive checks (>= 15 min sustained)
#   error   — scan failure
#
# Output files (local to ThinkPad — pushed to repo weekly by WeeklyPush):
#   archive\night-watch-heartbeat.txt   — last-run timestamp (read by Watchdog)
#   archive\night-watch-session.json    — inter-run session tracking state
#   logs\night-watch.jsonl              — observation log

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------
# TIME GATE
# ThinkPad must be set to Mountain Time (US & Canada) in Windows.
# Window: 21:30 to 06:00 the next morning.
# ---------------------------------------------------------------
$NowLocal    = [DateTime]::Now
$TimeVal     = $NowLocal.Hour * 60 + $NowLocal.Minute
$WindowStart = 21 * 60 + 30   # 1290
$WindowEnd   =  6 * 60 +  0   # 360

$inWindow = ($TimeVal -ge $WindowStart) -or ($TimeVal -lt $WindowEnd)
if (-not $inWindow) { exit 0 }

# ---------------------------------------------------------------
# PATHS
# ---------------------------------------------------------------
$ScriptDir     = $PSScriptRoot
$RepoRoot      = Split-Path $ScriptDir -Parent
$ArchiveDir    = Join-Path $RepoRoot "archive"
$LogDir        = Join-Path $RepoRoot "logs"
$HeartbeatFile = Join-Path $ArchiveDir "night-watch-heartbeat.txt"
$NightLog      = Join-Path $LogDir "night-watch.jsonl"
$SessionFile   = Join-Path $ArchiveDir "night-watch-session.json"

foreach ($d in @($ArchiveDir, $LogDir)) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d | Out-Null }
}

# ---------------------------------------------------------------
# KNOWN-GOOD DEVICES — never log these
# KnownMacs: Starlink hardware (confirmed from Starlink app)
# KnownHostPatterns: household workstations (matched against DNS hostname)
# Add household device MACs here after baseline week identifies them.
# ---------------------------------------------------------------
$KnownMacs = @(
    "74:24:9f:b9:eb:5f"   # Starlink Main Router
    "74:24:9f:a9:c7:df"   # Starlink Mesh Node
)
$KnownHostPatterns = @("thinkpad", "strayhawk", "precision", "mbay")

# ---------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------
function Write-NightLog {
    param([hashtable]$Record)
    ($Record | ConvertTo-Json -Compress) | Add-Content $NightLog -Encoding UTF8
}

# ---------------------------------------------------------------
# STAMP HEARTBEAT (always, even if scan finds nothing)
# ---------------------------------------------------------------
Set-Content $HeartbeatFile -Value ($NowLocal.ToString("o")) -Encoding UTF8

# ---------------------------------------------------------------
# LOAD SESSION STATE
# ---------------------------------------------------------------
$sessions = @{}
if (Test-Path $SessionFile) {
    try {
        $raw = Get-Content $SessionFile -Raw | ConvertFrom-Json
        foreach ($prop in $raw.PSObject.Properties) {
            $v = $prop.Value
            $sessions[$prop.Name] = @{
                count      = [int]$v.count
                first_seen = [string]$v.first_seen
                last_seen  = [string]$v.last_seen
                mac        = [string]$v.mac
                ip         = [string]$v.ip
                hostname   = [string]$v.hostname
            }
        }
    } catch { $sessions = @{} }
}

# ---------------------------------------------------------------
# ARP SCAN
# ---------------------------------------------------------------
try {
    $ts = $NowLocal.ToString("o")

    $neighbors = Get-NetNeighbor -State Reachable -ErrorAction SilentlyContinue |
                 Where-Object { $_.IPAddress -notmatch '^(169\.254|fe80|ff|224\.|239\.)' }

    $scanned = 0
    foreach ($n in $neighbors) {
        $mac = $n.LinkLayerAddress.ToLower() -replace '-', ':'
        $ip  = $n.IPAddress

        if ($mac -match '^(00:00:00|ff:ff:ff)') { continue }
        if ($KnownMacs -contains $mac) { continue }

        # Resolve hostname (best-effort)
        $hostname = ""
        try { $hostname = ([System.Net.Dns]::GetHostEntry($ip)).HostName } catch {}

        # Skip known workstations by hostname
        $skip = $false
        foreach ($pattern in $KnownHostPatterns) {
            if ($hostname -imatch $pattern) { $skip = $true; break }
        }
        if ($skip) { continue }

        # Session tracking
        $key  = $mac -replace ':', ''
        $prev = $sessions[$key]
        $continued = $prev -and
                     ([datetime]::Parse($prev.last_seen) -gt $NowLocal.AddMinutes(-10))

        if ($continued) {
            $count = $prev.count + 1
            $sessions[$key] = @{
                count      = $count
                first_seen = $prev.first_seen
                last_seen  = $ts
                mac        = $mac
                ip         = $ip
                hostname   = $hostname
            }
        } else {
            $count = 1
            $sessions[$key] = @{
                count      = 1
                first_seen = $ts
                last_seen  = $ts
                mac        = $mac
                ip         = $ip
                hostname   = $hostname
            }
        }

        $type = if ($count -ge 3) { "session" } else { "blip" }
        Write-NightLog @{
            ts         = $ts
            type       = $type
            mac        = $mac
            ip         = $ip
            hostname   = $hostname
            checks     = $count
            first_seen = $sessions[$key].first_seen
        }
        $scanned++
    }

    # Expire stale sessions (device not seen in 30 min)
    $cutoff  = $NowLocal.AddMinutes(-30)
    $expired = @($sessions.Keys | Where-Object {
        [datetime]::Parse($sessions[$_].last_seen) -lt $cutoff
    })
    foreach ($k in $expired) { $sessions.Remove($k) }

    # Persist session state
    $sessions | ConvertTo-Json -Depth 3 | Set-Content $SessionFile -Encoding UTF8

    Write-Host "[night-watch] $($NowLocal.ToString('HH:mm')) — Unknown devices logged: $scanned"

} catch {
    Write-Warning "[night-watch] Scan error: $_"
    Write-NightLog @{ ts = $NowLocal.ToString("o"); type = "error"; detail = "$_" }
    exit 1
}
