# fix-recur-blocks.ps1
# Converts 3 forbidden CAL-RECUR lines into two canonical [CAL] blocks.
# Doctrine: cal-widget.md limits CAL-RECUR to Sunday Mass and Daily Mass Wed only.
$ErrorActionPreference = 'Stop'
$file = 'C:\dev\family-ops\calendars.md'
$raw  = Get-Content -Path $file -Raw

$before = ([regex]'(?m)^\[CAL-RECUR ').Matches($raw).Count
Write-Host "CAL-RECUR lines before: $before  (expect 5)"
if ($before -ne 5) { throw "Unexpected CAL-RECUR count: $before" }

# 1. Drop the three violating CAL-RECUR lines
$raw = $raw -replace '(?m)^\[CAL-RECUR weekly start=2026-09-17 day=thu[^\r\n]*\r?\n', ''
$raw = $raw -replace '(?m)^\[CAL-RECUR weekly start=2026-09-14 day=mon[^\r\n]*\r?\n', ''
$raw = $raw -replace '(?m)^\[CAL-RECUR weekly start=2026-09-14 day=wed[^\r\n]*\r?\n', ''

$after = ([regex]'(?m)^\[CAL-RECUR ').Matches($raw).Count
Write-Host "CAL-RECUR lines after: $after  (expect 2)"
if ($after -ne 2) { throw "Removal failed, count is $after" }

# 2. Insert the two canonical blocks ahead of Knights of Columbus
$anchor = '### KNIGHTS OF COLUMBUS - 2026-27 (2nd Tuesday monthly)'
if ($raw -notmatch [regex]::Escape($anchor)) { throw 'Anchor not found' }
$block = @'
### MOLLY WONDERHOOD PROGRAM - School Year 2026-27
<!-- CANONICAL SOURCE. Do not duplicate individual Thursday entries in monthly sections. -->
<!-- Per official program calendar: Thanksgiving break 11/26, winter break 12/24-1/14, spring break 3/25 and 4/1. 30 scheduled Thursday learning days, final day 2027-05-27. -->
[CAL] 2026-09-17 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-09-24 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-10-01 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-10-08 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-10-15 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-10-22 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-10-29 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-11-05 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-11-12 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-11-19 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-12-03 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-12-10 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2026-12-17 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-01-21 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-01-28 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-02-04 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-02-11 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-02-18 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-02-25 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-03-04 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-03-11 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-03-18 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-04-08 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-04-15 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-04-22 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-04-29 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-05-06 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-05-13 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-05-20 11:30 [M] Wonderhood Program :: kids :: end=15:30
[CAL] 2027-05-27 11:30 [M] Wonderhood Program :: kids :: end=15:30

---

### GIRLS ON THE RUN - Fall 2026
<!-- CANONICAL SOURCE. Do not duplicate individual Mon/Wed practice entries in monthly sections. -->
<!-- Season ends at the 11/8 race. Mondays 9/14-11/2, Wednesdays 9/16-11/4. -->
[CAL] 2026-09-14 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-09-16 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-09-21 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-09-23 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-09-28 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-09-30 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-05 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-07 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-12 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-14 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-19 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-21 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-26 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-10-28 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-11-02 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30
[CAL] 2026-11-04 15:00 [M][R] Girls on the Run practice :: kids :: end=16:30

---
'@
$raw = $raw.Replace($anchor, $block + "`r`n" + $anchor)

# 3. Repoint the two Foreman notes at the new blocks
$oldW = '- **MOLLY WONDERHOOD PROGRAM entry (in RECURRING - Weekly) is canonical. Never add individual Thursday entries to the monthly date sections.**'
$newW = '- **MOLLY WONDERHOOD PROGRAM block is canonical. Never add individual Thursday entries to the monthly date sections. Duplicate entries cause double rendering on the Cockpit widget.**'
if ($raw -notmatch [regex]::Escape($oldW)) { throw 'Wonderhood note not found' }
$raw = $raw.Replace($oldW, $newW)

$oldG = '- **GIRLS ON THE RUN entries (in RECURRING - Weekly) are canonical. Never add individual Mon/Wed entries to the monthly date sections.**'
$newG = '- **GIRLS ON THE RUN block is canonical. Never add individual Mon/Wed practice entries to the monthly date sections. Duplicate entries cause double rendering on the Cockpit widget.**'
if ($raw -notmatch [regex]::Escape($oldG)) { throw 'GOTR note not found' }
$raw = $raw.Replace($oldG, $newG)

Set-Content -Path $file -Value $raw -NoNewline -Encoding UTF8

# 4. Verify by counting what actually landed
$v = Get-Content -Path $file -Raw
$w = ([regex]'(?m)^\[CAL\] [0-9-]+ 11:30 \[M\] Wonderhood Program ').Matches($v).Count
$g = ([regex]'(?m)^\[CAL\] [0-9-]+ 15:00 \[M\]\[R\] Girls on the Run practice ').Matches($v).Count
$r = ([regex]'(?m)^\[CAL-RECUR ').Matches($v).Count
Write-Host "Wonderhood lines: $w  (expect 30)"
Write-Host "Girls on the Run lines: $g  (expect 16)"
Write-Host "CAL-RECUR remaining: $r  (expect 2)"
if ($w -ne 30 -or $g -ne 16 -or $r -ne 2) { throw 'VERIFY FAILED - do not commit' }
Write-Host 'OK - 46 lines written, 2 permitted CAL-RECUR remain.'
