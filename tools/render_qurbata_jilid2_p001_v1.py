#!/usr/bin/env python3
"""Render only QURBATA Jilid 2 P001 with strict no-leakage and ordered L2->L3 ladder."""
from __future__ import annotations
import argparse, asyncio, csv, html, json
from pathlib import Path
from playwright.async_api import async_playwright
import render_qurbata_jilid2_foundation_v3 as base

ROOT=Path(__file__).resolve().parents[1]
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P001-V1.csv'
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'
DEFAULT_OUT=ROOT/'dist/jilid-2-p001-candidate-v18'

def read_csv(p):
    with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def arabic_html(s):
    # Keep base letters and combining marks in one uninterrupted shaping run.
    # Splitting marks into spans breaks Amiri Quran GPOS mark/mkmk attachment.
    return html.escape(str(s or ''))

P001_ROWS=[['بَتَ','تَبَ','بَثَ','ثَبَ'],['تِثُ','ثُتِ','بِثَ','ثَبُ'],['بَتِثُ','بَدِتُ','تَرَثِ'],['ثَذِبُ','بَوَتِ','تَاثُ'],['بَرِثُ','ثَدَبِ','تَزُبِ'],['ثَوَبِ','بَذِتُ','تَدُثِ'],['بَتَرُ','ثِبَدَ','تَبِوَ'],['بَزِثُ','تَرَبِ','ثَدِتُ']]
P001_BANNED_JOINING=set('جحخسشصضطظعغفقكلمنيه')

P001_CSS=base.base.CSS + r'''
.page{padding:5mm 8mm 2.5mm;position:relative}.header{height:17mm;flex:0 0 17mm;display:grid;grid-template-columns:25mm minmax(0,1fr) 12mm;align-items:center;gap:3mm;border:0;overflow:hidden}.brand-block{display:flex;align-items:flex-start;justify-content:flex-start;min-width:0}.brand-logo{width:23mm;height:16.5mm;object-fit:contain;display:block}.heading{min-width:0;height:100%;display:flex;align-items:center;justify-content:center;text-align:center;padding:0}.learning-header-title{color:#064d37;white-space:nowrap;font-family:"Segoe UI Semibold","Trebuchet MS",sans-serif;font-size:8.4pt;font-weight:700;line-height:1;letter-spacing:.11em;font-variant:small-caps}.page-number{background:#064d37;color:#fff;border-bottom:1.1mm solid #b98a2f;text-align:center;font-weight:700;padding:2.6mm 1mm 3.4mm;border-radius:0 0 3mm 3mm;font-size:12pt}.presentation{height:15mm;flex:0 0 15mm;margin:.5mm 3mm 1mm;padding:0;border:0;background:transparent;display:flex;align-items:center;justify-content:center;overflow:visible}.presentation-object-wrap{width:100%;height:100%;display:flex;align-items:center;justify-content:center;overflow:visible}.presentation-object{display:flex;align-items:center;justify-content:center;gap:2.2mm;direction:ltr;unicode-bidi:isolate;font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;font-size:27pt;line-height:1.18;color:#000;white-space:nowrap;overflow:visible;font-feature-settings:'mark' 1,'mkmk' 1}.presentation-object .arabic-part{direction:rtl;unicode-bidi:isolate;display:inline-block;line-height:1.18;padding:.7mm .4mm;overflow:visible;font-feature-settings:'mark' 1,'mkmk' 1}.presentation-object .arrow{font-family:Arial,sans-serif;font-size:21pt;line-height:1;color:#111}.j2-grid{height:142mm;flex:0 0 142mm;display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:repeat(8,minmax(0,1fr));column-gap:2.4mm;row-gap:4.6mm;padding:.8mm 0;direction:rtl;overflow:visible}.j2-object{position:relative;width:100%;height:100%;min-height:0;display:flex;align-items:center;justify-content:center;overflow:visible}.j2-object.l2{grid-column:span 3}.j2-object.l3{grid-column:span 4}.j2-glyph{font-family:'Amiri Quran','Amiri','Noto Naskh Arabic',serif;font-size:36pt;line-height:1.04;padding:.15mm 1mm .2mm;margin:0;overflow:visible;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility}
.targets{height:11.5mm;flex:0 0 11.5mm;margin-top:auto;margin-bottom:1mm;padding:.7mm 1mm .6mm;display:grid;grid-template-columns:1.2fr 1fr 1fr 1.35fr;gap:1.4mm;background:linear-gradient(to bottom,rgba(247,248,245,.92),rgba(255,255,255,.98));border-top:.22mm solid rgba(185,138,47,.58);border-radius:1.8mm 1.8mm 0 0;overflow:hidden}.target-item{min-height:9.7mm;padding:.25mm 1mm 0;border:0;justify-content:flex-start;background:transparent}.target-item+.target-item{border-left:.18mm solid rgba(185,138,47,.45)}.target-item span{display:block;color:#064d37;font-size:5.8pt;font-weight:800;line-height:1.1;white-space:nowrap}.target-item strong{display:block;margin-top:.4mm;font-size:5.2pt;line-height:1.18;font-weight:600;white-space:normal;overflow:hidden}.footer{height:6mm;flex:0 0 6mm;margin-top:0;margin-bottom:1.6mm;padding:.15mm 3mm;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));align-items:center;gap:3mm;background:rgba(247,248,245,.74);border-radius:1.6mm;color:#064d37;font-size:5.2pt;overflow:hidden}.footer .field{min-width:0;display:flex;gap:2mm;align-items:center}.footer .line{flex:1;min-width:0;border-bottom:.25mm dotted #777;height:3.5mm}.bottom-band{position:absolute;bottom:0;left:0;width:100%;height:1.8mm;background:#064d37}.bottom-band::after{content:"◇";position:absolute;left:50%;transform:translate(-50%,-55%);color:#b98a2f;background:white;padding:0 2mm;font-size:10pt}html[data-layout-debug="true"] .j2-object,html[data-layout-debug="true"] .presentation{outline:none!important}
'''

def flatten_rows():return[x for row in P001_ROWS for x in row]
def build_page_html(debug):
 d=' data-layout-debug="true"' if debug else '';cells=[];slot=1
 for ri,row in enumerate(P001_ROWS,1):
  cls='l2' if ri<=2 else 'l3'
  for obj in row:cells.append(f'<div class="j2-object {cls}" data-slot="{slot}" data-row="{ri}"><span class="j2-glyph" lang="ar" dir="rtl">{arabic_html(obj)}</span></div>');slot+=1
 p=f'''<div class="presentation-object"><span class="arabic-part" lang="ar">{arabic_html('بَتِثُ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{arabic_html('ثُ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{arabic_html('تِ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{arabic_html('بَ')}</span></div>'''
 return f'''<!doctype html><html{d}><head><meta charset="utf-8"><style>{P001_CSS}</style></head><body><main class="page with-presentation"><header class="header"><div class="brand-block"><img class="brand-logo" src="{LOGO.resolve().as_uri()}" alt="Logo QURBATA"></div><div class="heading"><div class="learning-header-title">QURBATA • JILID 2</div></div><div class="page-number">01</div></header><section class="presentation"><div class="presentation-object-wrap">{p}</div></section><section class="j2-grid">{''.join(cells)}</section><section class="targets"><div class="target-item"><span>Kompetensi</span><strong>Membaca huruf hijaiyah bersambung</strong></div><div class="target-item"><span>Subkompetensi</span><strong>Konsep dasar sambungan</strong></div><div class="target-item"><span>Tangga</span><strong>2 huruf → 3 huruf → pemutus sambungan</strong></div><div class="target-item"><span>NIDOM</span><strong>Registry Jilid 2 belum diikat</strong></div></section><footer class="footer"><div class="field"><strong>Nama Guru</strong><span class="line"></span></div><div class="field"><strong>Tanggal</strong><span class="line"></span></div><div class="field"><strong>Nilai</strong><span class="line"></span></div></footer><div class="bottom-band"></div></main></body></html>'''

async def fit_and_inspect(page):
 metrics=await base.base.fit_joined(page)
 issues=await page.evaluate('''()=>{const out=[],t=2,g=document.querySelector('.j2-grid'),b=document.querySelector('.targets');const rows={};for(const el of document.querySelectorAll('.j2-object')){const r=Number(el.dataset.row),x=el.querySelector('.j2-glyph').getBoundingClientRect();(rows[r]??=[]).push({slot:el.dataset.slot,box:x})}for(let r=1;r<=8;r++){const cur=rows[r]||[];for(const it of cur){const s=document.querySelector(`.j2-object[data-slot="${it.slot}"]`).getBoundingClientRect();const pad=r<=2?10:12;if(it.box.left<s.left-pad||it.box.right>s.right+pad)out.push({kind:'JOINED_INK_HORIZONTAL_ESCAPE',slot:it.slot,row:r})}if(r<8&&rows[r+1]){const lowerTop=Math.min(...rows[r+1].map(x=>x.box.top));const upperBottom=Math.max(...cur.map(x=>x.box.bottom));const gap=lowerTop-upperBottom;if(gap<8)out.push({kind:'INTER_ROW_CLEARANCE_TOO_SMALL',row:r,nextRow:r+1,upperBottom,lowerTop,gap,requiredGap:8})}}if(g&&b&&g.getBoundingClientRect().bottom>b.getBoundingClientRect().top+t)out.push({kind:'GRID_FOOTER_OVERLAP'});return out}''')
 return metrics,issues
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P001-V12.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as p:
  browser=await p.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready');count=await page.locator('.j2-object').count()
  if count!=26:raise RuntimeError(f'P001_OBJECT_COUNT_INVALID actual={count} expected=26')
  metrics,issues=await fit_and_inspect(page);report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if issues:
   kinds={}
   for x in issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
   raise RuntimeError('P001_LAYOUT_ISSUES='+str(len(issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
  await page.screenshot(path=str(png/'page-001.png'),full_page=True);pdf=out/'QURBATA-JILID-2-P001-CANDIDATE-V12.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await browser.close()
 return metrics,report,pdf

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));ap.add_argument('--debug',action='store_true');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
 if len(read_csv(MICRO))!=10:raise ValueError('P001_MICRO_LADDER_INVALID')
 for obj in flatten_rows():
  if P001_BANNED_JOINING.intersection(obj):raise ValueError('P001_COMPETENCY_LEAKAGE object='+obj)
 hdir=out/'html';hdir.mkdir(parents=True,exist_ok=True);h=hdir/'page-001.html';h.write_text(build_page_html(a.debug),encoding='utf-8');metrics,report,pdf=asyncio.run(render(h,out,a.debug))
 print('JILID2_P001_RENDERER_V12=PASS');print('PAGE=1');print('HARAKAT_POSITIONING=AMIRI_QURAN_NATIVE_OPENTYPE');print('HARAKAT_MANUAL_OFFSETS=DISABLED');print('OPENTYPE_MARK=ENABLED');print('OPENTYPE_MKMK=ENABLED');print('ROW_GAP_MM=4.6');print('GLYPH_LINE_HEIGHT=1.04');print('VERTICAL_VALIDATION=MINIMUM_8PX_INTER_ROW_CLEARANCE');print('PRACTICE_OBJECTS=26');print('COMPETENCY_LEAKAGE=0');print('LAYOUT_OVERFLOW=0');print(f'OVERFLOW_REPORT={report.relative_to(ROOT)}');print(f'PDF={pdf.relative_to(ROOT)}');return 0
if __name__=='__main__':raise SystemExit(main())
