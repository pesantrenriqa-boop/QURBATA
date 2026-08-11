#!/usr/bin/env python3
from __future__ import annotations
import argparse, asyncio, html, re, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / 'tools') not in sys.path:
    sys.path.insert(0, str(ROOT / 'tools'))

import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
import render_qurbata_jilid2_sukun_lab_v5 as sukunlab

SRC = ROOT / 'books/jilid-2/rebased'
DEFAULT = ROOT / 'dist/jilid-2-full-review'


def pnum(path: Path):
    m = re.search(r'QJ2-P(\d{3})', path.name, re.I)
    return int(m.group(1)) if m else None


def getsrc():
    pages = {}
    for path in SRC.glob('QJ2-P*.md'):
        n = pnum(path)
        if n and n not in pages:
            pages[n] = path
    return pages


def esc(text: str):
    return html.escape(text).replace('**', '')


def markdown_preview(text: str):
    out = []
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith('# '):
            out.append('<h1>' + esc(s[2:]) + '</h1>')
        elif s.startswith('## '):
            out.append('<h2>' + esc(s[3:]) + '</h2>')
        elif s.startswith('|'):
            out.append('<div class="row">' + esc(s) + '</div>')
        elif s.startswith('- '):
            out.append('<div class="bullet">• ' + esc(s[2:]) + '</div>')
        else:
            out.append('<p>' + esc(s) + '</p>')
    return ''.join(out)


def build(source_pages, font_uri: str):
    pages = []
    for n in range(1, 41):
        source = source_pages.get(n)
        body = markdown_preview(source.read_text(encoding='utf-8')) if source else '<div class="missing">SOURCE MISSING</div>'
        name = source.name if source else 'MISSING'
        pages.append(
            f'<section class="sheet"><div class="inner">'
            f'<div class="tag">FULL REVIEW PROOF - NOT FINAL PRINT</div>'
            f'<div class="folio">{n:02d}</div>'
            f'<div class="src">{html.escape(name)}</div>{body}'
            f'</div></section>'
        )

    css = f'''@page{{size:A5;margin:0}}
*{{box-sizing:border-box}}
@font-face{{font-family:q;src:url("{font_uri}")}}
body{{margin:0;background:#ddd}}
.sheet{{width:148mm;height:210mm;page-break-after:always;background:#fff;padding:8mm;overflow:hidden}}
.inner{{height:100%;position:relative;transform-origin:top left;font:7.2pt/1.2 q,Arial}}
.tag{{font:700 5.2pt Arial;color:#777;border-bottom:.2mm solid #b98a2f;padding-bottom:1mm}}
.folio{{position:absolute;right:0;top:-1mm;background:#064d37;color:white;padding:1.5mm 2mm;font:700 8pt Arial}}
.src{{font:5pt Consolas;color:#999;margin:1mm 0}}
h1{{font:700 10pt Arial;color:#064d37;margin:1mm 0}}
h2{{font:700 8pt Arial;color:#064d37;margin:1.3mm 0 .5mm}}
p,.row,.bullet{{margin:.45mm 0}}
.row{{font-size:6.4pt;border-bottom:.1mm solid #ddd;padding:.25mm}}
.missing{{margin-top:60mm;text-align:center;color:#b00;font:700 14pt Arial}}
'''
    script = '''<script>
(async () => {
  await document.fonts.ready;
  for (const sheet of document.querySelectorAll('.sheet')) {
    const inner = sheet.querySelector('.inner');
    const available = sheet.clientHeight;
    const needed = inner.scrollHeight;
    if (needed > available) {
      const zoom = Math.max(0.46, available / needed);
      inner.style.transform = 'scale(' + zoom + ')';
      inner.style.width = (100 / zoom) + '%';
    }
  }
})();
</script>'''
    return (
        '<!doctype html><html><head><meta charset="utf-8"><style>'
        + css
        + '</style></head><body>'
        + ''.join(pages)
        + script
        + '</body></html>'
    )


async def render(html_path: Path, out: Path):
    pdf = out / 'QURBATA-JILID-2-FULL-REVIEW-P001-P040.pdf'
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={'width': 1120, 'height': 1584})
        await page.goto(html_path.resolve().as_uri(), wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        await page.wait_for_timeout(300)
        count = await page.locator('.sheet').count()
        if count != 40:
            raise RuntimeError(f'PAGE_COUNT={count}')
        await page.pdf(
            path=str(pdf), format='A5', print_background=True,
            margin={'top': '0', 'right': '0', 'bottom': '0', 'left': '0'}
        )
        await browser.close()
    return pdf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output-dir', default=str(DEFAULT.relative_to(ROOT)))
    ap.add_argument('--font-file')
    ap.add_argument('--font-zip')
    ap.add_argument('--amiri-font')
    args = ap.parse_args()

    out = Path(args.output_dir)
    out = out if out.is_absolute() else ROOT / out
    out.mkdir(parents=True, exist_ok=True)

    source_pages = getsrc()
    missing = [n for n in range(1, 41) if n not in source_pages]
    kfg, _ = kfgloader.discover_font(args.font_file, args.font_zip, out)
    amiri = sukunlab.discover_amiri(args.amiri_font, out)
    hybrid = out / '_runtime_font' / 'KFGQPC-QURBATA-REVIEW-FROZEN-SUKUN.ttf'
    sukunlab.patch_font(kfg, amiri, hybrid, -1700)

    html_path = out / 'QURBATA-JILID-2-FULL-REVIEW.html'
    html_path.write_text(build(source_pages, hybrid.resolve().as_uri()), encoding='utf-8')
    pdf = asyncio.run(render(html_path, out))

    print('QURBATA_JILID2_FULL_REVIEW=PASS')
    print(f'SOURCE_PAGES_FOUND={len(source_pages)}')
    print('MISSING=' + (','.join(f'P{x:03d}' for x in missing) if missing else 'NONE'))
    print('ARTIFACT=REVIEW_PROOF_NOT_FINAL_PRINT')
    print(f'PDF={pdf.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
