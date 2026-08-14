#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P037';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪ';HA_F='ﮪَ';HA_K='ﮪِ';HA_D='ﮪُ'
# Correct opening dammah set: independent hamzah, alif-hamzah above, baa, taa.
# Hamzah-below-alif with dammah is explicitly forbidden.
FOCUS={'ءُ','أُ','بُ','تُ'}
EX=['ءُ بَ','أُ بِ','بُ تَ','تُ تِ','ءُ ثَ','أُ ثِ','بُ جَ','تُ جِ',
    'ءُ حَ خِ','أُ دَ ذِ','بُ رَ زِ','تُ سَ شِ','ءُ صَ ضِ','أُ طَ ظِ','بُ عَ غِ',
    'تُ فَ ءُ','ءُ قِ أُ','أُ كَ بُ','بُ لِ تُ','تُ مَ ءُ','ءُ نِ أُ',f'أُ {HA_F} بُ','بُ وَ تُ']
NAMES=['ا','ب','ت','ث','ج','ح','خ','د','ذ','ر','ز','س']
def run(s):return '<span class="run">'+''.join(f'<span>{x}</span>' for x in s.split())+'</span>'
def audit():
 ts=[x for e in EX for x in e.split()];focus=sum(x in FOCUS for x in ts);review=len(ts)-focus
 if len(ts)!=61:raise RuntimeError(f'P037_TOKEN_COUNT_FAIL {len(ts)}')
 if (focus,review)!=(31,30):raise RuntimeError(f'P037_BALANCE_FAIL focus={focus} review={review}')
 if 'إُ' in ts:raise RuntimeError('P037_HAMZAH_BELOW_ALIF_FORBIDDEN')
 if any(x in {'ه','هَ','هِ','هُ'} for x in ts+NAMES):raise RuntimeError('P037_ONE_HOLE_HA_FORBIDDEN')
def rows():
 o=[]
 for i in range(0,8,4):o.append('<div class="row r2">'+''.join(f'<div class="practice l2">{run(x)}</div>' for x in EX[i:i+4])+'</div>')
 for i in range(8,23,3):o.append('<div class="row r3">'+''.join(f'<div class="practice l3">{run(x)}</div>' for x in EX[i:i+3])+'</div>')
 return ''.join(o)
def doc(u):
 names=''.join(f'<span>{x}</span>' for x in NAMES)
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;flex:0 0 17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:18mm;flex:0 0 18mm;display:flex;align-items:center;justify-content:center;gap:14mm;font:45pt/1.18 "{FONT}";direction:rtl;overflow:visible}}.grid{{height:130mm;flex:0 0 130mm;display:grid;grid-template-rows:repeat(7,1fr);row-gap:1.8mm;padding:1.5mm 0}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;overflow:visible}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;align-items:center;justify-content:center;font:38pt/1.24 "{FONT}";white-space:nowrap;overflow:visible;padding-top:.6mm;padding-bottom:.6mm}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl;align-items:center;overflow:visible}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.name-strip{{height:23mm;flex:0 0 23mm;margin-top:0;border-top:.35mm solid #b9b9b9;display:flex;align-items:center;justify-content:space-between;direction:rtl;font:38pt/1.4 "{FONT}";padding:1mm 4mm 2mm;overflow:visible}}.name-strip>span{{display:inline-block;overflow:visible}}.safe{{height:2mm;flex:0 0 2mm}}.footer{{height:12mm;flex:0 0 12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:1.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">37</div></header><section class="presentation"><span>ءُ</span><span>أُ</span><span>بُ</span><span>تُ</span></section><section class="grid">{rows()}</section><section class="name-strip">{names}</section><div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P037-DAMMAH-01-CANDIDATE-V3-VERTICAL-FIT.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  g=await p.evaluate("()=>{let page=document.querySelector('.page').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),name=document.querySelector('.name-strip').getBoundingClientRect(),rows=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect());let gaps=rows.slice(1).map((r,i)=>r.top-rows[i].bottom);return {pageBottom:page.bottom,footerBottom:footer.bottom,bottomClear:page.bottom-footer.bottom,nameFooterGap:footer.top-name.bottom,minRowGap:Math.min(...gaps)}}")
  if g['footerBottom']>g['pageBottom'] or g['bottomClear']<0 or g['minRowGap']<0:raise RuntimeError('P037_VERTICAL_FIT_FAIL '+str(g))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P037-DAMMAH-01-CANDIDATE-V3-VERTICAL-FIT.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P037_DAMMAH=PASS');print('DAMMAH_BLOCK_PAGE=1_OF_9');print('MAIN_COMPETENCY=DAMMAH');print('MATERIAL_NEW=ءُ|أُ|بُ|تُ');print('HAMZAH_BELOW_ALIF=FORBIDDEN');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('VERTICAL_GLYPH_CLEARANCE=PASS');print('BOTTOM_PAGE_FIT=PASS');print('PRACTICE_FONT_PT=38');print('GRID_HEIGHT_MM=130');print('PDF='+str(pdf.relative_to(ROOT)))
