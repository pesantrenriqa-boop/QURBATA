#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P037';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪ';HA_F='ﮪَ';HA_K='ﮪِ';HA_D='ﮪُ'
FOCUS={'ءُ','أُ','بُ','تُ'}
EX=['ءُ بَ','أُ بِ','بُ ثَ','تُ تِ','ءُ ثَ','أُ ثِ','بُ جَ','تُ جِ','ءُ حَ خِ','أُ دَ ذِ','بُ رَ زِ','تُ سَ شِ','ءُ صَ ضِ','أُ طَ ظِ','بُ عَ غِ','تُ فَ ءُ','ءُ قِ أُ','أُ كَ بُ','بُ لِ تُ','تُ مَ ءُ','ءُ نِ أُ',f'أُ {HA_F} بُ','بُ وَ تُ']
# Isolated Arabic combining marks need a visible carrier. Dotted circle makes position explicit.
HARAKAT=[('fathah','◌َ'),('kasrah','◌ِ'),('dammah','◌ُ'),('fathah','◌َ'),('kasrah','◌ِ'),('dammah','◌ُ')]
NAME_REVIEW=['ا','ب','ت','ث']
def run(s):return '<span class="run">'+''.join(f'<span class="glyph">{x}</span>' for x in s.split())+'</span>'
def audit():
 ts=[x for e in EX for x in e.split()];focus=sum(x in FOCUS for x in ts);review=len(ts)-focus
 if len(ts)!=61:raise RuntimeError(f'P037_TOKEN_COUNT_FAIL {len(ts)}')
 if (focus,review)!=(31,30):raise RuntimeError(f'P037_BALANCE_FAIL focus={focus} review={review}')
 if 'إُ' in ts:raise RuntimeError('P037_HAMZAH_BELOW_ALIF_FORBIDDEN')
 if any(x in {'ه','هَ','هِ','هُ'} for x in ts+NAME_REVIEW):raise RuntimeError('P037_ONE_HOLE_HA_FORBIDDEN')
 if any(e.split()==['بُ','تَ'] for e in EX):raise RuntimeError('P037_UNWANTED_BUTA_READING')
 kinds=[k for k,_ in HARAKAT]
 if kinds.count('kasrah')!=2 or kinds.count('fathah')!=2 or kinds.count('dammah')!=2:raise RuntimeError('P037_HARAKAT_REVIEW_NOT_BALANCED')
 if not all(v.startswith('◌') for _,v in HARAKAT):raise RuntimeError('P037_HARAKAT_VISIBLE_CARRIER_REQUIRED')
 if len(NAME_REVIEW)>4:raise RuntimeError('P037_NAME_REVIEW_TOO_MUCH')
def rows():
 o=[]
 for i in range(0,8,4):o.append('<div class="row r2">'+''.join(f'<div class="practice l2">{run(x)}</div>' for x in EX[i:i+4])+'</div>')
 for i in range(8,23,3):o.append('<div class="row r3">'+''.join(f'<div class="practice l3">{run(x)}</div>' for x in EX[i:i+3])+'</div>')
 return ''.join(o)
def bottom_strip():
 marks=''.join(f'<span class="harakat-item {kind}" data-kind="{kind}"><span class="harakat-symbol">{symbol}</span></span>' for kind,symbol in HARAKAT)
 names=''.join(f'<span class="name-review-item">{x}</span>' for x in NAME_REVIEW)
 return f'<section class="learning-strip"><div class="harakat-review">{marks}</div><div class="strip-divider"></div><div class="name-review">{names}</div></section>'
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:grid;grid-template-rows:17mm 18mm 1fr 5mm 25mm 2mm 12mm;overflow:hidden}}.header{{position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{display:flex;align-items:center;justify-content:center;gap:14mm;font:44pt/1.3 "{FONT}";direction:rtl;overflow:visible}}.grid{{min-height:0;display:grid;grid-template-rows:repeat(7,minmax(0,1fr));row-gap:2.2mm;padding:2.2mm 0 2.8mm;overflow:visible}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center;overflow:visible;min-height:0}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;align-items:center;justify-content:center;font:36pt/1.28 "{FONT}";white-space:nowrap;overflow:visible;padding:.4mm 0}}.glyph{{display:inline-block;overflow:visible}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl;align-items:center;overflow:visible}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.name-gap{{min-height:5mm}}.learning-strip{{border-top:.35mm solid #b9b9b9;display:grid;grid-template-columns:1fr 1px 34mm;align-items:center;column-gap:4mm;padding:.8mm 2mm 1.2mm;overflow:visible}}.harakat-review{{display:flex;direction:rtl;align-items:center;justify-content:space-around;gap:3mm;height:100%;overflow:visible}}.harakat-item{{width:13mm;height:19mm;display:flex;align-items:center;justify-content:center;border-bottom:.65mm solid #222;overflow:visible}}.harakat-symbol{{font:39pt/1.05 "{FONT}";display:inline-flex;align-items:center;justify-content:center;min-width:10mm;min-height:14mm;text-align:center;overflow:visible}}.kasrah .harakat-symbol{{transform:translateY(-.2mm)}}.fathah .harakat-symbol,.dammah .harakat-symbol{{transform:translateY(-.8mm)}}.strip-divider{{height:18mm;background:#c9c9c9}}.name-review{{display:flex;direction:rtl;align-items:center;justify-content:space-between;gap:2.5mm;font:28pt/1.35 "{FONT}";overflow:visible}}.name-review-item{{display:flex;align-items:center;justify-content:center;min-width:6mm;overflow:visible}}.safe{{min-height:2mm}}.footer{{display:flex;justify-content:space-between;align-items:center;padding-bottom:1mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">37</div></header><section class="presentation"><span>ءُ</span><span>أُ</span><span>بُ</span><span>تُ</span></section><section class="grid">{rows()}</section><div class="name-gap"></div>{bottom_strip()}<div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P037-DAMMAH-01-CANDIDATE-V10-VISIBLE-KASRAH.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  g=await p.evaluate("()=>{let page=document.querySelector('.page').getBoundingClientRect(),grid=document.querySelector('.grid').getBoundingClientRect(),strip=document.querySelector('.learning-strip').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),rows=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect()),lastGlyphs=[...document.querySelectorAll('.row:last-child .glyph')].map(e=>e.getBoundingClientRect()),kas=[...document.querySelectorAll('.harakat-item.kasrah .harakat-symbol')].map(e=>({r:e.getBoundingClientRect(),t:e.textContent}));let maxGlyphBottom=Math.max(...lastGlyphs.map(x=>x.bottom));return {gridBottom:grid.bottom,lastRowBottom:rows.at(-1).bottom,lastGlyphToStrip:strip.top-maxGlyphBottom,stripBottom:strip.bottom,footerTop:footer.top,footerBottom:footer.bottom,pageBottom:page.bottom,kasrahCount:kas.length,kasrahTexts:kas.map(x=>x.t),kasrahMinH:Math.min(...kas.map(x=>x.r.height)),kasrahMinW:Math.min(...kas.map(x=>x.r.width))}}")
  if g['lastRowBottom']>g['gridBottom']+1:raise RuntimeError('P037_GRID_OVERFLOW '+str(g))
  if g['lastGlyphToStrip']<8:raise RuntimeError('P037_HARAKAT_STRIP_COLLISION '+str(g))
  if g['stripBottom']>g['footerTop'] or g['footerBottom']>g['pageBottom']+1:raise RuntimeError('P037_BOTTOM_FLOW_FAIL '+str(g))
  if g['kasrahCount']!=2 or any('ِ' not in t for t in g['kasrahTexts']) or g['kasrahMinH']<40 or g['kasrahMinW']<25:raise RuntimeError('P037_KASRAH_VISIBILITY_FAIL '+str(g))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P037-DAMMAH-01-CANDIDATE-V10-VISIBLE-KASRAH.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P037_DAMMAH=PASS');print('BOTTOM_STRIP_PRIMARY=HARAKAT');print('HARAKAT_DISPLAY=VISIBLE_DOTTED_CIRCLE_CARRIER');print('HARAKAT_REVIEW=◌َ|◌ِ|◌ُ');print('KASRAH_VISIBLE=YES');print('KASRAH_COUNT=2');print('HARAKAT_FONT_PT=39');print('PRACTICE_FONT_PT=36');print('HARAKAT_UNDERLINE=YES');print('NAME_REVIEW=ا|ب|ت|ث');print('BOTTOM_FLOW=SAFE');print('PDF='+str(pdf.relative_to(ROOT)))
