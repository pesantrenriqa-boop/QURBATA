param(
  [string]$InputPath="$PSScriptRoot\..\dist\indesign-final-normalized\QURBATA-INDESIGN-NORMALIZED-J1-J3.csv",
  [string]$OutputDir="$PSScriptRoot\..\dist\indesign-template-data"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)
if(!(Test-Path $InputPath)){throw "Input not found: $InputPath"}
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$rows=@(Import-Csv $InputPath)

function Get-Text($row,[string]$name){
  $p=$row.PSObject.Properties[$name]
  if($null -eq $p){return ''}
  return [string]$p.Value
}
function Put([ordered]$o,[string]$name,[string]$value){$o[$name]=$value}

$out=@()
foreach($row in $rows){
  $j=[int]$row.Jilid
  $cols=if($j-le2){4}else{3}
  $o=[ordered]@{
    PageCode=$row.PageCode
    Jilid=$row.Jilid
    PageNumber=$row.PageNumber
    PageTitle=$row.PageTitle
    Focus=$row.Focus
    MainMaterial=$row.MainMaterial
    TemplateColumns=$cols
    TemplateRows=8
    TemplateKey=("J{0}-{1}COL-8ROW" -f $j,$cols)
    ContentStatus=$row.ContentStatus
  }
  for($r=1;$r-le8;$r++){
    Put $o ("Row{0:D2}Count" -f $r) ([string]$cols)
    for($c=1;$c-le4;$c++){
      $name=("Row{0:D2}Cell{1:D2}" -f $r,$c)
      Put $o $name (Get-Text $row $name)
    }
  }
  $out += [pscustomobject]$o
}

$all=Join-Path $OutputDir 'QURBATA-INDESIGN-TEMPLATE-DATA-J1-J3.csv'
[IO.File]::WriteAllLines($all,($out|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
foreach($j in 1..3){
  $part=@($out|Where-Object{[int]$_.Jilid-eq$j})
  if($part.Count){
    $p=Join-Path $OutputDir ("QURBATA-INDESIGN-J{0}-{1}COL-8ROW.csv" -f $j,(if($j-le2){4}else{3}))
    [IO.File]::WriteAllLines($p,($part|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
  }
}
Write-Host 'QURBATA InDesign template data build complete'
foreach($g in ($out|Group-Object TemplateKey|Sort-Object Name)){Write-Host ("{0}: {1} pages" -f $g.Name,$g.Count)}
Write-Host ("CSV: {0}" -f $all)
