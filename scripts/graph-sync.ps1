# graph-sync.ps1 - Mobile Wave sync engine
# Parses calendars.md and keeps Bayer Family Ops Outlook calendar in sync via Microsoft Graph.
# Strict one-pen doctrine: calendars.md is the only truth.
# Foreign edits are detected, reverted, and logged to graph-sync-revert.log.
# Runs every 3 min via Scheduled Task. See setup-sync-task.ps1.

Set-StrictMode -Version 1
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------
$ClientId      = "eec121fa-f054-4214-af52-aa83371128ac"
$TokenUrl      = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
$ScriptDir     = $PSScriptRoot
$RepoRoot      = Split-Path $ScriptDir -Parent
$TokenFile     = Join-Path $ScriptDir "graph-token.json"
$StateFile     = Join-Path $ScriptDir "graph-sync-state.json"
$CalFile       = Join-Path $RepoRoot "calendars.md"
$RevertLog     = Join-Path $ScriptDir "graph-sync-revert.log"
$HeartbeatFile = Join-Path $ScriptDir "graph-sync-heartbeat.txt"
$ErrorLog      = Join-Path $ScriptDir "graph-sync-error.log"
$CalName       = "Bayer Family Ops"
$GraphBase     = "https://graph.microsoft.com/v1.0"
$TZ            = "America/Denver"
$RecurHorizon  = (Get-Date).AddYears(2)
$KaleaEmail      = "kalea.bayer.co@outlook.com"
$KaleaTokenFile  = Join-Path $ScriptDir "graph-token-kalea.json"
$KaleaStateFile  = Join-Path $ScriptDir "graph-sync-state-kalea.json"

$PillNames = @{
    D = 'Matt'; K = 'Kalea'; W = 'Wyatt'; M = 'Molly'
    R = 'Rileigh'; C = 'Cullen'; E = 'Emmitt'; B6 = 'Baby 6'
    OMA = 'Oma'; PAPA = 'Papa'; GUEST = 'Guest'
    FAM = 'Family'; KIDS = 'Kids'; MEAL = 'Meal'
}

# ---------------------------------------------------------------
# TOKEN
# ---------------------------------------------------------------
function Get-AccessToken {
    if (-not (Test-Path $TokenFile)) {
        throw "No token file at $TokenFile. Run graph-auth.ps1 first."
    }
    $t   = Get-Content $TokenFile -Raw | ConvertFrom-Json
    $tok = $t.access_token
    if ((Get-Date) -ge [datetime]::Parse($t.expires_at).AddMinutes(-5)) {
        Write-Host "[token] Refreshing..." -NoNewline
        $r = Invoke-RestMethod -Method Post -Uri $TokenUrl `
            -ContentType "application/x-www-form-urlencoded" `
            -Body @{
                grant_type    = "refresh_token"
                client_id     = $ClientId
                refresh_token = $t.refresh_token
                scope         = "Calendars.ReadWrite User.Read offline_access"
            }
        $tok = $r.access_token
        @{
            access_token  = $r.access_token
            refresh_token = $r.refresh_token
            expires_at    = (Get-Date).AddSeconds([int]$r.expires_in).ToString("o")
        } | ConvertTo-Json | Set-Content $TokenFile -Encoding UTF8
        Write-Host " done."
    }
    return $tok
}

# ---------------------------------------------------------------
# CALENDAR
# ---------------------------------------------------------------
function Get-CalendarId {
    param([string]$Tok)
    $h   = @{ Authorization = "Bearer $Tok" }
    $r   = Invoke-RestMethod -Method Get -Uri "$GraphBase/me/calendars" -Headers $h
    $cal = $r.value | Where-Object { $_.name -eq $CalName }
    if (-not $cal) {
        Write-Host "[calendar] '$CalName' not found. Creating..."
        $cal = Invoke-RestMethod -Method Post -Uri "$GraphBase/me/calendars" -Headers $h `
            -ContentType "application/json" -Body (@{ name = $CalName } | ConvertTo-Json)
    }
    return $cal.id
}

function Get-KaleaCalendarId {
    param([string]$Tok)
    $h   = @{ Authorization = "Bearer $Tok" }
    $r   = Invoke-RestMethod -Method Get -Uri "$GraphBase/me/calendars" -Headers $h
    $cal = $r.value | Where-Object { $_.name -eq $CalName }
    if (-not $cal) {
        Write-Host "[kalea-calendar] '$CalName' not found. Creating..."
        $cal = Invoke-RestMethod -Method Post -Uri "$GraphBase/me/calendars" -Headers $h `
            -ContentType "application/json" -Body (@{ name = $CalName } | ConvertTo-Json)
    }
    return $cal.id
}

function Ensure-KaleaShare {
    param([string]$Tok, [string]$CalId)
    $h = @{ Authorization = "Bearer $Tok" }
    try {
        $perms  = Invoke-RestMethod -Method Get `
            -Uri "$GraphBase/me/calendars/$CalId/calendarPermissions" -Headers $h
        $exists = $perms.value | Where-Object { $_.emailAddress.address -eq $KaleaEmail }
        if ($exists) { return }
    } catch {
        Write-Warning "[share] Could not read permissions: $_"
        return
    }
    Write-Host "[share] Sharing with $KaleaEmail (read-only)..."
    try {
        $body = @{
            emailAddress = @{ name = "Kalea"; address = $KaleaEmail }
            role         = "read"
            allowedRoles = @("read")
            isRemovable  = $true
        } | ConvertTo-Json -Depth 5
        Invoke-RestMethod -Method Post `
            -Uri "$GraphBase/me/calendars/$CalId/calendarPermissions" `
            -Headers $h -ContentType "application/json" -Body $body | Out-Null
        Write-Host "[share] Done. Kalea can now see Bayer Family Ops in Outlook."
    } catch {
        Write-Warning "[share] Share invite failed: $_. Can be re-attempted next run."
    }
}

# ---------------------------------------------------------------
# PARSE HELPERS
# ---------------------------------------------------------------
function Get-Pills {
    param([string]$Text)
    $pills = [System.Collections.Generic.List[string]]::new()
    while ($Text -match '^\s*\[([A-Z0-9]+)\](.*)$') {
        $pills.Add($Matches[1])
        $Text = $Matches[2]
    }
    return @{ pills = $pills.ToArray(); title = $Text.Trim() }
}

function Parse-Fields {
    param([string[]]$Parts)
    $f = @{}
    foreach ($p in $Parts) {
        $p = $p.Trim()
        if     ($p -match '^(\w+)="([^"]*)"')  { $f[$Matches[1]] = $Matches[2] }
        elseif ($p -match "^(\w+)='([^']*)'")  { $f[$Matches[1]] = $Matches[2] }
        elseif ($p -match '^(\w+)=(.+)$')      { $f[$Matches[1]] = $Matches[2].Trim() }
        elseif ($p -and $p -notmatch '=') {
            if (-not $f.ContainsKey('category')) { $f['category'] = $p }
        }
    }
    return $f
}

function Get-DayOfWeekNum {
    param([string]$Day)
    switch ($Day.ToLower()) {
        'sun' { return 0 }; 'mon' { return 1 }; 'tue' { return 2 }; 'wed' { return 3 }
        'thu' { return 4 }; 'fri' { return 5 }; 'sat' { return 6 }
    }
    return -1
}

# ---------------------------------------------------------------
# LOCAL ID + CONTENT HASH
# ---------------------------------------------------------------
function New-LocalId {
    param([string]$Date, [string]$Time, [string]$Subject)
    $norm  = ($Subject -replace '\[[^\]]+\]', '' -replace '[^a-zA-Z0-9]+', '-').Trim('-').ToLower()
    $raw   = "$Date|$Time|$norm"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($raw)
    $hash  = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
    return -join ($hash | ForEach-Object { $_.ToString('x2') })
}

function New-ContentHash {
    param($Ev)
    $raw   = "$(Strip-NonBmp $Ev.subject)|$($Ev.startDT)|$($Ev.endDT)|$($Ev.isAllDay)|$($Ev.location)|$($Ev.notes)|$($Ev.category)"
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($raw)
    $hash  = [System.Security.Cryptography.SHA256]::Create().ComputeHash($bytes)
    return -join ($hash | ForEach-Object { $_.ToString('x2') })
}

function Strip-NonBmp {
    param([string]$S)
    return ($S -replace "[^\u0000-\uFFFF]", "").Trim()
}

# ---------------------------------------------------------------
# PARSE [CAL] ENTRY
# ---------------------------------------------------------------
function Parse-CalEntry {
    param([string]$Line)
    if ($Line -notmatch '^\[CAL\] (\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}|ALL-DAY)\s+(.+)$') { return $null }
    $date = $Matches[1]
    $time = $Matches[2]
    $rest = $Matches[3]

    $parts = $rest -split '::'
    $pt    = Get-Pills $parts[0]
    $pills = $pt.pills
    $title = $pt.title
    if (-not $title) { return $null }
    $f     = Parse-Fields ($parts | Select-Object -Skip 1)

    $isAllDay = ($time -eq 'ALL-DAY')
    $cancel   = if ($f['cancel'])   { $f['cancel'] }   else { '' }
    $pending  = ($cancel -eq 'pending')
    $optional = ($f['optional'] -eq 'true')

    $pillStr = ($pills | ForEach-Object { "[$_]" }) -join ''
    $subject = if ($pillStr) { "$pillStr $title" } else { $title }
    if ($pending) { $subject = "$subject (PENDING)" }

    if ($isAllDay) {
        $startDT = $date
        $endDT   = if ($f['span']) {
            ([datetime]::ParseExact($f['span'], 'yyyy-MM-dd', $null)).AddDays(1).ToString('yyyy-MM-dd')
        } else {
            ([datetime]::ParseExact($date, 'yyyy-MM-dd', $null)).AddDays(1).ToString('yyyy-MM-dd')
        }
    } else {
        $startDT = "${date}T${time}:00"
        $endDT   = if ($f['end']) {
            "${date}T$($f['end']):00"
        } else {
            ([datetime]::ParseExact("${date}T${time}", 'yyyy-MM-ddTHH:mm', $null)).AddHours(1).ToString('yyyy-MM-ddTHH:mm:ss')
        }
    }

    return @{
        date      = $date
        time      = $time
        title     = $title
        subject   = $subject
        pills     = $pills
        startDT   = $startDT
        endDT     = $endDT
        isAllDay  = $isAllDay
        location  = if ($f['location']) { $f['location'] } else { '' }
        notes     = if ($f['notes'])    { $f['notes'] }    elseif ($f['note']) { $f['note'] } else { '' }
        category  = if ($f['category']) { $f['category'] } else { '' }
        cancel    = $cancel
        tentative = ($f['tentative'] -eq 'true')
        optional  = $optional
    }
}

# ---------------------------------------------------------------
# EXPAND [CAL-RECUR]
# ---------------------------------------------------------------
function Expand-CalRecur {
    param([string]$Line)
    if ($Line -notmatch '^\[CAL-RECUR\s+\w+\s+start=(\d{4}-\d{2}-\d{2})\s+day=(\w+)(?:\s+skip=([^\]]+))?\]\s+(\d{2}:\d{2})\s+(.+)$') { return @() }
    $startStr  = $Matches[1]
    $dayStr    = $Matches[2]
    $skipStr   = $Matches[3]
    $time      = $Matches[4]
    $rest      = $Matches[5]

    $skipDates = if ($skipStr) { $skipStr.Split(',') | ForEach-Object { $_.Trim() } } else { @() }
    $parts     = $rest -split '::'
    $pt        = Get-Pills $parts[0]
    $pills     = $pt.pills
    $title     = $pt.title
    $f         = Parse-Fields ($parts | Select-Object -Skip 1)
    $pillStr   = ($pills | ForEach-Object { "[$_]" }) -join ''
    $subject   = if ($pillStr) { "$pillStr $title" } else { $title }
    $targetDow = Get-DayOfWeekNum $dayStr

    $current = [datetime]::ParseExact($startStr, 'yyyy-MM-dd', $null)
    while ([int]$current.DayOfWeek -ne $targetDow) { $current = $current.AddDays(1) }

    $results = [System.Collections.Generic.List[hashtable]]::new()
    while ($current -le $RecurHorizon) {
        $d = $current.ToString('yyyy-MM-dd')
        if ($d -notin $skipDates) {
            $endDT = if ($f['end']) { "${d}T$($f['end']):00" } else {
                $current.AddHours([timespan]::Parse($time).TotalHours + 1).ToString('yyyy-MM-ddTHH:mm:ss')
            }
            $results.Add(@{
                date      = $d
                time      = $time
                title     = $title
                subject   = $subject
                pills     = $pills
                startDT   = "${d}T${time}:00"
                endDT     = $endDT
                isAllDay  = $false
                location  = if ($f['location']) { $f['location'] } else { '' }
                notes     = ''
                category  = if ($f['category']) { $f['category'] } else { '' }
                cancel    = ''
                tentative = $false
                optional  = ($f['optional'] -eq 'true')
            })
        }
        $current = $current.AddDays(7)
    }
    return $results.ToArray()
}

# ---------------------------------------------------------------
# PARSE FULL calendars.md
# ---------------------------------------------------------------
function Parse-CalendarsFile {
    param([string]$Path)
    $events = @{}
    foreach ($line in (Get-Content $Path -Encoding UTF8)) {
        $t = $line.Trim()
        if ($t.StartsWith('[CAL] ')) {
            $ev = Parse-CalEntry $t
            if ($ev -and $ev.cancel -ne 'confirmed') {
                $id  = New-LocalId $ev.date $ev.time $ev.subject
                $key = $id; $n = 1
                while ($events.ContainsKey($key)) { $n++; $key = "${id}_$n" }
                $events[$key] = $ev
            }
        } elseif ($t.StartsWith('[CAL-RECUR ')) {
            foreach ($ev in (Expand-CalRecur $t)) {
                $id  = New-LocalId $ev.date $ev.time "$($ev.subject)|RECUR"
                $key = $id; $n = 1
                while ($events.ContainsKey($key)) { $n++; $key = "${id}_$n" }
                $events[$key] = $ev
            }
        }
    }
    return $events
}

# ---------------------------------------------------------------
# BUILD GRAPH EVENT BODY
# ---------------------------------------------------------------
function Build-GraphBody {
    param($Ev)
    $lines = [System.Collections.Generic.List[string]]::new()
    if ($Ev.pills.Count -gt 0) {
        $names = $Ev.pills | ForEach-Object { if ($PillNames[$_]) { $PillNames[$_] } else { $_ } }
        $lines.Add("Who: $($names -join ', ')")
    }
    if ($Ev.notes)    { $lines.Add("Notes: $($Ev.notes)") }
    if ($Ev.category) { $lines.Add("Category: $($Ev.category)") }
    $desc = $lines -join "`n"

    $showAs = if ($Ev.optional) { 'free' } elseif ($Ev.tentative) { 'tentative' } else { 'busy' }

    $body = @{
        subject        = Strip-NonBmp $Ev.subject
        body           = @{ contentType = 'text'; content = $desc }
        showAs         = $showAs
        isReminderOn   = $false
    }

    if ($Ev.isAllDay) {
        $body['isAllDay'] = $true
        $body['start']    = @{ dateTime = "$($Ev.startDT)T00:00:00.0000000"; timeZone = 'UTC' }
        $body['end']      = @{ dateTime = "$($Ev.endDT)T00:00:00.0000000";   timeZone = 'UTC' }
    } else {
        $body['start'] = @{ dateTime = $Ev.startDT; timeZone = $TZ }
        $body['end']   = @{ dateTime = $Ev.endDT;   timeZone = $TZ }
    }
    if ($Ev.location) { $body['location']   = @{ displayName = $Ev.location } }
    if ($Ev.category) { $body['categories'] = @($Ev.category) }
    return $body
}

# ---------------------------------------------------------------
# GRAPH API HELPERS
# ---------------------------------------------------------------
function Invoke-Graph {
    param([string]$Method, [string]$Uri, [string]$Tok, $Body = $null)
    $h = @{ Authorization = "Bearer $Tok" }
    $p = @{ Method = $Method; Uri = $Uri; Headers = $h; ErrorAction = 'Stop' }
    if ($Body) { $p['ContentType'] = 'application/json'; $p['Body'] = ($Body | ConvertTo-Json -Depth 8) }
    return Invoke-RestMethod @p
}

function Get-AllGraphEvents {
    param([string]$CalId, [string]$Tok)
    $h   = @{ Authorization = "Bearer $Tok" }
    $all = [System.Collections.Generic.List[object]]::new()
    $url = "$GraphBase/me/calendars/$CalId/events?`$select=id,subject,start,end,isAllDay&`$top=100"
    do {
        $page = Invoke-RestMethod -Method Get -Uri $url -Headers $h
        foreach ($ev in $page.value) { $all.Add($ev) }
        $url = $page.'@odata.nextLink'
    } while ($url)
    return $all.ToArray()
}

# ---------------------------------------------------------------
# STATE FILE
# ---------------------------------------------------------------
function Load-State {
    param([string]$Path = $StateFile)
    if (-not (Test-Path $Path)) { return @{ calendar_id = ''; events = @{} } }
    try {
        $j = Get-Content $Path -Raw | ConvertFrom-Json
        $s = @{ calendar_id = $j.calendar_id; events = @{} }
        foreach ($p in $j.events.PSObject.Properties) {
            $s.events[$p.Name] = @{
                graphId     = $p.Value.graphId
                contentHash = $p.Value.contentHash
                subject     = $p.Value.subject
                start       = $p.Value.start
            }
        }
        return $s
    } catch {
        Write-Warning "[load-state] File unreadable at $Path. Starting fresh. Error: $_"
        return @{ calendar_id = ''; events = @{} }
    }
}

function Save-State {
    param($S, [string]$Path = $StateFile)
    @{
        calendar_id = $S.calendar_id
        last_run    = (Get-Date -Format 'o')
        events      = $S.events
    } | ConvertTo-Json -Depth 5 | Set-Content $Path -Encoding UTF8
}

# ---------------------------------------------------------------
# REVERT RECEIPT
# ---------------------------------------------------------------
function Write-Receipt {
    param([string]$Type, [string]$GraphId, [string]$Subject, [string]$Action, [string]$Detail = '')
    $entry = [ordered]@{
        ts      = (Get-Date -Format 'o')
        type    = $Type
        graphId = $GraphId
        subject = $Subject
        action  = $Action
        detail  = $Detail
    } | ConvertTo-Json -Compress
    Add-Content -Path $RevertLog -Value $entry -Encoding UTF8
}

# ---------------------------------------------------------------
# KALEA TOKEN (optional - push category colors to her account)
# ---------------------------------------------------------------
function Get-KaleaAccessToken {
    if (-not (Test-Path $KaleaTokenFile)) { return $null }
    try {
        $t   = Get-Content $KaleaTokenFile -Raw | ConvertFrom-Json
        $tok = $t.access_token
        if ((Get-Date) -ge [datetime]::Parse($t.expires_at).AddMinutes(-5)) {
            $r = Invoke-RestMethod -Method Post -Uri $TokenUrl `
                -ContentType "application/x-www-form-urlencoded" `
                -Body @{
                    grant_type    = "refresh_token"
                    client_id     = $ClientId
                    refresh_token = $t.refresh_token
                    scope         = "Calendars.ReadWrite User.Read offline_access"
                }
            $tok = $r.access_token
            @{
                access_token  = $r.access_token
                refresh_token = $r.refresh_token
                expires_at    = (Get-Date).AddSeconds([int]$r.expires_in).ToString("o")
            } | ConvertTo-Json | Set-Content $KaleaTokenFile -Encoding UTF8
        }
        return $tok
    } catch {
        Write-Warning "[kalea-token] Refresh failed - re-run graph-auth.ps1 -Out graph-token-kalea.json: $_"
        return $null
    }
}

# ---------------------------------------------------------------
# OUTLOOK CATEGORY COLORS
# ---------------------------------------------------------------
function Ensure-OutlookCategories {
    param([string]$Tok)
    $h = @{ Authorization = "Bearer $Tok" }

    $colorMap = [ordered]@{
        liturgical   = 'preset8'   # Purple
        kids         = 'preset7'   # Blue
        appointments = 'preset1'   # Orange
        family       = 'preset5'   # Teal
        '4h'         = 'preset4'   # Green
        meetings     = 'preset12'  # Gray
        holidays     = 'preset3'   # Yellow / Gold
        birthdays    = 'preset9'   # Cranberry
        meals        = 'preset0'   # Red
        farm         = 'preset19'  # Dark Green
        prompt       = 'preset13'  # Dark Gray
        misc         = 'preset13'  # Dark Gray (same as prompt)
    }

    try {
        $existing = Invoke-RestMethod -Method Get `
            -Uri "$GraphBase/me/outlook/masterCategories" -Headers $h
        $existingMap = @{}
        foreach ($c in $existing.value) { $existingMap[$c.displayName] = @{ id = $c.id; color = $c.color } }
    } catch {
        Write-Warning "[categories] Could not read master categories: $_"
        return
    }

    $added = 0; $updated = 0
    foreach ($cat in $colorMap.Keys) {
        $preset = $colorMap[$cat]
        if (-not $existingMap.ContainsKey($cat)) {
            try {
                $body = @{ displayName = $cat; color = $preset } | ConvertTo-Json
                Invoke-RestMethod -Method Post -Uri "$GraphBase/me/outlook/masterCategories" `
                    -Headers $h -ContentType "application/json" -Body $body | Out-Null
                $added++
            } catch { Write-Warning "[categories] Create '$cat' failed: $_" }
        } elseif ($existingMap[$cat].color -ne $preset) {
            try {
                $body = @{ color = $preset } | ConvertTo-Json
                Invoke-RestMethod -Method Patch `
                    -Uri "$GraphBase/me/outlook/masterCategories/$($existingMap[$cat].id)" `
                    -Headers $h -ContentType "application/json" -Body $body | Out-Null
                $updated++
            } catch { Write-Warning "[categories] Update '$cat' failed: $_" }
        }
    }
    if ($added -gt 0 -or $updated -gt 0) {
        Write-Host "[categories] Added: $added  Updated: $updated"
    }
}

# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------
try {
    Write-Host "[sync] $(Get-Date -Format 'HH:mm:ss') --- START ---"

    # 1. Auth + calendar
    $tok   = Get-AccessToken
    $calId = Get-CalendarId $tok
    Write-Host "[sync] Calendar ID: $calId"

    # 2. One-time share with Kalea (no-op if already shared)
    Ensure-KaleaShare $tok $calId

    # 2b. Push Outlook category color definitions to Matt's account (no-op when already set)
    Ensure-OutlookCategories $tok

    # 2c. Push same category colors to Kalea's account if her token exists
    $kaleaTok = Get-KaleaAccessToken
    if ($kaleaTok) { Ensure-OutlookCategories $kaleaTok }

    # 3. Parse calendars.md
    if (-not (Test-Path $CalFile)) { throw "calendars.md not found at $CalFile" }
    Write-Host "[sync] Parsing $CalFile"
    $desired = Parse-CalendarsFile $CalFile
    Write-Host "[sync] $($desired.Count) events parsed from calendars.md"

    if ($desired.Count -eq 0) {
        throw "calendars.md parsed to zero events. Aborting to protect existing calendar data."
    }

    # 4. Load state
    $state = Load-State
    if (-not $state.calendar_id) { $state.calendar_id = $calId }

    # 5a. Clean slate guard
    if ($state.events.Count -eq 0) {
        $existing = Get-AllGraphEvents $calId $tok
        if ($existing.Count -gt 0) {
            Write-Host "[sync] State is empty but calendar has $($existing.Count) events. Clearing first..."
            foreach ($gev in $existing) {
                try { Invoke-Graph 'Delete' "$GraphBase/me/calendars/$calId/events/$($gev.id)" $tok } catch {}
            }
            Write-Host "[sync] Calendar cleared. Creating fresh."
        }
    }

    # 5. Delete events no longer in calendars.md
    $toDelete = @($state.events.Keys | Where-Object { -not $desired.ContainsKey($_) })
    foreach ($id in $toDelete) {
        $gid  = $state.events[$id].graphId
        $subj = $state.events[$id].subject
        Write-Host "[delete] $subj"
        try {
            Invoke-Graph 'Delete' "$GraphBase/me/calendars/$calId/events/$gid" $tok
        } catch {
            Write-Warning "Delete failed for '$subj' ($gid): $_"
        }
        $state.events.Remove($id)
    }

    # 6. Create new + update changed events
    $created = 0; $updated = 0; $skipped = 0
    foreach ($id in $desired.Keys) {
        $ev      = $desired[$id]
        $gBody   = Build-GraphBody $ev
        $newHash = New-ContentHash $ev

        if (-not $state.events.ContainsKey($id)) {
            try {
                $gBody['transactionId'] = "$($id.Substring(0,8))-$($id.Substring(8,4))-$($id.Substring(12,4))-$($id.Substring(16,4))-$($id.Substring(20,12))"
                $r = Invoke-Graph 'Post' "$GraphBase/me/calendars/$calId/events" $tok $gBody
                $state.events[$id] = @{
                    graphId     = $r.id
                    contentHash = $newHash
                    subject     = Strip-NonBmp $ev.subject
                    start       = $ev.startDT
                }
                $created++
                if ($created % 50 -eq 0) { Write-Host "[sync] $created/$($desired.Count) created..." }
                Start-Sleep -Milliseconds 50
            } catch {
                Write-Warning "Create failed '$($ev.subject)': $_"
            }
        } else {
            if ($state.events[$id].contentHash -ne $newHash) {
                $gid = $state.events[$id].graphId
                try {
                    Invoke-Graph 'Patch' "$GraphBase/me/calendars/$calId/events/$gid" $tok $gBody | Out-Null
                    $state.events[$id].contentHash = $newHash
                    $state.events[$id].subject     = Strip-NonBmp $ev.subject
                    $state.events[$id].start       = $ev.startDT
                    $updated++
                } catch {
                    if ($_ -match '(404|itemNotFound)') {
                        try {
                            $gBody['transactionId'] = "$($id.Substring(0,8))-$($id.Substring(8,4))-$($id.Substring(12,4))-$($id.Substring(16,4))-$($id.Substring(20,12))"
                            $r = Invoke-Graph 'Post' "$GraphBase/me/calendars/$calId/events" $tok $gBody
                            $state.events[$id].graphId     = $r.id
                            $state.events[$id].contentHash = $newHash
                            $state.events[$id].subject     = Strip-NonBmp $ev.subject
                            $created++
                            Start-Sleep -Milliseconds 50
                        } catch {
                            Write-Warning "Recreate failed '$($ev.subject)': $_"
                        }
                    } else {
                        Write-Warning "Update failed '$($ev.subject)': $_"
                    }
                }
            } else {
                $skipped++
            }
        }
    }
    Write-Host "[sync] Created: $created  Updated: $updated  No-change: $skipped  Deleted: $($toDelete.Count)"

    # 7. Foreign event sweep
    $allGraph     = Get-AllGraphEvents $calId $tok
    $knownGids    = @($state.events.Values | ForEach-Object { $_.graphId })
    $foreignCount = 0

    foreach ($gev in $allGraph) {
        if ($gev.id -notin $knownGids) {
            Write-Warning "[foreign-create] '$($gev.subject)' - deleting and logging receipt"
            Write-Receipt 'foreign_create' $gev.id $gev.subject 'deleted'
            try {
                Invoke-Graph 'Delete' "$GraphBase/me/calendars/$calId/events/$($gev.id)" $tok
                $foreignCount++
            } catch {
                Write-Warning "Foreign delete failed ($($gev.id)): $_"
            }
        }
    }
    if ($foreignCount -gt 0) {
        Write-Host "[sync] $foreignCount foreign event(s) removed. Receipts: $RevertLog"
    }

    # 8. Kalea dual-push (if her token exists)
    if ($kaleaTok) {
        Write-Host "[kalea-sync] Syncing $($desired.Count) events to Kalea's owned calendar..."
        $kaleaCalId = Get-KaleaCalendarId $kaleaTok
        $kaleaState = Load-State $KaleaStateFile
        if (-not $kaleaState.calendar_id) { $kaleaState.calendar_id = $kaleaCalId }

        # Clean slate guard
        if ($kaleaState.events.Count -eq 0) {
            $kaleaExisting = Get-AllGraphEvents $kaleaCalId $kaleaTok
            if ($kaleaExisting.Count -gt 0) {
                Write-Host "[kalea-sync] State empty, calendar has $($kaleaExisting.Count) events. Clearing..."
                foreach ($gev in $kaleaExisting) {
                    try { Invoke-Graph 'Delete' "$GraphBase/me/calendars/$kaleaCalId/events/$($gev.id)" $kaleaTok } catch {}
                }
                Write-Host "[kalea-sync] Calendar cleared. Creating fresh."
            }
        }

        # Delete pass
        $kaleaToDelete = @($kaleaState.events.Keys | Where-Object { -not $desired.ContainsKey($_) })
        foreach ($id in $kaleaToDelete) {
            $gid = $kaleaState.events[$id].graphId
            try { Invoke-Graph 'Delete' "$GraphBase/me/calendars/$kaleaCalId/events/$gid" $kaleaTok } catch {}
            $kaleaState.events.Remove($id)
        }

        # Create/update pass
        $kCreated = 0; $kUpdated = 0; $kSkipped = 0
        foreach ($id in $desired.Keys) {
            $ev      = $desired[$id]
            $gBody   = Build-GraphBody $ev
            $newHash = New-ContentHash $ev

            if (-not $kaleaState.events.ContainsKey($id)) {
                try {
                    $gBody['transactionId'] = "$($id.Substring(0,8))-$($id.Substring(8,4))-$($id.Substring(12,4))-$($id.Substring(16,4))-$($id.Substring(20,12))"
                    $r = Invoke-Graph 'Post' "$GraphBase/me/calendars/$kaleaCalId/events" $kaleaTok $gBody
                    $kaleaState.events[$id] = @{
                        graphId     = $r.id
                        contentHash = $newHash
                        subject     = Strip-NonBmp $ev.subject
                        start       = $ev.startDT
                    }
                    $kCreated++
                    if ($kCreated % 50 -eq 0) { Write-Host "[kalea-sync] $kCreated/$($desired.Count) created..." }
                    Start-Sleep -Milliseconds 50
                } catch { Write-Warning "[kalea-sync] Create failed '$($ev.subject)': $_" }
            } else {
                if ($kaleaState.events[$id].contentHash -ne $newHash) {
                    $gid = $kaleaState.events[$id].graphId
                    try {
                        Invoke-Graph 'Patch' "$GraphBase/me/calendars/$kaleaCalId/events/$gid" $kaleaTok $gBody | Out-Null
                        $kaleaState.events[$id].contentHash = $newHash
                        $kaleaState.events[$id].subject     = Strip-NonBmp $ev.subject
                        $kaleaState.events[$id].start       = $ev.startDT
                        $kUpdated++
                    } catch { Write-Warning "[kalea-sync] Update failed '$($ev.subject)': $_" }
                } else { $kSkipped++ }
            }
        }
        Write-Host "[kalea-sync] Created: $kCreated  Updated: $kUpdated  No-change: $kSkipped  Deleted: $($kaleaToDelete.Count)"

        # Foreign sweep for Kalea's calendar
        $kaleaAllGraph  = Get-AllGraphEvents $kaleaCalId $kaleaTok
        $kaleaKnownGids = @($kaleaState.events.Values | ForEach-Object { $_.graphId })
        $kForeignCount  = 0
        foreach ($gev in $kaleaAllGraph) {
            if ($gev.id -notin $kaleaKnownGids) {
                try { Invoke-Graph 'Delete' "$GraphBase/me/calendars/$kaleaCalId/events/$($gev.id)" $kaleaTok; $kForeignCount++ } catch {}
            }
        }
        if ($kForeignCount -gt 0) { Write-Host "[kalea-sync] $kForeignCount foreign event(s) removed." }

        Save-State $kaleaState $KaleaStateFile
        Write-Host "[kalea-sync] Done."
    } else {
        Write-Warning "[kalea-sync] No token found at $KaleaTokenFile. Skipping Kalea calendar push."
    }

    # 9. Heartbeat + save state
    "$(Get-Date -Format 'o') OK events=$($desired.Count)" | Set-Content $HeartbeatFile -Encoding UTF8
    Save-State $state

    Write-Host "[sync] $(Get-Date -Format 'HH:mm:ss') --- DONE ---"

} catch {
    $msg = "$(Get-Date -Format 'o') FATAL: $_"
    Write-Warning $msg
    $msg | Add-Content $ErrorLog -Encoding UTF8
    exit 1
}
