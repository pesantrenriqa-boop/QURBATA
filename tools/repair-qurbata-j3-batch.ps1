param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$MasterPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-MASTER-1-8-FILLED.csv",
  [string]$AuditPath="$PSScriptRoot\..\dist\tartil-master\QURBATA-TARTIL-CONTENT-AUDIT.csv"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

function Split-Items([string]$s){
  if([string]::IsNullOrWhiteSpace($s)){ return @() }
  return @($s -split '\s*[·•]\s*|\s*\|\s*' | ForEach-Object { $_.Trim() } | Where-Object { $_ })
}

function Put-Range([hashtable]$map,[int]$a,[int]$b,[object[]]$items){
  $need=$b-$a+1
  if($a-lt1 -or $b-gt24 -or @($items).Count-ne$need){ return $false }
  for($i=0;$i-lt$need;$i++){ $map[$a+$i]=([string]$items[$i]).Trim() }
  return $true
}

function Make-Layout([hashtable]$slots){
  $rows=@()
  for($r=0;$r-lt8;$r++){
    $cells=@('','','','')
    for($c=0;$c-lt3;$c++){
      $idx=$r*3+$c+1
      if($slots.ContainsKey($idx)){ $cells[$c]=$slots[$idx] }
    }
    $rows+=[pscustomobject]@{Count=3;Cells=$cells}
  }
  return @($rows)
}

if(!(Test-Path $MasterPath)){ throw "Master not found: $MasterPath" }
$master=@(Import-Csv $MasterPath)
$audit=if(Test-Path $AuditPath){ @(Import-Csv $AuditPath) } else { @() }

$files=@(
 'QJ3-B02A-Materi-P011-P015.md',
 'QJ3-B02B-Materi-P016-P020.md',
 'QJ3-B03A-Materi-P021-P025.md',
 'QJ3-B03B-Materi-P026-P030.md',
 'QJ3-B04A-Materi-P031-P035.md',
 'QJ3-B04B-Materi-P036-P040.md'
)

$parsed=@{}

foreach($name in $files){
  $path=Join-Path $RepoRoot "books\jilid-3\pages\$name"
  if(!(Test-Path $path)){ continue }

  $lines=@(Get-Content -LiteralPath $path -Encoding UTF8)
  $currentCode=$null
  $pending=$null
  $numbered=@()

  foreach($line in $lines){
    if($line -match '^##\s+(QJ3-P\d{3})\b'){
      $currentCode=$Matches[1]
      if(-not $parsed.ContainsKey($currentCode)){
        $parsed[$currentCode]=[pscustomobject]@{Map=@{};File="books/jilid-3/pages/$name"}
      }
      $pending=$null
      $numbered=@()
      continue
    }

    if(!$currentCode){ continue }
    $map=$parsed[$currentCode].Map

    # Standard markdown table row, e.g. | 3 huruf | 1–8 | a · b · ... |
    if($line -match '^\s*\|'){
      $cells=@(($line.Trim().Trim('|') -split '\|') | ForEach-Object { $_.Trim() })
      for($ri=0;$ri-lt$cells.Count;$ri++){
        if($cells[$ri] -match '^\s*(\d{1,2})\s*[–—-]\s*(\d{1,2})\s*$'){
          $a=[int]$Matches[1];$b=[int]$Matches[2];$need=$b-$a+1

          # Most J3 rows keep all reading items in one material cell.
          $done=$false
          for($ci=0;$ci-lt$cells.Count;$ci++){
            if($ci-eq$ri){ continue }
            $items=@(Split-Items $cells[$ci])
            if($items.Count-eq$need){
              [void](Put-Range $map $a $b $items)
              $done=$true
              break
            }
          }

          # P032 style: one range covers paired columns (Tanpa/Dengan ال).
          if(!$done -and $need-eq2){
            $vals=@()
            for($ci=0;$ci-lt$cells.Count;$ci++){
              if($ci-eq$ri){ continue }
              $v=$cells[$ci].Trim()
              if(!$v -or $v-eq'—' -or $v -match '^(pasangan|pembuka|fokus|murojaah|transfer|\d+\s*huruf)'){ continue }
              foreach($x in @(Split-Items $v)){ $vals+=$x }
            }
            if($vals.Count-ge2){
              [void](Put-Range $map $a $b @($vals[$vals.Count-2],$vals[$vals.Count-1]))
            }
          }
          break
        }
      }
      continue
    }

    # Same-line block: **Kotak 1–4:** a · b · c · d
    if($line -match '^\*\*Kotak(?:\s+pembuka)?\s+(\d{1,2})\s*[–—-]\s*(\d{1,2})[^*]*\*\*\s*:?\s*(.+)$'){
      $a=[int]$Matches[1];$b=[int]$Matches[2]
      $items=@(Split-Items $Matches[3])
      if($items.Count-eq($b-$a+1)){ [void](Put-Range $map $a $b $items) }
      continue
    }

    # Label waiting for following line, e.g. **Kotak 5–12 — kata kompleks:**
    if($line -match '^\*\*Kotak(?:\s+pembuka)?\s+(\d{1,2})\s*[–—-]\s*(\d{1,2})[^*]*\*\*\s*:?[ ]*$'){
      $pending=[pscustomobject]@{A=[int]$Matches[1];B=[int]$Matches[2]}
      $numbered=@()
      continue
    }

    # Heading blocks: ### Kotak 9–12 ... or ### Tangga frasa — kotak 21–24
    if($line -match '^#{3,4}\s+.*?kotak\s+(\d{1,2})\s*[–—-]\s*(\d{1,2})'){
      $pending=[pscustomobject]@{A=[int]$Matches[1];B=[int]$Matches[2]}
      $numbered=@()
      continue
    }

    if($null-ne$pending){
      $need=$pending.B-$pending.A+1

      if($line -match '^\s*\d+\.\s+(.+?)\s*$'){
        $numbered+=$Matches[1].Trim()
        if($numbered.Count-eq$need){
          [void](Put-Range $map $pending.A $pending.B $numbered)
          $pending=$null
          $numbered=@()
        }
        continue
      }

      if([string]::IsNullOrWhiteSpace($line) -or $line -match '^\*\*(Source|Potongan)'){ continue }

      $items=@(Split-Items $line)
      if($items.Count-eq$need){
        [void](Put-Range $map $pending.A $pending.B $items)
        $pending=$null
        $numbered=@()
        continue
      }

      if($line -match '^#{2,4}\s+' -or $line -match '^\*\*Kotak'){
        $pending=$null
        $numbered=@()
      }
    }
  }
}

$fixed=0;$still=0
foreach($page in $master){
  if([int]$page.Jilid-ne3 -or -not $parsed.ContainsKey($page.PageCode)){ continue }
  $p=$parsed[$page.PageCode]
  $slots=$p.Map
  $count=$slots.Count
  Write-Host ("{0} parsed slots : {1}" -f $page.PageCode,$count)

  if($count-eq24){
    for($i=1;$i-le24;$i++){ $page.('Slot{0:D2}'-f$i)=$slots[$i] }
    $layout=@(Make-Layout $slots)
    for($r=1;$r-le8;$r++){
      $page.('Row{0:D2}Count'-f$r)=$layout[$r-1].Count
      for($c=1;$c-le4;$c++){
        $page.('Row{0:D2}Cell{1:D2}'-f$r,$c)=$layout[$r-1].Cells[$c-1]
      }
    }
    $page.ContentStatus='FILLED_24'
    $fixed++
  }else{
    $page.ContentStatus='PARTIAL_REVIEW'
    $still++
  }

  $ar=$audit | Where-Object { $_.PageCode -eq $page.PageCode } | Select-Object -First 1
  if($ar){
    $ar.ReadingCount=[string]$count
    $ar.ContentStatus=$page.ContentStatus
    $ar.SourceFile=$p.File
  }
}

[IO.File]::WriteAllLines($MasterPath,($master|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
if($audit.Count){ [IO.File]::WriteAllLines($AuditPath,($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom) }

Write-Host 'QURBATA J3 batch repair complete'
Write-Host "J3 pages fixed to 24 : $fixed"
Write-Host "J3 pages still review: $still"
Write-Host "Master                : $MasterPath"
