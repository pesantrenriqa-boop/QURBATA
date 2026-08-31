param([string]$ProgId='')
$ErrorActionPreference='Stop'
$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path
$JsxPath=Join-Path $PSScriptRoot 'indesign-qurbata-j1-apply-competency-blocks.jsx'
$DataPath=Join-Path $RepoRoot 'dist\indesign-template-data\QURBATA-J1-40P-COMPETENCY.tsv'
if (!(Test-Path $JsxPath)) { throw "JSX not found: $JsxPath" }
if (!(Test-Path $DataPath)) { throw "Competency register not found: $DataPath. Run build-qurbata-j1-40p-competency.ps1 first." }
$app=New-Object -ComObject InDesign.Application
Write-Host "Active doc : $($app.ActiveDocument.Name)"
Write-Host "Pages      : $($app.ActiveDocument.Pages.Count)"
if ([int]$app.ActiveDocument.Pages.Count -ne 40) { throw 'Active document must be the 40-page QURBATA J1 production document.' }
$jsx=[IO.File]::ReadAllText($JsxPath,[Text.Encoding]::UTF8)
$null=$app.DoScript($jsx,1246973031)
Write-Host 'Competency blocks applied.'
Write-Host "Pages      : $($app.ActiveDocument.Pages.Count)"