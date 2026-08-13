#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,html,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P018';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪَ'
LETTERS={'ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ','صَ','ضَ','طَ','ظَ','عَ','غَ','فَ','قَ','كَ','لَ','مَ','نَ',HA,'وَ','يَ'}
EX=['ءَ تَ جَ','أَ ثَ حَ','بَ جَ خَ','تَ حَ دَ','ثَ خَ ذَ','جَ دَ رَ','حَ ذَ زَ','خَ رَ سَ','دَ زَ شَ','ذَ سَ صَ','رَ شَ ضَ','زَ صَ طَ','سَ ضَ ظَ','شَ طَ عَ','صَ ظَ غَ','ضَ عَ فَ','طَ غَ قَ','ظَ فَ كَ','عَ قَ لَ','غَ كَ مَ','فَ لَ نَ','قَ مَ '+HA,'كَ نَ وَ','لَ '+HA+' يَ']
# Full-width randomized unvowelled letter-name practice row. No labels and no harakat.
NAMES=['ق','ب','ي','ث','د','ع','و','ج','ص','ك','م','ت']
UNVOWELLED_ALLOWED={'ا','ء','أ','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن','ه','ھ','ﮪ','و','ي'}
def obj(s):return '<span class="run">'+''.join(f'<span>{html.escape(x)}</span>' for x in s.split())+'</span>'
def audit():
 if len(EX)!=24 or any(len(x.split())!=3 for x in EX):raise RuntimeError('P018_THREE_LETTER_STRUCTURE_FAIL')
 ts=[t for e in EX for t in e.split()]
 if any(t not in LETTERS for t in ts):raise RuntimeError('P018_OUTSIDE_SCOPE')
 if len(NAMES)<10:raise RuntimeError('P018_NAME_ROW_NOT_FULL_ENOUGH')
 if any(any(ch in n for ch in 'ًٌٍَُِّْ') for n in NAMES):raise RuntimeError('P018_NAME_ROW_MUST_BE_UNVOWELLED')
 if any(n not in UNVOWELLED_ALLOWED for n in NAMES):raise RuntimeError('P018_NAME_ROW_OUTSIDE_ALLOWED_SET')
 if len(set(NAMES))!=len(NAMES):raise RuntimeError('P018_NAME_ROW_DUPLICATE')
def rows():return ''.join('<div class="row">'+''.join(f'<div class="practice">{obj(x)}</div>' for x in EX[i:i+3])+'</div>' for i in range(0,24,3))
def doc(u):
 names=''.join(f'<span>{x}</span>' for x in NAMES)
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}") format("truetype")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:14mm;display:flex;align-items:center;justify-content:center;color:#064d37;font:700 10.5pt Georgia;letter-spacing:.1em}}.grid{{height:131mm;flex:0 0 131mm;display:grid;grid-template-rows:repeat(8,1fr);row-gap:.7mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;gap:11mm}}.practice{{width:35mm;display:flex;justify-content:center;font:39pt/1 "{FONT}";white-space:nowrap}}.run{{display:inline-flex;direction:rtl;gap:2.4mm}}.name-strip{{height:20mm;flex:0 0 20mm;margin-top:1mm;border-top:.35mm solid #b9b9b9;display:flex;align-items:center;justify-content:space-between;direction:rtl;gap:0;font:39pt/1 "{FONT}";white-space:nowrap;padding:2.1mm 2mm 0}}.safe{{height:5mm;flex:0 0 5mm}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">18</div></header><section class="presentation">PENGAYAAN · KOMBINASI 3 HURUF</section><section class="grid">{rows()}</section><section class="name-strip">{names}</section><div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(p):
 if not p.exists():return p
 try:open(p,'ab').close();return p
 except PermissionError:pass
 for n in range(1,100):
  q=p.with_name(p.stem+f'-R{n}'+p.suffix)
  if not q.exists():return q
 raise RuntimeError('P018_NO_FREE_OUTPUT')
async def render(h):
 pdf=free(OUT/'QURBATA-JILID-1-P018-PENGAYAAN-3-HURUF-NAMA-HURUF-01-CANDIDATE-V5-FULL-ROW.pdf');png=free(OUT/'QURBATA-JILID-1-P018-PENGAYAAN-3-HURUF-NAMA-HURUF-01-CANDIDATE-V5-FULL-ROW.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  v=await p.locator('.practice').evaluate_all("e=>e.map(x=>[...x.querySelectorAll('span span')].map(y=>y.textContent.trim()).join(' '))")
  if v!=EX:raise RuntimeError('P018_RENDER_MISMATCH')
  nv=await p.locator('.name-strip > span').all_text_contents()
  if nv!=NAMES:raise RuntimeError('P018_NAME_ROW_RENDER_MISMATCH')
  if any(any(ch in x for ch in 'ًٌٍَُِّْ') for x in nv):raise RuntimeError('P018_NAME_ROW_HAS_HARAKAT')
  geom=await p.evaluate("()=>{let f=document.querySelector('.footer').getBoundingClientRect(),n=document.querySelector('.name-strip').getBoundingClientRect(),x=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect()),letters=[...document.querySelectorAll('.name-strip>span')].map(e=>e.getBoundingClientRect());let m=Math.max(...x.map(z=>z.bottom));let nl=Math.min(...letters.map(z=>z.left)),nr=Math.max(...letters.map(z=>z.right));return {ok:m<=n.top-5&&n.bottom<=f.top-5&&nl>=n.left&&nr<=n.right,mainClear:n.top-m,footerClear:f.top-n.bottom,nameLeft:nl-n.left,nameRight:n.right-nr,count:letters.length}}")
  if not geom['ok'] or geom['count']!=len(NAMES):raise RuntimeError('P018_SAFEAREA_FAIL '+str(geom))
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,geom
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P018-PENGAYAAN-3-HURUF-NAMA-HURUF-01-CANDIDATE-V5-FULL-ROW.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P018_ENRICHMENT_NAMES=PASS');print('MAIN_MATERIAL=THREE_LETTER_ENRICHMENT');print('NAME_ROW=UNVOWELLED_FULL_WIDTH_RANDOMIZED');print('NAME_ROW_SEQUENCE='+'|'.join(NAMES));print('NAME_ROW_COUNT='+str(len(NAMES)));print('NAME_ROW_FONT_PT=39');print('NAME_ROW_LAYOUT=FULL_WIDTH_SPACE_BETWEEN');print('NAME_ROW_SEPARATOR=THIN_LINE');print('NAME_ROW_MARGIN_TOP_MM=1');print('PDF='+str(pdf.relative_to(ROOT)))
