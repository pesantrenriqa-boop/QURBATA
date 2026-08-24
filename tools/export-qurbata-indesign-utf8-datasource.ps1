param(
  [string]$InputDir="$PSScriptRoot\..\dist\indesign-template-data",
  [string]$OutputDir="$PSScriptRoot\..\dist\indesign-template-data"
)
$ErrorActionPreference='Stop'
$utf8NoBom=New-Object System.Text.UTF8Encoding($false)
function Export-TabUtf8([string]$src,[string]$dst){
  if(!(Test-Path $src)){throw "Input not found: $src"}
  $data=@(Import-Csv $src)
  if($data.Count-eq0){throw "No rows in: $src"}
  $headers=@($data[0].PSObject.Properties.Name)
  $lines=New-Object System.Collections.Generic.List[string]
  $lines.Add(($headers -join "`t"))
  foreach($row in $data){
    $vals=foreach($h in $headers){
      $v=[string]$row.$h
      $v=$v.Replace("`t",' ').Replace("`r",' ').Replace("`n",' ')
      $v
    }
    $lines.Add(($vals -join "`t"))
  }
  [IO.File]::WriteAllLines($dst,$lines,$utf8NoBom)
  $test=@(Get-Content $dst -Encoding UTF8 | Select-Object -First 2)
  $hc=(($test[0]-split"`t").Count);$dc=(($test[1]-split"`t").Count)
  if($hc-ne$dc){throw "Column mismatch in $dst header=$hc data=$dc"}
  Write-Host ("{0}: rows={1} columns={2}" -f ([IO.Path]::GetFileName($dst)),$data.Count,$hc)
}
New-Item -ItemType Directory -Force -Path $OutputDir|Out-Null
Export-TabUtf8 (Join-Path $InputDir 'QURBATA-INDESIGN-J1-4COL-8ROW.csv') (Join-Path $OutputDir 'QURBATA-INDESIGN-J1-4COL-8ROW-UTF8.txt')
Export-TabUtf8 (Join-Path $InputDir 'QURBATA-INDESIGN-J2-4COL-8ROW.csv') (Join-Path $OutputDir 'QURBATA-INDESIGN-J2-4COL-8ROW-UTF8.txt')
Export-TabUtf8 (Join-Path $InputDir 'QURBATA-INDESIGN-J3-3COL-8ROW.csv') (Join-Path $OutputDir 'QURBATA-INDESIGN-J3-3COL-8ROW-UTF8.txt')
Write-Host 'QURBATA InDesign UTF-8 data sources ready'
