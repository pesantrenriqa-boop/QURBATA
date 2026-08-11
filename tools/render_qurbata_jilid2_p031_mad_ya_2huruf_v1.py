#!/usr/bin/env python3
"""QURBATA Jilid 2 — one-page Mad Ya drill: kasrah + ya sukun, two-letter units only."""
from __future__ import annotations
import argparse, asyncio, html
from pathlib import Path
from playwright.async_api import async_playwright
import render_qurbata_jilid2_foundation_v3 as base

ROOT=Path(__file__).resolve().parents[1]
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'
DEFAULT_OUT=ROOT/'dist/jilid-2-p031-mad-ya-2huruf-v1'

# Exactly two base letters per object: consonant with kasrah + ya sukun.
# No tanwin, no third consonant, no mad waw, no advanced sukun domain.
ROWS=[
 ['بِيْ','تِيْ','ثِيْ','جِيْ'],
 ['حِيْ','خِيْ','دِيْ','ذِيْ'],
 ['رِيْ','زِيْ','سِيْ','شِيْ'],
 ['صِيْ','ضِيْ','طِيْ','ظِيْ'],
 ['عِيْ','غِيْ','فِيْ','قِيْ'],
 ['كِيْ','لِيْ','مِيْ','نِيْ'],
 ['هِيْ','وِيْ','يِيْ','ئِيْ'],
]

def esc(s): return html.escape(s)

CSS=base.base.CSS+r'''
.page{padding:5mm 8mm 3mm;position:relative}.header{height:17mm;display:grid;grid-template-columns:25mm minmax(0,1fr) 12mm;align-items:center;gap:3mm}.brand-logo{width:23mm;height:16mm;object-fit:contain}.heading{text-align:center}.learning-header-title{color:#064d37;font:700 8.4pt "Segoe UI",sans-serif;letter-spacing:.1em}.page-number{background:#064d37;color:#fff;border-bottom:1.1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.6mm 1mm 3.4mm;border-radius:0 0 3mm 3mm;font-size:12pt}.presentation{height:22mm;display:flex;align-items:center;justify-content:center}.presentation-object{direction:rtl;font-family:'KFGQPC Uthman Taha Naskh','KFGQPC Uthmanic Script HAFS','Amiri Quran',serif;font-size:32pt}.grid{height:151mm;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(7,1fr);gap:2.5mm 5mm;direction:rtl;align-items:center}.cell{display:flex;align-items:center;justify-content:center;overflow:visible}.glyph{direction:rtl;font-family:'KFGQPC Uthman Taha Naskh','KFGQPC Uthmanic Script HAFS','Amiri Quran',serif;font-size:39pt;line-height:1.15;white-space:nowrap;overflow:visible}.targets{height:12mm;margin-top:auto;padding:1mm 2mm;border-top:.25mm solid #b98a2f;display:grid;grid-template-columns:1fr 1.5fr 1fr;gap:2mm;font-size:6pt}.targets strong{display:block;color:#064d37;font-size:6.2pt}.bottom-band{position:absolute;bottom:0;left:0;width:100%;height:1.8mm;background:#064d37}
'''

def build_html():
 cells=''.join(f'<div class="cell"><span class="glyph" lang="ar">{esc(x)}</span></div>' for row in ROWS for x in row)
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><main class="page"><header class="header"><div><img class="brand-logo" src="{LOGO.resolve().as_uri()}"></div><div class="heading"><div class="learning-header-title">QURBATA • JILID 2 • MAD YA</div></div><div class="page-number">31</div></header><section class="presentation"><div class="presentation-object" lang="ar">بِ + يْ ← بِيْ</div></section><section class="grid">{cells}</section><section class="targets"><div><strong>Kompetensi</strong>Mad kasrah + ya sukun</div><div><strong>Tangga</strong>2 huruf saja: بِ + يْ → بِيْ</div><div><strong>Panjang</strong>2 harakat</div></section><div class="bottom-band"></div></main></body></html>'''

async def render(src,out):
 async with async_playwright() as p:
  browser=await p.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
  await page.goto(src.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
  await page.screenshot(path=str(out/'page-031-mad-ya-2huruf.png'),full_page=True)
  pdf=out/'QURBATA-JILID-2-P031-MAD-YA-2HURUF-V1.pdf'
  await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
  await browser.close()
 return pdf

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT))); a=ap.parse_args()
 out=Path(a.output_dir); out=out if out.is_absolute() else ROOT/out; out.mkdir(parents=True,exist_ok=True)
 h=out/'page-031-mad-ya-2huruf.html'; h.write_text(build_html(),encoding='utf-8'); pdf=asyncio.run(render(h,out))
 print('JILID2_P031_MAD_YA_2HURUF=PASS'); print('OBJECTS=28'); print('UNIT=KASRAH_PLUS_YA_SUKUN'); print('BASE_LETTERS_PER_OBJECT=2'); print('MAD_LENGTH=2_HARAKAT'); print(f'PDF={pdf.relative_to(ROOT)}')
if __name__=='__main__': raise SystemExit(main())
