#!/usr/bin/env python3
"""Generate an A/B visual-QA page for QURBATA short-vowel rendering.

This does not alter the production renderer. It compares the current SVG strategy
against native Arabic combining marks using the active design-token Arabic font.
"""
from __future__ import annotations

import argparse
import html
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OLD = ROOT / "content/qwo/arabic-engine/anchors/jilid-1-short-vowels.yaml"
DEFAULT_NATIVE = ROOT / "content/qwo/arabic-engine/anchors/jilid-1-short-vowels-native-v2.yaml"
DEFAULT_TOKENS = ROOT / "books/jilid-1/layout/design-tokens.yaml"
DEFAULT_OUTPUT = ROOT / "dist/qae-ab-visual-qa-v1/index.html"
SAMPLES = [
    "بَ", "بِ", "بُ", "تَ", "تِ", "تُ", "ثَ", "ثِ", "ثُ",
    "جَ", "جِ", "جُ", "حَ", "حِ", "حُ", "خَ", "خِ", "خُ",
    "بَتَ", "بِتِ", "بُتُ", "بَدَ", "بَرَ", "خَلَقَ", "ذَهَبَ", "رَحِمَ",
]
MARK_NAMES = {"َ": "fathah", "ِ": "kasrah", "ُ": "dhammah"}


def load_yaml(path: Path):
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def graphemes(text: str) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    base = ""
    mark = ""
    for ch in text:
        if ch in MARK_NAMES:
            if base:
                mark = ch
                result.append((base, mark))
                base = ""
                mark = ""
        else:
            if base:
                result.append((base, ""))
            base = ch
    if base:
        result.append((base, mark))
    return result


def old_svg_token(base: str, mark_char: str, profile: dict) -> str:
    if not mark_char:
        return f'<span class="native-token">{html.escape(base)}</span>'
    name = MARK_NAMES[mark_char]
    mark = profile["marks"][name]
    anchor = profile.get("anchors", {}).get(base, {}).get(name) or profile["anchors"]["default"][name]
    svg = (
        f'<svg viewBox="{html.escape(str(mark["view_box"]))}" aria-hidden="true">'
        f'<path d="{html.escape(str(mark["path_d"]))}" fill="none" stroke="currentColor" '
        f'stroke-width="{float(mark["stroke_width"])}" stroke-linecap="round"/></svg>'
    )
    style = (
        f'--x:{float(anchor["x_em"])}em;--y:{float(anchor["y_em"])}em;'
        f'--s:{float(anchor["scale"])};--mw:{float(mark["width_em"])}em;'
        f'--mh:{float(mark["height_em"])}em;'
    )
    return f'<span class="svg-token" style="{style}"><span class="base">{html.escape(base)}</span><span class="svg-mark">{svg}</span></span>'


def render_old(text: str, profile: dict) -> str:
    return "".join(old_svg_token(base, mark, profile) for base, mark in graphemes(text))


def render_native(text: str) -> str:
    return f'<span class="native-token">{html.escape(text)}</span>'


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old-profile", default=str(DEFAULT_OLD.relative_to(ROOT)))
    parser.add_argument("--native-profile", default=str(DEFAULT_NATIVE.relative_to(ROOT)))
    parser.add_argument("--tokens", default=str(DEFAULT_TOKENS.relative_to(ROOT)))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT.relative_to(ROOT)))
    args = parser.parse_args()

    old_profile = load_yaml(ROOT / args.old_profile)
    native_profile = load_yaml(ROOT / args.native_profile)
    tokens = load_yaml(ROOT / args.tokens)
    arabic_font = str(tokens["fonts"]["arabic_family"])

    if native_profile.get("strategy", {}).get("primary_renderer") != "font-combining-mark":
        raise ValueError("NATIVE_PROFILE_PRIMARY_RENDERER_INVALID")

    rows = []
    for text in SAMPLES:
        rows.append(
            '<div class="sample-row">'
            f'<div class="label" dir="rtl">{html.escape(text)}</div>'
            f'<div class="render old" dir="rtl">{render_old(text, old_profile)}</div>'
            f'<div class="render native" dir="rtl">{render_native(text)}</div>'
            '</div>'
        )

    document = f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>QURBATA QAE A/B Visual QA v1</title>
<style>
:root {{ --arabic-font: "{html.escape(arabic_font)}"; }}
* {{ box-sizing: border-box; }}
body {{ margin: 24px; font-family: Arial, sans-serif; color: #111; background: #fff; }}
h1 {{ margin-bottom: 6px; }}
.note {{ max-width: 900px; color: #444; margin-bottom: 22px; line-height: 1.5; }}
.grid-head, .sample-row {{ display: grid; grid-template-columns: 130px minmax(240px,1fr) minmax(240px,1fr); gap: 14px; align-items: center; }}
.grid-head {{ font-weight: 700; padding: 10px 12px; border-bottom: 2px solid #111; }}
.sample-row {{ min-height: 92px; padding: 10px 12px; border-bottom: 1px solid #ddd; }}
.label {{ font-family: var(--arabic-font), serif; font-size: 34px; text-align: center; }}
.render {{ min-height: 68px; display:flex; align-items:center; justify-content:center; font-family: var(--arabic-font), serif; font-size: 54px; line-height: 1.4; }}
.old {{ background: #fafafa; }}
.native {{ background: #f7f8f5; }}
.svg-token {{ position: relative; display: inline-block; min-width: .7em; text-align:center; margin: 0 .04em; }}
.svg-token .base {{ display:inline-block; }}
.svg-mark {{ position:absolute; left:50%; top:0; width:var(--mw); height:var(--mh); transform: translate(calc(-50% + var(--x)), var(--y)) scale(var(--s)); transform-origin:center; pointer-events:none; }}
.svg-mark svg {{ width:100%; height:100%; overflow:visible; display:block; }}
.native-token {{ font-family: var(--arabic-font), serif; }}
.checks {{ margin-top: 24px; max-width: 900px; line-height: 1.7; }}
</style>
</head>
<body>
<h1>QURBATA QAE A/B Visual QA v1</h1>
<div class="note">Font aktif: <b>{html.escape(arabic_font)}</b>. Kolom SVG adalah strategi lama; kolom Native V2 memakai combining mark Unicode asli dari font aktif. Halaman ini hanya untuk QA dan tidak mengubah renderer produksi.</div>
<div class="grid-head"><div>Objek</div><div>SVG lama</div><div>Native V2</div></div>
{''.join(rows)}
<div class="checks"><b>Checklist visual:</b> fathah tidak gemuk; kasrah jelas berupa garis di bawah; dhammah mempertahankan identitas bentuk; harakat tidak tampak seperti titik; tidak bertabrakan dengan titik ب/ت/ث; jarak antarahuruf tetap natural pada objek 2–3 unit.</div>
</body></html>'''

    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    print(f"QAE_AB_SAMPLES={len(SAMPLES)}")
    print(f"QAE_OLD_PROFILE={old_profile.get('profile')}")
    print(f"QAE_NATIVE_PROFILE={native_profile.get('profile')}")
    print(f"QAE_ARABIC_FONT={arabic_font}")
    print(f"QAE_AB_OUTPUT={output.relative_to(ROOT)}")
    print("QAE_AB_VISUAL_QA_V1=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
