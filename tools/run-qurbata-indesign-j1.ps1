param(
    [ValidateSet('Audit','Cleanup','AuditCleanup')]
    [string]$Mode = 'Audit',
    [string]$ProgId = ''
)

$ErrorActionPreference = 'Stop'

$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path
$JsxPath = Join-Path $PSScriptRoot 'indesign-qurbata-j1-automation.jsx'
$DistDir = Join-Path $RepoRoot 'dist\indesign-automation'
$CommandPath = Join-Path $DistDir 'QURBATA-INDESIGN-COMMAND.txt'
$SummaryPath = Join-Path $DistDir 'QURBATA-J1-AUTOMATION-SUMMARY.txt'
$AuditPath = Join-Path $DistDir 'QURBATA-J1-OVERSET-AUDIT.tsv'

if (!(Test-Path $JsxPath)) {
    throw "JSX not found: $JsxPath"
}

New-Item -ItemType Directory -Force -Path $DistDir | Out-Null

$modeValue = switch ($Mode) {
    'Audit'        { 'AUDIT' }
    'Cleanup'      { 'CLEANUP' }
    'AuditCleanup' { 'AUDIT_CLEANUP' }
}

[IO.File]::WriteAllText(
    $CommandPath,
    "MODE=$modeValue`r`n",
    (New-Object System.Text.UTF8Encoding($false))
)

function Get-InDesignProgIds {
    param([string]$Explicit)

    if ($Explicit) { return @($Explicit) }

    $ids = New-Object System.Collections.Generic.List[string]
    $ids.Add('InDesign.Application')

    try {
        $keys = Get-ChildItem Registry::HKEY_CLASSES_ROOT -ErrorAction Stop |
            Where-Object { $_.PSChildName -like 'InDesign.Application*' } |
            Select-Object -ExpandProperty PSChildName
        foreach ($k in $keys) {
            if (-not $ids.Contains($k)) { $ids.Add($k) }
        }
    }
    catch {}

    return @($ids)
}

function Connect-InDesign {
    param([string[]]$Candidates)

    $errors = @()
    foreach ($id in $Candidates) {
        try {
            Write-Host "Trying COM ProgID: $id"
            $app = New-Object -ComObject $id
            if ($null -ne $app) {
                return [pscustomobject]@{ App=$app; ProgId=$id }
            }
        }
        catch {
            $errors += "$id => $($_.Exception.Message)"
        }
    }
    throw ("Could not connect to InDesign COM automation.`r`n" + ($errors -join "`r`n"))
}

Write-Host "QURBATA InDesign J1 automation"
Write-Host "Mode       : $modeValue"
Write-Host "JSX        : $JsxPath"
Write-Host "Command    : $CommandPath"
Write-Host ""
Write-Host "IMPORTANT: keep the 36-page MERGED J1 document open and active in InDesign."
Write-Host ""

$candidates = Get-InDesignProgIds -Explicit $ProgId
$conn = Connect-InDesign -Candidates $candidates
$app = $conn.App
Write-Host "Connected  : $($conn.ProgId)"

try { $docCount = [int]$app.Documents.Count }
catch { throw "Connected to InDesign, but could not read Documents.Count: $($_.Exception.Message)" }

if ($docCount -lt 1) {
    throw "InDesign is connected, but no document is open. Open the merged J1 document first."
}

try {
    $activeName = [string]$app.ActiveDocument.Name
    Write-Host "Active doc : $activeName"
}
catch {
    Write-Warning "Could not read active document name."
}

$javaScriptLanguage = 1246973031
$jsxCode = [IO.File]::ReadAllText($JsxPath, [Text.Encoding]::UTF8)

Write-Host "Running JSX inside InDesign..."

try {
    $null = $app.DoScript($jsxCode, $javaScriptLanguage)
}
catch {
    throw "InDesign DoScript failed: $($_.Exception.Message)"
}

Start-Sleep -Milliseconds 500

if (!(Test-Path $SummaryPath)) {
    throw "JSX returned, but summary file was not created: $SummaryPath"
}

Write-Host ""
Write-Host "SUCCESS - InDesign created the automation report."
Write-Host ""
Get-Content $SummaryPath
Write-Host ""
Write-Host "Audit TSV   : $AuditPath"
Write-Host "Summary TXT : $SummaryPath"
