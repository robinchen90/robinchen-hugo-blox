<#
.SYNOPSIS
  Submit one or more URLs to IndexNow so Bing/Yandex re-crawl them fast.

.DESCRIPTION
  Pings the shared IndexNow endpoint (api.indexnow.org), which forwards to all
  participating engines (Bing, Yandex, etc.). Use after publishing or editing a
  page. Only submit URLs that actually changed — re-submitting unchanged pages in
  bulk can trip rate limiting (HTTP 429). Bulk discovery is already handled by
  sitemap.xml; this is just for fast updates.

  The IndexNow key is public by design (it is hosted at the keyLocation URL), so
  keeping it in this script is fine.

.PARAMETER Urls
  One or more full URLs on robinchen.org to submit.

.EXAMPLE
  .\submit-indexnow.ps1 https://robinchen.org/post/new-paper/

.EXAMPLE
  .\submit-indexnow.ps1 https://robinchen.org/ https://robinchen.org/publication/
#>

[CmdletBinding()]
param(
  [Parameter(Mandatory = $true, ValueFromRemainingArguments = $true)]
  [string[]]$Urls
)

$Host_       = "robinchen.org"
$Key         = "79d5b075188d4e8cb676a5531a8fe163"
$KeyLocation = "https://robinchen.org/$Key.txt"
$Endpoint    = "https://api.indexnow.org/indexnow"

# Sanity-check that every URL belongs to the host IndexNow will validate against.
$bad = $Urls | Where-Object { $_ -notmatch "^https?://$([regex]::Escape($Host_))/" }
if ($bad) {
  Write-Error "These URLs are not on https://$Host_/ and will be rejected:`n  $($bad -join "`n  ")"
  exit 1
}

$body = @{
  host        = $Host_
  key         = $Key
  keyLocation = $KeyLocation
  urlList     = $Urls
} | ConvertTo-Json

Write-Host "Submitting $($Urls.Count) URL(s) to IndexNow:" -ForegroundColor Cyan
$Urls | ForEach-Object { Write-Host "  $_" }

try {
  $resp = Invoke-WebRequest -Uri $Endpoint -Method Post `
            -ContentType "application/json; charset=utf-8" `
            -Body $body -UseBasicParsing
  $code = [int]$resp.StatusCode
  if ($code -eq 200 -or $code -eq 202) {
    Write-Host "Success: HTTP $code (accepted)." -ForegroundColor Green
  } else {
    Write-Host "Unexpected response: HTTP $code" -ForegroundColor Yellow
  }
} catch {
  $code = if ($_.Exception.Response) { [int]$_.Exception.Response.StatusCode } else { "n/a" }
  Write-Error "Submission failed (HTTP $code): $($_.Exception.Message)"
  # 400 = invalid format | 403 = key not found/invalid | 422 = URL/key mismatch | 429 = too many requests
  exit 1
}
