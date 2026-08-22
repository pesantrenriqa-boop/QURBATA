param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$OutputDir="$PSScriptRoot\..\dist\indesign-data-v4",
  [int[]]$Jilid=@(1,2,3)
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

function Rel([string]$p){$p.Substring($RepoRoot.Length).TrimStart([char[]]'\/') -replace '\\','/'}
function SplitCells([string]$line){
  $s=$line.Trim();if($s.StartsWith('|')){$s=$s.Substring(1)};if($s.EndsWith('|')){$s=$s.Substring(0,$s.Length-1)}
  return @($s -split '\|' | ForEach-Object {$_.Trim()})
}
function Norm([string]$s){return (($s.ToLowerInvariant() -replace '[`*_]','' -replace '\s+',' ').Trim())}
function GetTitle([string]$t){$m=[regex]::Match($t,'(?m)^#{1,4}\s+(.+?)\s*$');if($m.Success){return $m.Groups[1].Value.Trim()};return ''}
function GetBold([string]$t,[string]$label){$m=[regex]::Match($t,"(?m)^\*\*$([regex]::Escape($label)):\*\*\s*(.+?)\s*$");if($m.Success){return $m.Groups[1].Value.Trim()};return ''}
function GetSection([string]$t,[string]$names){$m=[regex]::Match($t,"(?ms)^#{2,4}\s+[^\r\n]*(?:$names)[^\r\n]*\r?\n(.*?)(?=^#{1,4}\s+|\z)");if($m.Success){return $m.Groups[1].Value.Trim()};return ''}
function OneLine([string]$t){if(!$t){return ''};return (($t -replace '(?m)^\s*[|>#].*$','' -replace '\r?\n+',' ' -replace '\s+',' ').Trim())}
function Panel([string]$t,[string]$labels,[string]$heads){
  $m=[regex]::Match($t,"(?mi)^\s*[-*]?\s*\*\*(?:$labels)(?:\s+5\s+menit)?(?:/[^:*]+)?\s*:\*\*\s*(.+?)\s*$")
  if($m.Success){return $m.Groups[1].Value.Trim()}
  $s=GetSection $t $heads;if(!$s){return ''}
  $m=[regex]::Match($s,'(?m)^>\s*(.+)$');if($m.Success){return $m.Groups[1].Value.Trim()}
  $m=[regex]::Match($s,'(?m)^[-*]\s+(?:\*\*[^*]+:\*\*\s*)?(.+)$');if($m.Success){return $m.Groups[1].Value.Trim()}
  return OneLine $s
}
function PageFragments([IO.FileInfo]$f){
  $t=[IO.File]::ReadAllText($f.FullName,[Text.Encoding]::UTF8)
  $direct=[regex]::Match($f.BaseName,'QJ\d+-P\d{3}')
  $ms=[regex]::Matches($t,'(?m)^#{1,4}\s+.*?(QJ\d+-P\d{3}).*$')
  if($ms.Count -le 1 -and $direct.Success){return ,([pscustomobject]@{Code=$direct.Value;Text=$t;File=$f})}
  $out=@()
  for($i=0;$i-lt$ms.Count;$i++){
    $a=$ms[$i].Index;$b=if($i+1-lt$ms.Count){$ms[$i+1].Index}else{$t.Length}
    $out += [pscustomobject]@{Code=$ms[$i].Groups[1].Value;Text=$t.Substring($a,$b-$a);File=$f}
  }
  return @($out)
}
function ParseReadingRows([string]$t){
  $lines=$t -split "`r?`n";$all=@()
  for($i=0;$i-lt$lines.Count-1;$i++){
    if($lines[$i] -notmatch '^\s*\|' -or $lines[$i+1] -notmatch '^\s*\|\s*:?-{2,}'){continue}
    $hdr=@(SplitCells $lines[$i]);$norm=@($hdr|ForEach-Object{Norm $_})
    $no=-1;$mat=-1;$short=-1;$long=-1;$type=-1;$id=-1
    for($h=0;$h-lt$norm.Count;$h++){
      $x=$norm[$h]
      if($x -eq 'kotak'){$no=$h}elseif($no-lt0 -and $x -match '^(no\.?|nomor|tangga)$'){$no=$h}
      if($x -match '^(latihan|materi|bacaan|contoh|teks|sampel|kata)$'){$mat=$h}
      if($x -eq 'pendek'){$short=$h};if($x -eq 'panjang'){$long=$h}
      if($x -match '^(jenis|fungsi|tipe|label|status/fungsi|jenis/status)$'){$type=$h}
      if($x -match '^(exercise-id|id latihan|assessment-item-id)$'){$id=$h}
    }
    if($mat-lt0 -and ($short-lt0 -or $long-lt0)){continue}
    $ordinal=0
    for($r=$i+2;$r-lt$lines.Count;$r++){
      if($lines[$r] -notmatch '^\s*\|'){break}
      $c=@(SplitCells $lines[$r]);if(!$c.Count){continue}
      $rawNo=if($no-ge0 -and $no-lt$c.Count){$c[$no]}else{''}
      $kind=if($type-ge0 -and $type-lt$c.Count){$c[$type]}else{''}
      $ex=if($id-ge0 -and $id-lt$c.Count){$c[$id]}else{''}
      $reading=''
      if($short-ge0 -and $long-ge0 -and $short-lt$c.Count -and $long-lt$c.Count){
        $reading=($c[$short].Trim() + ' ⟷ ' + $c[$long].Trim())
      }elseif($mat-ge0 -and $mat-lt$c.Count){$reading=$c[$mat].Trim()}
      if(!$reading){continue}

      $nums=[regex]::Matches($rawNo,'\d{1,2}')
      $parts=@($reading -split '\s*[·•]\s*' | Where-Object {$_ -and $_.Trim()})
      if($nums.Count-ge2){
        $a=[int]$nums[0].Value;$b=[int]$nums[1].Value
        if($b-ge$a -and $parts.Count-eq($b-$a+1)){
          for($k=0;$k-lt$parts.Count;$k++){$all += [pscustomobject]@{No=$a+$k;Text=$parts[$k].Trim();ExerciseID='';Type=$kind}}
          continue
        }
      }

      $ordinal++;$seq=$ordinal
      if($rawNo -match '^\s*(\d{1,2})\s*$'){$seq=[int]$Matches[1]}
      elseif($ex -match '(?:I|L|K)(\d{1,2})$'){$seq=[int]$Matches[1]}
      if($seq-ge1 -and $seq-le24){$all += [pscustomobject]@{No=$seq;Text=$reading;ExerciseID=$ex;Type=$kind}}
    }
  }
  if(!$all.Count){return @()}
  $merged=@($all|Group-Object No|ForEach-Object{$_.Group[0]}|Sort-Object No)
  return @($merged)
}
function PageType([int]$j,[int]$p,[string]$title,[string]$text){
  if($j-eq1 -and $p -in @(18,28,36,38)){
    if($title-match 'Hafalan'){return 'SPECIAL-TAHFIDZ'}
    if($title-match 'Bahasa Arab'){return 'SPECIAL-ARABIC'}
    if($title-match 'Akhlak'){return 'SPECIAL-AKHLAK'}
    return 'SPECIAL'
  }
  return 'READING'
}
function Score([int]$j,[int]$p,[string]$path,[string]$text,[int]$count){
  $s=0;$norm=$path-replace '\\','/'
  if($count-eq24){$s+=1000}else{$s+=$count*10}
  if($text-match 'RECOVERED-SOURCE-INCOMPLETE|SUPERSEDED'){$s-=500}
  if($j-eq1 -and $norm-match '/books/jilid-1/pages/QJ1-P\d{3}\.md$'){$s+=200}
  if($j-eq2 -and $p-le24 -and $norm-match '/regenerated/'){$s+=200}
  if($j-eq2 -and $p-ge25 -and $norm-match '/rebased/'){$s+=200}
  if($j-eq3 -and $norm-match '/books/jilid-3/pages/QJ3-B'){$s+=180}
  if($j-eq3 -and $norm-match '/books/jilid-3/pages/QJ3-P\d{3}\.md$'){$s+=100}
  if($path-match 'Revisi'){$s+=25}
  return $s
}
function Candidates([int]$j){
  $base=Join-Path $RepoRoot "books\jilid-$j";if(!(Test-Path $base)){return @()}
  $dirs=@('pages');if($j-eq2){$dirs=@('regenerated','rebased','pages')};if($j-eq3){$dirs=@('pages','recovery')}
  $out=@()
  foreach($d in $dirs){
    $dir=Join-Path $base $d;if(!(Test-Path $dir)){continue}
    foreach($f in Get-ChildItem $dir -Filter '*.md' -File){
      foreach($frag in @(PageFragments $f)){
        $m=[regex]::Match([string]$frag.Code,"^QJ$j-P(\d{3})$");if(!$m.Success){continue}
        $p=[int]$m.Groups[1].Value;$rows=@(ParseReadingRows $frag.Text)
        $out += [pscustomobject]@{Code=$frag.Code;Page=$p;Text=$frag.Text;File=$frag.File;Rows=$rows;Count=$rows.Count;Score=(Score $j $p $frag.File.FullName $frag.Text $rows.Count)}
      }
    }
  }
  return @($out)
}
function Capacity([string]$s){
  $tokens=@($s -split '\s+'|Where-Object{$_}).Count
  if($tokens-eq2){return 4};if($tokens-eq3){return 3};if($tokens-ge4){return 2};return 3
}
function MakeLayout([object[]]$rows){
  $items=@($rows|Sort-Object No);$res=@();$idx=0
  for($r=1;$r-le8;$r++){
    $left=$items.Count-$idx;$rowsLeft=9-$r
    if($left-le0){$res+=[pscustomobject]@{Count=0;Cells=@('','','','')};continue}
    $min=[math]::Ceiling($left/[double]$rowsLeft);$pref=Capacity ([string]$items[$idx].Text)
    $cnt=[math]::Min(4,[math]::Max($min,$pref));if($cnt-gt$left){$cnt=$left}
    $cells=@('','','','');for($c=0;$c-lt$cnt;$c++){$cells[$c]=$items[$idx+$c].Text}
    $res+=[pscustomobject]@{Count=$cnt;Cells=$cells};$idx+=$cnt
  }
  return @($res)
}

New-Item -ItemType Directory -Force -Path $OutputDir|Out-Null
$records=@();$audit=@()
foreach($j in $Jilid){
  foreach($grp in (@(Candidates $j)|Group-Object Code|Sort-Object Name)){
    $ordered=@($grp.Group|Sort-Object -Property @{Expression={$_.Score};Descending=$true},@{Expression={$_.File.Length};Descending=$true})
    if(!$ordered.Count){continue}
    $chosen=$ordered[0];$top=@($ordered|Where-Object{$_.Score-eq$chosen.Score});$conflict=$top.Count-gt1
    $ptype=PageType $j $chosen.Page (GetTitle $chosen.Text) $chosen.Text
    $rows=@($chosen.Rows);$layout=@(MakeLayout $rows);while($layout.Count-lt8){$layout += [pscustomobject]@{Count=0;Cells=@('','','','')}}
    $r=[ordered]@{PageCode=$chosen.Code;Jilid=$j;PageNumber=$chosen.Page;PageType=$ptype;Title=GetTitle $chosen.Text;Status=GetBold $chosen.Text 'Status';SourceFile=Rel $chosen.File.FullName;SourceScore=$chosen.Score;SourceConflict=$conflict;ReadingCount=$rows.Count;Outcome=OneLine (GetSection $chosen.Text 'Outcome Halaman|Tujuan|Hasil Akhir');Nidom=Panel $chosen.Text 'NIDOM|NIDHOM' 'NIDOM|NIDHOM';BahasaArab=Panel $chosen.Text 'Fokus lisan|Bahasa Arab|Bahasa Arab/mufradat|Mufradat' 'Bahasa Arab|Segmen Bahasa Arab|Mufradat';Tahfidz=Panel $chosen.Text 'Tahfidz|Hafalan' 'Tahfidz|Hafalan';Akhlak=Panel $chosen.Text 'Hadis/akhlak|Akhlak' 'Tema Akhlak|Akhlak';CandidateFiles=($ordered|ForEach-Object{Rel $_.File.FullName})-join' | '}
    for($i=1;$i-le24;$i++){$x=$rows|Where-Object{$_.No-eq$i}|Select-Object -First 1;$r[('Slot{0:D2}'-f$i)]=if($x){$x.Text}else{''}}
    for($rr=1;$rr-le8;$rr++){
      $obj=$layout[$rr-1];$cells=@($obj.Cells);while($cells.Count-lt4){$cells+=''}
      $r[('Row{0:D2}Count'-f$rr)]=$obj.Count
      for($cc=1;$cc-le4;$cc++){$r[('Row{0:D2}Cell{1:D2}'-f$rr,$cc)]=$cells[$cc-1]}
    }
    $ready=($ptype-ne'READING') -or ($rows.Count-eq24 -and -not $conflict)
    $note=if($ptype-ne'READING'){'SPECIAL_PAGE_NO_24_READING_REQUIRED'}elseif($conflict){'MULTIPLE_EQUAL_SOURCE_CANDIDATES'}elseif($rows.Count-ne24){'READING_ROWS_NOT_24'}else{'OK'}
    $records += [pscustomobject]$r
    $audit += [pscustomobject]@{PageCode=$chosen.Code;PageType=$ptype;SourceFile=Rel $chosen.File.FullName;SourceConflict=$conflict;ReadingCount=$rows.Count;ReadyForTemplate=$ready;Note=$note}
  }
}
$records=@($records|Sort-Object Jilid,PageNumber);$audit=@($audit|Sort-Object PageCode)
$all=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA-MERGE.csv';$layoutPath=Join-Path $OutputDir 'QURBATA-INDESIGN-8ROW-LAYOUT.csv';$auditPath=Join-Path $OutputDir 'QURBATA-INDESIGN-EXPORT-AUDIT.csv';$json=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA.json'
[IO.File]::WriteAllLines($all,($records|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
$sel=@('PageCode','PageType','Title');for($r=1;$r-le8;$r++){$sel+=('Row{0:D2}Count'-f$r);for($c=1;$c-le4;$c++){$sel+=('Row{0:D2}Cell{1:D2}'-f$r,$c)}};$sel+=@('Nidom','BahasaArab','Tahfidz','Akhlak')
[IO.File]::WriteAllLines($layoutPath,($records|Select-Object $sel|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllLines($auditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllText($json,($records|ConvertTo-Json -Depth 6),$Utf8Bom)
Write-Host 'QURBATA InDesign V4 export complete'
Write-Host "Pages found          : $($records.Count)"
Write-Host "24-reading pages     : $(($audit|Where-Object{$_.PageType-eq'READING' -and $_.ReadingCount-eq24}).Count)"
Write-Host "Special pages        : $(($audit|Where-Object{$_.PageType-ne'READING'}).Count)"
Write-Host "Source conflicts     : $(($audit|Where-Object{$_.SourceConflict}).Count)"
Write-Host "Ready for template   : $(($audit|Where-Object{$_.ReadyForTemplate}).Count)"
Write-Host "Output               : $OutputDir"
