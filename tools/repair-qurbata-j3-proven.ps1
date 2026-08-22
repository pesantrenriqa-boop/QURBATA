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

$map=@{
  '011-015'='QJ3-B02A-Materi-P011-P015.md'
  '016-020'='QJ3-B02B-Materi-P016-P020.md'
  '021-025'='QJ3-B03A-Materi-P021-P025.md'
  '026-030'='QJ3-B03B-Materi-P026-P030.md'
  '031-035'='QJ3-B04A-Materi-P031-P035.md'
  '036-040'='QJ3-B04B-Materi-P036-P040.md'
}
function SourceFor([int]$n){
  if($n-le15){return $map['011-015']}
  if($n-le20){return $map['016-020']}
  if($n-le25){return $map['021-025']}
  if($n-le30){return $map['026-030']}
  if($n-le35){return $map['031-035']}
  return $map['036-040']
}
function ParsePage([string]$path,[string]$code){
  $lines=Get-Content -LiteralPath $path -Encoding UTF8
  $startHit=$lines|Select-String ("^## {0}\b" -f [regex]::Escape($code))|Select-Object -First 1
  if(!$startHit){return [pscustomobject]@{Count=0;Arr=(New-Object 'object[]' 25)}}
  $start=$startHit.LineNumber
  $nextHit=$lines|Select-String '^## QJ3-P\d{3}\b'|Where-Object{$_.LineNumber -gt $start}|Select-Object -First 1
  $end=if($nextHit){$nextHit.LineNumber}else{$lines.Count+1}
  $block=$lines[($start-1)..($end-2)]
  $arr=New-Object 'object[]' 25
  foreach($line in $block){
    if($line -notmatch '^\s*\|'){continue}
    $cells=@(($line.Trim().Trim('|') -split '\|')|ForEach-Object{$_.Trim()})
    if($cells.Count-lt3){continue}
    if($cells[1] -match '^\s*(\d{1,2})\s*[–—-]\s*(\d{1,2})\s*$'){
      $a=[int]$Matches[1];$b=[int]$Matches[2]
      $items=@($cells[2] -split '\s*[·•]\s*'|ForEach-Object{$_.Trim()}|Where-Object{$_})
      if($items.Count-eq($b-$a+1)){
        for($i=0;$i-lt$items.Count;$i++){$arr[$a+$i]=$items[$i]}
      }
    }
  }
  $count=@($arr[1..24]|Where-Object{$_}).Count
  return [pscustomobject]@{Count=$count;Arr=$arr}
}

$fixed=0;$review=0
for($n=11;$n-le40;$n++){
  $code=('QJ3-P{0:D3}' -f $n)
  $file=SourceFor $n
  $path=Join-Path $RepoRoot ("books\jilid-3\pages\$file")
  $result=ParsePage $path $code
  $count=[int]$result.Count
  Write-Host ("{0} parsed slots : {1}" -f $code,$count)
  $row=$master|Where-Object{$_.PageCode-eq$code}|Select-Object -First 1
  if(!$row){continue}
  if($count-eq24){
    $arr=$result.Arr
    for($i=1;$i-le24;$i++){$row.('Slot{0:D2}'-f$i)=[string]$arr[$i]}
    for($r=1;$r-le8;$r++){
      $row.('Row{0:D2}Count'-f$r)=3
      for($c=1;$c-le4;$c++){
        $idx=($r-1)*3+$c
        $row.('Row{0:D2}Cell{1:D2}'-f$r,$c)=if($c-le3){[string]$arr[$idx]}else{''}
      }
    }
    $row.ContentStatus='FILLED_24';$fixed++
  } else {$row.ContentStatus='PARTIAL_REVIEW';$review++}
  $ar=$audit|Where-Object{$_.PageCode-eq$code}|Select-Object -First 1
  if($ar){$ar.ReadingCount=[string]$count;$ar.ContentStatus=$row.ContentStatus;$ar.SourceFile=("books/jilid-3/pages/$file")}
}
[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}
Write-Host 'QURBATA J3 proven repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $review"
Write-Host "Master                : $MasterPath"
