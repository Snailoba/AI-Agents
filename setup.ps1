param(
    [switch]$Recreate
)

Set-Location $PSScriptRoot

$VenvPath = Join-Path $PSScriptRoot ".venv"
$PythonExe = Join-Path $VenvPath "Scripts\python.exe"

if ($Recreate -and (Test-Path $VenvPath)) {
    Remove-Item -Recurse -Force $VenvPath
}

if (-not (Test-Path $PythonExe)) {
    $PythonLauncher = Get-Command py -ErrorAction SilentlyContinue
    if ($PythonLauncher) {
        & py -3 -m venv $VenvPath
    } else {
        $SystemPython = Get-Command python -ErrorAction SilentlyContinue
        if ($SystemPython) {
            & python -m venv $VenvPath
        } else {
            throw "Python was not found. Install Python 3, then rerun .\setup.ps1."
        }
    }
}

& $PythonExe -m pip install --upgrade pip
& $PythonExe -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")

Write-Host ""
Write-Host "Setup complete."
Write-Host "CrewAI: python agent.py"
Write-Host "ADK: adk web ."