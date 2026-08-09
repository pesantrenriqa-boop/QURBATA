#!/usr/bin/env python3
"""Render only QURBATA Jilid 2 P001 with strict no-leakage and ordered L2->L3 ladder."""
from __future__ import annotations
import argparse, asyncio, csv, html, json
from pathlib import Path
from playwright.async_api import async_playwright
import render_qurbata_jilid2_foundation_v3 as base

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'content/qwo/registry/JILID-2-P001-PAGE-CONTRACT-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P001-V1.csv'
DEFAULT_DATA=ROOT/'content/qwo/composer/output/jilid-2-v1-joined-foundation'
DEFAULT_OUT=ROOT/'dist/jilid-2-p001-candidate-v3'

def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def esc(s): return html.escape(str(s or ''))

# Row 1-2: L2, four cells each. Row 3-8: L3, three cells each.
# From row 3 onward, non-joiners are deliberately interleaved so the learner sees real joining breaks.
P001_ROWS=[
    ['بَتَ','تَبَ','بَثَ','ثَبَ'],
    ['تِثُ','ثُتِ','بِثَ','ثَبُ'],
    ['بَتِثُ','بَدِتُ','تَرَثِ'],
    ['ثَذِبُ','بَوَتِ','تَاثُ'],
    ['بَرِثُ','ثَدَبِ','تَزُبِ'],
    ['ثَوَبِ','بَذِتُ','تَدُثِ'],
    ['بَتَرُ','ثِبَدَ','تَبِوَ'],
    ['بَزِثُ','تَرَبِ','ثَدِتُ'],
]
P001_BANNED_JOINING=set('جحخسشصضطظعغفقكلمنيه')
ACQUISITION=set('بتث')
NONJOIN=set('ادذرزو')

P001_CSS=base.base.CSS + r'''
.page{padding-top:5mm}
.header{height:14mm;flex:0 0 14mm}
.title-row{display:none!important}
.presentation{height:15mm;flex:0 0 15mm;margin:1mm 3mm 1.5mm;padding:0;border:0;background:transparent;display:flex;align-items:center;justify-content:center;overflow:hidden}
.presentation-copy{display:none!important}
.presentation-object-wrap{width:100%;height:100%;position:relative;overflow:hidden}
.presentation-object{position:absolute;left:50%;top:50%;display:inline-block;direction:ltr;unicode-bidi:isolate;font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;font-size:27pt;line-height:1;white-space:nowrap;transform:translate(-50%,-50%);transform-origin:center;color:#000}
.j2-grid{height:145mm;flex:0 0 145mm;display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(8,minmax(0,1fr));column-gap:2.4mm;row-gap:2.2mm;padding:1mm 0 1.5mm;direction:rtl;overflow:visible}
.j2-object{position:relative;width:100%;height:100%;min-height:0;display:flex;align-items:center;justify-content:center;overflow:visible}
.j2-object.l2{grid-column:span 3}
.j2-object.l3{grid-column:span 4}
.j2-glyph{font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;font-size:36pt}
.targets{height:15mm;flex:0 0 15mm}
'''

def flatten_rows(): return [x for row in P001_ROWS for x in row]

def build_page_html(debug:bool)->str:
    debug_attr=' data-layout-debug="true"' if debug else ''
    cells=[];slot=1
    for ri,row in enumerate(P001_ROWS,1):
        cls='l2' if ri<=2 else 'l3'
        for obj in row:
            cells.append(f'<div class="j2-object {cls}" data-slot="{slot}" data-row="{ri}"><span class="j2-glyph">{esc(obj)}</span></div>');slot+=1
    return f'''<!doctype html><html{debug_attr}><head><meta charset="utf-8"><style>{P001_CSS}</style></head><body>
<main class="page with-presentation">
  <header class="header"><div class="brand">QURBATA <span>• JILID 2</span></div><div class="page-no">1</div></header>
  <section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object">بَتِثُ ← ثُ ← تِ ← بَ</div></div></section>
  <section class="j2-grid">{''.join(cells)}</section>
  <section class="targets">
    <div class="target-item"><span>KOMPETENSI</span><strong>Membaca huruf hijaiyah bersambung</strong></div>
    <div class="target-item"><span>SUBKOMPETENSI</span><strong>Konsep dasar sambungan</strong></div>
    <div class="target-item"><span>TANGGA</span><strong>2 huruf → 3 huruf → pemutus sambungan</strong></div>
    <div class="target-item"><span>NIDOM</span><strong>Registry Jilid 2 belum diikat</strong></div>
  </section>
  <footer class="footer"><span>QURBATA • JILID 2</span><span>Guru: __________  Nilai: ____  Tanggal: ________</span></footer>
</main></body></html>'''

async def fit_and_inspect(page):
    pfit=await page.evaluate('''()=>{const wrap=document.querySelector('.presentation-object-wrap'),obj=document.querySelector('.presentation-object');const w=wrap.getBoundingClientRect().width,ow=obj.getBoundingClientRect().width,s= Math.min(1,Math.max(.62,(w-12)/Math.max(1,ow)));obj.style.transform=`translate(-50%,-50%) scaleX(${s})`;return s}''')
    metrics=await base.base.fit_joined(page)
    issues=await page.evaluate('''()=>{const out=[],t=2;const grid=document.querySelector('.j2-grid'),targets=document.querySelector('.targets');for(const slot of document.querySelectorAll('.j2-object')){const s=slot.getBoundingClientRect(),g=slot.querySelector('.j2-glyph').getBoundingClientRect();if(g.left<s.left-t||g.right>s.right+t)out.push({kind:'JOINED_GLYPH_OUTSIDE_SLOT',slot:slot.dataset.slot,row:slot.dataset.row,glyphLeft:g.left,glyphRight:g.right,slotLeft:s.left,slotRight:s.right})}if(grid&&targets){const g=grid.getBoundingClientRect(),b=targets.getBoundingClientRect();if(g.bottom>b.top+t)out.push({kind:'GRID_FOOTER_OVERLAP',gridBottom:g.bottom,targetsTop:b.top})}const p=document.querySelector('.presentation-object-wrap').getBoundingClientRect(),o=document.querySelector('.presentation-object').getBoundingClientRect();if(o.left<p.left-t||o.right>p.right+t)out.push({kind:'PRESENTATION_OBJECT_OUTSIDE_BAND'});return out}''')
    return metrics,pfit,issues

async def render(html_path:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P001-V3.json';png_dir=out/'png';png_dir.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as p:
        browser=await p.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(html_path.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=26:raise RuntimeError(f'P001_OBJECT_COUNT_INVALID actual={count} expected=26')
        metrics,pfit,issues=await fit_and_inspect(page)
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues:
            kinds={}
            for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P001_LAYOUT_ISSUES='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png_dir/'page-001.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P001-CANDIDATE-V3.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
        await browser.close()
    return metrics,pfit,report,pdf

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',default=str(DEFAULT_DATA.relative_to(ROOT)));ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--debug',action='store_true');a=ap.parse_args()
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    micro=read_csv(MICRO)
    if len(micro)!=10:raise ValueError(f'P001_MICRO_LADDER_INVALID actual={len(micro)} expected=10')
    objs=flatten_rows()
    if len(objs)!=26:raise ValueError(f'P001_OBJECT_COUNT actual={len(objs)} expected=26')
    for ri,row in enumerate(P001_ROWS,1):
        expected=4 if ri<=2 else 3
        if len(row)!=expected:raise ValueError(f'P001_ROW_PATTERN_INVALID row={ri} actual={len(row)} expected={expected}')
        if ri>=3 and any(len([c for c in obj if c in NONJOIN])==0 for obj in row[1:]):
            raise ValueError(f'P001_NONJOIN_VARIATION_MISSING row={ri}')
    for obj in objs:
        leaked=P001_BANNED_JOINING.intersection(obj)
        if leaked:raise ValueError('P001_COMPETENCY_LEAKAGE object='+obj+' leaked='+''.join(sorted(leaked)))
    html_dir=out/'html';html_dir.mkdir(parents=True,exist_ok=True);h=html_dir/'page-001.html';h.write_text(build_page_html(a.debug),encoding='utf-8')
    metrics,pfit,report,pdf=asyncio.run(render(h,out,a.debug))
    print('JILID2_P001_RENDERER_V3=PASS')
    print('PAGE=1')
    print('HEADER_EXPLANATORY_TITLE=REMOVED')
    print('PRESENTATION_LABEL=REMOVED')
    print('PRESENTATION_RESULT_POSITION=FAR_LEFT')
    print('COMPETENCY_LEAKAGE=0')
    print('ACQUISITION_LETTERS=بتث')
    print('NON_JOINING_REVIEW=ا|د|ذ|ر|ز|و')
    print('ROW_PATTERN=R1-2:4xL2|R3-8:3xL3')
    print('L2_AFTER_L3=FORBIDDEN')
    print('PRACTICE_OBJECTS=26')
    print('ARABIC_FONT_PRIMARY=Amiri Quran')
    print('LAYOUT_OVERFLOW=0')
    print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}')
    print(f'PDF={pdf.relative_to(ROOT)}')
    return 0
if __name__=='__main__':raise SystemExit(main())
