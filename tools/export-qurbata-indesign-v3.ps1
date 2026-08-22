param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$OutputDir="$PSScriptRoot\..\dist\indesign-data-v3",
  [int[]]$Jilid=@(1,2,3)
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)
function Rel([string]$p){$p.Substring($RepoRoot.Length).TrimStart([char[]]'\/') -replace '\\','/'}
function Cells([string]$l){$s=$l.Trim();if($s.StartsWith('|')){$s=$s.Substring(1)};if($s.EndsWith('|')){$s=$s.Substring(0,$s.Length-1)};,@($s -split '\|'|ForEach-Object{$_.Trim()})}
function NormalizeHeader([string]$s){(($s.ToLowerInvariant()-replace '[`*_]',''-replace '\s+',' ').Trim())}
function Title([string]$t){$m=[regex]::Match($t,'(?m)^#{1,4}\s+(.+?)\s*$');if($m.Success){$m.Groups[1].Value.Trim()}else{''}}
function Bold([string]$t,[string]$label){$m=[regex]::Match($t,"(?m)^\*\*$([regex]::Escape($label)):\*\*\s*(.+?)\s*$");if($m.Success){$m.Groups[1].Value.Trim()}else{''}}
function Section([string]$t,[string]$n){$m=[regex]::Match($t,"(?ms)^#{2,4}\s+[^\r\n]*(?:$n)[^\r\n]*\r?\n(.*?)(?=^#{1,4}\s+|\z)");if($m.Success){$m.Groups[1].Value.Trim()}else{''}}
function One([string]$t){if(!$t){''}else{(($t-replace '(?m)^\s*[|>#].*$',''-replace '\r?\n+',' '-replace '\s+',' ').Trim())}}
function Panel([string]$t,[string]$labels,[string]$heads){
  $m=[regex]::Match($t,"(?mi)^\s*[-*]?\s*\*\*(?:$labels)(?:\s+5\s+menit)?(?:/[^:*]+)?\s*:\*\*\s*(.+?)\s*$")
  if($m.Success){return $m.Groups[1].Value.Trim()}
  $s=Section $t $heads;if(!$s){return ''};$m=[regex]::Match($s,'(?m)^>\s*(.+)$');if($m.Success){return $m.Groups[1].Value.Trim()};$m=[regex]::Match($s,'(?m)^[-*]\s+(?:\*\*[^*]+:\*\*\s*)?(.+)$');if($m.Success){return $m.Groups[1].Value.Trim()};One $s
}
function Frags([IO.FileInfo]$f){
  $t=[IO.File]::ReadAllText($f.FullName,[Text.Encoding]::UTF8);$direct=[regex]::Match($f.BaseName,'QJ\d+-P\d{3}');$ms=[regex]::Matches($t,'(?m)^#{1,4}\s+.*?(QJ\d+-P\d{3}).*$')
  if($ms.Count-le1-and$direct.Success){return ,([pscustomobject]@{Code=$direct.Value;Text=$t;File=$f})}
  $o=@();for($i=0;$i-lt$ms.Count;$i++){$a=$ms[$i].Index;$b=if($i+1-lt$ms.Count){$ms[$i+1].Index}else{$t.Length};$o+=[pscustomobject]@{Code=$ms[$i].Groups[1].Value;Text=$t.Substring($a,$b-$a);File=$f}};,$o
}
function ParseRows([string]$t){
  $ls=$t-split "`r?`n";$tables=@()
  for($i=0;$i-lt$ls.Count-1;$i++){
    if($ls[$i]-notmatch '^\s*\|' -or $ls[$i+1]-notmatch '^\s*\|\s*:?-{2,}'){continue}
    $hdr=@(Cells $ls[$i]);$norm=@($hdr|ForEach-Object{NormalizeHeader $_});$mat=-1;$no=-1;$id=-1;$typ=-1
    for($x=0;$x-lt$norm.Count;$x++){
      if($norm[$x]-match '^(latihan|materi|bacaan|contoh|teks|sampel|kata)$'){$mat=$x}
      if($norm[$x]-match '^(no\.?|nomor|tangga|kotak)$'){$no=$x}
      if($norm[$x]-match '^(exercise-id|id latihan|assessment-item-id)$'){$id=$x}
      if($norm[$x]-match '^(jenis|fungsi|tipe|label)$'){$typ=$x}
    }
    if($mat-lt0){continue};$rows=@();$ord=0
    for($r=$i+2;$r-lt$ls.Count;$r++){
      if($ls[$r]-notmatch '^\s*\|'){break};$c=@(Cells $ls[$r]);if($c.Count-le$mat){continue};$reading=$c[$mat].Trim();if(!$reading){continue}
      $raw=if($no-ge0-and$no-lt$c.Count){$c[$no]}else{''};$kind=if($typ-ge0-and$typ-lt$c.Count){$c[$typ]}else{''};$exercise=if($id-ge0-and$id-lt$c.Count){$c[$id]}else{''}
      if($raw-match '^(\d{1,2})\s*[–-]\s*(\d{1,2})$'){
        $a=[int]$Matches[1];$b=[int]$Matches[2];$parts=@($reading -split '\s*[·•]\s*'|Where-Object{$_});if($parts.Count-eq($b-$a+1)){for($k=0;$k-lt$parts.Count;$k++){$rows+=[pscustomobject]@{No=$a+$k;Text=$parts[$k].Trim();ExerciseID='';Type=$kind}}};continue
      }
      $ord++;$seq=$ord;if($raw-match '^\d{1,2}$'){$seq=[int]$raw}elseif($raw-match '(?:K|L)(\d{1,2})$'){$seq=[int]$Matches[1];if(!$exercise){$exercise=$raw}}elseif($exercise-match '(?:I|L|K)(\d{1,2})$'){$seq=[int]$Matches[1]}
      if($seq-ge1-and$seq-le24){$rows+=[pscustomobject]@{No=$seq;Text=$reading;ExerciseID=$exercise;Type=$kind}}
    }
    $u=@($rows|Group-Object No|ForEach-Object{$_.Group[0]}|Sort-Object No);if($u.Count){$tables+=,[pscustomobject]@{Rows=$u;Count=$u.Count}}
  }
  if(!$tables.Count){return @()};$best=$tables|Sort-Object Count -Descending|Select-Object -First 1;,@($best.Rows)
}
function Rank([int]$j,[int]$pn,[string]$path,[string]$text,[int]$count){
  $p=$path-replace '\\','/';$score=0
  if($count-eq24){$score+=1000}else{$score+=$count*10}
  if($text-match 'RECOVERED-SOURCE-INCOMPLETE|PENDING-REGENERATION|SUPERSEDED'){$score-=500}
  if($j-eq1-and$p-match '/books/jilid-1/pages/QJ1-P\d{3}\.md$'){$score+=200}
  if($j-eq2-and$pn-le24-and$p-match '/regenerated/'){$score+=200}
  if($j-eq2-and$pn-ge25-and$p-match '/rebased/'){$score+=200}
  if($j-eq3-and$p-match '/books/jilid-3/pages/QJ3-P\d{3}\.md$'){$score+=100}
  if($j-eq3-and$p-match '/books/jilid-3/pages/QJ3-B'){$score+=180}
  if($path-match 'Revisi'){$score+=25};$score
}
function Candidates([int]$j){
  $base=Join-Path $RepoRoot "books\jilid-$j";if(!(Test-Path $base)){return @()};$dirs=@('pages');if($j-eq2){$dirs=@('regenerated','rebased','pages')};if($j-eq3){$dirs=@('pages','recovery')};$a=@()
  foreach($d in $dirs){
    $dir=Join-Path $base $d;if(!(Test-Path $dir)){continue}
    foreach($f in Get-ChildItem $dir -Filter '*.md' -File){
      foreach($g in @(Frags $f)){
        $codeMatch=[regex]::Match([string]$g.Code,"^QJ$j-P(\d{3})$")
        if(-not $codeMatch.Success){continue}
        $pn=[int]$codeMatch.Groups[1].Value
        $rows=@(ParseRows $g.Text)
        $a+=[pscustomobject]@{Code=$g.Code;Page=$pn;Text=$g.Text;File=$g.File;Rows=$rows;RowCount=$rows.Count;Score=(Rank $j $pn $g.File.FullName $g.Text $rows.Count)}
      }
    }
  }
  return @($a)
}
function Cap([string]$s){$tokens=@($s-split '\s+'|Where-Object{$_}).Count;if($tokens-eq2){4}elseif($tokens-eq3){3}else{3}}
function Layout([object[]]$rows){
  $it=@($rows|Sort-Object No);$o=@();$idx=0
  for($r=1;$r-le8;$r++){
    $left=$it.Count-$idx;$rowsLeft=9-$r
    if($left-le0){$o+=[pscustomobject]@{Count=0;Cells=@('','','','')};continue}
    $min=[math]::Ceiling($left/[double]$rowsLeft);$pref=Cap $it[$idx].Text;$cnt=[math]::Min(4,[math]::Max($min,$pref));if($cnt-gt$left){$cnt=$left}
    $cells=@('','','','');for($c=0;$c-lt$cnt;$c++){$cells[$c]=$it[$idx+$c].Text}
    $o+=[pscustomobject]@{Count=$cnt;Cells=$cells};$idx+=$cnt
  }
  return @($o)
}
New-Item -ItemType Directory -Force -Path $OutputDir|Out-Null
$records=@();$audit=@()
foreach($j in $Jilid){foreach($grp in (@(Candidates $j)|Group-Object Code|Sort-Object Name)){
  $ord=@($grp.Group | Sort-Object -Property @{Expression={$_.Score};Descending=$true}, @{Expression={$_.File.Length};Descending=$true})
  if($ord.Count-eq0){continue}
  $ch=$ord[0];$top=@($ord|Where-Object{$_.Score-eq$ch.Score});$conflict=($top.Count-gt1);$rows=@($ch.Rows);$lay=@(Layout $rows)
  while($lay.Count-lt8){$lay+=[pscustomobject]@{Count=0;Cells=@('','','','')}}
  $r=[ordered]@{PageCode=$ch.Code;Jilid=$j;PageNumber=$ch.Page;Title=Title $ch.Text;Status=Bold $ch.Text 'Status';SourceFile=Rel $ch.File.FullName;SourceScore=$ch.Score;SourceConflict=$conflict;CandidateFiles=($ord|ForEach-Object{Rel $_.File.FullName})-join' | ';ReadingCount=$rows.Count;Outcome=One (Section $ch.Text 'Outcome Halaman|Tujuan|Hasil Akhir');Nidom=Panel $ch.Text 'NIDOM|NIDHOM' 'NIDOM|NIDHOM';BahasaArab=Panel $ch.Text 'Fokus lisan|Bahasa Arab|Bahasa Arab/mufradat|Mufradat' 'Bahasa Arab|Segmen Bahasa Arab|Mufradat';Tahfidz=Panel $ch.Text 'Tahfidz|Hafalan' 'Tahfidz|Hafalan';Akhlak=Panel $ch.Text 'Hadis/akhlak|Akhlak' 'Tema Akhlak|Akhlak'}
  for($i=1;$i-le24;$i++){$x=$rows|Where-Object{$_.No-eq$i}|Select-Object -First 1;$r[('Slot{0:D2}'-f$i)]=if($x){$x.Text}else{''}}
  for($rr=1;$rr-le8;$rr++){
    $rowObj=$lay[$rr-1]
    if($null-eq$rowObj){$rowObj=[pscustomobject]@{Count=0;Cells=@('','','','')}}
    $rowCells=@($rowObj.Cells);while($rowCells.Count-lt4){$rowCells+=''}
    $r[('Row{0:D2}Count'-f$rr)]=$rowObj.Count
    for($cc=1;$cc-le4;$cc++){$r[('Row{0:D2}Cell{1:D2}'-f$rr,$cc)]=$rowCells[$cc-1]}
  }
  $records+=[pscustomobject]$r;$audit+=[pscustomobject]@{PageCode=$ch.Code;SourceFile=Rel $ch.File.FullName;SourceConflict=$conflict;ReadingCount=$rows.Count;ReadyForContentMerge=($rows.Count-eq24-and-not$conflict);Note=if($conflict){'MULTIPLE_EQUAL_SOURCE_CANDIDATES'}elseif($rows.Count-ne24){'READING_ROWS_NOT_24'}else{'OK'}}
}}
$records=@($records|Sort-Object Jilid,PageNumber);$audit=@($audit|Sort-Object PageCode)
$all=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA-MERGE.csv';$layout=Join-Path $OutputDir 'QURBATA-INDESIGN-8ROW-LAYOUT.csv';$aud=Join-Path $OutputDir 'QURBATA-INDESIGN-EXPORT-AUDIT.csv';$json=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA.json'
[IO.File]::WriteAllLines($all,($records|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
$sel=@('PageCode','Title');for($r=1;$r-le8;$r++){$sel+=('Row{0:D2}Count'-f$r);for($c=1;$c-le4;$c++){$sel+=('Row{0:D2}Cell{1:D2}'-f$r,$c)}};$sel+=@('Nidom','BahasaArab','Tahfidz','Akhlak');[IO.File]::WriteAllLines($layout,($records|Select-Object $sel|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllLines($aud,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom);[IO.File]::WriteAllText($json,($records|ConvertTo-Json -Depth 6),$Utf8Bom)
Write-Host 'QURBATA InDesign V3 export complete';Write-Host "Pages found          : $($records.Count)";Write-Host "24-reading pages     : $(($audit|Where-Object{$_.ReadingCount-eq24}).Count)";Write-Host "Source conflicts     : $(($audit|Where-Object{$_.SourceConflict}).Count)";Write-Host "Ready content merge  : $(($audit|Where-Object{$_.ReadyForContentMerge}).Count)";Write-Host "Output               : $OutputDir"
