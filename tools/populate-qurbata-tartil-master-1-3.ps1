param(
  [string]$RepoRoot=(Resolve-Path "$PSScriptRoot\..").Path,
  [string]$OutputDir="$PSScriptRoot\..\dist\tartil-master"
)
$ErrorActionPreference='Stop'
$Utf8Bom=New-Object System.Text.UTF8Encoding($true)

$buildScript=Join-Path $PSScriptRoot 'build-qurbata-tartil-master.ps1'
$extractScript=Join-Path $PSScriptRoot 'export-qurbata-indesign-v3.ps1'
if(!(Test-Path $buildScript)){throw "Missing $buildScript"}
if(!(Test-Path $extractScript)){throw "Missing $extractScript"}

# Run both scripts in the current PowerShell process so array parameters stay typed.
& $buildScript | Out-Host
$sourceOut=Join-Path $RepoRoot 'dist\tartil-source-1-3'
& $extractScript -RepoRoot $RepoRoot -OutputDir $sourceOut -Jilid @(1,2,3) | Out-Host

$skeletonPath=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8.csv'
$sourcePath=Join-Path $sourceOut 'QURBATA-INDESIGN-DATA-MERGE.csv'
$auditSourcePath=Join-Path $sourceOut 'QURBATA-INDESIGN-EXPORT-AUDIT.csv'
if(!(Test-Path $skeletonPath)){throw "Skeleton not found: $skeletonPath"}
if(!(Test-Path $sourcePath)){throw "J1-J3 source export not found: $sourcePath"}
if(!(Test-Path $auditSourcePath)){throw "J1-J3 source audit not found: $auditSourcePath"}

$master=@(Import-Csv $skeletonPath)
$source=@(Import-Csv $sourcePath)
$auditSource=@(Import-Csv $auditSourcePath)
$srcByCode=@{};foreach($s in $source){$srcByCode[$s.PageCode]=$s}
$auditByCode=@{};foreach($a in $auditSource){$auditByCode[$a.PageCode]=$a}

$filled=0;$partial=0;$missing=0;$future=0
$out=@();$audit=@()
foreach($m in $master){
  $code=$m.PageCode;$j=[int]$m.Jilid
  $state='FUTURE_J4_J8';$readingCount=0;$sourceFile='';$sourceConflict=$false
  if($j-le3){
    if($srcByCode.ContainsKey($code)){
      $s=$srcByCode[$code]
      $readingCount=if([string]::IsNullOrWhiteSpace([string]$s.ReadingCount)){0}else{[int]$s.ReadingCount}
      $sourceFile=[string]$s.SourceFile
      $sourceConflict=([string]$s.SourceConflict -eq 'True')
      for($i=1;$i-le24;$i++){$name=('Slot{0:D2}'-f$i);$m.$name=$s.$name}
      for($r=1;$r-le8;$r++){
        $cn=('Row{0:D2}Count'-f$r);$m.$cn=$s.$cn
        for($c=1;$c-le4;$c++){$n=('Row{0:D2}Cell{1:D2}'-f$r,$c);$m.$n=$s.$n}
      }
      if($readingCount-eq24 -and -not $sourceConflict){$state='FILLED_24';$filled++}
      elseif($readingCount-gt0){$state='PARTIAL_REVIEW';$partial++}
      else{$state='NO_READING_SOURCE';$missing++}
    }else{$state='NO_SOURCE_RECORD';$missing++}
  }else{$future++}
  $m.ContentStatus=$state
  $out+=$m
  $audit+=[pscustomobject]@{PageCode=$code;Jilid=$j;ReadingCount=$readingCount;ContentStatus=$state;SourceConflict=$sourceConflict;SourceFile=$sourceFile}
}

$outCsv=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8-FILLED.csv'
$outJson=Join-Path $OutputDir 'QURBATA-TARTIL-MASTER-1-8-FILLED.json'
$auditCsv=Join-Path $OutputDir 'QURBATA-TARTIL-CONTENT-AUDIT.csv'
[IO.File]::WriteAllLines($outCsv,@($out|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)
[IO.File]::WriteAllText($outJson,($out|ConvertTo-Json -Depth 5),$Utf8Bom)
[IO.File]::WriteAllLines($auditCsv,@($audit|ConvertTo-Csv -NoTypeInformation),$Utf8Bom)

Write-Host 'QURBATA TARTIL content populate complete'
Write-Host "Master pages          : $($out.Count)"
Write-Host "J1-J3 filled 24       : $filled"
Write-Host "J1-J3 partial review  : $partial"
Write-Host "J1-J3 no reading      : $missing"
Write-Host "J4-J8 future produce  : $future"
Write-Host "Filled master         : $outCsv"
Write-Host "Audit                 : $auditCsv"
