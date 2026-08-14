#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P040';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha'
FOCUS={'سُ','شُ','صُ','ضُ'}
EX=['سُ بَ','شُ بِ','صُ تَ','ضُ تِ','سُ ثَ','شُ ثِ','صُ جَ','ضُ جِ','سُ حَ شُ','شُ خِ صُ','صُ دَ ضُ','ضُ ذِ سُ','سُ رَ شُ','شُ زِ صُ','صُ سَ ضُ','ضُ شِ سُ','سُ صَ ضِ','شُ طَ ظِ','صُ عَ غِ','ضُ فَ قِ','سُ كَ لِ','شُ مَ نِ','صُ وَ يِ']
HARAKAT=['fathah','kasrah','dammah','fathah','kasrah','dammah'];NAME_REVIEW=['س','ش','ص','ض']
def run(s):return '<span class="run">'+''.join(f'<span class="glyph">{x}</span>' for x in s.split())+'</span>'
def audit():
 ts=[x for e in EX for x in e.split()];focus=sum(x in FOCUS for x in ts);review=len(ts)-focus
 if len(ts)!=61:raise RuntimeError(f'P040_TOKEN_COUNT_FAIL {len(ts)}')
 if (focus,review)!=(31,30):raise RuntimeError(f'P040_BALANCE_FAIL focus={focus} review={review}')
 if any(x in {'ه','هَ','هِ','هُ'} for x in ts+NAME_REVIEW):raise RuntimeError('P040_ONE_HOLE_HA_FORBIDDEN')
 if any(HARAKAT.count(k)!=2 for k in ('fathah','kasrah','dammah')):raise RuntimeError('P040_HARAKAT_REVIEW_NOT_BALANCED')
def rows():
 o=[]
 for i in range(0,8,4):o.append('<div class="row r2">'+''.join(f'<div class="practice l2">{run(x)}</div>' for x in EX[i:i+4])+'</div>')
 for i in range(8,23,3):o.append('<div class="row r3">'+''.join(f'<div class="practice l3">{run(x)}</div>' for x in EX[i:i+3])+'</div>')
 return ''.join(o)
def harakat_item(kind):
 mark={'fathah':'\u00a0َ','kasrah':'\u00a0ِ','dammah':'\u00a0ُ'}[kind]
 return f'<span class="harakat-item {kind}" data-kind="{kind}"><span class="mark-anchor"><span class="mark">{mark}</span></span><span class="position-line"></span></span>'
def bottom_strip():
 marks=''.join(harakat_item(k) for k in HARAKAT);names=''.join(f'<span class="name-review-item">{x}</span>' for x in NAME_REVIEW)
 return f'<section class="learning-strip"><div class="harakat-review">{marks}</div><div class="strip-divider"></div><div class="name-review">{names}</div></section>'
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:grid;grid-template-rows:17mm 18mm 1fr 3mm 19mm 2mm 12mm;overflow:hidden}}.header{{position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{display:flex;align-items:center;justify-content:center;gap:14mm;font:45pt/1.3 "{FONT}";direction:rtl;overflow:visible}}.grid{{min-height:0;display:grid;grid-template-rows:repeat(7,minmax(0,1fr));row-gap:2.4mm;padding:2.4mm 0 2.4mm;overflow:visible}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;overflow:visible;min-height:0}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;align-items:center;justify-content:center;font:39pt/1.28 "{FONT}";white-space:nowrap;overflow:visible;padding:.3mm 0}}.glyph{{display:inline-block;overflow:visible}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl;align-items:center;overflow:visible}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.name-gap{{min-height:3mm}}.learning-strip{{border-top:.35mm solid #b9b9b9;display:grid;grid-template-columns:1fr 1px 32mm;align-items:center;column-gap:3mm;padding:.3mm 2mm .5mm;overflow:visible}}.harakat-review{{display:flex;direction:rtl;align-items:center;justify-content:space-around;gap:2mm;height:100%;overflow:visible}}.harakat-item{{position:relative;width:12mm;height:15mm;display:block;overflow:visible}}.position-line{{position:absolute;left:1mm;right:1mm;top:7.5mm;height:.5mm;background:#222}}.mark-anchor{{position:absolute;left:50%;width:10mm;height:1px;transform:translateX(-50%);overflow:visible}}.mark{{position:absolute;left:50%;font:32pt/1 "{FONT}";width:10mm;text-align:center;transform:translateX(-50%);overflow:visible;white-space:pre}}.fathah .mark-anchor,.dammah .mark-anchor{{top:5.1mm}}.kasrah .mark-anchor{{top:10.1mm}}.fathah .mark,.dammah .mark{{bottom:-1.1mm}}.kasrah .mark{{top:-3.2mm}}.strip-divider{{height:14mm;background:#c9c9c9}}.name-review{{display:flex;direction:rtl;align-items:center;justify-content:space-between;gap:2mm;font:25pt/1.3 "{FONT}";overflow:visible}}.name-review-item{{display:flex;align-items:center;justify-content:center;min-width:5mm;overflow:visible}}.safe{{min-height:2mm}}.footer{{display:flex;justify-content:space-between;align-items:center;padding-bottom:1mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">40</div></header><section class="presentation"><span>سُ</span><span>شُ</span><span>صُ</span><span>ضُ</span></section><section class="grid">{rows()}</section><div class="name-gap"></div>{bottom_strip()}<div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P040-DAMMAH-04-CANDIDATE-V1-COMPACT-HARAKAT.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  g=await p.evaluate("()=>{let page=document.querySelector('.page').getBoundingClientRect(),grid=document.querySelector('.grid').getBoundingClientRect(),strip=document.querySelector('.learning-strip').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),rows=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect()),lastGlyphs=[...document.querySelectorAll('.row:last-child .glyph')].map(e=>e.getBoundingClientRect()),items=[...document.querySelectorAll('.harakat-item')].map(e=>{let a=e.querySelector('.mark-anchor').getBoundingClientRect(),l=e.querySelector('.position-line').getBoundingClientRect(),t=e.querySelector('.mark').textContent;return {k:e.dataset.kind,anchorY:a.top,lineTop:l.top,lineBottom:l.bottom,text:t}});return {gridBottom:grid.bottom,lastRowBottom:rows.at(-1).bottom,lastGlyphToStrip:strip.top-Math.max(...lastGlyphs.map(x=>x.bottom)),stripBottom:strip.bottom,footerTop:footer.top,footerBottom:footer.bottom,pageBottom:page.bottom,items}}")
  if g['lastRowBottom']>g['gridBottom']+1:raise RuntimeError('P040_GRID_OVERFLOW '+str(g))
  if g['lastGlyphToStrip']<5:raise RuntimeError('P040_HARAKAT_STRIP_COLLISION '+str(g))
  if g['stripBottom']>g['footerTop'] or g['footerBottom']>g['pageBottom']+1:raise RuntimeError('P040_BOTTOM_FLOW_FAIL '+str(g))
  if any('◌' in x['text'] for x in g['items']):raise RuntimeError('P040_DOTTED_CIRCLE_FORBIDDEN')
  for x in g['items']:
   if x['k']=='kasrah' and x['anchorY']<=x['lineBottom']+2:raise RuntimeError('P040_KASRAH_ANCHOR_NOT_BELOW_LINE '+str(x))
   if x['k'] in ('fathah','dammah') and x['anchorY']>=x['lineTop']-2:raise RuntimeError('P040_UPPER_HARAKAT_ANCHOR_NOT_ABOVE_LINE '+str(x))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P040-DAMMAH-04-CANDIDATE-V1-COMPACT-HARAKAT.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P040_DAMMAH=PASS');print('DAMMAH_BLOCK_PAGE=4_OF_9');print('MATERIAL_NEW=سُ|شُ|صُ|ضُ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('PRACTICE_FONT_PT=39');print('HARAKAT_FONT_PT=32');print('FATHAH_POSITION=ABOVE_LINE');print('KASRAH_POSITION=BELOW_LINE');print('DAMMAH_POSITION=ABOVE_LINE');print('NAME_REVIEW=س|ش|ص|ض');print('BOTTOM_FLOW=SAFE');print('PDF='+str(pdf.relative_to(ROOT)))
