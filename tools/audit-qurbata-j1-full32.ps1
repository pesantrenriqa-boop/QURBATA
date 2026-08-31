param(
  [string]$InputCsv = ".\dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW-FULL.csv",
  [string]$OutputDir = ".\dist\content-audit"
)
$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force $OutputDir | Out-Null
$data = Import-Csv $InputCsv
$cellFields = 1..8 | ForEach-Object { $r=$_; 1..4 | ForEach-Object { "Row{0:D2}Cell{1:D2}" -f $r,$_ } }

$rows = foreach($p in $data) {
  $vals = foreach($f in $cellFields) { ([string]$p.$f).Trim() }
  $nonempty = @($vals | Where-Object { $_ }).Count
  $unique = @($vals | Where-Object { $_ } | Sort-Object -Unique).Count
  $freq = $vals | Where-Object { $_ } | Group-Object | Sort-Object Count -Descending
  $maxRepeat = if($freq){$freq[0].Count}else{0}
  $topText = if($freq){$freq[0].Name}else{""}
  $twoBad=0; $threeBad=0
  foreach($r in 1..8) {
    foreach($c in 1..4) {
      $f="Row{0:D2}Cell{1:D2}" -f $r,$c
      $v=([string]$p.$f).Trim()
      if(!$v){continue}
      $n=@($v -split "\s+" | Where-Object {$_}).Count
      if($r -le 2 -and $n -ne 2){$twoBad++}
      if($r -ge 3 -and $n -ne 3){$threeBad++}
    }
  }
  [pscustomobject]@{
    PageNumber=$p.PageNumber; PageCode=$p.PageCode; Focus=$p.Focus; Status=$p.ContentStatus
    Filled=$nonempty; Unique=$unique; DuplicateSlots=($nonempty-$unique)
    MaxSameDrill=$maxRepeat; MostRepeated=$topText
    Row01_02ShapeErrors=$twoBad; Row03_08ShapeErrors=$threeBad
    DuplicateRate=[math]::Round((($nonempty-$unique)/[math]::Max($nonempty,1))*100,1)
  }
}
$rows | Export-Csv "$OutputDir\QURBATA-J1-PAGE-AUDIT.csv" -NoTypeInformation -Encoding UTF8

$all = foreach($p in $data){ foreach($f in $cellFields){ ([string]$p.$f).Trim() } }
$summary=[pscustomobject]@{
 Pages=$data.Count; TargetCells=$data.Count*32; Filled=@($all|?{$_}).Count
 Empty=@($all|?{!$_}).Count; UniqueDrills=@($all|?{$_}|Sort-Object -Unique).Count
 PagesWithShapeErrors=@($rows|?{$_.Row01_02ShapeErrors -gt 0 -or $_.Row03_08ShapeErrors -gt 0}).Count
 PagesWithDuplicateRateOver25=@($rows|?{$_.DuplicateRate -gt 25}).Count
 PagesWithOneDrillRepeated4Plus=@($rows|?{$_.MaxSameDrill -ge 4}).Count
}
$summary | Format-List | Out-String | Set-Content "$OutputDir\QURBATA-J1-AUDIT-SUMMARY.txt" -Encoding UTF8
$rows | Sort-Object DuplicateRate -Descending | Select-Object -First 15 |
  Format-Table PageNumber,PageCode,Focus,Filled,Unique,DuplicateRate,MaxSameDrill,MostRepeated,Row01_02ShapeErrors,Row03_08ShapeErrors -AutoSize |
  Out-String -Width 240 | Set-Content "$OutputDir\QURBATA-J1-AUDIT-TOP-DUPLICATES.txt" -Encoding UTF8

Write-Host "QURBATA J1 pedagogical data audit complete."
Get-Content "$OutputDir\QURBATA-J1-AUDIT-SUMMARY.txt"
Write-Host "Top duplicate-risk pages:"
Get-Content "$OutputDir\QURBATA-J1-AUDIT-TOP-DUPLICATES.txt"
