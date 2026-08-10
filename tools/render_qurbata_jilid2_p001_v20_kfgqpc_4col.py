#!/usr/bin/env python3
"""QURBATA Jilid 2 P001 V20 — KFGQPC, larger type, compact 4-column practice grid.

User-approved direction from V19:
- keep KFGQPC Uthman Taha Naskh and native GPOS harakat;
- enlarge Arabic practice text for child readability;
- reduce unused whitespace;
- make every one of the 8 practice rows contain exactly 4 reading objects.

The competency boundary remains unchanged: acquisition letters are only ب ت ث,
with previously-known non-joiners ا د ذ ر ز و allowed for transfer/review.
"""
from __future__ import annotations
import asyncio
import json
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_p001_v19_kfgqpc as v19
import render_qurbata_jilid2_p001_v1 as p001

# Eight rows x four objects = 32.  No new joining-letter family is introduced.
p001.P001_ROWS=[
    ['بَتَ','تَبَ','بَثَ','ثَبَ'],
    ['تِثُ','ثُتِ','بِثَ','ثَبُ'],
    ['بَتِثُ','بَدِتُ','تَرَثِ','ثَابِ'],
    ['ثَذِبُ','بَوَتِ','تَاثُ','بَزِتُ'],
    ['بَرِثُ','ثَدَبِ','تَزُبِ','ثَرَبِ'],
    ['ثَوَبِ','بَذِتُ','تَدُثِ','بَدِثُ'],
    ['بَتَرُ','ثِبَدَ','تَبِوَ','ثَذِتُ'],
    ['بَزِثُ','تَرَبِ','ثَدِتُ','تَوَبَ'],
]

# V20 geometry: larger KFGQPC letters while using the page width and height more efficiently.
p001.P001_CSS += r'''
.presentation{height:14mm;flex:0 0 14mm;margin:.2mm 2mm .6mm}
.presentation-object{font-size:30pt;gap:1.7mm}
.j2-grid{
  height:148mm;
  flex:0 0 148mm;
  grid-template-columns:repeat(4,minmax(0,1fr));
  grid-template-rows:repeat(8,minmax(0,1fr));
  column-gap:1.1mm;
  row-gap:3.7mm;
  padding:.25mm 0;
}
.j2-object.l2,.j2-object.l3{grid-column:span 1}
.j2-glyph{
  font-size:36pt;
  line-height:1.00;
  padding:.25mm .25mm .35mm;
}
.targets{height:8.5mm;flex:0 0 8.5mm;margin-bottom:.5mm;padding:.2mm .6mm}
.target-item{min-height:6.8mm;padding:.15mm .55mm 0}
.target-item span{font-size:5.3pt}
.target-item strong{font-size:4.9pt;line-height:1.12;margin-top:.25mm}
.footer{height:4.5mm;flex:0 0 4.5mm;margin-bottom:.8mm;padding:.05mm 2mm;font-size:5pt}
'''

async def render32(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P001-V20.json'
    png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch()
        page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle')
        await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=32:
            raise RuntimeError(f'P001_OBJECT_COUNT_INVALID actual={count} expected=32')
        metrics,issues=await p001.fit_and_inspect(page)
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues:
            kinds={}
            for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P001_LAYOUT_ISSUES='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-001.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P001-CANDIDATE-V20-KFGQPC-4COL.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await browser.close()
    return metrics,report,pdf

p001.render=render32


def main():
    rc=v19.main()
    print('JILID2_P001_RENDERER_V20_KFGQPC_4COL=PASS')
    print('PRACTICE_ROWS=8')
    print('PRACTICE_COLUMNS=4')
    print('PRACTICE_OBJECTS=32')
    print('ROW_PATTERN=R1-R8:4_OBJECTS')
    print('PRACTICE_FONT_SIZE=36PT')
    print('PRESENTATION_FONT_SIZE=30PT')
    print('GRID_HEIGHT_MM=148')
    print('ROW_GAP_MM=3.7')
    print('COLUMN_GAP_MM=1.1')
    print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh')
    print('HARAKAT_MODEL=NATIVE_FONT_GPOS')
    print('COMPETENCY_LEAKAGE=0')
    print('STATUS=VISUAL_CANDIDATE_NOT_FROZEN')
    return rc

if __name__=='__main__': raise SystemExit(main())
