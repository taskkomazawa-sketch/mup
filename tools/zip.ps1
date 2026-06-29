$source = Get-Location
$zip = "mup_review.zip"

$temp = Join-Path $env:TEMP "mup_review"

if (Test-Path $temp) {
    Remove-Item $temp -Recurse -Force
}

New-Item -ItemType Directory -Path $temp | Out-Null

robocopy $source $temp /E `
    /XD .git .venv __pycache__ .pytest_cache .streamlit tools `
    /XF *.pyc > $null

if (Test-Path $zip) {
    Remove-Item $zip
}

Compress-Archive "$temp\*" $zip

Remove-Item $temp -Recurse -Force

Write-Host ""
Write-Host "Created $zip"