param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$AuditPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-CONTENT-AUDIT.csv"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

function SplitItems([string]$s){
  if([string]::IsNullOrWhiteSpace($s)){ return @() }
  return @($s -split '\s*[·•]\s*|\s*\|\s*' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
}
function PutItems([object[]]$arr,[int]$a,[int]$b,[object[]]$items){
  $need=$b-$a+1
  if($a-lt1 -or $b-gt24 -or $items.Count-ne$need){ return $false }
  for($i=0;$i-lt$need;$i++){ $arr[$a+$i]=([string]$items[$i]).Trim() }
  return $true
}
function FilledCount([object[]]$arr){
  $n=0;for($i=1;$i-le24;$i++){if(-not [string]::IsNullOrWhiteSpace([string]$arr[$i])){$n++}};return $n
}

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
$slotsByPage=@{}
$fileByPage=@{}

foreach($name in $files){
  $path=Join-Path $RepoRoot "books\jilid-3\pages\$name"
  if(!(Test-Path $path)){continue}
  $code=$null;$pendingA=0;$pendingB=0;$numbered=@()
  foreach($line in @(Get-Content -LiteralPath $path -Encoding UTF8)){
    if($line -match '^##\s+(QJ3-P\d{3})(?:\s|$)'){
      $code=$Matches[1]
      if(-not $slotsByPage.ContainsKey($code)){$slotsByPage[$code]=New-Object 'object[]' 25}
      $fileByPage[$code]="books/jilid-3/pages/$name"
      $pendingA=0;$pendingB=0;$numbered=@();continue
    }
    if(!$code){continue}
    $arr=[object[]]$slotsByPage[$code]

    if($line -match '^\s*\|'){
      $cells=@(($line.Trim().Trim('|') -split '\|') | ForEach-Object{$_.Trim()})
      $rangeIndex=-1;$ra=0;$rb=0
      for($i=0;$i-lt$cells.Count;$i++){
        if($cells[$i] -match '^\s*(\d{1,2})\s*[–—-]\s*(\d{1,2})\s*$'){$rangeIndex=$i;$ra=[int]$Matches[1];$rb=[int]$Matches[2];break}
      }
      if($rangeIndex-ge0 -and $ra-ge1 -and $rb-le24){
        $need=$rb-$ra+1;$done=$false
        for($i=0;$i-lt$cells.Count;$i++){
          if($i-eq$rangeIndex){continue}
          $items=@(SplitItems $cells[$i])
          if($items.Count-eq$need){[void](PutItems $arr $ra $rb $items);$done=$true;break}
        }
        if(!$done -and $need-eq2){
          $vals=@()
          for($i=0;$i-lt$cells.Count;$i++){
            if($i-eq$rangeIndex){continue};$v=$cells[$i]
            if(!$v-or$v-eq'—'-or$v-match '^(pasangan|pembuka|fokus|murojaah|transfer|\d+\s*huruf)'){continue}
            foreach($x in @(SplitItems $v)){$vals+=$x}
          }
          if($vals.Count-ge2){[void](PutItems $arr $ra $rb @($vals[$vals.Count-2],$vals[$vals.Count-1]))}
        }
      }
      $slotsByPage[$code]=$arr
      continue
    }

    if($line -match '^\*\*Kotak(?:\s+pembuka)?\s+(\d{1,2})\s*[–—-]\s*(\d{1,2})[^*]*\*\*\s*:?\s*(.+)$'){
      $a=[int]$Matches[1];$b=[int]$Matches[2];$items=@(SplitItems $Matches[3]);if($items.Count-eq($b-$a+1)){[void](PutItems $arr $a $b $items)};$slotsByPage[$code]=$arr;continue
    }
    if($line -match '^\*\*Kotak(?:\s+pembuka)?\s+(\d{1,2})\s*[–—-]\s*(\d{1,2})[^*]*\*\*\s*:?\s*$'){
      $pendingA=[int]$Matches[1];$pendingB=[int]$Matches[2];$numbered=@();continue
    }
    if($line -match '^#{3,4}\s+.*?kotak\s+(\d{1,2})\s*[–—-]\s*(\d{1,2})'){
      $pendingA=[int]$Matches[1];$pendingB=[int]$Matches[2];$numbered=@();continue
    }

    if($pendingA-gt0){
      $need=$pendingB-$pendingA+1
      if($line -match '^\s*\d+\.\s+(.+?)\s*$'){
        $numbered+=$Matches[1].Trim()
        if($numbered.Count-eq$need){[void](PutItems $arr $pendingA $pendingB $numbered);$slotsByPage[$code]=$arr;$pendingA=0;$pendingB=0;$numbered=@()}
        continue
      }
      if([string]::IsNullOrWhiteSpace($line)-or$line-match '^\*\*(Source|Potongan)'){continue}
      $items=@(SplitItems $line)
      if($items.Count-eq$need){[void](PutItems $arr $pendingA $pendingB $items);$slotsByPage[$code]=$arr;$pendingA=0;$pendingB=0;$numbered=@();continue}
      if($line-match '^#{2,4}\s+'-or$line-match '^\*\*Kotak'){$pendingA=0;$pendingB=0;$numbered=@()}
    }
  }
}

$fixed=0;$still=0
foreach($page in $master){
  if([int]$page.Jilid-ne3 -or -not $slotsByPage.ContainsKey($page.PageCode)){continue}
  $arr=[object[]]$slotsByPage[$page.PageCode]
  $count=FilledCount $arr
  Write-Host ("{0} parsed slots : {1}" -f $page.PageCode,$count)
  if($count-eq24){
    for($i=1;$i-le24;$i++){$page.('Slot{0:D2}'-f$i)=[string]$arr[$i]}
    for($r=1;$r-le8;$r++){
      $page.('Row{0:D2}Count'-f$r)=3
      for($c=1;$c-le4;$c++){
        $idx=($r-1)*3+$c
        $page.('Row{0:D2}Cell{1:D2}'-f$r,$c)=if($c-le3){[string]$arr[$idx]}else{''}
      }
    }
    $page.ContentStatus='FILLED_24';$fixed++
  }else{$page.ContentStatus='PARTIAL_REVIEW';$still++}
  $ar=$audit|Where-Object{$_.PageCode-eq$page.PageCode}|Select-Object -First 1
  if($ar){$ar.ReadingCount=[string]$count;$ar.ContentStatus=$page.ContentStatus;$ar.SourceFile=$fileByPage[$page.PageCode]}
}
[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}
Write-Host 'QURBATA J3 direct repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $still"
Write-Host "Master                : $MasterPath"
