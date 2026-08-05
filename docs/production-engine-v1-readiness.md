# QURBATA Production Engine v1.0 — Readiness Gates

Status: IN PROGRESS
Branch: `content/qurbata-jilid-1-8-production`

Engine v1.0 may be declared READY only when every gate below passes in GitHub Actions.

## Mandatory gates

1. Source data
   - Page YAML parses successfully.
   - Every page declares a competency contract.
   - Object counts and object arity match the contract.

2. Competency safety
   - Page 1 contains only `ب`, `ت`, `ث`.
   - Page 1 contains only fathah.
   - No connected-letter material is accepted on Page 1.

3. QAE typography
   - Amiri Quran is active for base glyphs.
   - Harakat is rendered by inline SVG path.
   - No legacy `.arabic-mark` element is present.
   - No visible combining fathah leaks into rendered text.
   - Every visible learning token has exactly one QAE SVG mark.

4. Layout
   - Page size is A5 portrait.
   - Main page bounding box does not overflow the PDF canvas.
   - No learning object crosses the page content bounds.
   - No horizontal scrollbar or clipped page content exists.

5. Brand assets
   - Official QURBATA logo exists and renders with non-zero dimensions.

6. Outputs
   - HTML preview exists for every page.
   - PNG preview exists for every page.
   - Print PDF exists and is non-empty.
   - Runtime CSS exists and is non-empty.

7. Release evidence
   - GitHub Actions build is green.
   - `production-readiness.json` reports `ready: true`.

Until all gates pass, the official status remains `IN PROGRESS`.
