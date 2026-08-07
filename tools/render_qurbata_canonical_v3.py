#!/usr/bin/env python3
"""Render verified 24-slot QURBATA Jilid 1 pages to HTML, PNG, and PDF."""
from __future__ import annotations

import argparse
import asyncio
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
QAE_PATH = ROOT / "tools/qae_v2.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


QAE = load_module(QAE_PATH, "qurbata_qae_v2")


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"YAML_ROOT_MUST_BE_MAPPING: {path}")
    return data


def load_pages(data_dir: Path) -> list[dict[str, Any]]:
    paths = sorted(data_dir.glob("page-*.yaml"))
    if len(paths) != 36:
        raise ValueError(f"LAYOUT_PAGE_COUNT actual={len(paths)} expected=36")
    pages = [load_yaml(path) for path in paths]
    if sum(len(page.get("objects", [])) for page in pages) != 864:
        raise ValueError("LAYOUT_OBJECT_COUNT_MUST_BE_864")
    return pages


def build_token_css(tokens: dict[str, Any]) -> str:
    page, colors = tokens["page"], tokens["colors"]
    fonts, spacing, zones = tokens["fonts"], tokens["spacing"], tokens["zones"]
    variables = {
        "page-width": f"{page['width_mm']}mm",
        "page-height": f"{page['height_mm']}mm",
        "margin-top": f"{page['margin_top_mm']}mm",
        "margin-right": f"{page['margin_right_mm']}mm",
        "margin-bottom": f"{page['margin_bottom_mm']}mm",
        "margin-left": f"{page['margin_left_mm']}mm",
        "green": colors["green"], "gold": colors["gold"], "ink": colors["ink"],
        "soft": colors["soft"], "muted": colors["muted"],
        "arabic-font": f"\"{fonts['arabic_family']}\"",
        "latin-font": f"\"{fonts['latin_family']}\"",
        "material-title-size": f"{fonts['material_title_pt']}pt",
        "single-object-size": f"{fonts['single_object_pt']}pt",
        "pair-object-size": f"{fonts['pair_object_pt']}pt",
        "triple-object-size": f"{fonts['triple_object_pt']}pt",
        "header-size": f"{fonts['header_pt']}pt", "target-size": f"{fonts['target_pt']}pt",
        "footer-size": f"{fonts['footer_pt']}pt",
        "title-token-gap": f"{spacing['title_token_gap_mm']}mm",
        "pair-token-gap": f"{spacing['pair_token_gap_mm']}mm",
        "triple-token-gap": f"{spacing['triple_token_gap_mm']}mm",
        "group-gap": f"{spacing['group_gap_mm']}mm", "footer-gap": f"{spacing['footer_gap_mm']}mm",
        "group-inline-safety": f"{spacing['group_inline_safety_mm']}mm",
        "section-vertical-gap": f"{spacing['section_vertical_gap_mm']}mm",
        "header-height": f"{zones['header_height_mm']}mm",
        "targets-height": f"{zones['targets_height_mm']}mm",
        "material-title-height": f"{zones['material_title_height_mm']}mm",
        "singles-height": f"{zones['singles_height_mm']}mm", "pairs-height": f"{zones['pairs_height_mm']}mm",
        "triples-height": f"{zones['triples_height_mm']}mm", "footer-height": f"{zones['footer_height_mm']}mm",
        "bottom-band-height": f"{zones['bottom_band_height_mm']}mm",
    }
    return ":root {\n" + "\n".join(f"  --{key}: {value};" for key, value in variables.items()) + "\n}"


def compile_css(tokens: dict[str, Any], output: Path, book_dir: Path) -> None:
    css = [
        build_token_css(tokens),
        (book_dir / "layout/master-layout-v1.css").read_text(encoding="utf-8"),
        (book_dir / "layout/canonical-24-slot-v1.css").read_text(encoding="utf-8"),
    ]
    output.write_text("\n\n".join(css), encoding="utf-8")


def render_html(page: dict[str, Any], template_dir: Path, css: Path, logo: Path, output: Path, debug: bool) -> None:
    env = Environment(loader=FileSystemLoader(str(template_dir)), undefined=StrictUndefined, autoescape=True)
    html = env.get_template("canonical-24-slot-v1.html.j2").render(
        **page,
        css_uri=css.resolve().as_uri(),
        logo_uri=logo.resolve().as_uri(),
        layout_debug=debug,
    )
    output.write_text(html, encoding="utf-8")


async def inspect_layout(page) -> list[dict[str, Any]]:
    """Return only production-significant geometric overflows.

    QAE marks deliberately extend outside their inline token boxes. Therefore
    scrollWidth/scrollHeight on every Arabic descendant produces false positives.
    This gate checks the fixed A5 page box, major layout zones, and whether each
    rendered Arabic object remains geometrically contained by its 24-slot cell.
    """
    return await page.evaluate("""
    () => {
      const tolerance = 2;
      const issues = [];
      const add = (kind, el, extra = {}) => {
        el.classList.add('is-overflow');
        const r = el.getBoundingClientRect();
        issues.push({kind, className: el.className, x:r.x, y:r.y, width:r.width, height:r.height, ...extra});
      };

      const structural = document.querySelectorAll('.page, .header, .targets, .canonical-title, .canonical-grid, .footer');
      for (const el of structural) {
        if (el.scrollWidth > el.clientWidth + tolerance || el.scrollHeight > el.clientHeight + tolerance) {
          add('STRUCTURAL_SCROLL_OVERFLOW', el, {
            scrollWidth: el.scrollWidth,
            clientWidth: el.clientWidth,
            scrollHeight: el.scrollHeight,
            clientHeight: el.clientHeight,
          });
        }
      }

      for (const slot of document.querySelectorAll('.canonical-object')) {
        const content = slot.querySelector('.canonical-arabic');
        if (!content) continue;
        const s = slot.getBoundingClientRect();
        const c = content.getBoundingClientRect();
        const outside = c.left < s.left - tolerance || c.right > s.right + tolerance ||
                        c.top < s.top - tolerance || c.bottom > s.bottom + tolerance;
        if (outside) {
          add('OBJECT_OUTSIDE_SLOT', slot, {
            slot: slot.dataset.slot || null,
            contentLeft: c.left, contentRight: c.right,
            contentTop: c.top, contentBottom: c.bottom,
            slotLeft: s.left, slotRight: s.right,
            slotTop: s.top, slotBottom: s.bottom,
          });
        }
      }
      return issues;
    }
    """)


async def browser_render(html_paths: list[Path], png_dir: Path, pdf_path: Path, css: Path, font: str, report_path: Path) -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1120, "height": 1584}, device_scale_factor=2)
        sections: list[str] = []
        all_issues: list[dict[str, Any]] = []
        for html_path in html_paths:
            await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            font_ready = await page.evaluate("font => document.fonts.check(`32px '${font}'`, 'ب ت ث')", font)
            if not font_ready:
                raise RuntimeError(f"REQUIRED_FONT_NOT_ACTIVE: {font}")
            if await page.locator(".canonical-object").count() != 24:
                raise RuntimeError(f"CANONICAL_SLOT_COUNT_INVALID: {html_path}")
            issues = await inspect_layout(page)
            for issue in issues:
                issue["page"] = html_path.stem
            all_issues.extend(issues)
            await page.screenshot(path=str(png_dir / f"{html_path.stem}.png"), full_page=True)
            sections.append(await page.locator("main.page").evaluate("el => el.outerHTML"))

        report_path.write_text(json.dumps(all_issues, ensure_ascii=False, indent=2), encoding="utf-8")
        if all_issues:
            kinds: dict[str, int] = {}
            for issue in all_issues:
                kinds[issue["kind"]] = kinds.get(issue["kind"], 0) + 1
            summary = ",".join(f"{key}:{value}" for key, value in sorted(kinds.items()))
            raise RuntimeError(f"LAYOUT_OVERFLOW_COUNT={len(all_issues)} TYPES={summary} REPORT={report_path}")

        combined = "<!doctype html><html><head><meta charset='utf-8'><style>" + css.read_text(encoding="utf-8") + "</style></head><body>" + "".join(sections) + "</body></html>"
        await page.set_content(combined, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.pdf(path=str(pdf_path), format="A5", print_background=True, margin={"top":"0","right":"0","bottom":"0","left":"0"})
        await browser.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-dir", default="books/jilid-1")
    parser.add_argument("--data-dir", default="books/jilid-1/data-generated-pue-v1")
    parser.add_argument("--output-dir", default="dist/jilid-1-canonical-v3")
    parser.add_argument("--logo", default="books/shared/assets/qurbata-logo.svg")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    book_dir, data_dir, output_dir = ROOT / args.book_dir, ROOT / args.data_dir, ROOT / args.output_dir
    logo = ROOT / args.logo
    if not logo.is_file():
        raise FileNotFoundError(f"OFFICIAL_LOGO_NOT_FOUND: {logo}")
    tokens = load_yaml(book_dir / "layout/design-tokens.yaml")
    profile = QAE.load_qae_profile(ROOT / "content/qwo/arabic-engine/anchors/jilid-1-short-vowels.yaml")
    pages = [QAE.enrich_page(page, profile) for page in load_pages(data_dir)]

    html_dir, png_dir = output_dir / "html", output_dir / "png"
    html_dir.mkdir(parents=True, exist_ok=True); png_dir.mkdir(parents=True, exist_ok=True)
    runtime_css = output_dir / "runtime-layout.css"
    compile_css(tokens, runtime_css, book_dir)

    html_paths: list[Path] = []
    for page in pages:
        path = html_dir / f"page-{int(page['page']):03d}.html"
        render_html(page, book_dir / "templates", runtime_css, logo, path, args.debug)
        html_paths.append(path)

    pdf = output_dir / "QURBATA-JILID-1-CANONICAL-V3.pdf"
    report = output_dir / "LAYOUT-OVERFLOW-REPORT-V3.json"
    asyncio.run(browser_render(html_paths, png_dir, pdf, runtime_css, str(tokens["fonts"]["arabic_family"]), report))
    print(f"PAGES_RENDERED={len(html_paths)}")
    print("OBJECTS_RENDERED=864")
    print("LAYOUT_OVERFLOW=0")
    print(f"OVERFLOW_REPORT={report.relative_to(ROOT)}")
    print(f"PDF={pdf.relative_to(ROOT)}")
    print("CANONICAL_RENDERER_V3=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
