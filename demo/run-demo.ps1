[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string] $Weights,

    [string] $Video = (Join-Path $PSScriptRoot 'input.mp4')
)

$ErrorActionPreference = 'Stop'
$checkpoint = Get-Item -LiteralPath $Weights
$clip = Get-Item -LiteralPath $Video
if ($checkpoint.PSIsContainer -or $checkpoint.Extension -ine '.pt' -or $checkpoint.Length -eq 0) {
    throw 'Weights must be a non-empty .pt checkpoint.'
}
if ($clip.PSIsContainer -or $clip.Length -eq 0) {
    throw 'Video must be a non-empty file.'
}
$yolo = Get-Command yolo
$project = Split-Path -Parent $PSScriptRoot
$output = Join-Path $project 'runs\robotaxi'
$run = 'demo-' + (Get-Date -Format 'yyyyMMdd-HHmmss-fff')
& $yolo segment predict "model=$($checkpoint.FullName)" "source=$($clip.FullName)" 'imgsz=640' 'save=True' "project=$output" "name=$run"
if ($LASTEXITCODE -ne 0) {
    throw "Ultralytics predict failed with exit code $LASTEXITCODE."
}
Write-Output (Join-Path $output $run)
