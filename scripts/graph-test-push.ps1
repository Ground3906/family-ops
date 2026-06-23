# graph-test-push.ps1 -- Mobile Wave chunk 1 proof
# Creates Bayer Family Ops calendar if it does not exist.
# Pushes one test event. Verify it lands on Kalea's phone.
# Auto-refreshes token if near expiry.

$ClientId  = "eec121fa-f054-4214-af52-aa83371128ac"
$TokenUrl  = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
$TokenFile = Join-Path $PSScriptRoot "graph-token.json"
$CalName   = "Bayer Family Ops"
$Graph     = "https://graph.microsoft.com/v1.0"

# Load token
if (-not (Test-Path $TokenFile)) {
    Write-Host "No token found. Run graph-auth.ps1 first."
    exit 1
}
$T = Get-Content $TokenFile -Raw | ConvertFrom-Json

# Refresh if near expiry (within 5 min)
$AccessToken = $T.access_token
if ((Get-Date) -ge [datetime]::Parse($T.expires_at).AddMinutes(-5)) {
    Write-Host "Refreshing token..." -NoNewline
    try {
        $R = Invoke-RestMethod -Method Post -Uri $TokenUrl `
            -ContentType "application/x-www-form-urlencoded" `
            -Body @{
                grant_type    = "refresh_token"
                client_id     = $ClientId
                refresh_token = $T.refresh_token
                scope         = "Calendars.ReadWrite User.Read offline_access"
            } -ErrorAction Stop
        $AccessToken = $R.access_token
        @{
            access_token  = $R.access_token
            refresh_token = $R.refresh_token
            expires_at    = (Get-Date).AddSeconds([int]$R.expires_in).ToString("o")
        } | ConvertTo-Json | Set-Content -Path $TokenFile -Encoding UTF8
        Write-Host " done."
    } catch {
        Write-Host ""
        Write-Host "Token refresh failed. Run graph-auth.ps1 to re-authenticate."
        exit 1
    }
}

$AuthHeader = @{ Authorization = "Bearer $AccessToken" }

# Find or create Bayer Family Ops calendar
Write-Host "Checking for '$CalName' calendar..." -NoNewline
$Cals = Invoke-RestMethod -Method Get -Uri "$Graph/me/calendars" -Headers $AuthHeader
$Cal  = $Cals.value | Where-Object { $_.name -eq $CalName }

if (-not $Cal) {
    Write-Host " not found. Creating..." -NoNewline
    $Cal = Invoke-RestMethod -Method Post -Uri "$Graph/me/calendars" `
        -Headers $AuthHeader `
        -ContentType "application/json" `
        -Body (@{ name = $CalName } | ConvertTo-Json)
    Write-Host " created."
} else {
    Write-Host " found."
}

# Push test event
$Now   = Get-Date
$Start = $Now.AddHours(1).ToString("yyyy-MM-ddTHH:mm:ss")
$End   = $Now.AddHours(2).ToString("yyyy-MM-ddTHH:mm:ss")

$EventBody = @{
    subject = "FamilyOps Test Event"
    body    = @{
        contentType = "text"
        content     = "Bayer Family Ops calendar sync is live. Pushed by graph-test-push.ps1."
    }
    start = @{ dateTime = $Start; timeZone = "America/Denver" }
    end   = @{ dateTime = $End;   timeZone = "America/Denver" }
} | ConvertTo-Json -Depth 5

Write-Host "Pushing test event..." -NoNewline
$Ev = Invoke-RestMethod -Method Post `
    -Uri "$Graph/me/calendars/$($Cal.id)/events" `
    -Headers $AuthHeader `
    -ContentType "application/json" `
    -Body $EventBody
Write-Host " done."

Write-Host ""
Write-Host "=== SUCCESS ==="
Write-Host "Calendar : $CalName"
Write-Host "Event    : $($Ev.subject)"
Write-Host "Start    : $($Ev.start.dateTime) Mountain"
Write-Host "Event ID : $($Ev.id)"
Write-Host "==============="
Write-Host "Check Outlook on Kalea's phone."
