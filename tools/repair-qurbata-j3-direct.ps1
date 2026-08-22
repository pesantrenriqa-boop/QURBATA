param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$AuditPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-CONTENT-AUDIT.csv"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)
function SplitItems([string]$s){ if([string]::IsNullOrWhiteSpace($s)){return @()}; @($s -split '\s*[·•]\s*' | ForEach-Object {$_.Trim()} | Where-Object {$_}) }
function FilledCount([object[]]$arr){$n=0;for($i=1;$i-le24;$i++){if(-not [string]::IsNullOrWhiteSpace([string]$arr[$i])){$n++}};$n}
if(!(Test-Path $MasterPath)){throw "Master not found: $MasterPath"}
$master=@(Import-Csv $MasterPath)
$audit=if(Test-Path $AuditPath){@(Import-Csv $AuditPath)}else{@()}
$files=@('QJ3-B02A-Materi-P011-P015.md','QJ3-B02B-Materi-P016-P020.md','QJ3-B03A-Materi-P021-P025.md','QJ3-B03B-Materi-P026-P030.md','QJ3-B04A-Materi-P031-P035.md','QJ3-B04B-Materi-P036-P040.md')
$slotsByPage=@{};$fileByPage=@{}
foreach($name in $files){
 $path=Join-Path $RepoRoot "books\jilid-3\pages\$name";if(!(Test-Path $path)){continue}
 $code=$null
 foreach($line in Get-Content -LiteralPath $path -Encoding UTF8){
   if($line.StartsWith('## QJ3-P')){
     $m=[regex]::Match($line,'QJ3-P[0-9]{3}')
     if($m.Success){$code=$m.Value;if(-not $slotsByPage.ContainsKey($code)){$slotsByPage[$code]=New-Object 'object[]' 25};$fileByPage[$code]="books/jilid-3/pages/$name"}
     continue
   }
   if(!$code -or !$line.StartsWith('|')){continue}
   $cells=@($line.Trim().Trim('|').Split('|') | ForEach-Object {$_.Trim()})
   if($cells.Count -lt 3){continue}
   $range=$cells[1]
   $rm=[regex]::Match($range,'^([0-9]{1,2})[ ]*[–—-][ ]*([0-9]{1,2})$')
   if(!$rm.Success){continue}
   $a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$need=$b-$a+1
   $items=@(SplitItems $cells[2])
   if($items.Count -ne $need){continue}
   $arr=[object[]]$slotsByPage[$code]
   for($i=0;$i-lt$need;$i++){$arr[$a+$i]=$items[$i]}
   $slotsByPage[$code]=$arr
 }
}
$fixed=0;$still=0
foreach($page in $master){
 if([int]$page.Jilid-ne3 -or -not $slotsByPage.ContainsKey($page.PageCode)){continue}
 $arr=[object[]]$slotsByPage[$page.PageCode];$count=FilledCount $arr
 Write-Host ("{0} parsed slots : {1}" -f $page.PageCode,$count)
 if($count-eq24){
   for($i=1;$i-le24;$i++){$page.('Slot{0:D2}'-f$i)=[string]$arr[$i]}
   for($r=1;$r-le8;$r++){$page.('Row{0:D2}Count'-f$r)=3;for($c=1;$c-le4;$c++){$idx=($r-1)*3+$c;$page.('Row{0:D2}Cell{1:D2}'-f$r,$c)=if($c-le3){[string]$arr[$idx]}else{''}}}
   $page.ContentStatus='FILLED_24';$fixed++
 } else {$page.ContentStatus='PARTIAL_REVIEW';$still++}
 $ar=$audit|Where-Object{$_.PageCode-eq$page.PageCode}|Select-Object -First 1
 if($ar){$ar.ReadingCount=[string]$count;$ar.ContentStatus=$page.ContentStatus;$ar.SourceFile=$fileByPage[$page.PageCode]}
}
[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}
Write-Host 'QURBATA J3 direct repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $still"
Write-Host "Master                : $MasterPath"
