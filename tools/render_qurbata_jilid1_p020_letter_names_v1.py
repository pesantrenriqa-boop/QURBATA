#!/usr/bin/env python3
# QURBATA Jilid 1 P020 — halaman khusus belajar nama huruf tanpa harakat.
from pathlib import Path
import argparse,asyncio,html,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P020';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha'
# Tetap gunakan bentuk haa tunggal dua-lubang yang telah dipakai pada jilid ini.
HA='ﮪ'
LETTERS=['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س','ش','ص','ض','ط','ظ','ع','غ','ف','ق','ك','ل','م','ن',HA,'و','ي']
ROWS=[LETTERS[0:7],LETTERS[7:14],LETTERS[14:21],LETTERS[21:28]]
HARAKAT='ًٌٍَُِّْ'
def audit():
 if len(LETTERS)!=28:raise RuntimeError(f'P020_LETTER_COUNT_FAIL={len(LETTERS)}')
 if len(set(LETTERS))!=28:raise RuntimeError('P020_DUPLICATE_LETTER')
 if any(any(h in x for h in HARAKAT) for x in LETTERS):raise RuntimeError('P020_HARAKAT_FORBIDDEN')
 if LETTERS[:4]!=['ا','ب','ت','ث']:raise RuntimeError('P020_SEQUENCE_START_FAIL')
 if LETTERS[4:7]!=['ج','ح','خ']:raise RuntimeError('P020_SEQUENCE_SECOND_FAIL')
 if any(len(r)!=7 for r in ROWS):raise RuntimeError('P020_ROW_STRUCTURE_FAIL')
def rows_html():
 return ''.join('<div class="letter-row">'+''.join(f'<span>{html.escape(x)}</span>' for x in r)+'</div>' for r in ROWS)
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}") format("truetype")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;flex:0 0 17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:18mm;flex:0 0 18mm;display:flex;align-items:center;justify-content:center;color:#064d37;font:700 11pt Georgia;letter-spacing:.11em;border-bottom:.35mm solid #b9b9b9}}.letters{{height:149mm;flex:0 0 149mm;display:grid;grid-template-rows:repeat(4,1fr);row-gap:3mm;padding:5mm 1mm 3mm;direction:rtl}}.letter-row{{display:flex;align-items:center;justify-content:space-between;width:100%;font:44pt/1 "{FONT}";white-space:nowrap}}.letter-row span{{display:inline-flex;min-width:10mm;justify-content:center;align-items:center}}.safe{{height:5mm;flex:0 0 5mm}}.footer{{height:12mm;flex:0 0 12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">20</div></header><section class="presentation">NAMA HURUF</section><section class="letters">{rows_html()}</section><div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(p):
 if not p.exists():return p
 try:open(p,'ab').close();return p
 except PermissionError:pass
 for n in range(1,100):
  q=p.with_name(p.stem+f'-R{n}'+p.suffix)
  if not q.exists():return q
 raise RuntimeError('P020_NO_FREE_OUTPUT')
async def render(h):
 pdf=free(OUT/'QURBATA-JILID-1-P020-NAMA-HURUF-CANDIDATE-V1.pdf');png=free(OUT/'QURBATA-JILID-1-P020-NAMA-HURUF-CANDIDATE-V1.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  visible=await p.locator('.letter-row span').all_text_contents()
  if visible!=LETTERS:raise RuntimeError('P020_RENDER_SEQUENCE_MISMATCH')
  if any(any(h in x for h in HARAKAT) for x in visible):raise RuntimeError('P020_RENDER_HAS_HARAKAT')
  geom=await p.evaluate("()=>{let f=document.querySelector('.footer').getBoundingClientRect(),s=document.querySelector('.safe').getBoundingClientRect(),xs=[...document.querySelectorAll('.letter-row span')].map(e=>e.getBoundingClientRect());let mb=Math.max(...xs.map(x=>x.bottom)),ml=Math.min(...xs.map(x=>x.left)),mr=Math.max(...xs.map(x=>x.right)),page=document.querySelector('.page').getBoundingClientRect();return {ok:mb<=s.top&&s.top-mb>=5&&ml>=page.left&&mr<=page.right&&s.bottom<=f.top+1,clearance:s.top-mb,minLeft:ml-page.left,maxRight:page.right-mr,count:xs.length}}")
  if not geom['ok'] or geom['count']!=28:raise RuntimeError('P020_SAFEAREA_FAIL '+str(geom))
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P020-NAMA-HURUF-CANDIDATE-V1.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h));print('QJ1_P020_LETTER_NAMES=PASS');print('PAGE_TYPE=DEDICATED_LETTER_NAMES');print('HARAKAT=NONE');print('LETTER_COUNT=28');print('ROWS=4');print('LETTERS_PER_ROW=7');print('LETTER_FONT_PT=44');print('SEQUENCE=ا|ب|ت|ث|ج|ح|خ|د|ذ|ر|ز|س|ش|ص|ض|ط|ظ|ع|غ|ف|ق|ك|ل|م|ن|ﮪ|و|ي');print('PDF='+str(pdf.relative_to(ROOT)))
