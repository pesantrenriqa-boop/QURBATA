param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$AuditPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-CONTENT-AUDIT.csv"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

function Put([hashtable]$h,[int]$a,[object[]]$vals){
  for($i=0;$i-lt$vals.Count;$i++){
    $n=$a+$i
    if($n-ge1-and$n-le24){$h[$n]=([string]$vals[$i]).Trim()}
  }
}

function SplitItems([string]$s){
  return @($s -split '\s*[·•]\s*|\s*\|\s*' | ForEach-Object{$_.Trim()} | Where-Object{$_})
}

function ParseFragment([string]$frag){
  $slots=@{}

  # Markdown table rows: any row containing a numeric range and material cell(s).
  foreach($line in @($frag -split "`r`n|`n|`r")){
    if($line -notmatch '^\s*\|'){continue}
    $cells=@(($line.Trim().Trim('|') -split '\|') | ForEach-Object{$_.Trim()})
    $rangeIndex=-1;$a=0;$b=0
    for($i=0;$i-lt$cells.Count;$i++){
      $rm=[regex]::Match($cells[$i],'^\s*(\d{1,2})\s*[–-]\s*(\d{1,2})\s*$')
      if($rm.Success){$rangeIndex=$i;$a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;break}
    }
    if($rangeIndex-lt0){continue}
    $need=$b-$a+1

    # Prefer a single cell containing exactly the needed number of items.
    $done=$false
    for($i=0;$i-lt$cells.Count;$i++){
      if($i-eq$rangeIndex){continue}
      $items=@(SplitItems $cells[$i])
      if($items.Count-eq$need){Put $slots $a $items;$done=$true;break}
    }
    if($done){continue}

    # Paired columns, e.g. Tanpa ال / Dengan ال.
    $vals=@()
    for($i=0;$i-lt$cells.Count;$i++){
      if($i-eq$rangeIndex){continue}
      $v=$cells[$i]
      if(!$v-or$v-eq'—'){continue}
      if($v -match '^(3 huruf|4 huruf|5 huruf|6 huruf|7 huruf|8 huruf|pembuka|pasangan|fokus|murojaah|transfer)'){continue}
      $parts=@(SplitItems $v)
      foreach($p in $parts){$vals+=$p}
    }
    if($vals.Count-eq$need){Put $slots $a $vals}
  }

  # Bold blocks on same line, e.g. **Kotak 1–4:** a · b · c · d
  foreach($rm in [regex]::Matches($frag,'(?mi)^\*\*Kotak(?: pembuka)?\s+(\d{1,2})\s*[–-]\s*(\d{1,2})[^*]*\*\*\s*:?\s*(.+)$')){
    $a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$items=@(SplitItems $rm.Groups[3].Value)
    if($items.Count-eq($b-$a+1)){Put $slots $a $items}
  }

  # Bold blocks followed by values on next line.
  foreach($rm in [regex]::Matches($frag,'(?mis)^\*\*Kotak(?: pembuka)?\s+(\d{1,2})\s*[–-]\s*(\d{1,2})[^*]*\*\*\s*:?\s*\r?\n\s*([^\r\n#]+)')){
    $a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$items=@(SplitItems $rm.Groups[3].Value)
    if($items.Count-eq($b-$a+1)){Put $slots $a $items}
  }

  # Heading blocks, e.g. ### Kotak 9–12 ... followed by pipe-separated or numbered values.
  foreach($rm in [regex]::Matches($frag,'(?mis)^#{3,4}\s+[^\r\n]*?Kotak\s+(\d{1,2})\s*[–-]\s*(\d{1,2})[^\r\n]*\r?\n(.*?)(?=^#{2,4}\s+|^\*\*Kotak|\z)')){
    $a=[int]$rm.Groups[1].Value;$b=[int]$rm.Groups[2].Value;$need=$b-$a+1;$body=$rm.Groups[3].Value
    $num=@([regex]::Matches($body,'(?m)^\s*\d+\.\s+(.+?)\s*$') | ForEach-Object{$_.Groups[1].Value.Trim()})
    if($num.Count-eq$need){Put $slots $a $num;continue}
    $first=@($body -split "`r`n|`n|`r" | Where-Object{$_ -and $_ -notmatch '^\*\*Source' -and $_ -notmatch '^\*\*Potongan'} | Select-Object -First 1)
    if($first.Count){$items=@(SplitItems $first[0]);if($items.Count-eq$need){Put $slots $a $items}}
  }

  return [pscustomobject]@{Map=$slots;Count=$slots.Count}
}

function MakeLayout([hashtable]$slots){
  $rows=@()
  for($r=0;$r-lt8;$r++){
    $cells=@()
    for($c=1;$c-le3;$c++){$idx=$r*3+$c;$cells+=if($slots.ContainsKey($idx)){$slots[$idx]}else{''}}
    $rows+=[pscustomobject]@{Count=3;Cells=@($cells[0],$cells[1],$cells[2],'')}
  }
  return @($rows)
}

if(!(Test-Path $MasterPath)){throw "Master not found: $MasterPath"}
$master=@(Import-Csv $MasterPath)
$audit=if(Test-Path $AuditPath){@(Import-Csv $AuditPath)}else{@()}
$files=@('QJ3-B02A-Materi-P011-P015.md','QJ3-B02B-Materi-P016-P020.md','QJ3-B03A-Materi-P021-P025.md','QJ3-B03B-Materi-P026-P030.md','QJ3-B04A-Materi-P031-P035.md','QJ3-B04B-Materi-P036-P040.md')
$parsed=@{}

foreach($name in $files){
  $path=Join-Path $RepoRoot "books\jilid-3\pages\$name"
  if(!(Test-Path $path)){continue}
  $text=[IO.File]::ReadAllText($path,[Text.Encoding]::UTF8)
  $heads=[regex]::Matches($text,'(?m)^##\s+(QJ3-P\d{3})\b.*$')
  for($i=0;$i-lt$heads.Count;$i++){
    $start=$heads[$i].Index
    $end=if($i+1-lt$heads.Count){$heads[$i+1].Index}else{$text.Length}
    $code=$heads[$i].Groups[1].Value
    $frag=$text.Substring($start,$end-$start)
    $p=ParseFragment $frag
    $parsed[$code]=[pscustomobject]@{Map=$p.Map;Count=$p.Count;File="books/jilid-3/pages/$name"}
  }
}

$fixed=0;$still=0
foreach($page in $master){
  if([int]$page.Jilid-ne3 -or -not $parsed.ContainsKey($page.PageCode)){continue}
  $p=$parsed[$page.PageCode]
  $slots=[hashtable]$p.Map
  $count=[int]$p.Count
  Write-Host ("{0} parsed slots : {1}" -f $page.PageCode,$count)
  if($count-eq24){
    for($i=1;$i-le24;$i++){$page.('Slot{0:D2}'-f$i)=$slots[$i]}
    $layout=@(MakeLayout $slots)
    for($r=1;$r-le8;$r++){
      $page.('Row{0:D2}Count'-f$r)=$layout[$r-1].Count
      for($c=1;$c-le4;$c++){$page.('Row{0:D2}Cell{1:D2}'-f$r,$c)=$layout[$r-1].Cells[$c-1]}
    }
    $page.ContentStatus='FILLED_24';$fixed++
  }else{$page.ContentStatus='PARTIAL_REVIEW';$still++}
  $ar=$audit|Where-Object{$_.PageCode-eq$page.PageCode}|Select-Object -First 1
  if($ar){$ar.ReadingCount=[string]$count;$ar.ContentStatus=$page.ContentStatus;$ar.SourceFile=$p.File}
}

[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){[IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)}
Write-Host 'QURBATA J3 batch repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $still"
Write-Host "Master                : $MasterPath"
