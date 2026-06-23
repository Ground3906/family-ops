# graph-auth.ps1 -- One-time device-code sign-in for Microsoft Graph
# Run once on the ThinkPad. Saves token to scripts/graph-token.json (gitignored).
# Re-run any time the token stops working.

$ClientId  = "eec121fa-f054-4214-af52-aa83371128ac"
$Scope     = "Calendars.ReadWrite User.Read offline_access"
$DeviceUrl = "https://login.microsoftonline.com/consumers/oauth2/v2.0/devicecode"
$TokenUrl  = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
$TokenFile = Join-Path $PSScriptRoot "graph-token.json"

# Request device code
Write-Host "Requesting device code..." -NoNewline
$DC = Invoke-RestMethod -Method Post -Uri $DeviceUrl `
    -ContentType "application/x-www-form-urlencoded" `
    -Body @{ client_id = $ClientId; scope = $Scope }
Write-Host " done."

Write-Host ""
Write-Host "=== ACTION REQUIRED ==="
Write-Host "1. Open any browser and go to:  $($DC.verification_uri)"
Write-Host "2. Enter this code:             $($DC.user_code)"
Write-Host "3. Sign in as matthew.bayer@outlook.com"
Write-Host "========================"
Write-Host ""
Write-Host "Waiting for sign-in" -NoNewline

# Poll for token
$Interval  = [int]$DC.interval
$ExpiresAt = (Get-Date).AddSeconds([int]$DC.expires_in)
$Token     = $null

while ((Get-Date) -lt $ExpiresAt) {
    Start-Sleep -Seconds $Interval
    try {
        $Token = Invoke-RestMethod -Method Post -Uri $TokenUrl `
            -ContentType "application/x-www-form-urlencoded" `
            -Body @{
                grant_type  = "urn:ietf:params:oauth2:grant-type:device_code"
                client_id   = $ClientId
                device_code = $DC.device_code
            } -ErrorAction Stop
        break
    } catch {
        $Err = $null
        try { $Err = $_.ErrorDetails.Message | ConvertFrom-Json } catch {}
        if ($Err -and $Err.error -eq "authorization_pending") { Write-Host "." -NoNewline; continue }
        if ($Err -and $Err.error -eq "slow_down")             { $Interval += 5; continue }
        Write-Host ""
        Write-Host "Auth error: $($Err.error) -- $($Err.error_description)"
        exit 1
    }
}

if (-not $Token) {
    Write-Host ""
    Write-Host "Timed out. Run the script again."
    exit 1
}

# Save token
@{
    access_token  = $Token.access_token
    refresh_token = $Token.refresh_token
    expires_at    = (Get-Date).AddSeconds([int]$Token.expires_in).ToString("o")
} | ConvertTo-Json | Set-Content -Path $TokenFile -Encoding UTF8

Write-Host ""
Write-Host "Auth complete. Token saved to $TokenFile"
Write-Host "Run graph-test-push.ps1 next."
