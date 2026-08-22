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
function ParseMasterMap([int]$J){
  $path=Join-Path $RepoRoot ("books\jilid-{0}\QJ{0}-MASTER-Struktur-40-Halaman.md" -f $J)
  $text=ReadText $path; $rows=@(); if(!$text){ return @() }
  $lines=$text -split "`r?`n"
  for($i=0;$i-lt$lines.Count-1;$i++){
    if($lines[$i]-notmatch '^\s*\|\s*Halaman\s*\|'){continue}
    for($r=$i+2;$r-lt$lines.Count;$r++){
      if($lines[$r]-notmatch '^\s*\|'){break}
      $c=SplitCells $lines[$r]; if($c.Count-lt5){continue}
      if($c[0]-notmatch '^\d+$'){continue}
      $rows += [pscustomobject]@{Page=[int]$c[0];Code=$c[1];Focus=$c[2];Main=$c[3];Type=$c[4];MasterFile=("books/jilid-{0}/QJ{0}-MASTER-Struktur-40-Halaman.md" -f $J)}
    }
    break
  }
  return @($rows)
}
function IsTartilType([string]$Type){
  return $Type -notmatch 'Hafalan|Bahasa Arab|Akhlak|Hadis'
}

New-Item -ItemType Directory -Force -Path $OutputDir|Out-Null
$records=@()
for($j=1;$j-le8;$j++){
  $map=@(ParseMasterMap $j)
  foreach($p in $map){
    $isTartil=IsTartilType $p.Type
    $status='MASTER_ONLY'
    if($j-le3){$status='SOURCE_EXISTS_OR_RECOVERY'}
    if(-not $isTartil){$status='NON_TARTIL_LAYER_LATER'}
    $o=[ordered]@{
      PageCode=$p.Code;Jilid=$j;PageNumber=$p.Page;Focus=$p.Focus;MainMaterial=$p.Main;MasterType=$p.Type;TartilPage=$isTartil;ContentStatus=$status;MasterFile=$p.MasterFile
    }
    for($i=1;$i-le24;$i++){$o[('Slot{0:D2}'-f$i)]=''}
    for($r=1;$r-le8;$r++){
      $o[('Row{0:D2}Count'-f$r)]=0
      for($c=1;$c-le4;$c++){$o[('Row{0:D2}Cell{1:D2}'-f$r,$c)]=''}
    }
    $records += [pscustomobject]$o
  }
}
$records=@($records|Sort-Object Jilid,PageNumber)
$csv=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8.csv'
$json=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8.json'
$control=Join-Path $OutputDir 'QURBATA-TARTIL-PRODUCTION-CONTROL.csv'
[IO.File]::WriteAllLines($csv,($records|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllText($json,($records|ConvertTo-Json -Depth 5),$Utf8Bom)
$ctl=$records|Group-Object Jilid|ForEach-Object{
  [pscustomobject]@{
    Jilid=$_.Name
    Pages=$_.Count
    TartilPages=(@($_.Group|Where-Object {$_.TartilPage -eq $true})).Count
    DeferredPages=(@($_.Group|Where-Object {$_.TartilPage -ne $true})).Count
    SourceState=if([int]$_.Name -le3){'EXISTING_CONTENT_TO_NORMALIZE'}else{'CONTENT_TO_PRODUCE_FROM_MASTER'}
  }
}
[IO.File]::WriteAllLines($control,($ctl|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
Write-Host 'QURBATA TARTIL master skeleton complete'
Write-Host "Pages indexed        : $($records.Count)"
Write-Host "Tartil pages         : $((@($records|Where-Object {$_.TartilPage -eq $true})).Count)"
Write-Host "Deferred other layer : $((@($records|Where-Object {$_.TartilPage -ne $true})).Count)"
Write-Host "CSV                  : $csv"
Write-Host "Control              : $control"
