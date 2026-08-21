param(
    [string]$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path,
    [string]$OutputDir = "$PSScriptRoot\..\dist\indesign-data",
    [int[]]$Jilid = @(1,2,3,4,5,6,7,8)
)

$ErrorActionPreference = 'Stop'
$Utf8Bom = New-Object System.Text.UTF8Encoding($true)

function Get-SectionText {
    param([string]$Text,[string]$HeadingPattern)
    $m = [regex]::Match($Text, "(?ms)^##\s+[^\r\n]*$HeadingPattern[^\r\n]*\r?\n(.*?)(?=^##\s+|\z)")
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ''
}

function Get-FirstBoldValue {
    param([string]$Text,[string]$Label)
    $m = [regex]::Match($Text, "(?m)^\*\*$([regex]::Escape($Label)):\*\*\s*(.+?)\s*$")
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ''
}

function Get-PageTitle {
    param([string]$Text)
    $m = [regex]::Match($Text, '(?m)^#\s+(.+?)\s*$')
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ''
}

function Get-TanggaRows {
    param([string]$Text)
    $rows = @()
    foreach ($line in ($Text -split "`r?`n")) {
        if ($line -match '^\|\s*(\d{1,2})\s*\|\s*([^|]+?)\s*\|(?:\s*([^|]+?)\s*\|)?\s*([^|]+?)\s*\|\s*$') {
            $n = [int]$Matches[1]
            if ($n -ge 1 -and $n -le 24) {
                $exerciseId = $Matches[2].Trim()
                $maybeType = $Matches[3]
                $practice = $Matches[4].Trim()
                $type = ''
                if ($null -ne $maybeType -and $maybeType.Trim() -ne '') { $type = $maybeType.Trim() }
                $rows += [pscustomobject]@{ No=$n; ExerciseID=$exerciseId; Type=$type; Text=$practice }
            }
        }
    }
    return $rows | Sort-Object No -Unique
}

function Get-ArabicPilot {
    param([string]$Text)
    $m = [regex]::Match($Text, '(?m)^-\s*\*\*Fokus lisan:\*\*\s*(.+?)\s*$')
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ''
}

function Get-Akhlak {
    param([string]$Text)
    $section = Get-SectionText -Text $Text -HeadingPattern 'Tema Akhlak|Akhlak'
    $m = [regex]::Match($section, '(?m)^>\s*(.+?)\s*$')
    if ($m.Success) { return $m.Groups[1].Value.Trim() }
    return ''
}

function Get-Outcome {
    param([string]$Text)
    $section = Get-SectionText -Text $Text -HeadingPattern 'Outcome Halaman|Hasil Akhir'
    if (-not $section) { return '' }
    $plain = ($section -replace '(?m)^\s*[-*>#|].*$','' -replace '\r?\n+',' ' -replace '\s+',' ').Trim()
    return $plain
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$all = New-Object System.Collections.Generic.List[object]

foreach ($j in $Jilid) {
    $pagesDir = Join-Path $RepoRoot "books\jilid-$j\pages"
    if (-not (Test-Path $pagesDir)) { continue }

    $files = Get-ChildItem $pagesDir -Filter "QJ$j-P*.md" -File | Sort-Object Name
    foreach ($file in $files) {
        $text = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        $pageCodeMatch = [regex]::Match($file.BaseName, 'QJ\d+-P\d{3}')
        if (-not $pageCodeMatch.Success) { continue }
        $pageCode = $pageCodeMatch.Value
        $tangga = @(Get-TanggaRows -Text $text)

        $record = [ordered]@{
            PageCode       = $pageCode
            Jilid          = $j
            PageNumber     = [int]([regex]::Match($pageCode,'P(\d{3})').Groups[1].Value)
            Title          = Get-PageTitle -Text $text
            Status         = Get-FirstBoldValue -Text $text -Label 'Status'
            Version        = Get-FirstBoldValue -Text $text -Label 'Versi'
            Outcome        = Get-Outcome -Text $text
            ArabicOral     = Get-ArabicPilot -Text $text
            Akhlak         = Get-Akhlak -Text $text
            SourceFile     = $file.FullName.Substring($RepoRoot.Length).TrimStart('\','/') -replace '\\','/'
            TanggaCount    = $tangga.Count
        }

        for ($i=1; $i -le 24; $i++) {
            $row = $tangga | Where-Object No -eq $i | Select-Object -First 1
            $record[('ExerciseID{0:D2}' -f $i)] = if ($row) { $row.ExerciseID } else { '' }
            $record[('Type{0:D2}' -f $i)]       = if ($row) { $row.Type } else { '' }
            $record[('Slot{0:D2}' -f $i)]       = if ($row) { $row.Text } else { '' }
        }

        $all.Add([pscustomobject]$record)
    }
}

$csvPath = Join-Path $OutputDir 'QURBATA-INDESIGN-DATA-MERGE.csv'
$jsonPath = Join-Path $OutputDir 'QURBATA-INDESIGN-DATA.json'
$auditPath = Join-Path $OutputDir 'QURBATA-INDESIGN-EXPORT-AUDIT.csv'

$csv = $all | Sort-Object Jilid,PageNumber | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($csvPath, $csv, $Utf8Bom)

$json = $all | Sort-Object Jilid,PageNumber | ConvertTo-Json -Depth 6
[System.IO.File]::WriteAllText($jsonPath, $json, $Utf8Bom)

$audit = $all | Sort-Object Jilid,PageNumber | Select-Object PageCode,Jilid,PageNumber,Title,Status,TanggaCount,SourceFile,@{N='ReadyFor24SlotMerge';E={$_.TanggaCount -eq 24}}
$auditCsv = $audit | ConvertTo-Csv -NoTypeInformation
[System.IO.File]::WriteAllLines($auditPath, $auditCsv, $Utf8Bom)

Write-Host "QURBATA InDesign export complete"
Write-Host "Pages exported : $($all.Count)"
Write-Host "CSV            : $csvPath"
Write-Host "JSON           : $jsonPath"
Write-Host "AUDIT          : $auditPath"
Write-Host "24-slot pages  : $(($all | Where-Object TanggaCount -eq 24).Count)"
Write-Host "Other pages    : $(($all | Where-Object TanggaCount -ne 24).Count)"
