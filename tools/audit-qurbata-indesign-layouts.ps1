param(
  [string]$CsvPath="$PSScriptRoot\..\dist\indesign-final\QURBATA-INDESIGN-DATA-MERGE-J1-J3.csv"
)
$ErrorActionPreference='Stop'
if(!(Test-Path $CsvPath)){throw "CSV not found: $CsvPath"}
$rows=@(Import-Csv $CsvPath)
Write-Host 'QURBATA InDesign layout audit'
foreach($j in 1..3){
  $jr=@($rows|Where-Object{[int]$_.Jilid-eq$j})
  Write-Host ("Jilid {0} pages : {1}" -f $j,$jr.Count)
  foreach($g in ($jr|Group-Object LayoutKey|Sort-Object Count -Descending)){
    Write-Host ("  {0}  => {1}" -f $g.Name,$g.Count)
  }
}
