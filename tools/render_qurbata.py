#!/usr/bin/env python3
"""Render QURBATA YAML page sources into HTML, PNG previews, and one print PDF."""
from __future__ import annotations

import argparse
import asyncio
import unicodedata
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
FATHA = "َ"
FORBIDDEN_PAGE_1_MARKS = {"ِ", "ُ", "ْ", "ّ", "ً", "ٍ", "ٌ", "ٰ", "ٓ"}
PAGE_1_LETTERS = {"ب", "ت", "ث"}
REQUIRED_ARABIC_FONT = "Amiri Quran"


def load_pages(data_dir: Path) -> list[dict]:
    pages: list[dict] = []
    for path in sorted(data_dir.glob("page-*.yaml")):
        with path.open(encoding="utf-8") as handle:
            page = yaml.safe_load(handle)
        page["_source"] = str(path.relative_to(ROOT))
        pages.append(page)
    if not pages:
        raise RuntimeError(f"NO_PAGE_DATA_FOUND: {data_dir}")
    return pages


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


def validate_page(page: dict) -> None:
    required = ["volume", "lesson", "page", "identity", "material_title", "objects", "targets", "footer"]
    missing = [key for key in required if key not in page]
    if missing:
        raise ValueError(f"PAGE_SCHEMA_INVALID page={page.get('page')} missing={missing}")

    singles = page["objects"].get("singles", [])
    pairs = page["objects"].get("pairs", [])
    triples = page["objects"].get("triples", [])
    if len(singles) != 6 or len(pairs) != 8 or len(triples) != 8:
        raise ValueError(
            f"OBJECT_DISTRIBUTION_INVALID page={page['page']} "
            f"singles={len(singles)} pairs={len(pairs)} triples={len(triples)}"
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
    page: dict,
    template_dir: Path,
    css_path: Path,
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
        css_uri=css_path.resolve().as_uri(),
        logo_uri=logo_path.resolve().as_uri(),
    )
    output_path.write_text(html, encoding="utf-8")


async def assert_font_and_tokens(page) -> None:
    font_ready = await page.evaluate(
        "font => document.fonts.check(`32px \\\"${font}\\\"`, 'بَ تَ ثَ')",
        REQUIRED_ARABIC_FONT,
    )
    if not font_ready:
        raise RuntimeError(f"REQUIRED_FONT_NOT_ACTIVE: {REQUIRED_ARABIC_FONT}")

    title_tokens = await page.locator(".material-title-text .arabic-token").count()
    if title_tokens != 3:
        raise RuntimeError(f"MATERIAL_TITLE_TOKEN_COUNT_INVALID: {title_tokens}")

    connected_title = await page.locator(".material-title-text").evaluate(
        "el => getComputedStyle(el).display !== 'flex'"
    )
    if connected_title:
        raise RuntimeError("MATERIAL_TITLE_NOT_USING_SEPARATE_TOKEN_LAYOUT")


async def browser_render(html_paths: list[Path], png_dir: Path, pdf_path: Path, css_path: Path) -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1120, "height": 1584}, device_scale_factor=2)

        combined_sections: list[str] = []
        for html_path in html_paths:
            await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            await assert_font_and_tokens(page)
            await page.screenshot(
                path=str(png_dir / f"{html_path.stem}.png"),
                full_page=True,
                omit_background=False,
            )
            combined_sections.append(await page.locator("main.page").evaluate("el => el.outerHTML"))

        css_text = css_path.read_text(encoding="utf-8")
        combined_html = (
            "<!doctype html><html><head><meta charset='utf-8'><style>"
            + css_text
            + "</style></head><body>"
            + "".join(combined_sections)
            + "</body></html>"
        )
        await page.set_content(combined_html, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await assert_font_and_tokens(page)
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
    css_path = book_dir / "layout/master-layout-v1.css"
    logo_path = ROOT / args.logo
    html_dir = output_dir / "html"
    png_dir = output_dir / "png"
    html_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)

    pages = load_pages(book_dir / "data")
    html_paths: list[Path] = []
    for page_data in pages:
        validate_page(page_data)
        html_path = html_dir / f"page-{int(page_data['page']):03d}.html"
        render_html(
            page_data,
            book_dir / "templates",
            css_path,
            logo_path,
            html_path,
        )
        html_paths.append(html_path)

    pdf_path = output_dir / "QURBATA-JILID-1.pdf"
    asyncio.run(browser_render(html_paths, png_dir, pdf_path, css_path))
    print(f"PAGES_RENDERED={len(html_paths)}")
    print(f"LOGO=OFFICIAL_ASSET")
    print(f"ARABIC_FONT={REQUIRED_ARABIC_FONT}")
    print(f"PDF={pdf_path.relative_to(ROOT)}")
    print(f"PNG_DIR={png_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
