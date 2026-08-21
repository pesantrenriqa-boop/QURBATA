param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$OutputDir = "$PSScriptRoot\..\dist\indesign-data",
    [int[]]$Jilid = @(1,2,3,4,5,6,7,8)
)

$ErrorActionPreference = 'Stop'
$Utf8Bom = New-Object System.Text.UTF8Encoding($true)

function Rel([string]$Path) { return $Path.Substring($RepoRoot.Length).TrimStart([char[]]'\/') -replace '\\','/' }
function FirstBold([string]$Text,[string]$Label) {
    $m=[regex]::Match($Text,"(?m)^\*\*$([regex]::Escape($Label)):\*\*\s*(.+?)\s*$")
    if($m.Success){return $m.Groups[1].Value.Trim()}; return ''
}
function Title([string]$Text) {
    $m=[regex]::Match($Text,'(?m)^#{1,3}\s+(.+?)\s*$')
    if($m.Success){return $m.Groups[1].Value.Trim()}; return ''
}
function Section([string]$Text,[string]$Names) {
    $m=[regex]::Match($Text,"(?ms)^#{2,4}\s+[^\r\n]*(?:$Names)[^\r\n]*\r?\n(.*?)(?=^#{1,4}\s+|\z)")
    if($m.Success){return $m.Groups[1].Value.Trim()}; return ''
}
function OneLine([string]$Text) { return (($Text -replace '(?m)^\s*[|>#].*$','' -replace '\r?\n+',' ' -replace '\s+',' ').Trim()) }
function LabelValue([string]$Text,[string]$Labels) {
    $m=[regex]::Match($Text,"(?mi)^\s*[-*]\s*\*\*(?:$Labels)(?:\s+5\s+menit)?(?:/[^:*]+)?\s*:\*\*\s*(.+?)\s*$")
    if($m.Success){return $m.Groups[1].Value.Trim()}
    $m=[regex]::Match($Text,"(?mi)^\*\*(?:$Labels)(?:\s+5\s+menit)?(?:/[^:*]+)?\s*:\*\*\s*(.+?)\s*$")
    if($m.Success){return $m.Groups[1].Value.Trim()}
    return ''
}
function Get-PageFragments([System.IO.FileInfo]$File) {
    $text=[IO.File]::ReadAllText($File.FullName,[Text.Encoding]::UTF8)
    $direct=[regex]::Match($File.BaseName,'QJ\d+-P\d{3}')
    $codes=[regex]::Matches($text,'(?m)^#{1,4}\s+.*?(QJ\d+-P\d{3}).*$')
    if($codes.Count -le 1 -and $direct.Success){ return ,([pscustomobject]@{Code=$direct.Value;Text=$text;File=$File}) }
    $out=@()
    for($i=0;$i -lt $codes.Count;$i++){
        $start=$codes[$i].Index; $end=if($i+1 -lt $codes.Count){$codes[$i+1].Index}else{$text.Length}
        $out += [pscustomobject]@{Code=$codes[$i].Groups[1].Value;Text=$text.Substring($start,$end-$start);File=$File}
    }
    return $out
}
function Get-TableRows([string]$Text) {
    $lines=$Text -split "`r?`n"; $rows=@()
    for($i=0;$i -lt $lines.Count-2;$i++){
        if($lines[$i] -notmatch '^\s*\|'){continue}
        $hdr=@($lines[$i].Trim('|') -split '\|' | ForEach-Object {$_.Trim()})
        if($lines[$i+1] -notmatch '^\s*\|\s*:?-+'){continue}
        $noIdx=-1;$matIdx=-1;$idIdx=-1;$typeIdx=-1
        for($h=0;$h -lt $hdr.Count;$h++){
            $x=$hdr[$h].ToLowerInvariant()
            if($x -match '^(no\.?|tangga|kotak)$'){$noIdx=$h}
            if($x -match '^(latihan|materi|bacaan|contoh|teks)$'){$matIdx=$h}
            if($x -match 'exercise-id|id latihan'){$idIdx=$h}
            if($x -match '^(jenis|fungsi|tipe)$'){$typeIdx=$h}
        }
        if($noIdx -lt 0 -or $matIdx -lt 0){continue}
        for($r=$i+2;$r -lt $lines.Count;$r++){
            if($lines[$r] -notmatch '^\s*\|'){break}
            $c=@($lines[$r].Trim('|') -split '\|' | ForEach-Object {$_.Trim()})
            if($c.Count -le [Math]::Max($noIdx,$matIdx) -or $c[$noIdx] -notmatch '^\d{1,2}$'){continue}
            $n=[int]$c[$noIdx]; if($n -lt 1 -or $n -gt 24){continue}
            $rows += [pscustomobject]@{No=$n;Text=$c[$matIdx];ExerciseID=if($idIdx-ge 0-and$idIdx-lt$c.Count){$c[$idIdx]}else{''};Type=if($typeIdx-ge 0-and$typeIdx-lt$c.Count){$c[$typeIdx]}else{''}}
        }
    }
    return @($rows|Group-Object No|ForEach-Object{$_.Group[0]}|Sort-Object No)
}
function Rank-Source([int]$J,[int]$PageNumber,[string]$Path) {
    $normalizedPath=$Path -replace '\\','/'
    if($J-eq 1-and$normalizedPath-match'/pages/QJ1-P\d{3}\.md$'){return 100}
    if($J-eq 2-and$PageNumber-le 24-and$normalizedPath-match'/regenerated/'){return 100}
    if($J-eq 2-and$PageNumber-ge 25-and$normalizedPath-match'/rebased/'){return 100}
    if($J-eq 2-and$normalizedPath-match'/pages/'){return 70}
    if($J-eq 3-and$normalizedPath-match'/pages/QJ3-P\d{3}\.md$'){return 100}
    if($J-eq 3-and$normalizedPath-match'/pages/'){return 90}
    if($J-eq 3-and$normalizedPath-match'/recovery/'){return 80}
    if($normalizedPath-match"/jilid-$J/pages/"){return 90}; return 10
}
function Get-Candidates([int]$J) {
    $base=Join-Path $RepoRoot "books\jilid-$J"; if(-not(Test-Path $base)){return @()}
    $dirs=@('pages'); if($J-eq 2){$dirs=@('regenerated','rebased','pages')}; if($J-eq 3){$dirs=@('pages','recovery')}
    $all=@()
    foreach($d in $dirs){
        $dir=Join-Path $base $d; if(-not(Test-Path $dir)){continue}
        foreach($f in Get-ChildItem $dir -Filter '*.md' -File){
            foreach($frag in @(Get-PageFragments $f)){
                if($frag.Code -notmatch "^QJ$J-P(\d{3})$"){continue}; $pn=[int]$Matches[1]
                $all += [pscustomobject]@{Code=$frag.Code;Page=$pn;Text=$frag.Text;File=$frag.File;Rank=(Rank-Source $J $pn $frag.File.FullName)}
            }
        }
    }; return $all
}
function ExtractPanel([string]$Text,[string]$Labels,[string]$Headings) {
    $v=LabelValue $Text $Labels; if($v){return $v}
    $s=Section $Text $Headings; if(-not$s){return ''}
    $m=[regex]::Match($s,'(?m)^>\s*(.+)$'); if($m.Success){return $m.Groups[1].Value.Trim()}
    $m=[regex]::Match($s,'(?m)^[-*]\s+(?:\*\*[^*]+:\*\*\s*)?(.+)$'); if($m.Success){return $m.Groups[1].Value.Trim()}
    return OneLine $s
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$records=New-Object Collections.Generic.List[object]; $audit=New-Object Collections.Generic.List[object]
foreach($j in $Jilid){
    $cands=@(Get-Candidates $j)
    foreach($g in ($cands|Group-Object Code|Sort-Object Name)){
        $ordered=@($g.Group|Sort-Object @{Expression='Rank';Descending=$true},@{Expression={$_.File.Name-match'Revisi'};Descending=$true},@{Expression={$_.File.Length};Descending=$true})
        $chosen=$ordered[0]; $sameTop=@($ordered|Where-Object Rank-eq$chosen.Rank); $rows=@(Get-TableRows $chosen.Text); $conflict=$sameTop.Count-gt 1
        $r=[ordered]@{PageCode=$chosen.Code;Jilid=$j;PageNumber=$chosen.Page;Title=Title $chosen.Text;Status=FirstBold $chosen.Text 'Status';Version=FirstBold $chosen.Text 'Versi';SourceFile=Rel $chosen.File.FullName;SourcePriority=$chosen.Rank;SourceConflict=$conflict;CandidateCount=$ordered.Count;CandidateFiles=($ordered|ForEach-Object{Rel $_.File.FullName})-join' | ';TanggaCount=$rows.Count;Outcome=OneLine (Section $chosen.Text 'Outcome Halaman|Tujuan|Hasil Akhir');Nidom=ExtractPanel $chosen.Text 'NIDOM|NIDHOM' 'NIDOM|NIDHOM';BahasaArab=ExtractPanel $chosen.Text 'Bahasa Arab|Bahasa Arab/mufradat|Mufradat' 'Bahasa Arab|Segmen Bahasa Arab|Mufradat';Tahfidz=ExtractPanel $chosen.Text 'Tahfidz|Hafalan' 'Tahfidz|Hafalan';Akhlak=ExtractPanel $chosen.Text 'Hadis/akhlak|Akhlak' 'Tema Akhlak|Akhlak';PhysicalRows=8;DefaultCellsPerRow=3}
        for($i=1;$i-le24;$i++){ $x=$rows|Where-Object No-eq$i|Select-Object -First 1; $r[('ExerciseID{0:D2}'-f$i)]=if($x){$x.ExerciseID}else{''};$r[('Type{0:D2}'-f$i)]=if($x){$x.Type}else{''};$r[('Slot{0:D2}'-f$i)]=if($x){$x.Text}else{''} }
        for($row=1;$row-le8;$row++){ $r[('Row{0:D2}Count'-f$row)]=3; for($cell=1;$cell-le3;$cell++){ $slot=(($row-1)*3)+$cell;$r[('Row{0:D2}Cell{1:D2}'-f$row,$cell)]=$r[('Slot{0:D2}'-f$slot)] } }
        $records.Add([pscustomobject]$r)
        $audit.Add([pscustomobject]@{PageCode=$chosen.Code;SourceFile=Rel $chosen.File.FullName;SourcePriority=$chosen.Rank;CandidateCount=$ordered.Count;SourceConflict=$conflict;TanggaCount=$rows.Count;ReadyForContentMerge=($rows.Count-eq24-and-not$conflict);Note=if($conflict){'MULTIPLE_TOP_PRIORITY_SOURCES_REVIEW_REQUIRED'}elseif($rows.Count-ne24){'TANGGA_NOT_24_OR_PARSER_REVIEW_REQUIRED'}else{'OK'}})
    }
}
$sorted=@($records|Sort-Object Jilid,PageNumber)
$csvPath=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA-MERGE.csv';$jsonPath=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA.json';$auditPath=Join-Path $OutputDir 'QURBATA-INDESIGN-EXPORT-AUDIT.csv';$layoutPath=Join-Path $OutputDir 'QURBATA-INDESIGN-8ROW-LAYOUT.csv'
[IO.File]::WriteAllLines($csvPath,($sorted|ConvertTo-Csv -NoTypeInformation),$Utf8Bom);[IO.File]::WriteAllText($jsonPath,($sorted|ConvertTo-Json -Depth 7),$Utf8Bom);[IO.File]::WriteAllLines($auditPath,($audit|Sort-Object PageCode|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
$layout=$sorted|Select-Object PageCode,Title,Row01Count,Row01Cell01,Row01Cell02,Row01Cell03,Row02Count,Row02Cell01,Row02Cell02,Row02Cell03,Row03Count,Row03Cell01,Row03Cell02,Row03Cell03,Row04Count,Row04Cell01,Row04Cell02,Row04Cell03,Row05Count,Row05Cell01,Row05Cell02,Row05Cell03,Row06Count,Row06Cell01,Row06Cell02,Row06Cell03,Row07Count,Row07Cell01,Row07Cell02,Row07Cell03,Row08Count,Row08Cell01,Row08Cell02,Row08Cell03,Nidom,BahasaArab,Tahfidz,Akhlak
[IO.File]::WriteAllLines($layoutPath,($layout|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
Write-Host 'QURBATA InDesign content export complete';Write-Host "Pages found          : $($sorted.Count)";Write-Host "24-tangga pages      : $(($sorted|Where-Object TanggaCount-eq24).Count)";Write-Host "Source conflicts     : $(($audit|Where-Object SourceConflict).Count)";Write-Host "Ready content merge  : $(($audit|Where-Object ReadyForContentMerge).Count)";Write-Host "Data Merge CSV       : $csvPath";Write-Host "8-row layout CSV     : $layoutPath";Write-Host "JSON                 : $jsonPath";Write-Host "Audit                : $auditPath"
