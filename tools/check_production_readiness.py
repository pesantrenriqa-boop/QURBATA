#!/usr/bin/env python3
"""Post-render readiness checks for QURBATA Production Engine v1.0."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import Any

from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]


def require_file(path: Path, minimum_bytes: int = 1) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"REQUIRED_OUTPUT_MISSING: {path}")
    size = path.stat().st_size
    if size < minimum_bytes:
        raise ValueError(f"REQUIRED_OUTPUT_TOO_SMALL: {path} size={size}")


async def inspect_html(html_path: Path) -> dict[str, Any]:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1120, "height": 1584})
        await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
        await page.evaluate("document.fonts.ready")

        result = await page.evaluate(
            """
            () => {
              const main = document.querySelector('main.page');
              if (!main) throw new Error('MAIN_PAGE_NOT_FOUND');
              const pageRect = main.getBoundingClientRect();
              const logo = document.querySelector('.brand-logo');
              const tokens = [...document.querySelectorAll('.qae-token')];
              const marks = [...document.querySelectorAll('svg.qae-mark')];
              const objects = [...document.querySelectorAll('.object')];
              const overflowObjects = objects.filter((node) => {
                const r = node.getBoundingClientRect();
                return r.left < pageRect.left - 0.5 || r.right > pageRect.right + 0.5 ||
                       r.top < pageRect.top - 0.5 || r.bottom > pageRect.bottom + 0.5;
              });
              return {
                pageWidth: pageRect.width,
                pageHeight: pageRect.height,
                scrollWidth: main.scrollWidth,
                scrollHeight: main.scrollHeight,
                clientWidth: main.clientWidth,
                clientHeight: main.clientHeight,
                logoWidth: logo ? logo.getBoundingClientRect().width : 0,
                logoHeight: logo ? logo.getBoundingClientRect().height : 0,
                tokenCount: tokens.length,
                svgMarkCount: marks.length,
                legacyMarkCount: document.querySelectorAll('.arabic-mark').length,
                visibleCombiningFatha: document.body.innerText.includes('َ'),
                overflowObjectCount: overflowObjects.length,
                bodyHorizontalOverflow: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
              };
            }
            """
        )
        await browser.close()
        return result


async def run(output_dir: Path) -> dict[str, Any]:
    html_dir = output_dir / "html"
    png_dir = output_dir / "png"
    html_files = sorted(html_dir.glob("page-*.html"))
    if not html_files:
        raise RuntimeError("NO_HTML_PREVIEWS_FOUND")

    pdf_path = output_dir / "QURBATA-JILID-1.pdf"
    css_path = output_dir / "runtime-layout.css"
    require_file(pdf_path, 1_000)
    require_file(css_path, 100)

    page_reports: list[dict[str, Any]] = []
    for html_path in html_files:
        require_file(html_path, 500)
        png_path = png_dir / f"{html_path.stem}.png"
        require_file(png_path, 1_000)
        report = await inspect_html(html_path)
        if report["tokenCount"] <= 0:
            raise RuntimeError(f"NO_QAE_TOKENS: {html_path.name}")
        if report["tokenCount"] != report["svgMarkCount"]:
            raise RuntimeError(
                f"QAE_TOKEN_MARK_MISMATCH: {html_path.name} "
                f"tokens={report['tokenCount']} marks={report['svgMarkCount']}"
            )
        if report["legacyMarkCount"] != 0:
            raise RuntimeError(f"LEGACY_MARK_PRESENT: {html_path.name}")
        if report["visibleCombiningFatha"]:
            raise RuntimeError(f"COMBINING_FATHA_VISIBLE: {html_path.name}")
        if report["logoWidth"] <= 0 or report["logoHeight"] <= 0:
            raise RuntimeError(f"OFFICIAL_LOGO_NOT_RENDERED: {html_path.name}")
        if report["overflowObjectCount"] != 0:
            raise RuntimeError(f"LEARNING_OBJECT_OVERFLOW: {html_path.name}")
        if report["bodyHorizontalOverflow"]:
            raise RuntimeError(f"HORIZONTAL_PAGE_OVERFLOW: {html_path.name}")
        if report["scrollWidth"] > report["clientWidth"] + 1:
            raise RuntimeError(f"PAGE_SCROLL_WIDTH_OVERFLOW: {html_path.name}")
        if report["scrollHeight"] > report["clientHeight"] + 1:
            raise RuntimeError(f"PAGE_SCROLL_HEIGHT_OVERFLOW: {html_path.name}")
        page_reports.append({"page": html_path.name, **report})

    return {
        "schema_version": 1,
        "engine": "QURBATA Production Engine",
        "version": "1.0",
        "ready": True,
        "pages_checked": len(page_reports),
        "outputs": {
            "pdf": str(pdf_path.relative_to(ROOT)),
            "runtime_css": str(css_path.relative_to(ROOT)),
        },
        "checks": page_reports,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="dist/jilid-1")
    args = parser.parse_args()
    output_dir = ROOT / args.output_dir
    report = asyncio.run(run(output_dir))
    report_path = output_dir / "production-readiness.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("PRODUCTION_ENGINE_V1_READY=true")
    print(f"READINESS_REPORT={report_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
