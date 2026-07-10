# graph-auth.ps1 - Browser-based OAuth for Microsoft Graph
# Device code flow is blocked for personal Microsoft accounts in Default Directory tenants.
# This script opens a browser on the local machine, captures the callback, saves the token.
# Run ONCE on a machine with a browser (Precision or ThinkPad with active session).
# Copy token file to ThinkPad after if run on Precision.
#
# Usage:
#   .\graph-auth.ps1                            # saves to graph-token.json (Matt)
#   .\graph-auth.ps1 -Out graph-token-kalea.json  # saves to separate file (Kalea)

param([string]$Out = "graph-token.json")

$ClientId    = "eec121fa-f054-4214-af52-aa83371128ac"
$RedirectUri = "http://localhost:8888/"
$Scope       = "Calendars.ReadWrite Mail.Send User.Read offline_access"
$AuthUrl     = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
$TokenUrl    = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
$TokenFile   = Join-Path $PSScriptRoot $Out

# Build auth URL
$State       = [System.Guid]::NewGuid().ToString("N")
$FullAuthUrl = $AuthUrl +
    "?client_id=$ClientId" +
    "&response_type=code" +
    "&redirect_uri=$([uri]::EscapeDataString($RedirectUri))" +
    "&scope=$([uri]::EscapeDataString($Scope))" +
    "&state=$State" +
    "&prompt=select_account"

# Start local listener
$Listener = [System.Net.HttpListener]::new()
$Listener.Prefixes.Add("http://localhost:8888/")
try {
    $Listener.Start()
} catch {
    Write-Host "Could not start listener on port 8888. Check if another process is using it."
    exit 1
}

# Open browser
Write-Host "Opening browser for sign-in..."
Write-Host "Sign in with the Microsoft account for: $Out"
Write-Host "Waiting for callback..." -NoNewline
Start-Process $FullAuthUrl

# Block until Microsoft redirects back
$Context  = $Listener.GetContext()
$Code     = $Context.Request.QueryString["code"]
$RetState = $Context.Request.QueryString["state"]
$ErrParam = $Context.Request.QueryString["error"]

# Close browser tab gracefully
$Html  = "<html><body style='font-family:sans-serif;padding:40px'><h2>Sign-in complete.</h2><p>You can close this window and return to PowerShell.</p></body></html>"
$Bytes = [System.Text.Encoding]::UTF8.GetBytes($Html)
$Context.Response.ContentLength64 = $Bytes.Length
$Context.Response.OutputStream.Write($Bytes, 0, $Bytes.Length)
$Context.Response.Close()
$Listener.Stop()

Write-Host " done."

if ($ErrParam) { Write-Host "Auth error from Microsoft: $ErrParam"; exit 1 }
if (-not $Code) { Write-Host "No auth code received. Try again."; exit 1 }
if ($RetState -ne $State) { Write-Host "State mismatch. Aborting."; exit 1 }

# Exchange code for tokens
Write-Host "Exchanging code for tokens..." -NoNewline
try {
    $T = Invoke-RestMethod -Method Post -Uri $TokenUrl `
        -ContentType "application/x-www-form-urlencoded" `
        -Body @{
            grant_type   = "authorization_code"
            client_id    = $ClientId
            code         = $Code
            redirect_uri = $RedirectUri
            scope        = $Scope
        } -ErrorAction Stop
} catch {
    Write-Host ""
    Write-Host "Token exchange failed: $_"
    exit 1
}

@{
    access_token  = $T.access_token
    refresh_token = $T.refresh_token
    expires_at    = (Get-Date).AddSeconds([int]$T.expires_in).ToString("o")
} | ConvertTo-Json | Set-Content -Path $TokenFile -Encoding UTF8

Write-Host " done."
Write-Host ""
Write-Host "=== AUTH COMPLETE ==="
Write-Host "Token saved: $TokenFile"
Write-Host ""
if ($Out -eq "graph-token.json") {
    Write-Host "Token includes Mail.Send scope. inbox-watcher.ps1 email alerts are now enabled."
    Write-Host "Run graph-test-push.ps1 to push the test event."
} else {
    Write-Host "Copy $TokenFile to the ThinkPad scripts/ folder."
    Write-Host "graph-sync.ps1 will pick it up automatically on the next run."
}
