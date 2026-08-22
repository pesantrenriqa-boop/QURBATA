param(
  [string]$InputPath="$PSScriptRoot\..\dist\indesign-final\QURBATA-INDESIGN-DATA-MERGE-J1-J3.csv",
  [string]$OutputDir="$PSScriptRoot\..\dist\indesign-final-normalized"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)
if(!(Test-Path $InputPath)){throw "Input not found: $InputPath"}
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$src=@(Import-Csv $InputPath)

function TemplateColumns([int]$j){if($j-le2){return 4};if($j-eq3){return 3};return 0}
function GetSequentialItems($row){
  $items=@()
  for($r=1;$r-le8;$r++){
    for($c=1;$c-le4;$c++){
      $p=('Row{0:D2}Cell{1:D2}' -f $r,$c)
      $v=[string]$row.$p
      if(-not [string]::IsNullOrWhiteSpace($v)){$items+=$v}
    }
  }
  return @($items)
}

$out=@();$audit=@()
foreach($row in $src){
  $j=[int]$row.Jilid
  $cols=TemplateColumns $j
  if($cols-le0){continue}
  $items=@(GetSequentialItems $row)
  $capacity=8*$cols
  $o=[ordered]@{
    PageCode=$row.PageCode;Jilid=$row.Jilid;PageNumber=$row.PageNumber;PageTitle=$row.PageTitle;
    Focus=$row.Focus;MainMaterial=$row.MainMaterial;ContentStatus=$row.ContentStatus;
    TemplateColumns=$cols;TemplateRows=8;TemplateCapacity=$capacity;SourceItemCount=$items.Count;
    ContentPreserved=($true);LayoutStatus=''
  }
  $idx=0
  for($r=1;$r-le8;$r++){
    $o[('Row{0:D2}Count' -f $r)]=$cols
    for($c=1;$c-le4;$c++){
      $p=('Row{0:D2}Cell{1:D2}' -f $r,$c)
      if($c-le$cols -and $idx-lt$items.Count){$o[$p]=[string]$items[$idx];$idx++}else{$o[$p]=''}
    }
  }
  $blank=$capacity-$items.Count
  if($blank-lt0){$status='OVER_CAPACITY'}elseif($blank-eq0){$status='FULL'}else{$status='PADDED_EMPTY_CELLS'}
  $o.LayoutStatus=$status
  $out += [pscustomobject]$o
  $audit += [pscustomobject]@{
    PageCode=$row.PageCode;Jilid=$j;TemplateColumns=$cols;TemplateRows=8;TemplateCapacity=$capacity;
    SourceItemCount=$items.Count;EmptyTemplateCells=[math]::Max(0,$blank);OverflowItems=[math]::Max(0,-$blank);
    LayoutStatus=$status;ContentChanged='False'
  }
}

$all=Join-Path $OutputDir 'QURBATA-INDESIGN-NORMALIZED-J1-J3.csv'
$aud=Join-Path $OutputDir 'QURBATA-INDESIGN-NORMALIZED-AUDIT.csv'
[IO.File]::WriteAllLines($all,($out|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllLines($aud,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
foreach($j in 1..3){$part=@($out|Where-Object{[int]$_.Jilid-eq$j});if($part.Count){$p=Join-Path $OutputDir ("QURBATA-INDESIGN-J{0}-{1}COL.csv" -f $j,(TemplateColumns $j));[IO.File]::WriteAllLines($p,($part|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}}
Write-Host 'QURBATA InDesign normalized template map complete'
foreach($g in ($audit|Group-Object Jilid|Sort-Object Name)){
  $full=@($g.Group|Where-Object{$_.LayoutStatus-eq'FULL'}).Count
  $pad=@($g.Group|Where-Object{$_.LayoutStatus-eq'PADDED_EMPTY_CELLS'}).Count
  $over=@($g.Group|Where-Object{$_.LayoutStatus-eq'OVER_CAPACITY'}).Count
  $empty=($g.Group|Measure-Object EmptyTemplateCells -Sum).Sum
  Write-Host ("Jilid {0}: pages={1} cols={2} full={3} padded={4} over={5} empty-cells={6}" -f $g.Name,$g.Count,(TemplateColumns([int]$g.Name)),$full,$pad,$over,$empty)
}
Write-Host ("Normalized CSV : {0}" -f $all)
Write-Host ("Audit CSV      : {0}" -f $aud)
