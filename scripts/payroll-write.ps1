# payroll-write.ps1
# ThinkPad X1 Carbon - PowerShell 5.1 - ASCII only
# Listens on :8081. Receives POST /append, applies the operation against the
# CURRENT on-disk payroll-data.json, writes, commits and pushes.
#
# /append replaces the old /save endpoint. /save took the caller's whole
# in-memory copy of the ledger and wrote it over the file, so any writer
# holding a stale copy silently erased everything written since it loaded.
# /append never trusts the caller's copy: it re-reads from disk on every
# request and applies only the stated change. Two writers can no longer
# clobber each other.
#
# Accepted operation fields (all optional, combined in one request):
#   addEntries      array of ticket objects to prepend to entries
#   removeEntryIds  array of ticket ids to delete from entries
#   addLog          array of activity records to prepend to categories.log
#   totalsDelta     { kidId: { give, save, spend } } amounts to ADD to totals
#   setAccrualMonth "YYYY-MM"
#   setPayoutMonth  { kid, month }
#
# Git step checks the actual exit code of add/commit/push. The log only
# reports success when all three genuinely succeeded, tells a no-op apart
# from a real failure, and records the actual git error text.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

$RepoPath = 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops'
$DataPath = Join-Path $RepoPath 'payroll\payroll-data.json'
$LogPath  = Join-Path $RepoPath 'logs\payroll-write.log'
$Port     = 8081

# No BOM. The old script used [System.Text.Encoding]::UTF8, which emits one
# under .NET Framework and left a BOM on every save.
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Write-Log {
    param([string]$Msg)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$ts  $Msg" | Out-File -FilePath $LogPath -Append -Encoding ASCII
}

function Read-Ledger {
    if (-not (Test-Path $DataPath)) { return $null }
    $raw = [System.IO.File]::ReadAllText($DataPath)
    if ($raw.Length -gt 0 -and $raw[0] -eq [char]0xFEFF) { $raw = $raw.Substring(1) }
    if ($raw.Trim().Length -lt 2) { return $null }
    return $raw | ConvertFrom-Json
}

function Round2 { param($v) return [math]::Round([double]$v, 2) }

$null = New-Item -ItemType Directory -Path (Split-Path $LogPath) -Force

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://+:$Port/")

try {
    $listener.Start()
    Write-Log 'STARTED on port 8081 (append mode)'
} catch {
    Write-Log "FAILED to start listener: $_"
    exit 1
}

try {
    while ($listener.IsListening) {
        $ctx = $null
        try { $ctx = $listener.GetContext() } catch { Write-Log "GetContext error: $_"; continue }

        $req = $ctx.Request
        $res = $ctx.Response

        try {
            $res.AddHeader('Access-Control-Allow-Origin', '*')
            $res.AddHeader('Access-Control-Allow-Methods', 'POST, OPTIONS')
            $res.AddHeader('Access-Control-Allow-Headers', 'Content-Type')
        } catch {}

        if ($req.HttpMethod -eq 'OPTIONS') {
            $res.StatusCode = 200
            $res.Close()
            continue
        }

        # Old whole-file endpoint. Refused loudly on purpose. A cached copy of
        # the old page hitting this will show a save error rather than quietly
        # overwriting the ledger with whatever it loaded hours ago.
        if ($req.HttpMethod -eq 'POST' -and $req.Url.AbsolutePath -eq '/save') {
            $res.StatusCode = 410
            $res.Close()
            Write-Log 'Refused /save - caller is running a cached page, tell it to reload'
            continue
        }

        if ($req.HttpMethod -eq 'POST' -and $req.Url.AbsolutePath -eq '/append') {
            try {
                $reader = New-Object System.IO.StreamReader($req.InputStream, [System.Text.Encoding]::UTF8)
                $body   = $reader.ReadToEnd()
                $reader.Dispose()

                if ($body.Length -lt 2 -or $body.Trim()[0] -ne '{') {
                    $res.StatusCode = 400
                    $res.Close()
                    Write-Log 'Rejected: body did not look like JSON'
                    continue
                }

                $op = $body | ConvertFrom-Json

                # Fresh read every time. This is the whole point of the endpoint.
                $data = Read-Ledger
                if ($null -eq $data) {
                    $res.StatusCode = 500
                    $res.Close()
                    Write-Log 'Rejected: ledger on disk is missing or unreadable - refusing to create one from a caller payload'
                    continue
                }

                $changes = @()

                if ($op.PSObject.Properties.Name -contains 'addEntries' -and $op.addEntries) {
                    $incoming = @($op.addEntries)
                    $existing = @($data.entries | ForEach-Object { $_.id })
                    $added = 0
                    foreach ($e in $incoming) {
                        if ($existing -contains $e.id) { continue }
                        $data.entries = @($e) + @($data.entries)
                        $added++
                    }
                    if ($added -gt 0) { $changes += "add $added ticket(s)" }
                }

                if ($op.PSObject.Properties.Name -contains 'removeEntryIds' -and $op.removeEntryIds) {
                    $kill = @($op.removeEntryIds)
                    $before = @($data.entries).Count
                    $data.entries = @($data.entries | Where-Object { $kill -notcontains $_.id })
                    $gone = $before - @($data.entries).Count
                    if ($gone -gt 0) { $changes += "remove $gone ticket(s)" }
                }

                if ($op.PSObject.Properties.Name -contains 'addLog' -and $op.addLog) {
                    $logs = @($op.addLog)
                    $existing = @($data.categories.log | ForEach-Object { $_.id })
                    $added = 0
                    foreach ($l in $logs) {
                        if ($existing -contains $l.id) { continue }
                        $data.categories.log = @($l) + @($data.categories.log)
                        $added++
                    }
                    if ($added -gt 0) { $changes += "add $added activity record(s)" }
                }

                if ($op.PSObject.Properties.Name -contains 'totalsDelta' -and $op.totalsDelta) {
                    foreach ($p in $op.totalsDelta.PSObject.Properties) {
                        $kid = $p.Name
                        if (-not ($data.categories.totals.PSObject.Properties.Name -contains $kid)) { continue }
                        $bal = $data.categories.totals.$kid
                        $d   = $p.Value
                        foreach ($jar in @('give','save','spend')) {
                            if ($d.PSObject.Properties.Name -contains $jar) {
                                $bal.$jar = Round2 ($bal.$jar + $d.$jar)
                            }
                        }
                        $changes += "adjust $kid"
                    }
                }

                if ($op.PSObject.Properties.Name -contains 'setAccrualMonth' -and $op.setAccrualMonth) {
                    $data.categories.lastAccrualMonth = [string]$op.setAccrualMonth
                    $changes += "accrual month $($op.setAccrualMonth)"
                }

                if ($op.PSObject.Properties.Name -contains 'setPayoutMonth' -and $op.setPayoutMonth) {
                    $k = $op.setPayoutMonth.kid
                    $m = [string]$op.setPayoutMonth.month
                    if ($data.categories.lastPayoutMonth.PSObject.Properties.Name -contains $k) {
                        $data.categories.lastPayoutMonth.$k = $m
                    } else {
                        $data.categories.lastPayoutMonth | Add-Member -NotePropertyName $k -NotePropertyValue $m -Force
                    }
                    $changes += "payout month $k $m"
                }

                if ($changes.Count -eq 0) {
                    $res.StatusCode = 200
                    $res.Close()
                    Write-Log 'No-op - request contained nothing to apply'
                    continue
                }

                $json = $data | ConvertTo-Json -Depth 12
                [System.IO.File]::WriteAllText($DataPath, $json, $Utf8NoBom)

                $res.StatusCode = 200
                $res.Close()

                $gitStatus = "unknown"
                try {
                    Push-Location $RepoPath

                    git add payroll/payroll-data.json 2>&1 | Out-Null
                    if ($LASTEXITCODE -ne 0) {
                        $gitStatus = "add failed (exit $LASTEXITCODE)"
                    } else {
                        $staged = git diff --cached --stat -- payroll/payroll-data.json 2>&1
                        if (-not $staged) {
                            $gitStatus = "no change to commit"
                        } else {
                            $stamp = Get-Date -Format 'yyyy-MM-dd HH:mm'
                            $commitOut = git commit -m "payroll: $($changes -join ', ') $stamp" 2>&1
                            if ($LASTEXITCODE -ne 0) {
                                $gitStatus = "commit failed (exit $LASTEXITCODE): $commitOut"
                            } else {
                                # Rebase onto whatever an agent pushed while we were local.
                                # Without this the push loses to the remote and the two
                                # copies drift apart with nothing saying so.
                                git pull --rebase 2>&1 | Out-Null
                                if ($LASTEXITCODE -ne 0) {
                                    $gitStatus = "pull --rebase failed (exit $LASTEXITCODE) - local and repo have diverged"
                                } else {
                                    $pushOut = git push 2>&1
                                    if ($LASTEXITCODE -ne 0) {
                                        $gitStatus = "push failed (exit $LASTEXITCODE): $pushOut"
                                    } else {
                                        $gitStatus = "ok"
                                    }
                                }
                            }
                        }
                    }

                    Pop-Location
                } catch {
                    Pop-Location
                    $gitStatus = "exception: $_"
                }

                if ($gitStatus -eq "ok") {
                    Write-Log "Applied and pushed - $($changes -join ', ')"
                } elseif ($gitStatus -eq "no change to commit") {
                    Write-Log "Applied (no git change) - $($changes -join ', ')"
                } else {
                    Write-Log "Applied to disk but git FAILED - $gitStatus"
                }
            } catch {
                Write-Log "Handler error: $_"
                try { $res.StatusCode = 500; $res.Close() } catch {}
            }
        } else {
            $res.StatusCode = 405
            $res.Close()
        }
    }
} finally {
    $listener.Stop()
    Write-Log 'STOPPED'
}
