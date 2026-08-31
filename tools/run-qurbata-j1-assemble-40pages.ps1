param(
    [string]$ProgId = ''
)

$ErrorActionPreference = 'Stop'

$RepoRoot = (Resolve-Path "$PSScriptRoot\..").Path
$JsxPath = Join-Path $PSScriptRoot 'indesign-qurbata-j1-assemble-40pages.jsx'

if (!(Test-Path $JsxPath)) {
    throw "JSX not found: $JsxPath"
}

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
    foreach ($id in $Candidates) {
        try {
            Write-Host "Trying COM ProgID: $id"
            $app = New-Object -ComObject $id
            if ($null -ne $app) {
                return [pscustomobject]@{ App=$app; ProgId=$id }
            }
        }
        catch {}
    }
    throw "Could not connect to InDesign COM automation."
}

$conn = Connect-InDesign -Candidates (Get-InDesignProgIds -Explicit $ProgId)
$app = $conn.App

Write-Host "Connected  : $($conn.ProgId)"
Write-Host "Active doc : $($app.ActiveDocument.Name)"
Write-Host "Pages      : $($app.ActiveDocument.Pages.Count)"

if ([int]$app.ActiveDocument.Pages.Count -ne 36) {
    throw "Active document must be the 36-page Tartil production document before assembly."
}

$javaScriptLanguage = 1246973031
$jsxCode = [IO.File]::ReadAllText($JsxPath, [Text.Encoding]::UTF8)

Write-Host "Inserting special pages 18, 28, 36, 38..."
$null = $app.DoScript($jsxCode, $javaScriptLanguage)

Write-Host "Assembly complete."
Write-Host "Pages      : $($app.ActiveDocument.Pages.Count)"
Write-Host "Expected   : 40"
