$ErrorActionPreference = 'Stop'

$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path
$InputCsv = Join-Path $RepoRoot 'dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW.csv'
$OutputCsv = Join-Path $RepoRoot 'dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW-FULL.csv'
$Report = Join-Path $RepoRoot 'dist\indesign-template-data\QURBATA-J1-FULL-32-REPORT.txt'

if (!(Test-Path $InputCsv)) { throw "Input CSV not found: $InputCsv" }

$data = Import-Csv $InputCsv
$cellFields = 1..8 | ForEach-Object {
    $r = $_
    1..4 | ForEach-Object { "Row{0:D2}Cell{1:D2}" -f $r,$_ }
}

$emptyBefore = 0
foreach ($p in $data) {
    foreach ($f in $cellFields) {
        if ([string]::IsNullOrWhiteSpace([string]$p.$f)) { $emptyBefore++ }
    }
}

foreach ($p in $data) {
    $two = New-Object System.Collections.Generic.List[string]
    $three = New-Object System.Collections.Generic.List[string]

    foreach ($f in $cellFields) {
        $v = ([string]$p.$f).Trim()
        if ($v) {
            $count = @($v -split '\s+' | Where-Object { $_ }).Count
            if ($count -eq 2 -and -not $two.Contains($v)) { $two.Add($v) }
            if ($count -eq 3 -and -not $three.Contains($v)) { $three.Add($v) }
        }
    }

    if ($two.Count -eq 0 -or $three.Count -eq 0) {
        throw "$($p.PageCode): insufficient existing page-local drills for safe fill."
    }

    $pageNo = [int]$p.PageNumber
    $i2 = $pageNo % $two.Count
    $i3 = ($pageNo * 3) % $three.Count

    for ($r=1; $r -le 8; $r++) {
        for ($c=1; $c -le 4; $c++) {
            $f = "Row{0:D2}Cell{1:D2}" -f $r,$c
            if ([string]::IsNullOrWhiteSpace([string]$p.$f)) {
                if ($r -le 2) {
                    $p.$f = $two[$i2 % $two.Count]
                    $i2++
                } else {
                    $p.$f = $three[$i3 % $three.Count]
                    $i3++
                }
            }
        }
        $countField = "Row{0:D2}Count" -f $r
        $p.$countField = '4'
    }
    $p.ContentStatus = 'FILLED_32'
}

$emptyAfter = 0
foreach ($p in $data) {
    foreach ($f in $cellFields) {
        if ([string]::IsNullOrWhiteSpace([string]$p.$f)) { $emptyAfter++ }
    }
}

if ($emptyAfter -ne 0) { throw "Validation failed: $emptyAfter empty cells remain." }

$data | Export-Csv $OutputCsv -NoTypeInformation -Encoding UTF8

$total = $data.Count * 32
@"
QURBATA J1 FULL 32-CELL REPORT
Pages: $($data.Count)
Total target cells: $total
Empty before: $emptyBefore
Filled: $($emptyBefore - $emptyAfter)
Empty after: $emptyAfter
Existing non-empty cells changed: 0
Rule: rows 1-2 use existing page-local 2-unit drills; rows 3-8 use existing page-local 3-unit drills.
"@ | Set-Content $Report -Encoding UTF8

Write-Host "QURBATA J1 FULL-32 READY"
Write-Host "Pages       : $($data.Count)"
Write-Host "Total cells : $total"
Write-Host "Empty before: $emptyBefore"
Write-Host "Empty after : $emptyAfter"
Write-Host "CSV         : $OutputCsv"
Write-Host "Report      : $Report"
