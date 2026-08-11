#!/usr/bin/env python3
"""Render QURBATA Jilid 2 P002-P020 from regenerated current sources using KFGQPC.

Source of truth: books/jilid-2/regenerated/QJ2-Pxxx-*.md
- extracts the 24 Tangga Baca objects from each page source;
- does NOT reuse the legacy Amiri foundation dataset;
- base font: KFGQPC Uthman Taha Naskh;
- frozen sukun baseline V7.6 is embedded in the runtime font for consistency,
  although P002-P020 policy forbids sukun/tanwin/tasydid in practice objects.
"""
from __future__ import annotations
import argparse, asyncio, html, re, sys
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfg

SRC=ROOT/'books/jilid-2/regenerated'
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'
DEFAULT_OUT=ROOT/'dist/jilid-2-p002-p020-kfgqpc'
FONT_FAMILY='QURBATA KFGQPC Uthman Taha Frozen Sukun'

CSS=r'''
@page{size:A5;margin:0}*{box-sizing:border-box}html,body{margin:0;padding:0;background:#fff}body{font-family:Arial,sans-serif;color:#171717}.page{width:148mm;height:210mm;padding:5mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden;page-break-after:always;position:relative}.header{height:17mm;flex:0 0 17mm;display:grid;grid-template-columns:25mm minmax(0,1fr) 12mm;align-items:center;gap:3mm}.brand-logo{width:23mm;height:16.5mm;object-fit:contain}.heading{text-align:center;color:#064d37;font-family:"Segoe UI Semibold","Trebuchet MS",sans-serif;font-size:8.4pt;font-weight:700;letter-spacing:.11em}.page-number{background:#064d37;color:#fff;border-bottom:1.1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.6mm 1mm 3.4mm;border-radius:0 0 3mm 3mm;font-size:12pt}.presentation{height:14mm;flex:0 0 14mm;display:flex;align-items:center;justify-content:center;border-top:.18mm solid rgba(185,138,47,.35);border-bottom:.18mm solid rgba(185,138,47,.35);margin:0 3mm 1mm}.presentation strong{font-size:7.8pt;color:#064d37;text-align:center}.grid{height:143mm;flex:0 0 143mm;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(8,minmax(0,1fr));column-gap:4mm;row-gap:4.8mm;padding:1mm 0;direction:rtl;overflow:visible}.cell{display:flex;align-items:center;justify-content:center;overflow:visible}.glyph{font-family:"QURBATA KFGQPC Uthman Taha Frozen Sukun",serif;font-size:32pt;line-height:1.04;white-space:nowrap;direction:rtl;unicode-bidi:isolate;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}.targets{height:11.5mm;flex:0 0 11.5mm;margin-top:auto;margin-bottom:1mm;padding:.7mm 1mm .6mm;display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:1.4mm;background:linear-gradient(to bottom,rgba(247,248,245,.92),rgba(255,255,255,.98));border-top:.22mm solid rgba(185,138,47,.58)}.target span{display:block;color:#064d37;font-size:5.6pt;font-weight:800}.target strong{display:block;margin-top:.4mm;font-size:5.1pt;line-height:1.18}.footer{height:6mm;flex:0 0 6mm;margin-bottom:1.6mm;padding:.15mm 3mm;display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;align-items:center;background:rgba(247,248,245,.74);font-size:5.2pt;color:#064d37}.field{display:flex;gap:2mm}.line{flex:1;border-bottom:.25mm dotted #777}.bottom-band{position:absolute;bottom:0;left:0;width:100%;height:1.8mm;background:#064d37}
'''

def page_source(n:int)->Path:
    hits=sorted(SRC.glob(f'QJ2-P{n:03d}-*.md'))
    if not hits:raise FileNotFoundError(f'CURRENT_REGENERATED_SOURCE_NOT_FOUND=P{n:03d}')
    return hits[0]

def parse_source(path:Path):
    text=path.read_text(encoding='utf-8')
    fm=re.search(r'^\*\*Fokus:\*\*\s*(.+?)\s*$',text,re.M)
    focus=fm.group(1).strip() if fm else path.stem
    objects=[]
    for line in text.splitlines():
        s=line.strip()
        if not (s.startswith('|') and s.endswith('|')):continue
        cols=[c.strip() for c in s.strip('|').split('|')]
        if len(cols)<4 or not cols[0].isdigit():continue
        if 1<=int(cols[0])<=24:objects.append(cols[2])
    if len(objects)!=24:raise ValueError(f'PRACTICE_OBJECT_COUNT_INVALID source={path} count={len(objects)} expected=24')
    return focus,objects

def esc(s):return html.escape(str(s))

def page_html(n:int,focus:str,objects:list[str]):
    cells=''.join(f'<div class="cell"><span class="glyph" lang="ar" dir="rtl">{esc(x)}</span></div>' for x in objects)
    return f'''<main class="page" data-page="{n}"><header class="header"><div><img class="brand-logo" src="{LOGO.resolve().as_uri()}"></div><div class="heading">QURBATA • JILID 2</div><div class="page-number">{n:02d}</div></header><section class="presentation"><strong>{esc(focus)}</strong></section><section class="grid">{cells}</section><section class="targets"><div class="target"><span>KOMPETENSI</span><strong>{esc(focus)}</strong></div><div class="target"><span>TANGGA</span><strong>24 objek latihan</strong></div><div class="target"><span>FONT</span><strong>KFGQPC Uthman Taha</strong></div></section><footer class="footer"><div class="field"><strong>Guru</strong><span class="line"></span></div><div class="field"><strong>Tanggal</strong><span class="line"></span></div><div class="field"><strong>Nilai</strong><span class="line"></span></div></footer><div class="bottom-band"></div></main>'''

async def render(html_path:Path,out:Path):
    pdf=out/'QURBATA-JILID-2-P002-P020-KFGQPC-CURRENT-REVIEW.pdf';png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(html_path.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        pages=await p.locator('main.page').count()
        if pages!=19:raise RuntimeError(f'PAGE_COUNT_INVALID={pages}')
        glyphs=await p.locator('.glyph').count()
        if glyphs!=456:raise RuntimeError(f'GLYPH_COUNT_INVALID={glyphs}')
        for n in range(2,21):
            el=p.locator(f'main.page[data-page="{n}"]');await el.screenshot(path=str(png/f'page-{n:03d}.png'))
        await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    return pdf

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--font-file');ap.add_argument('--font-zip');ap.add_argument('--amiri-font');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    kfg_path,kfgsrc=kfg.discover_font(a.font_file,a.font_zip,out);amiri_path,amsrc=kfg.discover_amiri(a.amiri_font,out);font=kfg.build_frozen_sukun_font(kfg_path,amiri_path,out)
    sections=[];manifest=['page\tsource\tobjects\tfocus']
    for n in range(2,21):
        src=page_source(n);focus,objects=parse_source(src);sections.append(page_html(n,focus,objects));manifest.append(f'P{n:03d}\t{src.relative_to(ROOT)}\t24\t{focus}')
    ff=f'@font-face{{font-family:"{FONT_FAMILY}";src:url("{font.resolve().as_uri()}") format("truetype");font-display:block;}}'
    html_doc='<!doctype html><html><head><meta charset="utf-8"><style>'+CSS+ff+'</style></head><body>'+''.join(sections)+'</body></html>'
    h=out/'QURBATA-JILID-2-P002-P020-KFGQPC-CURRENT-REVIEW.html';h.write_text(html_doc,encoding='utf-8');(out/'P002-P020-SOURCE-MANIFEST.tsv').write_text('\n'.join(manifest)+'\n',encoding='utf-8');pdf=asyncio.run(render(h,out))
    print('JILID2_P002_P020_KFGQPC=PASS');print('PAGES_RENDERED=19');print('RANGE=P002-P020');print('PRACTICE_OBJECTS_RENDERED=456');print('SOURCE=books/jilid-2/regenerated/QJ2-Pxxx-*.md');print('LEGACY_AMIRI_FOUNDATION_DATASET=NOT_USED');print('BASE_FONT=KFGQPC_UTHMAN_TAHA');print('SUKUN_BASELINE=V7.6_FROZEN');print('SUKUN_Y_SHIFT=-1700');print(f'KFGQPC_SOURCE={kfgsrc}');print(f'AMIRI_GLYPH_SOURCE={amsrc}');print(f'PDF={pdf.relative_to(ROOT)}');return 0
if __name__=='__main__':raise SystemExit(main())
