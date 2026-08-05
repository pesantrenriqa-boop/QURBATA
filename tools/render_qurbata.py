#!/usr/bin/env python3
"""Render QURBATA page YAML into HTML, PNG, and print PDF."""
from __future__ import annotations

import argparse
import asyncio
import unicodedata
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from playwright.async_api import async_playwright

from qae import enrich_page, load_qae_profile

ROOT = Path(__file__).resolve().parents[1]
FATHA = "َ"
FORBIDDEN_PAGE_1_MARKS = {"ِ", "ُ", "ْ", "ّ", "ً", "ٍ", "ٌ", "ٰ", "ٓ"}
PAGE_1_LETTERS = {"ب", "ت", "ث"}


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"YAML_NOT_FOUND: {path}")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"YAML_ROOT_MUST_BE_MAPPING: {path}")
    return data


def load_pages(data_dir: Path) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    for path in sorted(data_dir.glob("page-*.yaml")):
        page = load_yaml(path)
        page["_source"] = str(path.relative_to(ROOT))
        pages.append(page)
    if not pages:
        raise RuntimeError(f"NO_PAGE_DATA_FOUND: {data_dir}")
    return pages


def require_number(mapping: dict[str, Any], key: str, section: str) -> float:
    value = mapping.get(key)
    if not isinstance(value, (int, float)):
        raise ValueError(f"TOKEN_NUMBER_REQUIRED section={section} key={key} value={value!r}")
    return float(value)


def validate_tokens(tokens: dict[str, Any]) -> None:
    sections = ["page", "colors", "fonts", "spacing", "zones", "objects", "arabic_rendering"]
    missing = [name for name in sections if not isinstance(tokens.get(name), dict)]
    if missing:
        raise ValueError(f"DESIGN_TOKEN_SECTIONS_MISSING: {missing}")
    if tokens["page"].get("size") != "A5":
        raise ValueError("ONLY_A5_LAYOUT_IS_SUPPORTED")
    if tokens["fonts"].get("arabic_family") != "Amiri Quran":
        raise ValueError("ARABIC_FONT_MUST_BE_AMIRI_QURAN")
    rendering = tokens["arabic_rendering"]
    if rendering.get("engine") != "QAE" or rendering.get("mark_renderer") != "css-shape":
        raise ValueError("QAE_CSS_SHAPE_RENDERER_REQUIRED")
    if not isinstance(rendering.get("profile_path"), str):
        raise ValueError("QAE_PROFILE_PATH_REQUIRED")
    for key in ("singles_count", "pairs_count", "triples_count"):
        if not isinstance(tokens["objects"].get(key), int) or tokens["objects"][key] < 1:
            raise ValueError(f"OBJECT_COUNT_INVALID: {key}")

    page = tokens["page"]
    zones = tokens["zones"]
    usable = require_number(page, "height_mm", "page") - require_number(page, "margin_top_mm", "page") - require_number(page, "margin_bottom_mm", "page")
    occupied = sum(require_number(zones, key, "zones") for key in (
        "header_height_mm", "targets_height_mm", "material_title_height_mm",
        "singles_height_mm", "pairs_height_mm", "triples_height_mm", "footer_height_mm",
    ))
    if occupied > usable:
        raise ValueError(f"VERTICAL_TOKENS_OVERFLOW occupied={occupied} usable={usable}")


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


def compile_runtime_css(tokens: dict[str, Any], master_path: Path, output_path: Path) -> None:
    output_path.write_text(build_token_css(tokens) + "\n\n" + master_path.read_text(encoding="utf-8"), encoding="utf-8")


def base_letters(text: str) -> list[str]:
    return [char for char in text if unicodedata.category(char).startswith("L")]


def validate_page_1_text(text: str, context: str) -> None:
    letters = base_letters(text)
    invalid = sorted(set(letters) - PAGE_1_LETTERS)
    forbidden = sorted(mark for mark in FORBIDDEN_PAGE_1_MARKS if mark in text)
    if invalid:
        raise ValueError(f"PAGE_1_LETTER_OUT_OF_SCOPE context={context} letters={invalid}")
    if forbidden:
        raise ValueError(f"PAGE_1_FORBIDDEN_MARK context={context} marks={forbidden}")
    if any(letter + FATHA not in text for letter in letters):
        raise ValueError(f"PAGE_1_NON_FATHA_LETTER context={context} text={text!r}")


def validate_page(page: dict[str, Any], tokens: dict[str, Any]) -> None:
    required = ["volume", "lesson", "page", "identity", "material_title", "objects", "targets", "footer"]
    missing = [key for key in required if key not in page]
    if missing:
        raise ValueError(f"PAGE_SCHEMA_INVALID page={page.get('page')} missing={missing}")
    singles, pairs, triples = page["objects"]["singles"], page["objects"]["pairs"], page["objects"]["triples"]
    expected = tokens["objects"]
    if (len(singles), len(pairs), len(triples)) != (expected["singles_count"], expected["pairs_count"], expected["triples_count"]):
        raise ValueError(f"OBJECT_DISTRIBUTION_INVALID page={page['page']}")
    if any(not isinstance(item, list) or len(item) != 2 for item in pairs):
        raise ValueError(f"PAIR_OBJECT_INVALID page={page['page']}")
    if any(not isinstance(item, list) or len(item) != 3 for item in triples):
        raise ValueError(f"TRIPLE_OBJECT_INVALID page={page['page']}")
    if int(page["page"]) == 1:
        if page["material_title"] != ["بَ", "تَ", "ثَ"]:
            raise ValueError("PAGE_1_TITLE_MUST_BE_BA_TA_THA_WITH_FATHA")
        for index, item in enumerate(singles, 1):
            validate_page_1_text(item, f"single-{index}")
        for name, groups in (("pair", pairs), ("triple", triples)):
            for object_index, item in enumerate(groups, 1):
                for token_index, token in enumerate(item, 1):
                    validate_page_1_text(token, f"{name}-{object_index}-token-{token_index}")


def render_html(page: dict[str, Any], template_dir: Path, css_path: Path, logo_path: Path, output_path: Path) -> None:
    if not logo_path.is_file():
        raise FileNotFoundError(f"OFFICIAL_LOGO_NOT_FOUND: {logo_path}")
    env = Environment(loader=FileSystemLoader(str(template_dir)), undefined=StrictUndefined, autoescape=True)
    html = env.get_template("page.html.j2").render(**page, css_uri=css_path.resolve().as_uri(), logo_uri=logo_path.resolve().as_uri())
    output_path.write_text(html, encoding="utf-8")


async def assert_render(page, required_font: str) -> None:
    font_ready = await page.evaluate("font => document.fonts.check(`32px \\\"${font}\\\"`, 'ب ت ث')", required_font)
    if not font_ready:
        raise RuntimeError(f"REQUIRED_FONT_NOT_ACTIVE: {required_font}")
    if await page.locator(".material-title-text .qae-token").count() != 3:
        raise RuntimeError("QAE_TITLE_TOKEN_COUNT_INVALID")
    if await page.locator(".arabic-mark").count() != 0:
        raise RuntimeError("LEGACY_ARABIC_MARK_STILL_PRESENT")
    qae_marks = await page.locator(".qae-mark").count()
    if qae_marks == 0:
        raise RuntimeError("QAE_MARKS_NOT_RENDERED")
    visible_combining_fatha = await page.locator("body").evaluate("el => el.innerText.includes('َ')")
    if visible_combining_fatha:
        raise RuntimeError("COMBINING_FATHA_LEAKED_TO_RENDERED_TEXT")


async def browser_render(html_paths: list[Path], png_dir: Path, pdf_path: Path, css_path: Path, required_font: str) -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1120, "height": 1584}, device_scale_factor=2)
        sections: list[str] = []
        for html_path in html_paths:
            await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            await assert_render(page, required_font)
            await page.screenshot(path=str(png_dir / f"{html_path.stem}.png"), full_page=True, omit_background=False)
            sections.append(await page.locator("main.page").evaluate("el => el.outerHTML"))
        combined = "<!doctype html><html><head><meta charset='utf-8'><style>" + css_path.read_text(encoding="utf-8") + "</style></head><body>" + "".join(sections) + "</body></html>"
        await page.set_content(combined, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await assert_render(page, required_font)
        await page.pdf(path=str(pdf_path), format="A5", print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        await browser.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-dir", default="books/jilid-1")
    parser.add_argument("--output-dir", default="dist/jilid-1")
    parser.add_argument("--logo", default="books/shared/assets/qurbata-logo.svg")
    args = parser.parse_args()

    book_dir, output_dir = ROOT / args.book_dir, ROOT / args.output_dir
    tokens = load_yaml(book_dir / "layout/design-tokens.yaml")
    validate_tokens(tokens)
    qae_profile_path = ROOT / tokens["arabic_rendering"]["profile_path"]
    qae_profile = load_qae_profile(qae_profile_path)

    html_dir, png_dir = output_dir / "html", output_dir / "png"
    html_dir.mkdir(parents=True, exist_ok=True); png_dir.mkdir(parents=True, exist_ok=True)
    runtime_css = output_dir / "runtime-layout.css"
    compile_runtime_css(tokens, book_dir / "layout/master-layout-v1.css", runtime_css)

    html_paths: list[Path] = []
    for page_data in load_pages(book_dir / "data"):
        validate_page(page_data, tokens)
        enriched = enrich_page(page_data, qae_profile)
        html_path = html_dir / f"page-{int(page_data['page']):03d}.html"
        render_html(enriched, book_dir / "templates", runtime_css, ROOT / args.logo, html_path)
        html_paths.append(html_path)

    pdf_path = output_dir / "QURBATA-JILID-1.pdf"
    font = str(tokens["fonts"]["arabic_family"])
    asyncio.run(browser_render(html_paths, png_dir, pdf_path, runtime_css, font))
    print(f"PAGES_RENDERED={len(html_paths)}")
    print("DESIGN_TOKENS=ACTIVE")
    print(f"QAE_PROFILE={qae_profile.get('profile')}")
    print("QAE_MARK_RENDERER=CSS_SHAPE")
    print(f"PDF={pdf_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
