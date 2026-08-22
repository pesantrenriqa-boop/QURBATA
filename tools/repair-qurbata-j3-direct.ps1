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

$files=@(
 'QJ3-B02A-Materi-P011-P015.md',
 'QJ3-B02B-Materi-P016-P020.md',
 'QJ3-B03A-Materi-P021-P025.md',
 'QJ3-B03B-Materi-P026-P030.md',
 'QJ3-B04A-Materi-P031-P035.md',
 'QJ3-B04B-Materi-P036-P040.md'
)

$parsed=@{}

foreach($name in $files){
  $path=Join-Path $RepoRoot "books\jilid-3\pages\$name"
  if(!(Test-Path $path)){continue}

  $lines=@(Get-Content -LiteralPath $path -Encoding UTF8)
  $heads=@($lines | Select-String '^## QJ3-P\d{3}\b')

  for($h=0;$h-lt$heads.Count;$h++){
    $start=[int]$heads[$h].LineNumber
    $end=if($h+1-lt$heads.Count){[int]$heads[$h+1].LineNumber}else{$lines.Count+1}
    $code=([regex]::Match($heads[$h].Line,'QJ3-P\d{3}')).Value
    if(!$code){continue}

    $block=@($lines[($start-1)..($end-2)])
    $arr=[object[]]::new(25)

    foreach($line in $block){
      if($line -notmatch '^\s*\|'){continue}
      $cells=@(($line.Trim().Trim('|') -split '\|') | ForEach-Object {$_.Trim()})
      if($cells.Count-lt3){continue}
      if($cells[1] -notmatch '^\s*(\d{1,2})\s*[–—-]\s*(\d{1,2})\s*$'){continue}

      $a=[int]$Matches[1]
      $b=[int]$Matches[2]
      if($a-lt1-or$b-gt24-or$b-lt$a){continue}

      $items=@($cells[2] -split '\s*[·•]\s*' | ForEach-Object {$_.Trim()} | Where-Object {$_})
      if($items.Count-ne($b-$a+1)){continue}

      for($i=0;$i-lt$items.Count;$i++){$arr[$a+$i]=$items[$i]}
    }

    $count=@($arr[1..24] | Where-Object {$_}).Count
    $obj=[ordered]@{PageCode=$code;Count=$count;SourceFile="books/jilid-3/pages/$name"}
    for($i=1;$i-le24;$i++){$obj[('Slot{0:D2}'-f$i)]=[string]$arr[$i]}
    $parsed[$code]=[pscustomobject]$obj
  }
}

$fixed=0
$still=0
foreach($page in $master){
  if([int]$page.Jilid-ne3 -or -not $parsed.ContainsKey($page.PageCode)){continue}
  $p=$parsed[$page.PageCode]
  $count=[int]$p.Count
  Write-Host ("{0} parsed slots : {1}" -f $page.PageCode,$count)

  if($count-eq24){
    for($i=1;$i-le24;$i++){$page.('Slot{0:D2}'-f$i)=[string]$p.('Slot{0:D2}'-f$i)}
    for($r=1;$r-le8;$r++){
      $page.('Row{0:D2}Count'-f$r)=3
      for($c=1;$c-le4;$c++){
        $idx=($r-1)*3+$c
        $page.('Row{0:D2}Cell{1:D2}'-f$r,$c)=if($c-le3){[string]$p.('Slot{0:D2}'-f$idx)}else{''}
      }
    }
    $page.ContentStatus='FILLED_24'
    $fixed++
  }else{
    $page.ContentStatus='PARTIAL_REVIEW'
    $still++
  }

  $ar=$audit|Where-Object{$_.PageCode-eq$page.PageCode}|Select-Object -First 1
  if($ar){$ar.ReadingCount=[string]$count;$ar.ContentStatus=$page.ContentStatus;$ar.SourceFile=$p.SourceFile}
}

[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}

Write-Host 'QURBATA J3 direct repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $still"
Write-Host "Master                : $MasterPath"
