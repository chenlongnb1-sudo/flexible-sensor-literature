$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent $PSScriptRoot
$LogDir = Join-Path $Root 'logs'
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$Stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$Log = Join-Path $LogDir "daily-literature-$Stamp.log"

Start-Transcript -Path $Log -Append | Out-Null
try {
    Set-Location -LiteralPath $Root
    $Python = (Get-Command py -ErrorAction SilentlyContinue).Source
    if (-not $Python) { $Python = (Get-Command python -ErrorAction Stop).Source }

    & $Python -m scripts.daily_literature_pipeline --git-sync
    if ($LASTEXITCODE -ne 0) { throw "daily_literature_pipeline exited with code $LASTEXITCODE" }

    & $Python scripts/send_daily_notification.py
    if ($LASTEXITCODE -ne 0) { throw "send_daily_notification exited with code $LASTEXITCODE" }
}
finally {
    Stop-Transcript | Out-Null
}
