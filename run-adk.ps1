param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$AdkArgs
)

Set-Location $PSScriptRoot

if (-not $AdkArgs -or $AdkArgs.Count -eq 0) {
    $AdkArgs = @('web', '.')
}

Write-Host "Starting ADK in env 'adk-env' with: adk $($AdkArgs -join ' ')"
conda run --no-capture-output -n adk-env adk @AdkArgs