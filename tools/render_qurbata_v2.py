#!/usr/bin/env python3
"""QURBATA Production Renderer v2: design tokens + QAE SVG + validated page data."""
from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from playwright.async_api import async_playwright

from qae import enrich_page, load_qae_profile

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"YAML_NOT_FOUND: {path}")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"YAML_ROOT_MUST_BE_MAPPING: {path}")
    return data


def load_pages(data_dir: Path) -> list[dict[str, Any]]:
    pages = [load_yaml(path) for path in sorted(data_dir.glob("page-*.yaml"))]
    if not pages:
        raise RuntimeError(f"NO_PAGE_DATA_FOUND: {data_dir}")
    return pages


def validate_tokens(tokens: dict[str, Any]) -> None:
    for section in ("page", "colors", "fonts", "spacing", "zones", "objects", "arabic_rendering"):
        if not isinstance(tokens.get(section), dict):
            raise ValueError(f"DESIGN_TOKEN_SECTION_MISSING: {section}")
    if tokens["page"].get("size") != "A5":
        raise ValueError("ONLY_A5_LAYOUT_IS_SUPPORTED")
    if tokens["fonts"].get("arabic_family") != "Amiri Quran":
        raise ValueError("ARABIC_FONT_MUST_BE_AMIRI_QURAN")
    rendering = tokens["arabic_rendering"]
    if rendering.get("engine") != "QAE":
        raise ValueError("QAE_ENGINE_REQUIRED")
    if rendering.get("mark_renderer") != "inline-svg-path":
        raise ValueError("QAE_INLINE_SVG_PATH_REQUIRED")
    if not isinstance(rendering.get("profile_path"), str):
        raise ValueError("QAE_PROFILE_PATH_REQUIRED")


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
        "green": colors["green"],
        "gold": colors["gold"],
        "ink": colors["ink"],
        "soft": colors["soft"],
        "muted": colors["muted"],
        "arabic-font": f"\"{fonts['arabic_family']}\"",
        "latin-font": f"\"{fonts['latin_family']}\"",
        "material-title-size": f"{fonts['material_title_pt']}pt",
        "single-object-size": f"{fonts['single_object_pt']}pt",
        "pair-object-size": f"{fonts['pair_object_pt']}pt",
        "triple-object-size": f"{fonts['triple_object_pt']}pt",
        "header-size": f"{fonts['header_pt']}pt",
        "target-size": f"{fonts['target_pt']}pt",
        "footer-size": f"{fonts['footer_pt']}pt",
        "title-token-gap": f"{spacing['title_token_gap_mm']}mm",
        "pair-token-gap": f"{spacing['pair_token_gap_mm']}mm",
        "triple-token-gap": f"{spacing['triple_token_gap_mm']}mm",
        "group-gap": f"{spacing['group_gap_mm']}mm",
        "footer-gap": f"{spacing['footer_gap_mm']}mm",
        "group-inline-safety": f"{spacing['group_inline_safety_mm']}mm",
        "section-vertical-gap": f"{spacing['section_vertical_gap_mm']}mm",
        "header-height": f"{zones['header_height_mm']}mm",
        "targets-height": f"{zones['targets_height_mm']}mm",
        "material-title-height": f"{zones['material_title_height_mm']}mm",
        "singles-height": f"{zones['singles_height_mm']}mm",
        "pairs-height": f"{zones['pairs_height_mm']}mm",
        "triples-height": f"{zones['triples_height_mm']}mm",
        "footer-height": f"{zones['footer_height_mm']}mm",
        "bottom-band-height": f"{zones['bottom_band_height_mm']}mm",
    }
    return ":root {\n" + "\n".join(f"  --{key}: {value};" for key, value in variables.items()) + "\n}"


def compile_css(tokens: dict[str, Any], master_css: Path, runtime_css: Path) -> None:
    runtime_css.write_text(
        build_token_css(tokens) + "\n\n" + master_css.read_text(encoding="utf-8"),
        encoding="utf-8",
    )


def render_html(
    page_data: dict[str, Any],
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
    html = env.get_template("page.html.j2").render(
        **page_data,
        css_uri=css_path.resolve().as_uri(),
        logo_uri=logo_path.resolve().as_uri(),
    )
    output_path.write_text(html, encoding="utf-8")


async def assert_page(page, required_font: str) -> None:
    font_ready = await page.evaluate(
        "font => document.fonts.check(`32px \\\"${font}\\\"`, 'ب ت ث')",
        required_font,
    )
    if not font_ready:
        raise RuntimeError(f"REQUIRED_FONT_NOT_ACTIVE: {required_font}")
    if await page.locator(".qae-token").count() == 0:
        raise RuntimeError("QAE_TOKENS_NOT_RENDERED")
    if await page.locator("svg.qae-mark").count() == 0:
        raise RuntimeError("QAE_INLINE_SVG_MARKS_NOT_RENDERED")
    if await page.locator(".arabic-mark").count() != 0:
        raise RuntimeError("LEGACY_ARABIC_MARK_PRESENT")
    leaked = await page.locator("body").evaluate("el => el.innerText.includes('َ')")
    if leaked:
        raise RuntimeError("COMBINING_FATHA_LEAKED_TO_VISIBLE_TEXT")


async def browser_render(
    html_paths: list[Path],
    png_dir: Path,
    pdf_path: Path,
    css_path: Path,
    required_font: str,
) -> None:
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(viewport={"width": 1120, "height": 1584}, device_scale_factor=2)
        sections: list[str] = []
        for html_path in html_paths:
            await page.goto(html_path.resolve().as_uri(), wait_until="networkidle")
            await page.evaluate("document.fonts.ready")
            await assert_page(page, required_font)
            await page.screenshot(
                path=str(png_dir / f"{html_path.stem}.png"),
                full_page=True,
                omit_background=False,
            )
            sections.append(await page.locator("main.page").evaluate("el => el.outerHTML"))

        combined = (
            "<!doctype html><html><head><meta charset='utf-8'><style>"
            + css_path.read_text(encoding="utf-8")
            + "</style></head><body>"
            + "".join(sections)
            + "</body></html>"
        )
        await page.set_content(combined, wait_until="networkidle")
        await page.evaluate("document.fonts.ready")
        await assert_page(page, required_font)
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
    tokens = load_yaml(book_dir / "layout/design-tokens.yaml")
    validate_tokens(tokens)
    qae_profile = load_qae_profile(ROOT / tokens["arabic_rendering"]["profile_path"])

    html_dir, png_dir = output_dir / "html", output_dir / "png"
    html_dir.mkdir(parents=True, exist_ok=True)
    png_dir.mkdir(parents=True, exist_ok=True)
    runtime_css = output_dir / "runtime-layout.css"
    compile_css(tokens, book_dir / "layout/master-layout-v1.css", runtime_css)

    html_paths: list[Path] = []
    for page in load_pages(book_dir / "data"):
        enriched = enrich_page(page, qae_profile)
        html_path = html_dir / f"page-{int(page['page']):03d}.html"
        render_html(enriched, book_dir / "templates", runtime_css, ROOT / args.logo, html_path)
        html_paths.append(html_path)

    pdf_path = output_dir / "QURBATA-JILID-1.pdf"
    asyncio.run(
        browser_render(
            html_paths,
            png_dir,
            pdf_path,
            runtime_css,
            str(tokens["fonts"]["arabic_family"]),
        )
    )
    print(f"PAGES_RENDERED={len(html_paths)}")
    print("RENDERER=QURBATA_PRODUCTION_V2")
    print("QAE_MARK_RENDERER=INLINE_SVG_PATH")
    print(f"QAE_PROFILE={qae_profile.get('profile')}")
    print(f"PDF={pdf_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
