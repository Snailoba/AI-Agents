param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$AdkArgs
)

Set-Location $PSScriptRoot

if (-not $AdkArgs -or $AdkArgs.Count -eq 0) {
    $AdkArgs = @('web', '.')
}

$AdkExe = Join-Path $PSScriptRoot ".venv\Scripts\adk.exe"
$PythonExe = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not $env:OLLAMA_API_BASE) {
    $env:OLLAMA_API_BASE = "http://localhost:11434"
}

Write-Host "Starting ADK with: adk $($AdkArgs -join ' ')"

if (Test-Path $AdkExe) {
    & $AdkExe @AdkArgs
} elseif (Test-Path $PythonExe) {
    & $PythonExe -m adk @AdkArgs
} else {
    throw "Missing .venv. Run .\setup.ps1 first."
}