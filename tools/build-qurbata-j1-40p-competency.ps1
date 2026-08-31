param(
    [string]$InputCsv = '.\dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW-FULL-REFINED.csv',
    [string]$FallbackCsv = '.\dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW.csv',
    [string]$SpecialCsv = '.\data\indesign\QURBATA-J1-SPECIAL-PAGES.csv',
    [string]$OutputTsv = '.\dist\indesign-template-data\QURBATA-J1-40P-COMPETENCY.tsv'
)
$ErrorActionPreference = 'Stop'
if (!(Test-Path $InputCsv)) { if (Test-Path $FallbackCsv) { $InputCsv = $FallbackCsv } else { throw 'No J1 source CSV found.' } }
if (!(Test-Path $SpecialCsv)) { throw "Special-page manifest not found: $SpecialCsv" }
$data = Import-Csv $InputCsv
$special = Import-Csv $SpecialCsv
$byPage = @{}
foreach ($row in $data) {
    $n = [int]$row.PageNumber
    $main = ([string]$row.MainMaterial).Trim()
    $focus = ([string]$row.Focus).Trim()
    $target = "Peserta mampu membaca latihan pada fokus '$focus' dengan tepat, lancar, dan konsisten."
    if ($main -and $main -notmatch '^—') {
        $primary = ($main -split '\|')[0].Trim()
        if ($primary) { $target = "Peserta mampu mengenali dan membaca $primary pada fokus '$focus' dengan tepat, lancar, dan konsisten." }
    }
    $byPage[$n] = [pscustomobject]@{ PageNumber=$n; PageCode=$row.PageCode; PageType='TARTIL'; CompetencyCode=('QJ1-C{0:D2}' -f $n); CompetencyTitle=$focus; CompetencyTarget=$target; Status='ACTIVE' }
}
foreach ($s in $special) {
    $n = [int]$s.PageNumber
    $byPage[$n] = [pscustomobject]@{ PageNumber=$n; PageCode=$s.PageCode; PageType=$s.PageType; CompetencyCode=('QJ1-C{0:D2}' -f $n); CompetencyTitle=$s.Focus; CompetencyTarget='Target kompetensi khusus menunggu mapping dan pengesahan final.'; Status=$s.Status }
}
$rows = foreach ($n in 1..40) { if (!$byPage.ContainsKey($n)) { throw "Missing competency registration for page $n." }; $byPage[$n] }
New-Item -ItemType Directory -Force (Split-Path $OutputTsv) | Out-Null
$tab = [char]9
$header = @('PageNumber','PageCode','PageType','CompetencyCode','CompetencyTitle','CompetencyTarget','Status') -join $tab
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add($header)
foreach ($r in $rows) {
    $vals = @($r.PageNumber,$r.PageCode,$r.PageType,$r.CompetencyCode,([string]$r.CompetencyTitle -replace '[\t\r\n]',' '),([string]$r.CompetencyTarget -replace '[\t\r\n]',' '),$r.Status)
    $lines.Add(($vals -join $tab))
}
$outDir = (Resolve-Path (Split-Path $OutputTsv)).Path
$outPath = Join-Path $outDir (Split-Path $OutputTsv -Leaf)
[IO.File]::WriteAllLines($outPath,$lines,(New-Object System.Text.UTF8Encoding($false)))
Write-Host 'QURBATA J1 competency register ready.'
Write-Host "Rows      : $($rows.Count)"
Write-Host "Tartil    : $(@($rows | Where-Object {$_.PageType -eq 'TARTIL'}).Count)"
Write-Host "Special   : $(@($rows | Where-Object {$_.PageType -ne 'TARTIL'}).Count)"
Write-Host "Output    : $OutputTsv"
$rows | Format-Table PageNumber,PageCode,PageType,CompetencyCode,CompetencyTitle -AutoSize