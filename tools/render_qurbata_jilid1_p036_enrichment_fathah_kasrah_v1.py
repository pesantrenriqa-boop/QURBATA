#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P036';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪ';HA_F='ﮪَ';HA_K='ﮪِ'
EX=['يَ وِ '+HA_F,'نِ مَ لِ','كَ قِ فَ','غِ عَ ظِ','طَ ضِ صَ','شِ سَ زِ','رَ ذِ دَ','خِ حَ جِ','ثَ تِ بَ','إِ ءَ يِ','وَ '+HA_K+' نَ','مِ لَ كِ','قَ فِ غَ','عِ ظَ طِ','ضَ صِ شَ','سِ زَ رِ','ذَ دِ خَ','حِ جَ ثِ','تَ بِ ءَ','يِ وَ '+HA_K,'نَ مِ لَ']
NAMES=['ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م']
def run(s):return '<span class="run">'+''.join(f'<span>{x}</span>' for x in s.split())+'</span>'
def audit():
 ts=[x for e in EX for x in e.split()]
 if len(EX)!=21 or any(len(e.split())!=3 for e in EX):raise RuntimeError('P036_GRID_CONTENT_FAIL')
 if len(ts)!=63:raise RuntimeError(f'P036_TOKEN_COUNT_FAIL {len(ts)}')
 if any(x in {'ه','هَ','هِ'} for x in ts+NAMES):raise RuntimeError('P036_ONE_HOLE_HA_FORBIDDEN')
def rows():return ''.join('<div class="row">'+''.join(f'<div class="practice">{run(x)}</div>' for x in EX[i:i+3])+'</div>' for i in range(0,21,3))
def doc(u):
 names=''.join(f'<span>{x}</span>' for x in NAMES)
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 10mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:18mm;display:flex;align-items:center;justify-content:center;gap:16mm;font:42pt "{FONT}";direction:rtl}}.grid{{height:121mm;display:grid;grid-template-rows:repeat(7,1fr);row-gap:2.6mm;padding:2mm 0 1mm}}.row{{display:grid;grid-template-columns:repeat(3,34mm);column-gap:7mm;direction:rtl;align-items:center;justify-content:center}}.practice{{width:34mm;min-width:34mm;display:flex;align-items:center;justify-content:center;font:30pt/1.2 "{FONT}";white-space:nowrap;overflow:visible}}.run{{display:inline-flex;direction:rtl;gap:3.8mm;align-items:center}}.name-strip{{height:23mm;margin-top:1mm;border-top:.35mm solid #b9b9b9;display:flex;align-items:center;justify-content:space-between;direction:rtl;font:38pt/1.4 "{FONT}";padding:1mm 4mm 2mm;overflow:visible}}.name-strip>span{{display:inline-block;overflow:visible}}.safe{{height:5mm}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">36</div></header><section class="presentation"><span>مَ</span><span>مِ</span><span>نَ</span><span>نِ</span></section><section class="grid">{rows()}</section><section class="name-strip">{names}</section><div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P036-PENGAYAAN-FATHAH-KASRAH-02-CANDIDATE-V3-SPACED.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  g=await p.evaluate("()=>{let grid=document.querySelector('.grid').getBoundingClientRect(),rows=[...document.querySelectorAll('.row')],cells=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect()),runs=[...document.querySelectorAll('.run')].map(e=>e.getBoundingClientRect());let rg=rows.map(r=>[...r.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect()).sort((a,b)=>a.left-b.left));let gaps=rg.flatMap(a=>a.slice(1).map((x,i)=>x.left-a[i].right));return {left:Math.min(...runs.map(x=>x.left))-grid.left,right:grid.right-Math.max(...runs.map(x=>x.right)),minGroupGap:Math.min(...gaps),rows:new Set(cells.map(x=>Math.round(x.top))).size}}")
  if g['left']<12 or g['right']<12 or g['minGroupGap']<20 or g['rows']!=7:raise RuntimeError('P036_SPACING_SAFE_FAIL '+str(g))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P036-PENGAYAAN-FATHAH-KASRAH-02-CANDIDATE-V3-SPACED.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P036_ENRICHMENT=PASS');print('LAYOUT=7_ROWS_X_3_GROUPS_FIXED');print('GROUP_CELL_WIDTH_MM=34');print('GROUP_SPACING_MM=7');print('INTRA_GROUP_SPACING_MM=3.8');print('PRACTICE_FONT_PT=30');print('SPACING_AUDIT=PASS');print('HA_GLYPH=TWO_HOLE_ONLY');print('PDF='+str(pdf.relative_to(ROOT)))
