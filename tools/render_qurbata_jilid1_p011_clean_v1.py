#!/usr/bin/env python3
# QURBATA Jilid 1 P011 — فَ قَ. Cumulative pattern after P010 enrichment.
from pathlib import Path
import argparse, asyncio, html, sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P011';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha'
FOCUS={'فَ','قَ'};REVIEW={'ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ','صَ','ضَ','طَ','ظَ','عَ','غَ'}
EXERCISES=['فَ ءَ','قَ أَ','فَ بَ','قَ تَ','ثَ فَ','جَ قَ','حَ فَ','خَ قَ','فَ دَ فَ','قَ ذَ قَ','فَ رَ فَ','قَ زَ قَ','فَ سَ فَ','قَ شَ قَ','فَ صَ فَ','قَ ضَ قَ','طَ فَ ظَ','عَ قَ غَ','ءَ فَ أَ','بَ قَ تَ','ثَ فَ جَ','حَ قَ خَ','رَ فَ زَ','سَ قَ شَ']
def obj(s):return '<span class="run">'+''.join(f'<span>{html.escape(x)}</span>' for x in s.split())+'</span>'
def rows():
 a=EXERCISES[:-1];o=[]
 for i in range(0,8,4):o.append('<div class="row r2">'+''.join(f'<div class="practice l2">{obj(x)}</div>' for x in a[i:i+4])+'</div>')
 for i in range(8,23,3):o.append('<div class="row r3">'+''.join(f'<div class="practice l3">{obj(x)}</div>' for x in a[i:i+3])+'</div>')
 return ''.join(o)
def audit():
 if len(EXERCISES)!=24:raise RuntimeError('P011_SOURCE_COUNT_FAIL')
 for e in EXERCISES[:8]:
  t=e.split()
  if len(t)!=2 or len(set(t)&FOCUS)!=1 or len(set(t)&REVIEW)!=1:raise RuntimeError(f'P011_FIRST_TWO_ROWS_PATTERN_FAIL={e}')
 rendered=EXERCISES[:-1];ts=[x for e in rendered for x in e.split()]
 if any(x not in FOCUS|REVIEW for x in ts):raise RuntimeError('P011_WHITELIST_FAIL')
 if any(not(set(e.split())&FOCUS) for e in rendered):raise RuntimeError('P011_EXAMPLE_WITHOUT_FOCUS')
 f=sum(x in FOCUS for x in ts);r=len(ts)-f
 if (len(ts),f,r)!=(61,31,30):raise RuntimeError(f'P011_BALANCE_FAIL tokens={len(ts)} focus={f} review={r}')
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}") format("truetype")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;flex:0 0 17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{position:absolute;left:50%;transform:translateX(-50%);color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:20mm;display:flex;align-items:center;justify-content:center;gap:18mm;font:46pt "{FONT}";direction:rtl}}.grid{{height:142mm;flex:0 0 142mm;display:grid;grid-template-rows:repeat(7,1fr);row-gap:1.4mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;justify-content:center;font:40pt/1 "{FONT}";white-space:nowrap}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.bottom-safe-spacer{{height:8mm;flex:0 0 8mm}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">11</div></header><section class="presentation"><span>فَ</span><span>قَ</span></section><section class="grid">{rows()}</section><div class="bottom-safe-spacer"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(b):
 if not b.exists():return b
 try:open(b,'ab').close();return b
 except PermissionError:pass
 for n in range(1,100):
  p=b.with_name(b.stem+f'-R{n}'+b.suffix)
  if not p.exists():return p
 raise RuntimeError('P011_NO_FREE_OUTPUT')
async def render(h):
 pdf=free(OUT/'QURBATA-JILID-1-P011-FA-QAF-CANDIDATE-V1-CUMULATIVE.pdf');png=free(OUT/'QURBATA-JILID-1-P011-FA-QAF-CANDIDATE-V1-CUMULATIVE.png');expected=EXERCISES[:-1]
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  visible=await p.locator('.practice').evaluate_all("els=>els.map(e=>[...e.querySelectorAll('.run > span')].map(x=>x.textContent.trim()).join(' '))")
  if visible!=expected:raise RuntimeError('P011_RENDERED_CONTENT_MISMATCH')
  for e in visible[:8]:
   t=e.split()
   if len(t)!=2 or len(set(t)&FOCUS)!=1 or len(set(t)&REVIEW)!=1:raise RuntimeError(f'P011_VISUAL_FIRST_TWO_ROWS_PATTERN_FAIL={e}')
  g=await p.evaluate("""()=>{const sp=document.querySelector('.bottom-safe-spacer').getBoundingClientRect(),xs=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect());const mb=Math.max(...xs.map(x=>x.bottom));return {ok:mb<=sp.top&&sp.top-mb>=6,clearance:sp.top-mb,count:xs.length}}""")
  if not g['ok'] or g['count']!=23:raise RuntimeError(f'P011_SAFE_AREA_FAIL {g}')
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P011-FA-QAF-CANDIDATE-V1-CUMULATIVE.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P011_FA_QAF_CUMULATIVE=PASS');print('MATERIAL_NEW=فَ|قَ');print('ROWS_1_2=NEW_PLUS_PREVIOUS_VERIFIED');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('PRACTICE_FONT_PT=40');print('GROUP_SPACING=PRESERVED');print('BOTTOM_GLYPH_OVERFLOW=0');print('PDF='+str(pdf.relative_to(ROOT)))
