#!/usr/bin/env python3
"""Render QURBATA YAML page sources into HTML, PNG previews, and one print PDF."""
from __future__ import annotations

import argparse
import asyncio
import unicodedata
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from playwright.async_api import async_playwright

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
    required_sections = ["page", "colors", "fonts", "spacing", "zones", "objects", "arabic_rendering"]
    missing = [section for section in required_sections if not isinstance(tokens.get(section), dict)]
    if missing:
        raise ValueError(f"DESIGN_TOKEN_SECTIONS_MISSING: {missing}")

    page = tokens["page"]
    fonts = tokens["fonts"]
    zones = tokens["zones"]
    objects = tokens["objects"]

    if page.get("size") != "A5":
        raise ValueError("ONLY_A5_LAYOUT_IS_SUPPORTED")
    if fonts.get("arabic_family") != "Amiri Quran":
        raise ValueError("ARABIC_FONT_MUST_BE_AMIRI_QURAN")
    for key in ("singles_count", "pairs_count", "triples_count"):
        if not isinstance(objects.get(key), int) or objects[key] < 1:
            raise ValueError(f"OBJECT_COUNT_INVALID: {key}")

    usable_height = require_number(page, "height_mm", "page") - require_number(page, "margin_top_mm", "page") - require_number(page, "margin_bottom_mm", "page")
    occupied_height = sum(
        require_number(zones, key, "zones")
        for key in (
            "header_height_mm",
            "targets_height_mm",
            "material_title_height_mm",
            "singles_height_mm",
            "pairs_height_mm",
            "triples_height_mm",
            "footer_height_mm",
        )
    )
    if occupied_height > usable_height:
        raise ValueError(
            f"VERTICAL_TOKENS_OVERFLOW occupied={occupied_height} usable={usable_height}"
        )


def css_value(value: Any) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    return str(value)


def build_token_css(tokens: dict[str, Any]) -> str:
    page = tokens["page"]
    colors = tokens["colors"]
    fonts = tokens["fonts"]
    spacing = tokens["spacing"]
    zones = tokens["zones"]

    variables = {
        "page-width": f"{css_value(page['width_mm'])}mm",
        "page-height": f"{css_value(page['height_mm'])}mm",
        "margin-top": f"{css_value(page['margin_top_mm'])}mm",
        "margin-right": f"{css_value(page['margin_right_mm'])}mm",
        "margin-bottom": f"{css_value(page['margin_bottom_mm'])}mm",
        "margin-left": f"{css_value(page['margin_left_mm'])}mm",
        "green": colors["green"],
        "gold": colors["gold"],
        "ink": colors["ink"],
        "soft": colors["soft"],
        "muted": colors["muted"],
        "arabic-font": f"\"{fonts['arabic_family']}\"",
        "latin-font": f"\"{fonts['latin_family']}\"",
        "material-title-size": f"{css_value(fonts['material_title_pt'])}pt",
        "single-object-size": f"{css_value(fonts['single_object_pt'])}pt",
        "pair-object-size": f"{css_value(fonts['pair_object_pt'])}pt",
        "triple-object-size": f"{css_value(fonts['triple_object_pt'])}pt",
        "header-size": f"{css_value(fonts['header_pt'])}pt",
        "target-size": f"{css_value(fonts['target_pt'])}pt",
        "footer-size": f"{css_value(fonts['footer_pt'])}pt",
        "title-token-gap": f"{css_value(spacing['title_token_gap_mm'])}mm",
        "pair-token-gap": f"{css_value(spacing['pair_token_gap_mm'])}mm",
        "triple-token-gap": f"{css_value(spacing['triple_token_gap_mm'])}mm",
        "group-gap": f"{css_value(spacing['group_gap_mm'])}mm",
        "footer-gap": f"{css_value(spacing['footer_gap_mm'])}mm",
        "header-height": f"{css_value(zones['header_height_mm'])}mm",
        "targets-height": f"{css_value(zones['targets_height_mm'])}mm",
        "material-title-height": f"{css_value(zones['material_title_height_mm'])}mm",
        "singles-height": f"{css_value(zones['singles_height_mm'])}mm",
        "pairs-height": f"{css_value(zones['pairs_height_mm'])}mm",
        "triples-height": f"{css_value(zones['triples_height_mm'])}mm",
        "footer-height": f"{css_value(zones['footer_height_mm'])}mm",
        "bottom-band-height": f"{css_value(zones['bottom_band_height_mm'])}mm",
    }
    lines = [":root {"]
    lines.extend(f"  --{name}: {value};" for name, value in variables.items())
    lines.append("}")
    return "\n".join(lines)


def compile_runtime_css(tokens: dict[str, Any], master_css_path: Path, output_path: Path) -> None:
    master_css = master_css_path.read_text(encoding="utf-8")
    output_path.write_text(build_token_css(tokens) + "\n\n" + master_css, encoding="utf-8")


def base_letters(text: str) -> list[str]:
    return [ch for ch in text if unicodedata.category(ch).startswith("L")]


def validate_page_1_text(text: str, *, context: str) -> None:
    letters = base_letters(text)
    invalid_letters = sorted(set(letters) - PAGE_1_LETTERS)
    forbidden_marks = sorted(mark for mark in FORBIDDEN_PAGE_1_MARKS if mark in text)
    if invalid_letters:
        raise ValueError(f"PAGE_1_LETTER_OUT_OF_SCOPE context={context} letters={invalid_letters}")
    if forbidden_marks:
        raise ValueError(f"PAGE_1_FORBIDDEN_MARK context={context} marks={forbidden_marks}")
    if any(letter + FATHA not in text for letter in letters):
        raise ValueError(f"PAGE_1_NON_FATHA_LETTER context={context} text={text!r}")


def validate_page(page: dict[str, Any], tokens: dict[str, Any]) -> None:
    required = ["volume", "lesson", "page", "identity", "material_title", "objects", "targets", "footer"]
    missing = [key for key in required if key not in page]
    if missing:
        raise ValueError(f"PAGE_SCHEMA_INVALID page={page.get('page')} missing={missing}")

    singles = page["objects"].get("singles", [])
    pairs = page["objects"].get("pairs", [])
    triples = page["objects"].get("triples", [])
    expected = tokens["objects"]
    if (
        len(singles) != expected["singles_count"]
        or len(pairs) != expected["pairs_count"]
        or len(triples) != expected["triples_count"]
    ):
        raise ValueError(
            f"OBJECT_DISTRIBUTION_INVALID page={page['page']} "
            f"singles={len(singles)}/{expected['singles_count']} "
            f"pairs={len(pairs)}/{expected['pairs_count']} "
            f"triples={len(triples)}/{expected['triples_count']}"
        )
    if any(not isinstance(item, list) or len(item) != 2 for item in pairs):
        raise ValueError(f"PAIR_OBJECT_INVALID page={page['page']}")
    if any(not isinstance(item, list) or len(item) != 3 for item in triples):
        raise ValueError(f"TRIPLE_OBJECT_INVALID page={page['page']}")

    if int(page["page"]) == 1:
        if page["material_title"] != ["بَ", "تَ", "ثَ"]:
            raise ValueError("PAGE_1_TITLE_MUST_BE_BA_TA_THA_WITH_FATHA")
        for index, item in enumerate(singles, start=1):
            validate_page_1_text(item, context=f"single-{index}")
        for group_name, groups in (("pair", pairs), ("triple", triples)):
            for object_index, item in enumerate(groups, start=1):
                for letter_index, token in enumerate(item, start=1):
                    validate_page_1_text(
                        token,
                        context=f"{group_name}-{object_index}-token-{letter_index}",
                    )


def render_html(
    page: dict[str, Any],
    template_dir: Path,
    runtime_css_path: Path,
    logo_path: Path,
    output_path: Path,
) -> None:
    if not logo_path.is_file():
        raise FileNotFoundError(f"OFFICIAL_LOGO_NOT_FOUND: {logo_path}")
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        undefined=StrictUndefined,
        autoescape=True,
    )
    template = env.get_template("page.html.j2")
    html = template.render(
        **page,
        css_uri=runtime_css_path.resolve().as_uri(),
        logo_uri=logo_path.resolve().as_uri(),
    )
    output_path.write_text(html, encoding="utf-8")


async def assert_font_and_tokens(page, required_arabic_font: str) -> None:
    font_ready = await page.evaluate(
        "font => document.fonts.check(`32px \\\"${font}\\\"`, 'بَ تَ ثَ')",
        required_arabic_font,
    )
    if not font_ready:
        raise RuntimeError(f"REQUIRED_FONT_NOT_ACTIVE: {required_arabic_font}")

    title_tokens = await page.locator(".material-title-text .arabic-token").count()
    if title_tokens != 3:
        raise RuntimeError(f"MATERIAL_TITLE_TOKEN_COUNT_INVALID: {title_tokens}")

    display = await page.locator(".material-title-text").evaluate("el => getComputedStyle(el).display")
    if display != "flex":
        raise RuntimeError("MATERIAL_TITLE_NOT_USING_SEPARATE_TOKEN_LAYOUT")


async def browser_render(
    html_paths: list[Path],
    png_dir: Path,
    pdf_path: Path,
    runtime_css_path: Path,
    required_arabic_font: str,
) -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1120, "height": 1584}, device_scale_factor=2)

        combined_sections: list[str] = []
        for html_path in html_paths:
            await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            await assert_font_and_tokens(page, required_arabic_font)
            await page.screenshot(
                path=str(png_dir / f"{html_path.stem}.png"),
                full_page=True,
                omit_background=False,
            )
            combined_sections.append(await page.locator("main.page").evaluate("el => el.outerHTML"))

        css_text = runtime_css_path.read_text(encoding="utf-8")
        combined_html = (
            "<!doctype html><html><head><meta charset='utf-8'><style>"
            + css_text
            + "</style></head><body>"
            + "".join(combined_sections)
            + "</body></html>"
        )
        await page.set_content(combined_html, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await assert_font_and_tokens(page, required_arabic_font)
        await page.pdf(
            path=str(pdf_path),
            format="A5",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        await browser.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-dir", default="books/jilid-1")
    parser.add_argument("--output-dir", default="dist/jilid-1")
    parser.add_argument("--logo", default="books/shared/assets/qurbata-logo.svg")
    args = parser.parse_args()

    book_dir = ROOT / args.book_dir
    output_dir = ROOT / args.output_dir
    master_css_path = book_dir / "layout/master-layout-v1.css"
    token_path = book_dir / "layout/design-tokens.yaml"
    logo_path = ROOT / args.logo
    html_dir = output_dir / "html"
    png_dir = output_dir / "png"
    runtime_css_path = output_dir / "runtime-layout.css"
    html_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)

    tokens = load_yaml(token_path)
    validate_tokens(tokens)
    compile_runtime_css(tokens, master_css_path, runtime_css_path)

    pages = load_pages(book_dir / "data")
    html_paths: list[Path] = []
    for page_data in pages:
        validate_page(page_data, tokens)
        html_path = html_dir / f"page-{int(page_data['page']):03d}.html"
        render_html(
            page_data,
            book_dir / "templates",
            runtime_css_path,
            logo_path,
            html_path,
        )
        html_paths.append(html_path)

    pdf_path = output_dir / "QURBATA-JILID-1.pdf"
    required_arabic_font = str(tokens["fonts"]["arabic_family"])
    asyncio.run(
        browser_render(
            html_paths,
            png_dir,
            pdf_path,
            runtime_css_path,
            required_arabic_font,
        )
    )
    print(f"PAGES_RENDERED={len(html_paths)}")
    print("DESIGN_TOKENS=ACTIVE")
    print(f"TOKEN_FILE={token_path.relative_to(ROOT)}")
    print("LOGO=OFFICIAL_ASSET")
    print(f"ARABIC_FONT={required_arabic_font}")
    print(f"PDF={pdf_path.relative_to(ROOT)}")
    print(f"PNG_DIR={png_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
