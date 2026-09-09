# payroll-accrual.ps1
# ThinkPad X1 Carbon - PowerShell 5.1 - ASCII only
# Adds each child's fixed monthly allowance to their jars. Registered as
# BayerFamilyOps-PayrollAccrual (SYSTEM), runs on the 1st of every month.
#
# Why this is a scheduled task and not code in the page: the Payroll screen
# only runs while someone is looking at it. Accrual lived on a button there
# from July to September 2026 and never fired once, because nobody opened
# the screen on the right day. Monthly work does not belong to a web page.
#
# Safe to run more than once. lastAccrualMonth is checked first, so a manual
# run, a retry, or a catch-up after the machine was off cannot double-pay.
# The task is registered with StartWhenAvailable so a missed 1st still runs.
#
# Writes through the same append endpoint the Cockpit uses, so it can never
# overwrite a stamp made while it was working.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

$RepoPath   = 'C:\Users\ThinkPad X1 Carbon\Documents\family-ops'
$DataPath   = Join-Path $RepoPath 'payroll\payroll-data.json'
$LogPath    = Join-Path $RepoPath 'logs\payroll-accrual.log'
$AppendUrl  = 'http://127.0.0.1:8081/append'

# Mirror of the RATES table in payroll-current.html. If a rate changes there,
# it changes here. Source of truth for the policy is ledger/allowance.md.
$RATES = @{
    wyatt   = @{ give = 1; save = 3; spend = 10 }
    molly   = @{ give = 1; save = 2; spend = 7  }
    rileigh = @{ give = 1; save = 1; spend = 6  }
    cullen  = @{ give = 1; save = 1; spend = 4  }
    emmitt  = @{ give = 1; save = 1; spend = 4  }
}

function Write-Log {
    param([string]$Msg)
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "$ts  $Msg" | Out-File -FilePath $LogPath -Append -Encoding ASCII
}

$null = New-Item -ItemType Directory -Path (Split-Path $LogPath) -Force

try {
    if (-not (Test-Path $DataPath)) {
        Write-Log 'ABORT - payroll-data.json not found'
        exit 1
    }

    $raw = [System.IO.File]::ReadAllText($DataPath)
    if ($raw.Length -gt 0 -and $raw[0] -eq [char]0xFEFF) { $raw = $raw.Substring(1) }
    $data = $raw | ConvertFrom-Json

    $mk        = Get-Date -Format 'yyyy-MM'
    $monthName = (Get-Date).ToString('MMMM yyyy')

    if ($data.categories.lastAccrualMonth -eq $mk) {
        Write-Log "SKIP - $mk already accrued"
        exit 0
    }

    $delta = @{}
    $logs  = @()
    $today = Get-Date -Format 'yyyy-MM-dd'
    $total = 0

    foreach ($kid in $RATES.Keys) {
        if (-not ($data.categories.totals.PSObject.Properties.Name -contains $kid)) {
            Write-Log "WARN - $kid is in the rate table but not in the ledger, skipped"
            continue
        }
        $r = $RATES[$kid]
        $delta[$kid] = @{ give = $r.give; save = $r.save; spend = $r.spend }
        $logs += @{
            id     = "accrue-$mk-$kid"
            kidId  = $kid
            type   = 'accrue'
            note   = "$monthName allowance added"
            date   = $today
        }
        $total += ($r.give + $r.save + $r.spend)
    }

    if ($logs.Count -eq 0) {
        Write-Log 'ABORT - nothing to accrue'
        exit 1
    }

    $op = @{
        addLog          = $logs
        totalsDelta     = $delta
        setAccrualMonth = $mk
    } | ConvertTo-Json -Depth 8

    $resp = Invoke-WebRequest -Uri $AppendUrl -Method POST -ContentType 'application/json' -Body $op -UseBasicParsing -TimeoutSec 30
    if ($resp.StatusCode -eq 200) {
        Write-Log "OK - $mk accrued for $($logs.Count) kids, `$$total total"
    } else {
        Write-Log "FAIL - append returned HTTP $($resp.StatusCode)"
        exit 1
    }
} catch {
    Write-Log "FAIL - $_"
    exit 1
}
