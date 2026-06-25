param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CrewAiArgs
)

Set-Location $PSScriptRoot

if (-not $CrewAiArgs -or $CrewAiArgs.Count -eq 0) {
    $CrewAiArgs = @()
}

conda run -n crewai-env python .\agent.py @CrewAiArgs