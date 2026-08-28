param(
    [ValidateSet('Audit','Cleanup','AuditCleanup')]
    [string]$Mode = 'Audit',
    [string]$InDesignExe = ''
)

$ErrorActionPreference = 'Stop'

$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path
$JsxPath = Join-Path $PSScriptRoot 'indesign-qurbata-j1-automation.jsx'
$DistDir = Join-Path $RepoRoot 'dist\indesign-automation'
$CommandPath = Join-Path $DistDir 'QURBATA-INDESIGN-COMMAND.txt'

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
    "MODE=$modeValue\`r\`n",
    (New-Object System.Text.UTF8Encoding($false))
)

function Find-InDesignExe {
    param([string]$Explicit)

    if ($Explicit) {
        if (!(Test-Path $Explicit)) {
            throw "InDesign.exe not found at explicit path: $Explicit"
        }
        return (Resolve-Path $Explicit).Path
    }

    $roots = @()
    if ($env:ProgramFiles) {
        $roots += (Join-Path $env:ProgramFiles 'Adobe')
    }
    $pf86 = [Environment]::GetFolderPath('ProgramFilesX86')
    if ($pf86) {
        $roots += (Join-Path $pf86 'Adobe')
    }

    $roots = $roots | Where-Object { $_ -and (Test-Path $_) }

    foreach ($root in $roots) {
        $found = Get-ChildItem -Path $root -Filter 'InDesign.exe' -File -Recurse -ErrorAction SilentlyContinue |
            Sort-Object FullName -Descending |
            Select-Object -First 1
        if ($found) { return $found.FullName }
    }

    return $null
}

$exe = Find-InDesignExe -Explicit $InDesignExe

Write-Host "QURBATA InDesign J1 automation"
Write-Host "Mode       : $modeValue"
Write-Host "JSX        : $JsxPath"
Write-Host "Command    : $CommandPath"

if (-not $exe) {
    Write-Warning "InDesign.exe was not found automatically."
    Write-Host ""
    Write-Host "Open InDesign, then run this JSX from Window > Utilities > Scripts:"
    Write-Host "  $JsxPath"
    Write-Host ""
    Write-Host "The command file has already been prepared for mode $modeValue."
    exit 2
}

Write-Host "InDesign   : $exe"
Write-Host ""
Write-Host "Make sure the MERGED QURBATA J1 document is the active InDesign document."
Write-Host "Launching JSX through InDesign..."

$quotedJsx = '"' + $JsxPath + '"'

try {
    Start-Process -FilePath $exe -ArgumentList @('-run', $quotedJsx) | Out-Null
    Write-Host ""
    Write-Host "Launch request sent."
    Write-Host "Expected report:"
    Write-Host "  $(Join-Path $DistDir 'QURBATA-J1-OVERSET-AUDIT.tsv')"
    Write-Host "  $(Join-Path $DistDir 'QURBATA-J1-AUTOMATION-SUMMARY.txt')"
}
catch {
    Write-Warning "Direct -run launch failed: $($_.Exception.Message)"
    Write-Host ""
    Write-Host "Fallback: in InDesign run the JSX manually from the Scripts panel:"
    Write-Host "  $JsxPath"
    exit 3
}
