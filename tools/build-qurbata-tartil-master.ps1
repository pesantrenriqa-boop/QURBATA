param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$OutputDir="$PSScriptRoot\..\dist\tartil-master"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

function ReadText([string]$Path){ if(Test-Path $Path){ return [IO.File]::ReadAllText($Path,[Text.Encoding]::UTF8) }; return '' }
function SplitCells([string]$Line){
  $s=$Line.Trim(); if($s.StartsWith('|')){$s=$s.Substring(1)}; if($s.EndsWith('|')){$s=$s.Substring(0,$s.Length-1)}
  return @($s -split '\|' | ForEach-Object {$_.Trim()})
}
function Normalize([string]$s){ return (($s.ToLowerInvariant() -replace '[`*_]','' -replace '\s+',' ').Trim()) }
function InferType([int]$J,[string]$Focus,[string]$ExplicitType){
  if($ExplicitType){ return $ExplicitType }
  if($J -in @(2,3)){ return 'Tartil' }
  if($Focus -match 'Hafalan'){return 'Hafalan'}
  if($Focus -match 'Bahasa Arab'){return 'Bahasa Arab'}
  if($Focus -match 'Akhlak|Hadis'){return 'Akhlak/Hadis'}
  return 'Tartil'
}
function ParseMasterMap([int]$J){
  $path=Join-Path $RepoRoot ("books\jilid-{0}\QJ{0}-MASTER-Struktur-40-Halaman.md" -f $J)
  $text=ReadText $path; $rows=@(); if(!$text){ return @() }
  $lines=$text -split "`r?`n"
  for($i=0;$i-lt$lines.Count-1;$i++){
    if($lines[$i]-notmatch '^\s*\|'){continue}
    $hdr=@(SplitCells $lines[$i]); $norm=@($hdr|ForEach-Object{Normalize $_})
    $codeIdx=[array]::IndexOf($norm,'kode')
    if($codeIdx -lt 0){continue}
    $pageIdx=-1
    for($x=0;$x-lt$norm.Count;$x++){ if($norm[$x] -match '^(halaman|hlm)$'){$pageIdx=$x;break} }
    if($pageIdx -lt 0){continue}
    $focusIdx=-1;$mainIdx=-1;$typeIdx=-1
    for($x=0;$x-lt$norm.Count;$x++){
      if($focusIdx-lt0 -and $norm[$x]-match '^fokus'){$focusIdx=$x}
      if($mainIdx-lt0 -and $norm[$x]-match '^(materi baru/utama|materi utama|tangga|tangga kompleksitas)$'){$mainIdx=$x}
      if($typeIdx-lt0 -and $norm[$x]-eq 'jenis'){$typeIdx=$x}
    }
    for($r=$i+2;$r-lt$lines.Count;$r++){
      if($lines[$r]-notmatch '^\s*\|'){break}
      $c=@(SplitCells $lines[$r]); if($c.Count-le[math]::Max($pageIdx,$codeIdx)){continue}
      if($c[$pageIdx]-notmatch '^\d+$'){continue}
      $code=$c[$codeIdx]
      if($code -notmatch ("^QJ{0}-P\d{{3}}$" -f $J)){continue}
      $focus=if($focusIdx-ge0-and$focusIdx-lt$c.Count){$c[$focusIdx]}else{''}
      $main=if($mainIdx-ge0-and$mainIdx-lt$c.Count){$c[$mainIdx]}else{''}
      if(!$main -and $c.Count-gt($codeIdx+1)){$main=$c[$c.Count-1]}
      $explicitType=if($typeIdx-ge0-and$typeIdx-lt$c.Count){$c[$typeIdx]}else{''}
      $type=InferType $J $focus $explicitType
      $rows += [pscustomobject]@{Page=[int]$c[$pageIdx];Code=$code;Focus=$focus;Main=$main;Type=$type;MasterFile=("books/jilid-{0}/QJ{0}-MASTER-Struktur-40-Halaman.md" -f $J)}
    }
    break
  }
  return @($rows)
}
function IsTartilType([string]$Type){ return $Type -notmatch 'Hafalan|Bahasa Arab|Akhlak|Hadis' }

New-Item -ItemType Directory -Force -Path $OutputDir|Out-Null
$records=@()
for($j=1;$j-le8;$j++){
  $map=@(ParseMasterMap $j)
  foreach($p in $map){
    $isTartil=IsTartilType $p.Type
    $status='MASTER_ONLY'
    if($j-le3){$status='SOURCE_EXISTS_OR_RECOVERY'}
    if(-not $isTartil){$status='NON_TARTIL_LAYER_LATER'}
    $o=[ordered]@{PageCode=$p.Code;Jilid=$j;PageNumber=$p.Page;Focus=$p.Focus;MainMaterial=$p.Main;MasterType=$p.Type;TartilPage=$isTartil;ContentStatus=$status;MasterFile=$p.MasterFile}
    for($i=1;$i-le24;$i++){$o[('Slot{0:D2}'-f$i)]=''}
    for($r=1;$r-le8;$r++){$o[('Row{0:D2}Count'-f$r)]=0;for($c=1;$c-le4;$c++){$o[('Row{0:D2}Cell{1:D2}'-f$r,$c)]=''}}
    $records += [pscustomobject]$o
  }
}
$records=@($records|Sort-Object Jilid,PageNumber)
$csv=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8.csv';$json=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8.json';$control=Join-Path $OutputDir 'QURBATA-TARTIL-PRODUCTION-CONTROL.csv'
[IO.File]::WriteAllLines($csv,($records|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllText($json,($records|ConvertTo-Json -Depth 5),$Utf8Bom)
$ctl=$records|Group-Object Jilid|ForEach-Object{[pscustomobject]@{Jilid=$_.Name;Pages=$_.Count;TartilPages=(@($_.Group|Where-Object {$_.TartilPage -eq $true})).Count;DeferredPages=(@($_.Group|Where-Object {$_.TartilPage -ne $true})).Count;SourceState=if([int]$_.Name -le3){'EXISTING_CONTENT_TO_NORMALIZE'}else{'CONTENT_TO_PRODUCE_FROM_MASTER'}}}
[IO.File]::WriteAllLines($control,($ctl|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
Write-Host 'QURBATA TARTIL master skeleton complete'
Write-Host "Pages indexed        : $($records.Count)"
Write-Host "Tartil pages         : $((@($records|Where-Object {$_.TartilPage -eq $true})).Count)"
Write-Host "Deferred other layer : $((@($records|Where-Object {$_.TartilPage -ne $true})).Count)"
foreach($g in ($records|Group-Object Jilid|Sort-Object Name)){Write-Host ("Jilid {0}              : {1}" -f $g.Name,$g.Count)}
Write-Host "CSV                  : $csv"
Write-Host "Control              : $control"
