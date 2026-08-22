param(
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$OutputDir="$PSScriptRoot\..\dist\indesign-final",
  [int]$MaxJilid=3
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

if(!(Test-Path $MasterPath)){throw "Master not found: $MasterPath"}
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$master=@(Import-Csv $MasterPath)

function AsBool($v){return ([string]$v -match '^(?i:true|1|yes)$')}
function Get-RowCount($row,[int]$r){
  $p=('Row{0:D2}Count' -f $r)
  $v=$row.$p
  if($null -eq $v -or [string]::IsNullOrWhiteSpace([string]$v)){return 0}
  return [int]$v
}
function Get-LayoutKey($row){
  $a=@();for($r=1;$r-le8;$r++){$a+=([string](Get-RowCount $row $r))}
  return ($a -join '-')
}
function Get-UniformLayout($row){
  $a=@();for($r=1;$r-le8;$r++){$a+=(Get-RowCount $row $r)}
  $nz=@($a|Where-Object{$_ -gt0}|Select-Object -Unique)
  if($nz.Count-eq1){return [int]$nz[0]}
  return 0
}
function NonEmptyCellCount($row){
  $n=0
  for($r=1;$r-le8;$r++){
    for($c=1;$c-le4;$c++){
      $p=('Row{0:D2}Cell{1:D2}' -f $r,$c)
      if(-not [string]::IsNullOrWhiteSpace([string]$row.$p)){$n++}
    }
  }
  return $n
}

$rows=@($master | Where-Object {
  [int]$_.Jilid -le $MaxJilid -and (AsBool $_.TartilPage)
} | Sort-Object {[int]$_.Jilid},{[int]$_.PageNumber})

$export=@()
$audit=@()
foreach($row in $rows){
  $layoutKey=Get-LayoutKey $row
  $uniform=Get-UniformLayout $row
  $cellCount=NonEmptyCellCount $row
  $o=[ordered]@{
    PageCode=$row.PageCode
    Jilid=$row.Jilid
    PageNumber=$row.PageNumber
    PageTitle=("QURBATA JILID {0} - HALAMAN {1}" -f $row.Jilid,$row.PageNumber)
    Focus=$row.Focus
    MainMaterial=$row.MainMaterial
    ContentStatus=$row.ContentStatus
    LayoutKey=$layoutKey
    UniformColumns=$uniform
  }
  for($r=1;$r-le8;$r++){
    $o[('Row{0:D2}Count' -f $r)]=Get-RowCount $row $r
    for($c=1;$c-le4;$c++){
      $p=('Row{0:D2}Cell{1:D2}' -f $r,$c)
      $o[$p]=[string]$row.$p
    }
  }
  $export += [pscustomobject]$o
  $status=if($cellCount-gt0 -and @((1..8)|Where-Object{(Get-RowCount $row $_)-le0}).Count-eq0){'READY_FOR_INDDesign'}else{'REVIEW'}
  $audit += [pscustomobject]@{
    PageCode=$row.PageCode;Jilid=$row.Jilid;PageNumber=$row.PageNumber;ContentStatus=$row.ContentStatus;
    LayoutKey=$layoutKey;UniformColumns=$uniform;NonEmptyCells=$cellCount;InDesignStatus=$status
  }
}

$allPath=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA-MERGE-J1-J3.csv'
$auditPath=Join-Path $OutputDir 'QURBATA-INDESIGN-AUDIT-J1-J3.csv'
[IO.File]::WriteAllLines($allPath,($export|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllLines($auditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)

foreach($cols in 1..4){
  $part=@($export|Where-Object{[int]$_.UniformColumns -eq $cols})
  if($part.Count){
    $p=Join-Path $OutputDir ("QURBATA-INDESIGN-{0}COL.csv" -f $cols)
    [IO.File]::WriteAllLines($p,($part|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
  }
}
$mixed=@($export|Where-Object{[int]$_.UniformColumns -eq0})
if($mixed.Count){[IO.File]::WriteAllLines((Join-Path $OutputDir 'QURBATA-INDESIGN-MIXED.csv'),($mixed|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}

$ready=@($audit|Where-Object{$_.InDesignStatus-eq'READY_FOR_INDDesign'}).Count
$review=$audit.Count-$ready
Write-Host 'QURBATA InDesign final export complete'
Write-Host ("Pages exported        : {0}" -f $export.Count)
Write-Host ("Ready for InDesign    : {0}" -f $ready)
Write-Host ("Review                : {0}" -f $review)
foreach($g in ($export|Group-Object UniformColumns|Sort-Object Name)){Write-Host ("Layout columns {0}      : {1}" -f $g.Name,$g.Count)}
Write-Host ("Data Merge CSV        : {0}" -f $allPath)
Write-Host ("Audit CSV             : {0}" -f $auditPath)
