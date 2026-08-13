#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P021';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha'
LETTERS=['ق','ب','ي','ث','د','ع','و','ج','ص','ك','م','ت','غ','ا','ل','خ','ز','ف','س','ن','ط','ح','ذ','ض','ر','ش','ظ','ﮪ']
if len(LETTERS)!=28 or len(set(LETTERS))!=28:raise RuntimeError('P021_LETTER_SET_FAIL')
def doc(u):
 rows=''.join('<div class="row">'+''.join(f'<span>{x}</span>' for x in LETTERS[i:i+7])+'</div>' for i in range(0,28,7))
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}") format("truetype")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:16mm;display:flex;align-items:center;justify-content:center;color:#064d37;font:700 11pt Georgia;letter-spacing:.1em}}.grid{{height:152mm;display:grid;grid-template-rows:repeat(4,1fr);row-gap:3mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:space-between;padding:0 3mm;font:44pt/1 "{FONT}";white-space:nowrap}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">21</div></header><section class="presentation">NAMA HURUF · ACAK</section><section class="grid">{rows}</section><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(p):
 if not p.exists():return p
 for n in range(1,100):
  q=p.with_name(p.stem+f'-R{n}'+p.suffix)
  if not q.exists():return q
 raise RuntimeError('P021_NO_FREE_OUTPUT')
async def render(h):
 pdf=free(OUT/'QURBATA-JILID-1-P021-NAMA-HURUF-ACAK-CANDIDATE-V1.pdf')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  vals=await p.locator('.row span').all_text_contents()
  if vals!=LETTERS:raise RuntimeError('P021_RENDER_MISMATCH')
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P021-NAMA-HURUF-ACAK-CANDIDATE-V1.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h));print('QJ1_P021_LETTER_NAMES_RANDOM=PASS');print('PAGE_TYPE=LETTER_NAME_RECOGNITION');print('HARAKAT=NONE');print('LETTER_COUNT=28');print('ORDER=RANDOMIZED');print('LETTER_FONT_PT=44');print('PDF='+str(pdf.relative_to(ROOT)))
