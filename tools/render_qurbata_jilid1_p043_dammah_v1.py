#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P043';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha'
FOCUS={'مُ','نُ','وُ','يُ'}
# 61 tokens = 31 focus + 30 cumulative fathah/kasrah review.
EX=['مُ بَ','نُ بِ','وُ تَ','يُ تِ','مُ ثَ','نُ ثِ','وُ جَ','يُ جِ',
    'مُ حَ نُ','نُ خِ وُ','وُ دَ يُ','يُ ذِ مُ','مُ رَ نُ','نُ زِ وُ','وُ سَ يُ','يُ شِ مُ',
    'مُ صَ ضِ','نُ طَ ظِ','وُ عَ غِ','يُ فَ قِ','مُ كَ لِ','نُ ءَ إِ','وُ بَ تِ']
ARABIC_NUMERALS=['١','٢','٣','٤','٥','٦','٧','٨','٩','١٠'];NAME_REVIEW=['م','ن','و','ي']
def run(s):return '<span class="run">'+''.join(f'<span class="glyph">{x}</span>' for x in s.split())+'</span>'
def audit():
 ts=[x for e in EX for x in e.split()];focus=sum(x in FOCUS for x in ts);review=len(ts)-focus
 if len(ts)!=61:raise RuntimeError(f'P043_TOKEN_COUNT_FAIL {len(ts)}')
 if (focus,review)!=(31,30):raise RuntimeError(f'P043_BALANCE_FAIL focus={focus} review={review}')
 if 'إُ' in ts:raise RuntimeError('P043_HAMZAH_BELOW_ALIF_DAMMAH_FORBIDDEN')
 if 'أِ' in ts:raise RuntimeError('P043_HAMZAH_ABOVE_ALIF_KASRAH_FORBIDDEN')
 if 'إِ' not in ts:raise RuntimeError('P043_HAMZAH_BELOW_ALIF_KASRAH_REQUIRED')
 if any(x in {'ه','هَ','هِ','هُ'} for x in ts+NAME_REVIEW):raise RuntimeError('P043_ONE_HOLE_HA_FORBIDDEN')
 if ARABIC_NUMERALS!=['١','٢','٣','٤','٥','٦','٧','٨','٩','١٠']:raise RuntimeError('P043_ARABIC_NUMERAL_SEQUENCE_FAIL')
def rows():
 o=[]
 for i in range(0,8,4):o.append('<div class="row r2">'+''.join(f'<div class="practice l2">{run(x)}</div>' for x in EX[i:i+4])+'</div>')
 for i in range(8,23,3):o.append('<div class="row r3">'+''.join(f'<div class="practice l3">{run(x)}</div>' for x in EX[i:i+3])+'</div>')
 return ''.join(o)
def bottom_strip():
 nums=''.join(f'<span class="number-item">{x}</span>' for x in ARABIC_NUMERALS);names=''.join(f'<span class="name-review-item">{x}</span>' for x in NAME_REVIEW)
 return f'<section class="learning-strip"><div class="number-review">{nums}</div><div class="strip-divider"></div><div class="name-review">{names}</div></section>'
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:grid;grid-template-rows:17mm 18mm 1fr 3mm 19mm 2mm 12mm;overflow:hidden}}.header{{position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{display:flex;align-items:center;justify-content:center;gap:14mm;font:45pt/1.3 "{FONT}";direction:rtl;overflow:visible}}.grid{{min-height:0;display:grid;grid-template-rows:repeat(7,minmax(0,1fr));row-gap:2.4mm;padding:2.4mm 0;overflow:visible}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;overflow:visible;min-height:0}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;align-items:center;justify-content:center;font:39pt/1.28 "{FONT}";white-space:nowrap;overflow:visible;padding:.3mm 0}}.glyph{{display:inline-block;overflow:visible}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl;align-items:center;overflow:visible}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.learning-strip{{border-top:.35mm solid #b9b9b9;display:grid;grid-template-columns:1fr 1px 32mm;align-items:center;column-gap:3mm;padding:.3mm 2mm .5mm;overflow:visible}}.number-review{{display:flex;direction:rtl;align-items:center;justify-content:space-between;gap:1.4mm;height:100%;font:25pt/1.1 Arial,"{FONT}";overflow:visible}}.number-item{{display:flex;align-items:center;justify-content:center;min-width:5.5mm;white-space:nowrap}}.strip-divider{{height:14mm;background:#c9c9c9}}.name-review{{display:flex;direction:rtl;align-items:center;justify-content:space-between;gap:2mm;font:25pt/1.3 "{FONT}"}}.name-review-item{{display:flex;align-items:center;justify-content:center;min-width:5mm}}.safe{{min-height:2mm}}.footer{{display:flex;justify-content:space-between;align-items:center;padding-bottom:1mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">43</div></header><section class="presentation"><span>مُ</span><span>نُ</span><span>وُ</span><span>يُ</span></section><section class="grid">{rows()}</section><div></div>{bottom_strip()}<div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P043-DAMMAH-07-CANDIDATE-V2-KASRAH-HAMZAH-FIX.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  g=await p.evaluate("()=>{let page=document.querySelector('.page').getBoundingClientRect(),grid=document.querySelector('.grid').getBoundingClientRect(),strip=document.querySelector('.learning-strip').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),rows=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect()),lastGlyphs=[...document.querySelectorAll('.row:last-child .glyph')].map(e=>e.getBoundingClientRect()),nums=[...document.querySelectorAll('.number-item')].map(e=>e.textContent);return {gridBottom:grid.bottom,lastRowBottom:rows.at(-1).bottom,lastGlyphToStrip:strip.top-Math.max(...lastGlyphs.map(x=>x.bottom)),stripBottom:strip.bottom,footerTop:footer.top,footerBottom:footer.bottom,pageBottom:page.bottom,nums}}")
  if g['lastRowBottom']>g['gridBottom']+1:raise RuntimeError('P043_GRID_OVERFLOW '+str(g))
  if g['lastGlyphToStrip']<5:raise RuntimeError('P043_STRIP_COLLISION '+str(g))
  if g['stripBottom']>g['footerTop'] or g['footerBottom']>g['pageBottom']+1:raise RuntimeError('P043_BOTTOM_FLOW_FAIL '+str(g))
  if g['nums']!=ARABIC_NUMERALS:raise RuntimeError('P043_ARABIC_NUMERAL_RENDER_FAIL '+str(g))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P043-DAMMAH-07-CANDIDATE-V2-KASRAH-HAMZAH-FIX.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P043_DAMMAH=PASS');print('MATERIAL_NEW=مُ|نُ|وُ|يُ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('KASRAH_HAMZAH_FORM=إِ');print('HAMZAH_ABOVE_ALIF_KASRAH=FORBIDDEN');print('BOTTOM_STRIP_PRIMARY=ARABIC_NUMERALS');print('BOTTOM_FLOW=SAFE');print('PDF='+str(pdf.relative_to(ROOT)))
