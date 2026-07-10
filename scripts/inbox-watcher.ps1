# inbox-watcher.ps1 - Receipt watcher for Bayer Family Ops.
# Polls Filing Cabinet\Inbox every 60 seconds for PDF and image files.
# Two-gate ready check: placeholder (not an OneDrive stub) + 15-second size stability.
# On clear: writes placeholder JSONL record to archive\receipts-log.jsonl, moves file to Cabinet root.
# Writes heartbeat to archive\watcher-heartbeat.txt on every cycle.
# Emails via Microsoft Graph on any processing failure.
# Runs as SYSTEM via BayerFamilyOps-InboxWatcher scheduled task (boot trigger, no time limit).
#
# NOTE: Email alerts require Mail.Send scope on the Graph token.
# If alerts are silent, re-run graph-auth.ps1 to re-authorize with Mail.Send.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------
$ClientId             = "eec121fa-f054-4214-af52-aa83371128ac"
$TokenUrl             = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
$ScriptDir            = $PSScriptRoot
$RepoRoot             = Split-Path $ScriptDir -Parent
$TokenFile            = Join-Path $ScriptDir "graph-token.json"
$OneDriveBase         = "C:\Users\ThinkPad X1 Carbon\OneDrive"
$InboxPath            = Join-Path $OneDriveBase "Filing Cabinet\Inbox"
$CabinetRoot          = Join-Path $OneDriveBase "Filing Cabinet"
$ArchiveDir           = Join-Path $RepoRoot "archive"
$ReceiptsLog          = Join-Path $ArchiveDir "receipts-log.jsonl"
$HeartbeatFile        = Join-Path $ArchiveDir "watcher-heartbeat.txt"
$ErrorLog             = Join-Path $ArchiveDir "watcher-error.log"
$AlertTo              = "matthew.bayer@outlook.com"
$PollIntervalSeconds  = 60
$SizeStabilitySeconds = 15
$ValidExtensions      = @('.pdf', '.jpg', '.jpeg', '.png')

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
        Write-Host "[watcher] Alert sent: $Subject"
    } catch {
        "$(Get-Date -Format 'o') ALERT-SEND-FAIL: $_" | Add-Content $ErrorLog -Encoding UTF8
    }
}

# ---------------------------------------------------------------
# GATE 1: FILE IS LOCAL (not an OneDrive cloud stub)
# FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS = 0x400000
# FILE_ATTRIBUTE_RECALL_ON_OPEN        = 0x040000
# Either flag set means file is not fully downloaded locally.
# ---------------------------------------------------------------
function Test-FileLocal {
    param([string]$Path)
    try {
        $attrs = [int](Get-Item $Path -ErrorAction Stop).Attributes
        return (($attrs -band 0x400000) -eq 0) -and (($attrs -band 0x040000) -eq 0)
    } catch { return $false }
}

# ---------------------------------------------------------------
# PROCESS ONE FILE
# ---------------------------------------------------------------
function Invoke-ProcessFile {
    param([string]$FilePath)
    $leaf = Split-Path $FilePath -Leaf
    $ext  = [System.IO.Path]::GetExtension($leaf).ToLower()

    Write-Host "[watcher] Processing: $leaf"

    # Gate 1: not a OneDrive stub. Poll up to 2 minutes.
    $gateAttempts = 0
    while (-not (Test-FileLocal $FilePath)) {
        $gateAttempts++
        if ($gateAttempts -gt 12) {
            Send-Alert "[FamilyOps] Watcher: placeholder timeout" `
                "File stuck as online-only stub after 2 min. Will retry next cycle. File: $leaf"
            return
        }
        Write-Host "[watcher] Gate 1: waiting for OneDrive download ($gateAttempts/12)..."
        Start-Sleep -Seconds 10
    }

    # Gate 2: size stable over 15 seconds.
    $s1 = 0
    $s2 = 0
    try {
        $s1 = (Get-Item $FilePath -ErrorAction Stop).Length
        if ($s1 -eq 0) {
            Write-Warning "[watcher] Zero-byte file: $leaf. Skipping."
            return
        }
        Start-Sleep -Seconds $SizeStabilitySeconds
        $s2 = (Get-Item $FilePath -ErrorAction Stop).Length
        if ($s1 -ne $s2) {
            Write-Warning "[watcher] Size unstable for $leaf ($s1 -> $s2). Deferring to next cycle."
            return
        }
    } catch {
        Write-Warning "[watcher] Size check error for $leaf`: $_"
        return
    }

    # Determine destination path. Stamp if name collision.
    $dest = Join-Path $CabinetRoot $leaf
    if (Test-Path $dest) {
        $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
        $base  = [System.IO.Path]::GetFileNameWithoutExtension($leaf)
        $dest  = Join-Path $CabinetRoot "$base-$stamp$ext"
    }

    # Write JSONL record.
    try {
        $record = [ordered]@{
            ts              = (Get-Date -Format 'o')
            filename        = $leaf
            size_bytes      = $s2
            file_type       = $ext.TrimStart('.')
            source_path     = $FilePath
            dest_path       = $dest
            extracted_facts = [ordered]@{}
        } | ConvertTo-Json -Compress -Depth 3
        Add-Content -Path $ReceiptsLog -Value $record -Encoding UTF8
    } catch {
        Send-Alert "[FamilyOps] Watcher: log write failed" "Could not write JSONL for $leaf`: $_"
        return
    }

    # Move to Filing Cabinet root.
    try {
        Move-Item -LiteralPath $FilePath -Destination $dest -ErrorAction Stop
        Write-Host "[watcher] Filed: $leaf -> $(Split-Path $dest -Leaf)"
    } catch {
        Send-Alert "[FamilyOps] Watcher: move failed" "Could not move $leaf to cabinet root: $_"
    }
}

# ---------------------------------------------------------------
# MAIN POLLING LOOP
# ---------------------------------------------------------------
try {
    Write-Host "[watcher] $(Get-Date -Format 'HH:mm:ss') Starting."
    Write-Host "[watcher] Inbox:   $InboxPath"
    Write-Host "[watcher] Cabinet: $CabinetRoot"

    if (-not (Test-Path $InboxPath)) { throw "Inbox path not found: $InboxPath" }

    while ($true) {
        try {
            $files = Get-ChildItem -LiteralPath $InboxPath -File -ErrorAction SilentlyContinue |
                Where-Object {
                    ($ValidExtensions -contains $_.Extension.ToLower()) -and
                    ($_.Name -notlike '~$*') -and
                    ($_.Name -notlike '*.tmp')
                }
            foreach ($f in $files) {
                try {
                    Invoke-ProcessFile $f.FullName
                } catch {
                    $msg = "$(Get-Date -Format 'o') ERROR on $($f.Name): $_"
                    $msg | Add-Content $ErrorLog -Encoding UTF8
                    try { Send-Alert "[FamilyOps] Watcher: unhandled error" $msg } catch {}
                }
            }
        } catch {
            "$(Get-Date -Format 'o') POLL-ERROR: $_" | Add-Content $ErrorLog -Encoding UTF8
        }

        # Heartbeat: written on every cycle regardless of file activity.
        "$(Get-Date -Format 'o') OK" | Set-Content $HeartbeatFile -Encoding UTF8
        Start-Sleep -Seconds $PollIntervalSeconds
    }

} catch {
    $fatal = "$(Get-Date -Format 'o') FATAL: $_"
    Write-Warning $fatal
    $fatal | Add-Content $ErrorLog -Encoding UTF8
    try { Send-Alert "[FamilyOps] Watcher FATAL: script stopped" $fatal } catch {}
    exit 1
}
