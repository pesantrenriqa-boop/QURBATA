param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$AuditPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-CONTENT-AUDIT.csv"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)
function SplitCells([string]$line){$s=$line.Trim();if($s.StartsWith('|')){$s=$s.Substring(1)};if($s.EndsWith('|')){$s=$s.Substring(0,$s.Length-1)};return @($s -split '\|'|ForEach-Object{$_.Trim()})}
function PutRange([hashtable]$slots,[int]$a,[int]$b,[string[]]$items){if($a-lt1-or$b-gt24-or$b-lt$a){return};$need=$b-$a+1;if($items.Count-ne$need){return};for($i=0;$i-lt$need;$i++){$v=$items[$i].Trim();if($v-and-not$slots.ContainsKey($a+$i)){$slots[$a+$i]=$v}}}
function ParseFragment([string]$text){
  $slots=@{};$lines=$text-split "`r?`n"
  for($i=0;$i-lt$lines.Count-1;$i++){
    if($lines[$i]-notmatch '^\s*\|' -or $lines[$i+1]-notmatch '^\s*\|\s*:?-{2,}'){continue}
    for($r=$i+2;$r-lt$lines.Count;$r++){
      if($lines[$r]-notmatch '^\s*\|'){break};$c=@(SplitCells $lines[$r]);$rangeIdx=-1;$a=0;$b=0
      for($x=0;$x-lt$c.Count;$x++){$rm=[regex]::Match($c[$x],'^\s*(\d{1,2})\s*[–-]\s*(\d{1,2})\s*$');if($rm.Success){$rangeIdx=$x;$a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;break}}
      if($rangeIdx-lt0){continue};$need=$b-$a+1;$done=$false
      foreach($x in 0..($c.Count-1)){if($x-eq$rangeIdx){continue};$parts=@($c[$x]-split '\s*[·•]\s*'|Where-Object{$_ -and $_.Trim()});if($parts.Count-eq$need){PutRange $slots $a $b $parts;$done=$true;break}}
      if($done){continue}
      $vals=@();foreach($x in 0..($c.Count-1)){if($x-eq$rangeIdx){continue};$v=$c[$x].Trim();if(!$v-or$v-eq'—'-or$v-match '^(pembuka|pasangan|fokus|murojaah|transfer|\d+ huruf)'){continue};$vals+=$v}
      if($vals.Count-eq$need){PutRange $slots $a $b $vals}
    }
  }
  $rxBold=[regex]::Matches($text,'(?ms)\*\*Kotak\s+(\d{1,2})\s*[–-]\s*(\d{1,2})[^*]*\*\*\s*:?\s*(.*?)(?=\r?\n\s*(?:\*\*|###|##)|\z)')
  foreach($rm in $rxBold){$a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$body=$rm.Groups[3].Value.Trim();$parts=@($body -split '\s*[·•]\s*|\s*\|\s*'|ForEach-Object{($_ -replace '\s+',' ').Trim()}|Where-Object{$_});if($parts.Count-ge($b-$a+1)){PutRange $slots $a $b @($parts[0..($b-$a)])}}
  $rxHead=[regex]::Matches($text,'(?ms)^#{3,4}\s+(?:Tangga[^\r\n]*?—\s*)?kotak\s+(\d{1,2})\s*[–-]\s*(\d{1,2})[^\r\n]*\r?\n(.*?)(?=^#{2,4}\s+|^\*\*Kotak|\z)',[Text.RegularExpressions.RegexOptions]::IgnoreCase -bor [Text.RegularExpressions.RegexOptions]::Multiline)
  foreach($rm in $rxHead){$a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$body=$rm.Groups[3].Value.Trim();$need=$b-$a+1;$numbered=[regex]::Matches($body,'(?m)^\s*\d+\.\s+(.+?)\s*$');if($numbered.Count-eq$need){$vals=@();foreach($n in $numbered){$vals+=$n.Groups[1].Value.Trim()};PutRange $slots $a $b $vals;continue};$first=($body-split "`r?`n"|Where-Object{$_ -and $_ -notmatch '^\*\*Source' -and $_ -notmatch '^\*\*Potongan'}|Select-Object -First 1);$parts=@($first -split '\s*\|\s*|\s*[·•]\s*'|Where-Object{$_ -and $_.Trim()});if($parts.Count-eq$need){PutRange $slots $a $b $parts}}
  $rxPlain=[regex]::Matches($text,'(?ms)(?:Kotak pembuka|Kotak)\s+(\d{1,2})\s*[–-]\s*(\d{1,2})\s*:\*?\*?\s*\r?\n?([^\r\n#]+)',[Text.RegularExpressions.RegexOptions]::IgnoreCase)
  foreach($rm in $rxPlain){$a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$parts=@($rm.Groups[3].Value -split '\s*[·•]\s*|\s*\|\s*'|Where-Object{$_ -and $_.Trim()});if($parts.Count-eq($b-$a+1)){PutRange $slots $a $b $parts}}
  # Special paired tables like QJ3-P032: one range maps to two reading columns.
  for($i=0;$i-lt$lines.Count-1;$i++){
    if($lines[$i]-notmatch '^\s*\|'){continue}
    $hdr=@(SplitCells $lines[$i]);if($hdr.Count-lt4){continue}
    if(($hdr -join ' ') -notmatch 'Tanpa ال' -or ($hdr -join ' ') -notmatch 'Dengan ال'){continue}
    for($r=$i+2;$r-lt$lines.Count;$r++){
      if($lines[$r]-notmatch '^\s*\|'){break};$c=@(SplitCells $lines[$r]);if($c.Count-lt4){continue}
      $rm=[regex]::Match($c[1],'^\s*(\d{1,2})\s*[–-]\s*(\d{1,2})\s*$');if(!$rm.Success){continue};$a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$need=$b-$a+1
      if($need-eq2 -and $c[2] -and $c[3] -and $c[3]-ne'—'){PutRange $slots $a $b @($c[2],$c[3])}
      elseif($need-eq4){$parts=@($c[2]-split '\s*[·•]\s*'|Where-Object{$_});if($parts.Count-eq4){PutRange $slots $a $b $parts}}
    }
  }
  return $slots
}
function MakeLayout([hashtable]$slots){$vals=@();for($i=1;$i-le24;$i++){if($slots.ContainsKey($i)){$vals+=$slots[$i]}else{$vals+=''}};$rows=@();for($r=0;$r-lt8;$r++){$cells=@($vals[($r*3)..($r*3+2)]);$rows+=[pscustomobject]@{Count=3;Cells=@($cells[0],$cells[1],$cells[2],'')}};return @($rows)}
if(!(Test-Path $MasterPath)){throw "Master not found: $MasterPath"}
$master=@(Import-Csv $MasterPath);$audit=@();if(Test-Path $AuditPath){$audit=@(Import-Csv $AuditPath)}
$files=@('QJ3-B02A-Materi-P011-P015.md','QJ3-B02B-Materi-P016-P020.md','QJ3-B03A-Materi-P021-P025.md','QJ3-B03B-Materi-P026-P030.md','QJ3-B04A-Materi-P031-P035.md','QJ3-B04B-Materi-P036-P040.md')
$parsed=@{}
foreach($name in $files){$path=Join-Path $RepoRoot ("books\jilid-3\pages\$name");if(!(Test-Path $path)){continue};$t=[IO.File]::ReadAllText($path,[Text.Encoding]::UTF8);$ms=[regex]::Matches($t,'(?m)^##\s+(QJ3-P\d{3})\b.*$');for($i=0;$i-lt$ms.Count;$i++){$start=$ms[$i].Index;$end=if($i+1-lt$ms.Count){$ms[$i+1].Index}else{$t.Length};$frag=$t.Substring($start,$end-$start);$parsed[$ms[$i].Groups[1].Value]=[pscustomobject]@{Slots=(ParseFragment $frag);File=("books/jilid-3/pages/$name")}}}
$fixed=0;$still=0
foreach($m in $master){if([int]$m.Jilid-ne3-or-not$parsed.ContainsKey($m.PageCode)){continue};$p=$parsed[$m.PageCode];$slots=$p.Slots;$count=$slots.Count;if($count-eq24){for($i=1;$i-le24;$i++){$n=('Slot{0:D2}'-f$i);$m.$n=$slots[$i]};$lay=@(MakeLayout $slots);for($r=1;$r-le8;$r++){$m.('Row{0:D2}Count'-f$r)=$lay[$r-1].Count;for($c=1;$c-le4;$c++){$m.('Row{0:D2}Cell{1:D2}'-f$r,$c)=$lay[$r-1].Cells[$c-1]}};$m.ContentStatus='FILLED_24';$fixed++}else{$still++}
  $aRow=$audit|Where-Object{$_.PageCode-eq$m.PageCode}|Select-Object -First 1;if($aRow){$aRow.ReadingCount=[string]$count;$aRow.ContentStatus=if($count-eq24){'FILLED_24'}else{'PARTIAL_REVIEW'};$aRow.SourceFile=$p.File}
}
[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}
Write-Host 'QURBATA J3 batch repair complete';Write-Host "J3 pages fixed to 24 : $fixed";Write-Host "J3 pages still review: $still";Write-Host "Master                : $MasterPath"
