#!/usr/bin/env python3
# QURBATA Jilid 1 P016 — Pengayaan I: mastery kombinasi 2 huruf, seluruh kompetensi huruf P001-P015.
from pathlib import Path
import argparse,asyncio,html,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P016';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪَ'
LETTERS={'ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ','صَ','ضَ','طَ','ظَ','عَ','غَ','فَ','قَ','كَ','لَ','مَ','نَ',HA,'وَ','يَ'}
EX=['ءَ يَ','أَ وَ','بَ '+HA,'تَ نَ','ثَ مَ','جَ لَ','حَ كَ','خَ قَ','دَ فَ','ذَ غَ','رَ عَ','زَ ظَ','سَ طَ','شَ ضَ','صَ زَ','ضَ سَ','طَ شَ','ظَ صَ','عَ رَ','غَ ذَ','فَ دَ','قَ خَ','كَ حَ','لَ جَ','مَ ثَ','نَ تَ',HA+' بَ','وَ أَ','يَ ءَ','بَ يَ','تَ وَ','جَ '+HA]
def obj(s):return '<span class="run">'+''.join(f'<span>{html.escape(x)}</span>' for x in s.split())+'</span>'
def audit():
 if len(EX)!=32 or any(len(x.split())!=2 for x in EX):raise RuntimeError('P016_TWO_LETTER_STRUCTURE_FAIL')
 ts=[t for e in EX for t in e.split()]
 if any(t not in LETTERS for t in ts):raise RuntimeError('P016_OUTSIDE_SCOPE')
 if LETTERS-set(ts):raise RuntimeError('P016_COVERAGE_MISSING='+str(LETTERS-set(ts)))
def rows():return ''.join('<div class="row">'+''.join(f'<div class="practice">{obj(x)}</div>' for x in EX[i:i+4])+'</div>' for i in range(0,32,4))
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}") format("truetype")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:16mm;display:flex;align-items:center;justify-content:center;color:#064d37;font:700 11pt Georgia;letter-spacing:.1em}}.grid{{height:146mm;display:grid;grid-template-rows:repeat(8,1fr);row-gap:1mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;gap:9mm}}.practice{{width:23mm;display:flex;justify-content:center;font:40pt/1 "{FONT}";white-space:nowrap}}.run{{display:inline-flex;direction:rtl;gap:2.8mm}}.safe{{height:7mm}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">16</div></header><section class="presentation">PENGAYAAN · KOMBINASI 2 HURUF</section><section class="grid">{rows()}</section><div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(p):
 if not p.exists():return p
 try:open(p,'ab').close();return p
 except PermissionError:pass
 for n in range(1,100):
  q=p.with_name(p.stem+f'-R{n}'+p.suffix)
  if not q.exists():return q
 raise RuntimeError('P016_NO_FREE_OUTPUT')
async def render(h):
 pdf=free(OUT/'QURBATA-JILID-1-P016-PENGAYAAN-2-HURUF-CANDIDATE-V1.pdf');png=free(OUT/'QURBATA-JILID-1-P016-PENGAYAAN-2-HURUF-CANDIDATE-V1.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');v=await p.locator('.practice').evaluate_all("e=>e.map(x=>[...x.querySelectorAll('span span')].map(y=>y.textContent.trim()).join(' '))")
  if v!=EX:raise RuntimeError('P016_RENDER_MISMATCH')
  g=await p.evaluate("()=>{let s=document.querySelector('.safe').getBoundingClientRect(),x=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect());let m=Math.max(...x.map(z=>z.bottom));return {ok:m<=s.top&&s.top-m>=5,clearance:s.top-m}}")
  if not g['ok']:raise RuntimeError('P016_SAFEAREA_FAIL '+str(g))
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P016-PENGAYAAN-2-HURUF-CANDIDATE-V1.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h));print('QJ1_P016_ENRICHMENT=PASS');print('NEW_MATERIAL=NONE');print('COMPETENCY_SCOPE=P001-P015');print('ENRICHMENT_FOCUS=TWO_LETTER_MASTERY');print('LETTER_COVERAGE=29_OF_29');print('PDF='+str(pdf.relative_to(ROOT)))
