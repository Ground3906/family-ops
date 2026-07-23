# payroll-nav-patch.ps1
# Adds a Payroll button to the bottom nav bar of cal-widget-current.html.
# Run with -DryRun first to verify the match before applying.
# ASCII only - PowerShell 5.1 / 7
#
# Usage:
#   .\payroll-nav-patch.ps1 -DryRun       <- shows what it found, no changes
#   .\payroll-nav-patch.ps1 -Apply        <- makes the change, commits, pushes
#
# Run from the repo root on Precision or ThinkPad.

param(
    [switch]$DryRun,
    [switch]$Apply
)

if (-not $DryRun -and -not $Apply) {
    Write-Host "Specify -DryRun or -Apply. Start with -DryRun." -ForegroundColor Yellow
    exit 0
}

$RepoPath  = $PSScriptRoot | Split-Path
$WidgetFile = Join-Path $RepoPath 'cal-widget-current.html'

if (-not (Test-Path $WidgetFile)) {
    Write-Host "ERROR: cal-widget-current.html not found at $WidgetFile" -ForegroundColor Red
    Write-Host "Run from the repo root or adjust RepoPath." -ForegroundColor Red
    exit 1
}

$content = Get-Content -Path $WidgetFile -Raw -Encoding UTF8
Write-Host "Read $($content.Length) chars from cal-widget-current.html"

# - STEP 1: Find the bottom nav section -
# Looks for the bottom bar container -- adjust the pattern if the dry-run
# shows it didn't match. The widget uses id="nav" or id="bottom-bar" or
# similar for the 96px bottom ribbon.
$navPatterns = @(
    'id="nav"',
    'id="bottom-bar"',
    'id="bottombar"',
    '--nh',
    'height:.*var\(--nh\)'
)

$foundPattern = $null
foreach ($p in $navPatterns) {
    if ($content -match $p) {
        $foundPattern = $p
        break
    }
}

if (-not $foundPattern) {
    Write-Host ""
    Write-Host "WARNING: No nav pattern matched. Paste the bottom nav section here so Al can" -ForegroundColor Yellow
    Write-Host "write a precise patch. Look for the bottom bar in the HTML and paste 20-30 lines." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Showing last 200 chars of file as orientation:"
    Write-Host $content.Substring($content.Length - 200)
    exit 1
}

Write-Host "Matched pattern: '$foundPattern'"

# - STEP 2: Find the WFD button as the nav anchor -
# What's for Dinner is a documented bottom-nav-tier item.
# We inject the Payroll button adjacent to it.
$wfdPatterns = @(
    "What's for Dinner",
    "whats-for-dinner",
    "wfd",
    "Dinner",
    "showWFD",
    "showDinner"
)

$wfdAnchor = $null
foreach ($p in $wfdPatterns) {
    if ($content -match [regex]::Escape($p)) {
        $wfdAnchor = $p
        break
    }
}

Write-Host ""
if ($wfdAnchor) {
    Write-Host "WFD anchor found: '$wfdAnchor'"
    # Extract ~300 chars around the anchor for review
    $idx = $content.IndexOf($wfdAnchor)
    $start = [Math]::Max(0, $idx - 150)
    $excerpt = $content.Substring($start, [Math]::Min(400, $content.Length - $start))
    Write-Host ""
    Write-Host "--- EXCERPT AROUND WFD ANCHOR ---"
    Write-Host $excerpt
    Write-Host "--- END EXCERPT ---"
} else {
    Write-Host "WFD anchor NOT found. Paste the nav section here so Al can write the precise patch."
    exit 1
}

if ($DryRun) {
    Write-Host ""
    Write-Host "DRY-RUN complete. Review the excerpt above." -ForegroundColor Cyan
    Write-Host "If the nav structure looks right, paste it to Al for the precise Replace() and re-run with -Apply." -ForegroundColor Cyan
    exit 0
}

# - STEP 3: Apply (ONLY after DryRun verified) -
# PLACEHOLDER -- do not run -Apply until Al has written the precise Replace()
# target below based on the DryRun output.
#
# Once Al provides the target string, replace these two variables:
$OldStr = 'REPLACE_ME_WITH_DRYRUN_OUTPUT'
$NewStr = 'REPLACE_ME_WITH_NEW_HTML'

if ($OldStr -eq 'REPLACE_ME_WITH_DRYRUN_OUTPUT') {
    Write-Host ""
    Write-Host "STOP: Run -DryRun first, paste the output to Al, then re-run setup." -ForegroundColor Red
    Write-Host "The Replace() target has not been filled in yet." -ForegroundColor Red
    exit 1
}

if ($content.IndexOf($OldStr) -lt 0) {
    Write-Host "ERROR: Target string not found in file. Patch is stale or file changed." -ForegroundColor Red
    exit 1
}

$patched = $content.Replace($OldStr, $NewStr)
Set-Content -Path $WidgetFile -Value $patched -Encoding UTF8 -NoNewline

Write-Host "Patch applied. Committing..."
Push-Location $RepoPath
git add cal-widget-current.html
git commit -m "cal-widget: add Payroll nav button (payroll-nav-patch)"
git push
Pop-Location
Write-Host "Done. ThinkPad will pull on next 3-min cycle." -ForegroundColor Green
