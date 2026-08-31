param(
 [string]$SourceCsv='.\dist\indesign-template-data\QURBATA-INDESIGN-J1-4COL-8ROW-FULL-REFINED.csv',
 [string]$CompetencyTsv='.\dist\indesign-template-data\QURBATA-J1-40P-COMPETENCY.tsv',
 [string]$Output='.\dist\scribus\QURBATA-J1-PAGE01-TEST.sla'
)
$ErrorActionPreference='Stop'
if(!(Test-Path $SourceCsv)){throw "Source CSV not found: $SourceCsv"}
if(!(Test-Path $CompetencyTsv)){throw "Competency TSV not found: $CompetencyTsv"}
$data=Import-Csv $SourceCsv
$p=@($data|Where-Object{[int]$_.PageNumber -eq 1})[0]
$c=@(Import-Csv $CompetencyTsv -Delimiter ([char]9)|Where-Object{[int]$_.PageNumber -eq 1})[0]
if(!$p){throw 'Page 1 data not found.'}; if(!$c){throw 'Page 1 competency not found.'}
function X([string]$s){if($null -eq $s){return ''};return [Security.SecurityElement]::Escape($s)}
function F([double]$mm){return [string]::Format([Globalization.CultureInfo]::InvariantCulture,'0.###',$mm*2.834645669)}
$cells=@(); foreach($r in 1..8){foreach($col in 1..4){$name=('Row{0:D2}Cell{1:D2}' -f $r,$col);$cells += [string]$p.$name}}
if(@($cells|Where-Object{$_ -and $_.Trim()}).Count -ne 32){throw 'Page 1 does not contain 32 filled cells.'}
$W=148.0;$H=210.0;$margin=13.0;$gridY=55.0;$gridW=$W-2*$margin;$gridH=120.0;$gapX=2.2;$gapY=1.6;$cellW=($gridW-3*$gapX)/4;$cellH=($gridH-7*$gapY)/8
$objects=New-Object System.Collections.Generic.List[string]
function AddText([double]$x,[double]$y,[double]$w,[double]$h,[string]$txt,[double]$fs,[string]$font,[string]$name){$esc=X $txt;$objects.Add("<PAGEOBJECT XPOS='$(F $x)' YPOS='$(F $y)' WIDTH='$(F $w)' HEIGHT='$(F $h)' PTYPE='4' ANNAME='$(X $name)' FRTYPE='0' CLIPEDIT='0' PWIDTH='0' PCOLOR='None'><ITEXT CH='$esc' FONT='$(X $font)' FONTSIZE='$fs'/><para PARENT='QURBATA Center'/></PAGEOBJECT>")}
function AddCell([double]$x,[double]$y,[double]$w,[double]$h,[string]$txt,[string]$name){$esc=X $txt;$objects.Add("<PAGEOBJECT XPOS='$(F $x)' YPOS='$(F $y)' WIDTH='$(F $w)' HEIGHT='$(F $h)' PTYPE='4' ANNAME='$(X $name)' FRTYPE='0' CLIPEDIT='0' PWIDTH='0.7' PCOLOR='Black'><ITEXT CH='$esc' FONT='KFGQPC Uthman Taha Naskh' FONTSIZE='24'/><para PARENT='QURBATA Arabic'/></PAGEOBJECT>")}
AddText 13 11 122 8 'QURBATA JILID 1' 9 'Arial' 'Header'
AddText 13 27 122 7 ("$($c.CompetencyCode) - $($c.CompetencyTitle)") 10 'Arial' 'CompetencyTitle'
AddText 13 35 122 12 ('Target: '+$c.CompetencyTarget) 7.5 'Arial' 'CompetencyTarget'
$i=0;foreach($r in 0..7){foreach($col in 0..3){$x=$margin+$col*($cellW+$gapX);$y=$gridY+$r*($cellH+$gapY);AddCell $x $y $cellW $cellH $cells[$i] ("R$($r+1)C$($col+1)");$i++}}
AddText 13 188 35 7 'QURBATA - JILID 1' 7 'Arial' 'FooterLeft'
$footerArabic=[string]::Concat([char]0x062A,[char]0x064E,[char]0x0639,[char]0x064E,[char]0x0644,[char]0x0651,[char]0x064E,[char]0x0645,[char]0x0652,' - ',[char]0x0627,[char]0x0650,[char]0x0639,[char]0x0652,[char]0x0645,[char]0x064E,[char]0x0644,[char]0x0652,' - ',[char]0x0639,[char]0x064E,[char]0x0644,[char]0x0651,[char]0x0650,[char]0x0645,[char]0x0652)
AddText 48 188 87 7 $footerArabic 8 'KFGQPC Uthman Taha Naskh' 'FooterCenter'
$nl=[Environment]::NewLine
$xml='<?xml version="1.0" encoding="UTF-8"?>'+$nl+'<SCRIBUSUTF8NEW Version="1.6.6">'+$nl
$xml+="<DOCUMENT ANZPAGES='1' PAGEWIDTH='$(F $W)' PAGEHEIGHT='$(F $H)' BORDERLEFT='$(F $margin)' BORDERRIGHT='$(F $margin)' BORDERTOP='$(F 10)' BORDERBOTTOM='$(F 10)' PRESET='0' ORIENTATION='0' PAGESIZE='Custom' FIRSTNUM='1' BOOK='0' AUTOTEXT='0' ScratchLeft='100' ScratchRight='100' ScratchTop='100' ScratchBottom='100'>"+$nl
$xml+='<COLOR NAME="Black" SPACE="CMYK" C="0" M="0" Y="0" K="100"/>'+$nl+'<COLOR NAME="White" SPACE="CMYK" C="0" M="0" Y="0" K="0"/>'+$nl
$xml+='<STYLE NAME="QURBATA Center" ALIGN="1" LINESPMode="0"/>'+$nl+'<STYLE NAME="QURBATA Arabic" ALIGN="1" LINESPMode="0"/>'+$nl
$xml+="<PAGE NUM='0' NAM='' MNAM='' Size='Custom' Orientation='0' PAGEWIDTH='$(F $W)' PAGEHEIGHT='$(F $H)' BORDERTOP='$(F 10)' BORDERBOTTOM='$(F 10)' BORDERLEFT='$(F $margin)' BORDERRIGHT='$(F $margin)' LEFT='$(F $margin)' PRESET='0' VerticalGuides='' HorizontalGuides=''/>"+$nl
$xml+=($objects -join $nl)+$nl+'</DOCUMENT>'+$nl+'</SCRIBUSUTF8NEW>'+$nl
New-Item -ItemType Directory -Force (Split-Path $Output)|Out-Null
$outDir=(Resolve-Path (Split-Path $Output)).Path;$outPath=Join-Path $outDir (Split-Path $Output -Leaf)
[IO.File]::WriteAllText($outPath,$xml,(New-Object Text.UTF8Encoding($false)))
Write-Host 'QURBATA Scribus Page-1 TEST ready.'
Write-Host 'Cells       : 32/32'
Write-Host "Competency  : $($c.CompetencyCode) - $($c.CompetencyTitle)"
Write-Host "Output      : $Output"