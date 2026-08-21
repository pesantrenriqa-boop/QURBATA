param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$OutputDir = "$PSScriptRoot\..\dist\indesign-data",
    [int[]]$Jilid = @(1,2,3,4,5,6,7,8)
)

$ErrorActionPreference = 'Stop'
$Utf8Bom = New-Object System.Text.UTF8Encoding($true)

function Rel([string]$Path) {
    return $Path.Substring($RepoRoot.Length).TrimStart([char[]]'\/') -replace '\\','/'
}

function FirstBold([string]$Text,[string]$Label) {
    $m=[regex]::Match($Text,"(?m)^\*\*$([regex]::Escape($Label)):\*\*\s*(.+?)\s*$")
    if($m.Success){return $m.Groups[1].Value.Trim()}
    return ''
}

function Title([string]$Text) {
    $m=[regex]::Match($Text,'(?m)^#{1,3}\s+(.+?)\s*$')
    if($m.Success){return $m.Groups[1].Value.Trim()}
    return ''
}

function Section([string]$Text,[string]$Names) {
    $m=[regex]::Match($Text,"(?ms)^#{2,4}\s+[^\r\n]*(?:$Names)[^\r\n]*\r?\n(.*?)(?=^#{1,4}\s+|\z)")
    if($m.Success){return $m.Groups[1].Value.Trim()}
    return ''
}

function OneLine([string]$Text) {
    if(-not $Text){return ''}
    return (($Text -replace '(?m)^\s*[|>#].*$','' -replace '\r?\n+',' ' -replace '\s+',' ').Trim())
}

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
    if($codes.Count -le 1 -and $direct.Success){
        return ,([pscustomobject]@{Code=$direct.Value;Text=$text;File=$File})
    }
    $out=@()
    for($i=0;$i -lt $codes.Count;$i++){
        $start=$codes[$i].Index
        $end=if($i+1 -lt $codes.Count){$codes[$i+1].Index}else{$text.Length}
        $out += [pscustomobject]@{Code=$codes[$i].Groups[1].Value;Text=$text.Substring($start,$end-$start);File=$File}
    }
    return $out
}

function Split-TableCells([string]$Line) {
    $s=$Line.Trim()
    if($s.StartsWith('|')){$s=$s.Substring(1)}
    if($s.EndsWith('|')){$s=$s.Substring(0,$s.Length-1)}
    return @($s -split '\|' | ForEach-Object {$_.Trim()})
}

function Normalize-Header([string]$s) {
    return (($s.ToLowerInvariant() -replace '[`*_]','' -replace '\s+',' ').Trim())
}

function Get-ReadingRows([string]$Text) {
    $lines=$Text -split "`r?`n"
    $tables=@()

    for($i=0;$i -lt $lines.Count-1;$i++){
        if($lines[$i] -notmatch '^\s*\|'){continue}
        if($lines[$i+1] -notmatch '^\s*\|\s*:?-{2,}'){continue}

        $hdr=@(Split-TableCells $lines[$i])
        $norm=@($hdr | ForEach-Object {Normalize-Header $_})

        $matIdx=-1; $noIdx=-1; $idIdx=-1; $typeIdx=-1
        for($h=0;$h -lt $norm.Count;$h++){
            $x=$norm[$h]
            if($x -match '^(latihan|materi|bacaan|contoh|teks)$'){$matIdx=$h}
            if($x -match '^(no\.?|nomor|tangga)$'){$noIdx=$h}
            if($x -match '^(exercise-id|id latihan)$'){$idIdx=$h}
            if($x -match '^(jenis|fungsi|tipe|label)$'){$typeIdx=$h}
            if($x -eq 'kotak' -and $noIdx -lt 0){$noIdx=$h}
        }
        if($matIdx -lt 0){continue}

        $rows=@(); $ordinal=0
        for($r=$i+2;$r -lt $lines.Count;$r++){
            if($lines[$r] -notmatch '^\s*\|'){break}
            $cells=@(Split-TableCells $lines[$r])
            if($cells.Count -le $matIdx){continue}
            if(($cells -join '') -match '^-+$'){continue}

            $ordinal++
            $seq=$ordinal
            $exercise=''
            if($noIdx -ge 0 -and $noIdx -lt $cells.Count){
                $raw=$cells[$noIdx]
                if($raw -match '^\d{1,2}$'){$seq=[int]$raw}
                elseif($raw -match '(?:K|L)(\d{1,2})$'){$seq=[int]$Matches[1];$exercise=$raw}
                elseif($raw -match 'QJ\d+-P\d+-L(\d{1,2})'){$seq=[int]$Matches[1];$exercise=$raw}
                elseif($raw -match 'QB-J\d+-H\d+-K(\d{1,2})'){$seq=[int]$Matches[1];$exercise=$raw}
            }
            if($idIdx -ge 0 -and $idIdx -lt $cells.Count){$exercise=$cells[$idIdx]}
            $kind=if($typeIdx -ge 0 -and $typeIdx -lt $cells.Count){$cells[$typeIdx]}else{''}
            $reading=$cells[$matIdx].Trim()
            if(-not $reading){continue}
            if($seq -ge 1 -and $seq -le 24){
                $rows += [pscustomobject]@{No=$seq;Text=$reading;ExerciseID=$exercise;Type=$kind}
            }
        }
        if($rows.Count -gt 0){
            $tables += ,([pscustomobject]@{Rows=@($rows|Sort-Object No -Unique);Count=$rows.Count;Header=($hdr -join ' | ')})
        }
    }

    if($tables.Count -eq 0){return @()}
    $best=$tables | Sort-Object @{Expression={if($_.Count -eq 24){1000}else{$_.Count}};Descending=$true} | Select-Object -First 1
    return @($best.Rows)
}

function Count-ArabicBaseLetters([string]$Text) {
    if(-not $Text){return 0}
    $clean=$Text -replace '[\u064B-\u065F\u0670\u06D6-\u06ED\sـ]',''
    $m=[regex]::Matches($clean,'[\u0621-\u063A\u0641-\u064A\u0671\u067E\u0686\u06A4\u06AF\u06BE]')
    return $m.Count
}

function Preferred-Capacity([object]$Item) {
    if(-not $Item){return 0}
    $text=[string]$Item.Text
    $tokenCount=@($text -split '\s+' | Where-Object {$_ -ne ''}).Count
    if($tokenCount -ge 2 -and $tokenCount -le 4){
        if($tokenCount -eq 2){return 4}
        if($tokenCount -eq 3){return 3}
        if($tokenCount -ge 4){return 2}
    }
    $letters=Count-ArabicBaseLetters $text
    if($letters -le 2){return 4}
    if($letters -eq 3){return 3}
    if($letters -eq 4){return 2}
    return 1
}

function Build-8RowLayout([object[]]$Items) {
    $items=@($Items|Sort-Object No)
    $result=@(); $idx=0
    for($row=1;$row -le 8;$row++){
        $remaining=$items.Count-$idx
        $rowsLeft=9-$row
        if($remaining -le 0){
            $result += [pscustomobject]@{Count=0;Cells=@('','','','');Compression=$false}
            continue
        }
        $minNeeded=[Math]::Ceiling($remaining/[double]$rowsLeft)
        $pref=Preferred-Capacity $items[$idx]
        if($pref -lt 1){$pref=3}
        $count=[Math]::Max([int]$minNeeded,[int]$pref)
        if($count -gt 4){$count=4}
        if($count -gt $remaining){$count=$remaining}
        $compression=($count -gt $pref)
        $cells=@('','','','')
        for($c=0;$c -lt $count;$c++){$cells[$c]=$items[$idx+$c].Text}
        $result += [pscustomobject]@{Count=$count;Cells=$cells;Compression=$compression}
        $idx += $count
    }
    return @($result)
}

function Rank-Source([int]$J,[int]$PageNumber,[string]$Path) {
    $normPath=$Path -replace '\\','/'
    if($J -eq 1 -and $normPath -match '/books/jilid-1/pages/QJ1-P\d{3}\.md$'){return 120}
    if($J -eq 2 -and $PageNumber -le 24 -and $normPath -match '/books/jilid-2/regenerated/'){return 120}
    if($J -eq 2 -and $PageNumber -ge 25 -and $normPath -match '/books/jilid-2/rebased/'){return 120}
    if($J -eq 2 -and $normPath -match '/books/jilid-2/pages/'){return 90}
    if($J -eq 3 -and $normPath -match '/books/jilid-3/pages/QJ3-P\d{3}\.md$'){return 120}
    if($J -eq 3 -and $normPath -match '/books/jilid-3/pages/'){return 100}
    if($J -eq 3 -and $normPath -match '/books/jilid-3/recovery/'){return 80}
    if($normPath -match "/books/jilid-$J/pages/"){return 100}
    return 10
}

function Get-Candidates([int]$J) {
    $base=Join-Path $RepoRoot "books\jilid-$J"
    if(-not(Test-Path $base)){return @()}
    $dirs=@('pages')
    if($J -eq 2){$dirs=@('regenerated','rebased','pages')}
    if($J -eq 3){$dirs=@('pages','recovery')}
    $all=@()
    foreach($d in $dirs){
        $dir=Join-Path $base $d
        if(-not(Test-Path $dir)){continue}
        foreach($f in Get-ChildItem $dir -Filter '*.md' -File){
            foreach($frag in @(Get-PageFragments $f)){
                if($frag.Code -notmatch "^QJ$J-P(\d{3})$"){continue}
                $pn=[int]$Matches[1]
                $all += [pscustomobject]@{Code=$frag.Code;Page=$pn;Text=$frag.Text;File=$frag.File;Rank=(Rank-Source $J $pn $frag.File.FullName)}
            }
        }
    }
    return $all
}

function ExtractPanel([string]$Text,[string]$Labels,[string]$Headings) {
    $v=LabelValue $Text $Labels
    if($v){return $v}
    $s=Section $Text $Headings
    if(-not $s){return ''}
    $m=[regex]::Match($s,'(?m)^>\s*(.+)$')
    if($m.Success){return $m.Groups[1].Value.Trim()}
    $m=[regex]::Match($s,'(?m)^[-*]\s+(?:\*\*[^*]+:\*\*\s*)?(.+)$')
    if($m.Success){return $m.Groups[1].Value.Trim()}
    return OneLine $s
}

function Extract-BahasaArab([string]$Text) {
    $v=LabelValue $Text 'Fokus lisan'
    if($v){return $v}
    return ExtractPanel $Text 'Bahasa Arab|Bahasa Arab/mufradat|Mufradat' 'Bahasa Arab|Segmen Bahasa Arab|Mufradat'
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$records=New-Object Collections.Generic.List[object]
$audit=New-Object Collections.Generic.List[object]

foreach($j in $Jilid){
    $cands=@(Get-Candidates $j)
    foreach($g in ($cands|Group-Object Code|Sort-Object Name)){
        $ordered=@($g.Group|Sort-Object @{Expression='Rank';Descending=$true},@{Expression={$_.File.Name-match'Revisi'};Descending=$true},@{Expression={$_.File.Length};Descending=$true})
        if($ordered.Count -eq 0){continue}
        $chosen=$ordered[0]
        $sameTop=@($ordered|Where-Object {$_.Rank -eq $chosen.Rank})
        $rows=@(Get-ReadingRows $chosen.Text)
        $conflict=$sameTop.Count -gt 1
        $layout=@(Build-8RowLayout $rows)
        $compression=@($layout|Where-Object {$_.Compression}).Count -gt 0

        $r=[ordered]@{
            PageCode=$chosen.Code
            Jilid=$j
            PageNumber=$chosen.Page
            Title=Title $chosen.Text
            Status=FirstBold $chosen.Text 'Status'
            Version=FirstBold $chosen.Text 'Versi'
            SourceFile=Rel $chosen.File.FullName
            SourcePriority=$chosen.Rank
            SourceConflict=$conflict
            CandidateCount=$ordered.Count
            CandidateFiles=($ordered|ForEach-Object{Rel $_.File.FullName}) -join ' | '
            TanggaCount=$rows.Count
            Outcome=OneLine (Section $chosen.Text 'Outcome Halaman|Tujuan|Hasil Akhir')
            Nidom=ExtractPanel $chosen.Text 'NIDOM|NIDHOM' 'NIDOM|NIDHOM'
            BahasaArab=Extract-BahasaArab $chosen.Text
            Tahfidz=ExtractPanel $chosen.Text 'Tahfidz|Hafalan' 'Tahfidz|Hafalan'
            Akhlak=ExtractPanel $chosen.Text 'Hadis/akhlak|Akhlak' 'Tema Akhlak|Akhlak'
            PhysicalRows=8
            LayoutCompressionRequired=$compression
        }

        for($i=1;$i -le 24;$i++){
            $x=$rows|Where-Object {$_.No -eq $i}|Select-Object -First 1
            $r[('ExerciseID{0:D2}'-f$i)]=if($x){$x.ExerciseID}else{''}
            $r[('Type{0:D2}'-f$i)]=if($x){$x.Type}else{''}
            $r[('Slot{0:D2}'-f$i)]=if($x){$x.Text}else{''}
        }

        for($row=1;$row -le 8;$row++){
            $lr=$layout[$row-1]
            $r[('Row{0:D2}Count'-f$row)]=$lr.Count
            for($cell=1;$cell -le 4;$cell++){
                $r[('Row{0:D2}Cell{1:D2}'-f$row,$cell)]=$lr.Cells[$cell-1]
            }
        }

        $records.Add([pscustomobject]$r)
        $audit.Add([pscustomobject]@{
            PageCode=$chosen.Code
            SourceFile=Rel $chosen.File.FullName
            SourcePriority=$chosen.Rank
            CandidateCount=$ordered.Count
            SourceConflict=$conflict
            TanggaCount=$rows.Count
            ReadyForContentMerge=($rows.Count -eq 24 -and -not $conflict)
            LayoutCompressionRequired=$compression
            Note=if($conflict){'MULTIPLE_TOP_PRIORITY_SOURCES_REVIEW_REQUIRED'}elseif($rows.Count -ne 24){'READING_ROWS_NOT_24_OR_PARSER_REVIEW_REQUIRED'}elseif($compression){'CONTENT_OK_LAYOUT_COMPRESSION_REVIEW'}else{'OK'}
        })
    }
}

$sorted=@($records|Sort-Object Jilid,PageNumber)
$csvPath=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA-MERGE.csv'
$jsonPath=Join-Path $OutputDir 'QURBATA-INDESIGN-DATA.json'
$auditPath=Join-Path $OutputDir 'QURBATA-INDESIGN-EXPORT-AUDIT.csv'
$layoutPath=Join-Path $OutputDir 'QURBATA-INDESIGN-8ROW-LAYOUT.csv'

[IO.File]::WriteAllLines($csvPath,($sorted|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllText($jsonPath,($sorted|ConvertTo-Json -Depth 7),$Utf8Bom)
[IO.File]::WriteAllLines($auditPath,($audit|Sort-Object PageCode|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)

$layoutProps=@('PageCode','Title')
for($row=1;$row -le 8;$row++){
    $layoutProps += ('Row{0:D2}Count'-f$row)
    for($cell=1;$cell -le 4;$cell++){$layoutProps += ('Row{0:D2}Cell{1:D2}'-f$row,$cell)}
}
$layoutProps += @('Nidom','BahasaArab','Tahfidz','Akhlak','LayoutCompressionRequired')
$layoutData=$sorted|Select-Object -Property $layoutProps
[IO.File]::WriteAllLines($layoutPath,($layoutData|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)

$pages24=@($sorted|Where-Object {$_.TanggaCount -eq 24}).Count
$conflicts=@($audit|Where-Object {$_.SourceConflict}).Count
$ready=@($audit|Where-Object {$_.ReadyForContentMerge}).Count
$compressed=@($audit|Where-Object {$_.LayoutCompressionRequired}).Count

Write-Host 'QURBATA InDesign content export complete'
Write-Host "Pages found              : $($sorted.Count)"
Write-Host "24-reading pages         : $pages24"
Write-Host "Source conflicts         : $conflicts"
Write-Host "Ready content merge      : $ready"
Write-Host "Layout compression review: $compressed"
Write-Host "Data Merge CSV           : $csvPath"
Write-Host "8-row layout CSV         : $layoutPath"
Write-Host "JSON                     : $jsonPath"
Write-Host "Audit                    : $auditPath"
