# payroll-write.ps1
# ThinkPad X1 Carbon - PowerShell 5.1 - ASCII only
# Listens on :8081, receives POST /save, writes payroll-data.json, commits and pushes.
# Registered via setup-payroll-write.ps1 as BayerFamilyOps-PayrollWrite (SYSTEM).
#
# Git step checks the actual exit code of add/commit/push. logs\payroll-write.log only
# reports success when all three genuinely succeeded, tells a no-op (identical content,
# nothing to commit) apart from a real failure, and logs the actual git error text when
# something breaks. Item 3 of the 2026-08-19 archive-pipeline fix.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

$RepoPath = 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops'
$DataPath = Join-Path $RepoPath 'payroll\payroll-data.json'
$LogPath  = Join-Path $RepoPath 'logs\payroll-write.log'
$Port     = 8081

function Write-Log {
    param([string]$Msg)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$ts  $Msg" | Out-File -FilePath $LogPath -Append -Encoding ASCII
}

# Ensure log dir exists
$null = New-Item -ItemType Directory -Path (Split-Path $LogPath) -Force

$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://+:$Port/")

try {
    $listener.Start()
    Write-Log 'STARTED on port 8081'
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

        # CORS headers on every response
        try {
            $res.AddHeader('Access-Control-Allow-Origin', '*')
            $res.AddHeader('Access-Control-Allow-Methods', 'POST, OPTIONS')
            $res.AddHeader('Access-Control-Allow-Headers', 'Content-Type')
        } catch {}

        # Preflight
        if ($req.HttpMethod -eq 'OPTIONS') {
            $res.StatusCode = 200
            $res.Close()
            continue
        }

        # Write endpoint
        if ($req.HttpMethod -eq 'POST' -and $req.Url.AbsolutePath -eq '/save') {
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

                $null = New-Item -ItemType Directory -Path (Split-Path $DataPath) -Force
                [System.IO.File]::WriteAllText($DataPath, $body, [System.Text.Encoding]::UTF8)

                $res.StatusCode = 200
                $res.Close()

                # Git commit and push - runs after response is sent.
                # Every step's real exit code is checked. Nothing is assumed to have
                # worked just because it ran.
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
                            $commitOut = git commit -m "payroll: auto-save $stamp" 2>&1
                            if ($LASTEXITCODE -ne 0) {
                                $gitStatus = "commit failed (exit $LASTEXITCODE): $commitOut"
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

                    Pop-Location
                } catch {
                    Pop-Location
                    $gitStatus = "exception: $_"
                }

                if ($gitStatus -eq "ok") {
                    Write-Log 'Saved and pushed'
                } elseif ($gitStatus -eq "no change to commit") {
                    Write-Log 'Saved (no git change - identical content)'
                } else {
                    Write-Log "Git FAILED - $gitStatus"
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
