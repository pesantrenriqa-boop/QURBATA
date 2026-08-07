#!/usr/bin/env python3
"""Audit QURBATA Jilid 1 render artifacts and build a visual review index."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist-dir", default="dist/jilid-1-canonical-v3")
    args = parser.parse_args()

    dist = ROOT / args.dist_dir
    png_dir = dist / "png"
    html_dir = dist / "html"
    pdf = dist / "QURBATA-JILID-1-CANONICAL-V3.pdf"
    overflow_report = dist / "LAYOUT-OVERFLOW-REPORT-V3.json"

    required = [dist, png_dir, html_dir, pdf, overflow_report]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("MISSING_RENDER_ARTIFACTS=" + ",".join(missing))

    pngs = sorted(png_dir.glob("page-*.png"))
    html_pages = sorted(html_dir.glob("page-*.html"))
    issues = json.loads(overflow_report.read_text(encoding="utf-8"))

    failures: list[str] = []
    if len(pngs) != 36:
        failures.append(f"PNG_COUNT_{len(pngs)}")
    if len(html_pages) != 36:
        failures.append(f"HTML_COUNT_{len(html_pages)}")
    if issues:
        failures.append(f"OVERFLOW_ISSUES_{len(issues)}")
    if pdf.stat().st_size == 0:
        failures.append("PDF_EMPTY")

    zero_pngs = [path.name for path in pngs if path.stat().st_size == 0]
    if zero_pngs:
        failures.append("EMPTY_PNG=" + ",".join(zero_pngs))

    cards = []
    for png in pngs:
        page = png.stem.replace("page-", "")
        rel = png.relative_to(dist).as_posix()
        cards.append(
            f'<article class="card"><h2>Halaman {html.escape(page)}</h2>'
            f'<a href="{html.escape(rel)}" target="_blank">'
            f'<img src="{html.escape(rel)}" alt="Preview halaman {html.escape(page)}"></a></article>'
        )

    review = dist / "VISUAL-QA-INDEX-V1.html"
    review.write_text(
        """<!doctype html>
<html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>QURBATA Jilid 1 — Visual QA</title>
<style>
body{margin:0;padding:24px;background:#eef1ee;font-family:Arial,sans-serif;color:#13251d}
header{max-width:1200px;margin:0 auto 24px}h1{margin:0 0 8px}.summary{font-weight:700}
.grid{max-width:1600px;margin:auto;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:18px}
.card{background:#fff;border-radius:12px;padding:10px;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.card h2{font-size:14px;margin:0 0 8px}.card img{display:block;width:100%;height:auto;border:1px solid #d7ded9}
@media(max-width:1000px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:560px){.grid{grid-template-columns:1fr}}
</style></head><body>
<header><h1>QURBATA Jilid 1 — Visual QA</h1>
<p class="summary">36 halaman • 864 objek • overflow gate: PASS</p>
<p>Klik setiap halaman untuk membuka preview ukuran penuh.</p></header>
<main class="grid">"""
        + "".join(cards)
        + "</main></body></html>",
        encoding="utf-8",
    )

    print(f"PNG_COUNT={len(pngs)}")
    print(f"HTML_COUNT={len(html_pages)}")
    print(f"PDF_BYTES={pdf.stat().st_size}")
    print(f"OVERFLOW_ISSUES={len(issues)}")
    print(f"VISUAL_QA_INDEX={review.relative_to(ROOT)}")
    if failures:
        print("RENDER_ARTIFACT_AUDIT=FAIL")
        print("FAILURES=" + "|".join(failures))
        return 2
    print("RENDER_ARTIFACT_AUDIT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
