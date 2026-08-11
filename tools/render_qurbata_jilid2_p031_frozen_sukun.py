#!/usr/bin/env python3
"""Render QURBATA Jilid 2 P031 (Mad Ya I) with frozen sukun baseline V7.6.

Production rules:
- base letters: KFGQPC Uthman Taha Naskh
- sukun codepoint: U+0652
- visual sukun outline: Amiri U+06E1
- frozen vertical shift: -1700 KFGQPC units
- no manual detached marks; OpenType mark/mkmk preserved
"""
from __future__ import annotations
import argparse, asyncio, html, json, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))

import render_qurbata_jilid2_foundation_v3 as base
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
import render_qurbata_jilid2_sukun_lab_v5 as sukun

LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'
DEFAULT_OUT=ROOT/'dist/jilid-2-p031-frozen-sukun'
FONT_FAMILY='QURBATA KFGQPC Hybrid Frozen Sukun'
SUKUN_Y_SHIFT=-1700

ROWS=[
 ['كِتَبَ','قِيْلَ','مِهَنَ'],
 ['دِيْنٌ','نِعَمَ','تِيْنٌ'],
 ['قَالَ','كَانَ','كَرِيْمٌ'],
 ['عَذَابَ','رَحِيْمٌ','سَلَامَ'],
 ['عَلِيْمٌ','نَهَارَ','حَكِيْمٌ'],
 ['حِسَابَ','عَظِيْمٌ','طَعَامَ'],
 ['يَتِيْمٌ','شَرَابَ','قَرِيْبٌ'],
 ['لِبَاسَ','بَعِيْدٌ','مَكَانَ'],
]

CSS=base.base.CSS+r'''
.page{padding:5mm 8mm 2.5mm;position:relative}.header{height:17mm;flex:0 0 17mm;display:grid;grid-template-columns:25mm minmax(0,1fr) 12mm;align-items:center;gap:3mm;border:0;overflow:hidden}.brand-block{display:flex;align-items:flex-start;justify-content:flex-start}.brand-logo{width:23mm;height:16.5mm;object-fit:contain}.heading{height:100%;display:flex;align-items:center;justify-content:center;text-align:center}.learning-header-title{color:#064d37;white-space:nowrap;font-family:"Segoe UI Semibold","Trebuchet MS",sans-serif;font-size:8.4pt;font-weight:700;line-height:1;letter-spacing:.11em;font-variant:small-caps}.page-number{background:#064d37;color:#fff;border-bottom:1.1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.6mm 1mm 3.4mm;border-radius:0 0 3mm 3mm;font-size:12pt}.presentation{height:15mm;flex:0 0 15mm;margin:.5mm 3mm 1mm;display:flex;align-items:center;justify-content:center;overflow:visible}.presentation-object{direction:rtl;font-family:"QURBATA KFGQPC Hybrid Frozen Sukun",serif;font-size:28pt;line-height:1.15;white-space:nowrap;font-feature-settings:'mark' 1,'mkmk' 1}.j2-grid{height:142mm;flex:0 0 142mm;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(8,minmax(0,1fr));column-gap:3mm;row-gap:5.8mm;padding:.8mm 0;direction:rtl;overflow:visible}.j2-object{display:flex;align-items:center;justify-content:center;overflow:visible}.j2-glyph{font-family:"QURBATA KFGQPC Hybrid Frozen Sukun",serif;font-size:31pt;line-height:1.00;padding:.15mm 1mm .2mm;overflow:visible;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility}.targets{height:11.5mm;flex:0 0 11.5mm;margin-top:auto;margin-bottom:1mm;padding:.7mm 1mm .6mm;display:grid;grid-template-columns:1.2fr 1fr 1fr 1.35fr;gap:1.4mm;background:linear-gradient(to bottom,rgba(247,248,245,.92),rgba(255,255,255,.98));border-top:.22mm solid rgba(185,138,47,.58);border-radius:1.8mm 1.8mm 0 0;overflow:hidden}.target-item{min-height:9.7mm;padding:.25mm 1mm 0}.target-item+.target-item{border-left:.18mm solid rgba(185,138,47,.45)}.target-item span{display:block;color:#064d37;font-size:5.8pt;font-weight:800;line-height:1.1;white-space:nowrap}.target-item strong{display:block;margin-top:.4mm;font-size:5.2pt;line-height:1.18;font-weight:600}.footer{height:6mm;flex:0 0 6mm;margin-bottom:1.6mm;padding:.15mm 3mm;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));align-items:center;gap:3mm;background:rgba(247,248,245,.74);border-radius:1.6mm;color:#064d37;font-size:5.2pt}.footer .field{display:flex;gap:2mm;align-items:center}.footer .line{flex:1;border-bottom:.25mm dotted #777;height:3.5mm}.bottom-band{position:absolute;bottom:0;left:0;width:100%;height:1.8mm;background:#064d37}.bottom-band::after{content:"◇";position:absolute;left:50%;transform:translate(-50%,-55%);color:#b98a2f;background:white;padding:0 2mm;font-size:10pt}
'''

def ah(s:str)->str:return html.escape(s)

def build_html(font_uri:str)->str:
    cells=[];slot=1
    for ri,row in enumerate(ROWS,1):
        for obj in row:
            cells.append(f'<div class="j2-object" data-slot="{slot}" data-row="{ri}"><span class="j2-glyph" lang="ar" dir="rtl">{ah(obj)}</span></div>');slot+=1
    ff=f'@font-face{{font-family:"{FONT_FAMILY}";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block;}}'
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><style>{CSS}{ff}</style></head><body><main class="page with-presentation"><header class="header"><div class="brand-block"><img class="brand-logo" src="{LOGO.resolve().as_uri()}" alt="Logo QURBATA"></div><div class="heading"><div class="learning-header-title">QURBATA • JILID 2 • MAD YA I</div></div><div class="page-number">31</div></header><section class="presentation"><div class="presentation-object" lang="ar" dir="rtl">قِ → قِيْ &nbsp;&nbsp; دِ → دِيْ &nbsp;&nbsp; تِ → تِيْ</div></section><section class="j2-grid">{''.join(cells)}</section><section class="targets"><div class="target-item"><span>Kompetensi</span><strong>Membedakan kasrah pendek dan mad ya</strong></div><div class="target-item"><span>Subkompetensi</span><strong>Kasrah + يْ dibaca 2 harakat</strong></div><div class="target-item"><span>Murojaah</span><strong>Mad alif, sambung, pemutus, tanwin</strong></div><div class="target-item"><span>Sukun</span><strong>Baseline V7.6 frozen · Y=-1700</strong></div></section><footer class="footer"><div class="field"><strong>Nama Guru</strong><span class="line"></span></div><div class="field"><strong>Tanggal</strong><span class="line"></span></div><div class="field"><strong>Nilai</strong><span class="line"></span></div></footer><div class="bottom-band"></div></main></body></html>'''

async def render(h:Path,out:Path):
    png_dir=out/'png';png_dir.mkdir(parents=True,exist_ok=True)
    report=out/'LAYOUT-REPORT-J2-P031-FROZEN-SUKUN.json'
    async with async_playwright() as pw:
        browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        ok=await page.evaluate("()=>document.fonts.check('31pt \\\"QURBATA KFGQPC Hybrid Frozen Sukun\\\"','قِيْلَ')")
        if not ok:raise RuntimeError('P031_HYBRID_FONT_BINDING_FAIL')
        count=await page.locator('.j2-object').count()
        if count!=24:raise RuntimeError(f'P031_OBJECT_COUNT_INVALID={count}')
        issues=await page.evaluate('''()=>{const out=[];const els=[...document.querySelectorAll('.j2-glyph')];for(const e of els){const r=e.getBoundingClientRect();if(r.left<0||r.right>document.documentElement.clientWidth)out.push({kind:'HORIZONTAL_OVERFLOW',text:e.textContent});}const g=document.querySelector('.j2-grid').getBoundingClientRect(),t=document.querySelector('.targets').getBoundingClientRect();if(g.bottom>t.top+2)out.push({kind:'GRID_TARGET_OVERLAP',gap:t.top-g.bottom});return out}''')
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues:raise RuntimeError(f'P031_LAYOUT_ISSUES={len(issues)} REPORT={report}')
        await page.screenshot(path=str(png_dir/'page-031.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P031-MAD-YA-FROZEN-SUKUN.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await browser.close()
    return pdf,report

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--font-file');ap.add_argument('--font-zip');ap.add_argument('--amiri-font');a=ap.parse_args()
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    kfg,kfgsrc=kfgloader.discover_font(a.font_file,a.font_zip,out)
    amiri=sukun.discover_amiri(a.amiri_font,out)
    hybrid=out/'_runtime_font'/'KFGQPC-QURBATA-FROZEN-SUKUN-V7-6.ttf'
    meta=sukun.patch_font(kfg,amiri,hybrid,SUKUN_Y_SHIFT)
    hdir=out/'html';hdir.mkdir(parents=True,exist_ok=True);h=hdir/'page-031.html';h.write_text(build_html(hybrid.resolve().as_uri()),encoding='utf-8')
    pdf,report=asyncio.run(render(h,out))
    print('JILID2_P031_FROZEN_SUKUN=PASS');print('PAGE=31');print('FOCUS=MAD_YA');print('BASE_LETTERS=KFGQPC_UTHMAN_TAHA');print('SUKUN_BASELINE_VERSION=V7.6');print('SUKUN_BASELINE_STATUS=FROZEN');print('SUKUN_RENDER_CODEPOINT=U+0652');print('SUKUN_VISUAL_OUTLINE=AMIRI_U+06E1');print(f'SUKUN_Y_SHIFT={SUKUN_Y_SHIFT}');print('POSITIONING=KFGQPC_U+0652_GPOS_PRESERVED');print(f'KFGQPC_SOURCE={kfgsrc}');print(f'PDF={pdf.relative_to(ROOT)}');print(f'LAYOUT_REPORT={report.relative_to(ROOT)}');print('BOOK_PAGE_TARGET=QJ2-P031');return 0

if __name__=='__main__':raise SystemExit(main())
