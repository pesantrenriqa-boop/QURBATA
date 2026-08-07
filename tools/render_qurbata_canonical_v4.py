#!/usr/bin/env python3
"""Render QURBATA Jilid 1 integrated 40-page YAML with native QAE combining marks."""
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
NATIVE_PROFILE = ROOT / "content/qwo/arabic-engine/anchors/jilid-1-short-vowels-native-v2.yaml"
SPECIAL_PAGES = {20, 40}


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"YAML_ROOT_MUST_BE_MAPPING: {path}")
    return data


def load_native_profile(path: Path) -> dict[str, Any]:
    profile = load_yaml(path)
    if profile.get("engine") != "QAE":
        raise ValueError("QAE_PROFILE_ENGINE_INVALID")
    if profile.get("strategy", {}).get("primary_renderer") != "font-combining-mark":
        raise ValueError("QAE_NATIVE_PRIMARY_RENDERER_REQUIRED")
    marks = profile.get("marks", {})
    if set(marks) != {"fathah", "kasrah", "dhammah"}:
        raise ValueError("QAE_NATIVE_MARK_SET_INVALID")
    return profile


def load_pages(data_dir: Path) -> list[dict[str, Any]]:
    paths = sorted(data_dir.glob("page-*.yaml"))
    if len(paths) != 40:
        raise ValueError(f"LAYOUT_PAGE_COUNT actual={len(paths)} expected=40")
    pages = [load_yaml(path) for path in paths]
    if [int(page.get("page", 0)) for page in pages] != list(range(1, 41)):
        raise ValueError("LAYOUT_PAGE_SEQUENCE_INVALID")

    reading = 0
    letter_names = 0
    for page in pages:
        number = int(page["page"])
        kind = page.get("page_kind")
        objects = page.get("objects", [])
        names = page.get("letter_names", [])
        if number in SPECIAL_PAGES:
            if kind != "LETTER_NAMES" or objects or len(names) != 14:
                raise ValueError(f"SPECIAL_PAGE_CONTENT_INVALID page={number}")
            letter_names += len(names)
        else:
            if kind != "READING" or len(objects) != 24 or names:
                raise ValueError(f"READING_PAGE_CONTENT_INVALID page={number}")
            for item in objects:
                if item.get("render_mode") != "qae-native-short-vowel":
                    raise ValueError(f"NATIVE_RENDER_MODE_REQUIRED page={number} slot={item.get('slot')}")
                if not item.get("tokens"):
                    raise ValueError(f"NATIVE_TOKENS_REQUIRED page={number} slot={item.get('slot')}")
            reading += len(objects)
    if reading != 912 or letter_names != 28:
        raise ValueError(f"LAYOUT_CONTENT_TOTAL_INVALID reading={reading} letter_names={letter_names}")
    return pages


def build_token_css(tokens: dict[str, Any]) -> str:
    page, colors = tokens["page"], tokens["colors"]
    fonts, spacing, zones = tokens["fonts"], tokens["spacing"], tokens["zones"]
    variables = {
        "page-width": f"{page['width_mm']}mm", "page-height": f"{page['height_mm']}mm",
        "margin-top": f"{page['margin_top_mm']}mm", "margin-right": f"{page['margin_right_mm']}mm",
        "margin-bottom": f"{page['margin_bottom_mm']}mm", "margin-left": f"{page['margin_left_mm']}mm",
        "green": colors["green"], "gold": colors["gold"], "ink": colors["ink"],
        "soft": colors["soft"], "muted": colors["muted"],
        "arabic-font": f"\"{fonts['arabic_family']}\"", "latin-font": f"\"{fonts['latin_family']}\"",
        "material-title-size": f"{fonts['material_title_pt']}pt", "single-object-size": f"{fonts['single_object_pt']}pt",
        "pair-object-size": f"{fonts['pair_object_pt']}pt", "triple-object-size": f"{fonts['triple_object_pt']}pt",
        "header-size": f"{fonts['header_pt']}pt", "target-size": f"{fonts['target_pt']}pt", "footer-size": f"{fonts['footer_pt']}pt",
        "title-token-gap": f"{spacing['title_token_gap_mm']}mm", "pair-token-gap": f"{spacing['pair_token_gap_mm']}mm",
        "triple-token-gap": f"{spacing['triple_token_gap_mm']}mm", "group-gap": f"{spacing['group_gap_mm']}mm",
        "footer-gap": f"{spacing['footer_gap_mm']}mm", "group-inline-safety": f"{spacing['group_inline_safety_mm']}mm",
        "section-vertical-gap": f"{spacing['section_vertical_gap_mm']}mm",
        "header-height": f"{zones['header_height_mm']}mm", "targets-height": f"{zones['targets_height_mm']}mm",
        "material-title-height": f"{zones['material_title_height_mm']}mm", "singles-height": f"{zones['singles_height_mm']}mm",
        "pairs-height": f"{zones['pairs_height_mm']}mm", "triples-height": f"{zones['triples_height_mm']}mm",
        "footer-height": f"{zones['footer_height_mm']}mm", "bottom-band-height": f"{zones['bottom_band_height_mm']}mm",
    }
    return ":root {\n" + "\n".join(f"  --{key}: {value};" for key, value in variables.items()) + "\n}"


def compile_css(tokens: dict[str, Any], output: Path, book_dir: Path) -> None:
    special_css = r'''
.qae-native { font-family: var(--arabic-font); font-feature-settings: "liga" 0, "calt" 0; unicode-bidi: isolate; }
.qae-native-token { display: inline-block; }
.unit-length-1 .canonical-arabic { font-size: var(--single-object-size); }
.unit-length-2 .canonical-arabic { font-size: var(--pair-object-size); }
.unit-length-3 .canonical-arabic { font-size: var(--triple-object-size); }
.letter-name-grid { box-sizing:border-box; height:130mm; display:grid; grid-template-columns:repeat(2, 1fr); grid-template-rows:repeat(7, 1fr); gap:2.5mm; padding:3mm 8mm; direction:rtl; }
.letter-name-card { min-width:0; min-height:0; display:flex; align-items:center; justify-content:center; gap:5mm; border:0.25mm solid rgba(185,138,47,.38); border-radius:2mm; background:#fff; }
.letter-name-letter { font-family:var(--arabic-font); font-size:30pt; color:var(--green); line-height:1; }
.letter-name-arabic { font-family:var(--arabic-font); font-size:18pt; color:var(--ink); line-height:1.2; }
.page-kind-letter_names .canonical-title strong { font-family:var(--latin-font); }
'''
    css = [build_token_css(tokens),
           (book_dir / "layout/master-layout-v1.css").read_text(encoding="utf-8"),
           (book_dir / "layout/canonical-24-slot-v1.css").read_text(encoding="utf-8"),
           special_css]
    output.write_text("\n\n".join(css), encoding="utf-8")


def render_html(page: dict[str, Any], template_dir: Path, css: Path, logo: Path, output: Path, debug: bool, profile: dict[str, Any]) -> None:
    env = Environment(loader=FileSystemLoader(str(template_dir)), undefined=StrictUndefined, autoescape=True)
    enriched = dict(page)
    enriched["qae"] = {"profile": profile.get("profile")}
    html = env.get_template("canonical-j1-v2.html.j2").render(
        **enriched, css_uri=css.resolve().as_uri(), logo_uri=logo.resolve().as_uri(), layout_debug=debug,
    )
    output.write_text(html, encoding="utf-8")


async def inspect_layout(page, page_number: int) -> list[dict[str, Any]]:
    return await page.evaluate("""(pageNumber) => {
      const tolerance = 2;
      const issues = [];
      const add = (kind, el, extra={}) => { const r=el.getBoundingClientRect(); issues.push({kind,className:el.className,x:r.x,y:r.y,width:r.width,height:r.height,...extra}); };
      for (const el of document.querySelectorAll('.page,.header,.targets,.canonical-title,.footer,.canonical-grid,.letter-name-grid')) {
        if (el.scrollWidth > el.clientWidth + tolerance || el.scrollHeight > el.clientHeight + tolerance) add('STRUCTURAL_SCROLL_OVERFLOW', el, {scrollWidth:el.scrollWidth,clientWidth:el.clientWidth,scrollHeight:el.scrollHeight,clientHeight:el.clientHeight});
      }
      for (const slot of document.querySelectorAll('.canonical-object')) {
        const content=slot.querySelector('.canonical-arabic'); if(!content) continue;
        const s=slot.getBoundingClientRect(), c=content.getBoundingClientRect();
        if(c.left<s.left-tolerance||c.right>s.right+tolerance||c.top<s.top-tolerance||c.bottom>s.bottom+tolerance) add('OBJECT_OUTSIDE_SLOT',slot,{slot:slot.dataset.slot});
      }
      for (const card of document.querySelectorAll('.letter-name-card')) {
        const r=card.getBoundingClientRect();
        if(r.width<=0||r.height<=0) add('LETTER_NAME_CARD_INVALID',card,{pageNumber});
      }
      return issues;
    }""", page_number)


async def browser_render(html_paths: list[Path], png_dir: Path, pdf_path: Path, css: Path, font: str, report_path: Path) -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width":1120,"height":1584}, device_scale_factor=2)
        sections: list[str] = []
        all_issues: list[dict[str, Any]] = []
        for page_number, html_path in enumerate(html_paths, 1):
            await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            font_ready = await page.evaluate("font => document.fonts.check(`32px '${font}'`, 'بَ بِ بُ')", font)
            if not font_ready:
                raise RuntimeError(f"REQUIRED_FONT_NOT_ACTIVE: {font}")
            object_count = await page.locator(".canonical-object").count()
            name_count = await page.locator(".letter-name-card").count()
            if page_number in SPECIAL_PAGES:
                if object_count != 0 or name_count != 14:
                    raise RuntimeError(f"SPECIAL_RENDER_COUNT_INVALID page={page_number} objects={object_count} names={name_count}")
            else:
                if object_count != 24 or name_count != 0:
                    raise RuntimeError(f"READING_RENDER_COUNT_INVALID page={page_number} objects={object_count} names={name_count}")
            issues = await inspect_layout(page, page_number)
            for issue in issues: issue["page"] = f"page-{page_number:03d}"
            all_issues.extend(issues)
            await page.screenshot(path=str(png_dir / f"page-{page_number:03d}.png"), full_page=True)
            sections.append(await page.locator("main.page").evaluate("el => el.outerHTML"))

        report_path.write_text(json.dumps(all_issues, ensure_ascii=False, indent=2), encoding="utf-8")
        if all_issues:
            kinds: dict[str,int] = {}
            for issue in all_issues: kinds[issue["kind"]] = kinds.get(issue["kind"],0)+1
            summary = ",".join(f"{k}:{v}" for k,v in sorted(kinds.items()))
            raise RuntimeError(f"LAYOUT_OVERFLOW_COUNT={len(all_issues)} TYPES={summary} REPORT={report_path}")

        combined = "<!doctype html><html><head><meta charset='utf-8'><style>" + css.read_text(encoding="utf-8") + "</style></head><body>" + "".join(sections) + "</body></html>"
        await page.set_content(combined, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await page.pdf(path=str(pdf_path), format="A5", print_background=True, margin={"top":"0","right":"0","bottom":"0","left":"0"})
        await browser.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-dir", default="books/jilid-1")
    parser.add_argument("--data-dir", default="books/jilid-1/data-generated-v5-native")
    parser.add_argument("--output-dir", default="dist/jilid-1-canonical-v4-native")
    parser.add_argument("--logo", default="books/shared/assets/qurbata-logo.svg")
    parser.add_argument("--profile", default=str(NATIVE_PROFILE.relative_to(ROOT)))
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    book_dir, data_dir, output_dir = ROOT/args.book_dir, ROOT/args.data_dir, ROOT/args.output_dir
    logo, profile_path = ROOT/args.logo, ROOT/args.profile
    if not logo.is_file(): raise FileNotFoundError(f"OFFICIAL_LOGO_NOT_FOUND: {logo}")
    profile = load_native_profile(profile_path)
    pages = load_pages(data_dir)
    tokens = load_yaml(book_dir / "layout/design-tokens.yaml")

    html_dir, png_dir = output_dir/"html", output_dir/"png"
    html_dir.mkdir(parents=True, exist_ok=True); png_dir.mkdir(parents=True, exist_ok=True)
    runtime_css = output_dir/"runtime-layout.css"
    compile_css(tokens, runtime_css, book_dir)

    html_paths: list[Path] = []
    for page_data in pages:
        path = html_dir / f"page-{int(page_data['page']):03d}.html"
        render_html(page_data, book_dir/"templates", runtime_css, logo, path, args.debug, profile)
        html_paths.append(path)

    pdf = output_dir/"QURBATA-JILID-1-CANONICAL-V4-NATIVE.pdf"
    report = output_dir/"LAYOUT-OVERFLOW-REPORT-V4.json"
    asyncio.run(browser_render(html_paths, png_dir, pdf, runtime_css, str(tokens["fonts"]["arabic_family"]), report))
    print("PAGES_RENDERED=40")
    print("READING_OBJECTS_RENDERED=912")
    print("LETTER_NAMES_RENDERED=28")
    print(f"QAE_PROFILE={profile.get('profile')}")
    print("LAYOUT_OVERFLOW=0")
    print(f"OVERFLOW_REPORT={report.relative_to(ROOT)}")
    print(f"PDF={pdf.relative_to(ROOT)}")
    print("CANONICAL_RENDERER_V4=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
