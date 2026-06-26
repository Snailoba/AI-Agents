param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CrewAiArgs
)

Set-Location $PSScriptRoot

if (-not $CrewAiArgs -or $CrewAiArgs.Count -eq 0) {
    $CrewAiArgs = @()
}

$PythonExe = Join-Path $PSScriptRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $PythonExe)) {
    throw "Missing .venv. Run .\setup.ps1 first."
}

& $PythonExe .\crewai_agent.py @CrewAiArgs