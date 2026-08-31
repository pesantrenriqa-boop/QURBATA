param(
  [string]$InputCsv = ".\dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW.csv",
  [string]$OutputCsv = ".\dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW-FULL-REFINED.csv",
  [string]$Report = ".\dist\content-audit\QURBATA-J1-FULL32-REFINED-REPORT.txt"
)

$ErrorActionPreference = "Stop"

if (!(Test-Path $InputCsv)) { throw "Input CSV not found: $InputCsv" }
New-Item -ItemType Directory -Force (Split-Path $OutputCsv) | Out-Null
New-Item -ItemType Directory -Force (Split-Path $Report) | Out-Null

$data = Import-Csv $InputCsv

$cellFields = 1..8 | ForEach-Object {
  $r = $_
  1..4 | ForEach-Object { "Row{0:D2}Cell{1:D2}" -f $r,$_ }
}

function Get-TokensInOrder {
  param($Page)
  $seen = @{}
  $out = New-Object System.Collections.Generic.List[string]
  foreach($f in $cellFields) {
    $v = ([string]$Page.$f).Trim()
    if(!$v){ continue }
    foreach($t in ($v -split "\s+" | Where-Object { $_ })) {
      if(!$seen.ContainsKey($t)) {
        $seen[$t] = $true
        $out.Add($t)
      }
    }
  }
  return @($out)
}

function Get-PriorityTokens {
  param($Page)
  $seen = @{}
  $out = New-Object System.Collections.Generic.List[string]
  foreach($r in 1..2) {
    foreach($c in 1..4) {
      $f = "Row{0:D2}Cell{1:D2}" -f $r,$c
      $v = ([string]$Page.$f).Trim()
      if(!$v){ continue }
      foreach($t in ($v -split "\s+" | Where-Object { $_ })) {
        if(!$seen.ContainsKey($t)) {
          $seen[$t]=$true
          $out.Add($t)
        }
      }
    }
  }
  return @($out)
}

$changed = New-Object System.Collections.Generic.List[object]

foreach($p in $data) {
  # Existing source material is frozen; only originally blank cells are fill targets.
  $existing = @{}
  foreach($f in $cellFields) {
    $v = ([string]$p.$f).Trim()
    if($v){ $existing[$v] = $true }
  }

  $tokens = @(Get-TokensInOrder $p)
  $priority = @(Get-PriorityTokens $p)

  if($tokens.Count -lt 2) { throw "$($p.PageCode): not enough page-local syllable tokens." }
  if($priority.Count -eq 0) { $priority = $tokens }

  # Build deterministic 3-unit candidates from page-local repertoire.
  # At least one priority token is placed first to keep new/review focus salient.
  $candidates = New-Object System.Collections.Generic.List[string]
  $candidateSeen = @{}

  foreach($a in $priority) {
    foreach($b in $tokens) {
      foreach($c in $tokens) {
        $cand = "$a $b $c"
        if(!$existing.ContainsKey($cand) -and !$candidateSeen.ContainsKey($cand)) {
          $candidateSeen[$cand] = $true
          $candidates.Add($cand)
        }
      }
    }
  }

  # Fallback: all page-local triples if the priority-first set is insufficient.
  if($candidates.Count -lt 8) {
    foreach($a in $tokens) {
      foreach($b in $tokens) {
        foreach($c in $tokens) {
          $cand = "$a $b $c"
          if(!$existing.ContainsKey($cand) -and !$candidateSeen.ContainsKey($cand)) {
            $candidateSeen[$cand] = $true
            $candidates.Add($cand)
          }
        }
      }
    }
  }

  $targets = New-Object System.Collections.Generic.List[string]
  foreach($r in 1..8) {
    foreach($c in 1..4) {
      $f = "Row{0:D2}Cell{1:D2}" -f $r,$c
      if([string]::IsNullOrWhiteSpace([string]$p.$f)) {
        $targets.Add($f)
      }
    }
  }

  if($candidates.Count -lt $targets.Count) {
    throw "$($p.PageCode): only $($candidates.Count) safe unique candidates for $($targets.Count) blanks."
  }

  for($i=0; $i -lt $targets.Count; $i++) {
    $field = $targets[$i]
    $value = $candidates[$i]
    $p.$field = $value
    $existing[$value] = $true
    $changed.Add([pscustomobject]@{
      PageCode=$p.PageCode
      PageNumber=$p.PageNumber
      Field=$field
      Value=$value
    })
  }

  foreach($r in 1..8) {
    $countField = "Row{0:D2}Count" -f $r
    $p.$countField = "4"
  }
  $p.ContentStatus = "FILLED_32_REFINED"
}

# Validation
$empty = 0
$shapeErrors = 0
foreach($p in $data) {
  foreach($r in 1..8) {
    foreach($c in 1..4) {
      $f = "Row{0:D2}Cell{1:D2}" -f $r,$c
      $v = ([string]$p.$f).Trim()
      if(!$v){ $empty++; continue }
      $n = @($v -split "\s+" | Where-Object { $_ }).Count
      if($r -le 2 -and $n -ne 2){ $shapeErrors++ }
      if($r -ge 3 -and $n -ne 3){ $shapeErrors++ }
    }
  }
}

if($empty -ne 0){ throw "Validation failed: $empty empty cells remain." }
if($shapeErrors -ne 0){ throw "Validation failed: $shapeErrors row-shape errors." }

$data | Export-Csv $OutputCsv -NoTypeInformation -Encoding UTF8

$perPage = foreach($p in $data) {
  $vals = foreach($f in $cellFields){ ([string]$p.$f).Trim() }
  $filled = @($vals | Where-Object { $_ }).Count
  $unique = @($vals | Where-Object { $_ } | Sort-Object -Unique).Count
  $freq = $vals | Where-Object {$_} | Group-Object | Sort-Object Count -Descending
  [pscustomobject]@{
    PageNumber=$p.PageNumber
    PageCode=$p.PageCode
    Focus=$p.Focus
    Filled=$filled
    Unique=$unique
    DuplicateRate=[math]::Round((($filled-$unique)/[math]::Max($filled,1))*100,1)
    MaxSameDrill=if($freq){$freq[0].Count}else{0}
    MostRepeated=if($freq){$freq[0].Name}else{""}
  }
}

@"
QURBATA J1 FULL-32 REFINED
Pages: $($data.Count)
Changed filler cells: $($changed.Count)
Empty after: $empty
Shape errors: $shapeErrors
Pages duplicate rate >25%: $(@($perPage | Where-Object {$_.DuplicateRate -gt 25}).Count)
Pages duplicate rate =25%: $(@($perPage | Where-Object {$_.DuplicateRate -eq 25}).Count)
Pages max same drill >=4: $(@($perPage | Where-Object {$_.MaxSameDrill -ge 4}).Count)
Output: $OutputCsv

Top duplicate-risk pages:
$($perPage | Sort-Object DuplicateRate -Descending | Select-Object -First 15 | Format-Table PageNumber,PageCode,Focus,Filled,Unique,DuplicateRate,MaxSameDrill,MostRepeated -AutoSize | Out-String -Width 220)
"@ | Set-Content $Report -Encoding UTF8

$changed | Export-Csv ".\dist\content-audit\QURBATA-J1-FULL32-REFINED-CHANGES.csv" -NoTypeInformation -Encoding UTF8

Write-Host "QURBATA J1 FULL-32 refinement complete."
Get-Content $Report
