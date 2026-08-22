param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$AuditPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-CONTENT-AUDIT.csv"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)
if(!(Test-Path $MasterPath)){throw "Master not found: $MasterPath"}
$master=@(Import-Csv $MasterPath)
$audit=if(Test-Path $AuditPath){@(Import-Csv $AuditPath)}else{@()}

function Get-SourceFile([int]$n){
  if($n-le15){return 'QJ3-B02A-Materi-P011-P015.md'}
  if($n-le20){return 'QJ3-B02B-Materi-P016-P020.md'}
  if($n-le25){return 'QJ3-B03A-Materi-P021-P025.md'}
  if($n-le30){return 'QJ3-B03B-Materi-P026-P030.md'}
  if($n-le35){return 'QJ3-B04A-Materi-P031-P035.md'}
  return 'QJ3-B04B-Materi-P036-P040.md'
}

$rangePattern='^\s*(\d{1,2})\s*[\u2013\u2014-]\s*(\d{1,2})\s*$'
$itemSplitPattern='\s*[\u00B7\u2022]\s*'

$fixed=0
$review=0
for($n=11;$n-le40;$n++){
  $code=('QJ3-P{0:D3}' -f $n)
  $file=Get-SourceFile $n
  $path=Join-Path $RepoRoot ("books\jilid-3\pages\$file")
  $lines=@(Get-Content -LiteralPath $path -Encoding UTF8)

  $startIndex=-1
  for($i=0;$i-lt$lines.Count;$i++){
    if($lines[$i].StartsWith("## $code ") -or $lines[$i] -eq "## $code"){$startIndex=$i;break}
  }

  $arr=New-Object 'object[]' 25
  if($startIndex-ge0){
    $endIndex=$lines.Count
    for($i=$startIndex+1;$i-lt$lines.Count;$i++){
      if($lines[$i].StartsWith('## QJ3-P')){$endIndex=$i;break}
    }

    for($i=$startIndex;$i-lt$endIndex;$i++){
      $line=$lines[$i]
      if(!$line.TrimStart().StartsWith('|')){continue}

      $cells=@(($line.Trim().Trim('|') -split '\|') | ForEach-Object {$_.Trim()})
      if($cells.Count-lt3){continue}

      $range=$cells[1]
      if($range -match $rangePattern){
        $a=[int]$Matches[1]
        $b=[int]$Matches[2]
      } else {
        continue
      }
      $need=$b-$a+1

      $items=@($cells[2] -split $itemSplitPattern | ForEach-Object {$_.Trim()} | Where-Object {$_})
      if($items.Count-ne$need){continue}

      for($k=0;$k-lt$items.Count;$k++){$arr[$a+$k]=$items[$k]}
    }
  }

  $count=@($arr[1..24] | Where-Object {$_}).Count
  Write-Host ("{0} parsed slots : {1}" -f $code,$count)

  $row=$master | Where-Object {$_.PageCode -eq $code} | Select-Object -First 1
  if(!$row){continue}

  if($count-eq24){
    for($i=1;$i-le24;$i++){$row.('Slot{0:D2}'-f$i)=[string]$arr[$i]}
    for($r=1;$r-le8;$r++){
      $row.('Row{0:D2}Count'-f$r)=3
      for($c=1;$c-le4;$c++){
        $idx=($r-1)*3+$c
        if($c-le3){$row.('Row{0:D2}Cell{1:D2}'-f$r,$c)=[string]$arr[$idx]}else{$row.('Row{0:D2}Cell{1:D2}'-f$r,$c)=''}
      }
    }
    $row.ContentStatus='FILLED_24'
    $fixed++
  }else{
    $row.ContentStatus='PARTIAL_REVIEW'
    $review++
  }

  $ar=$audit | Where-Object {$_.PageCode -eq $code} | Select-Object -First 1
  if($ar){
    $ar.ReadingCount=[string]$count
    $ar.ContentStatus=$row.ContentStatus
    $ar.SourceFile=("books/jilid-3/pages/$file")
  }
}

[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}
Write-Host 'QURBATA J3 proven repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $review"
Write-Host "Master                : $MasterPath"
