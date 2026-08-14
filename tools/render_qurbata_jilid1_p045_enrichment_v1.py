#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P045';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪ';HA_F='ﮪَ';HA_K='ﮪِ';HA_D='ﮪُ'
# Final enrichment: each 3-letter group contains one fathah, one kasrah, one dammah.
EX=['يِ وُ نَ','مُ لِ كَ','قَ فُ غِ','عِ ظَ طُ','ضُ صِ شَ','سَ زُ رِ','ذِ دَ خُ',
    'حُ جِ ثَ','تَ بِ أُ','إِ ءَ بُ','ثُ تِ جَ','حَ خُ دِ','ذُ رَ زِ','سِ شَ صُ',
    'ضَ طِ ظُ','عُ غَ فِ','قِ كَ لُ','مَ نِ وَ','يُ '+HA_F+' بِ',HA_K+' وُ تَ','ثِ جُ حَ']
ARABIC_NUMERALS=['١','٢','٣','٤','٥','٦','٧','٨','٩','١٠'];NAME_REVIEW=['ا','ب','م','ي']
def run(s):return '<span class="run">'+''.join(f'<span class="glyph">{x}</span>' for x in s.split())+'</span>'
def hk(t):
 return 'f' if t.endswith('َ') else 'k' if t.endswith('ِ') else 'd' if t.endswith('ُ') else '?'
def audit():
 groups=[e.split() for e in EX];ts=[x for g in groups for x in g]
 if len(EX)!=21 or any(len(g)!=3 for g in groups) or len(ts)!=63:raise RuntimeError('P045_ENRICHMENT_GRID_FAIL')
 if any(sorted(hk(x) for x in g)!=['d','f','k'] for g in groups):raise RuntimeError('P045_HARAKAT_MIX_FAIL')
 c={h:sum(hk(x)==h for x in ts) for h in ('f','k','d')}
 if c!={'f':21,'k':21,'d':21}:raise RuntimeError('P045_HARAKAT_BALANCE_FAIL '+str(c))
 if 'أِ' in ts:raise RuntimeError('P045_WRONG_KASRAH_HAMZAH_FORM')
 if 'إُ' in ts:raise RuntimeError('P045_WRONG_DAMMAH_HAMZAH_FORM')
 if any(x in {'ه','هَ','هِ','هُ'} for x in ts):raise RuntimeError('P045_ONE_HOLE_HA_FORBIDDEN')
def rows():return ''.join('<div class="row">'+''.join(f'<div class="practice">{run(x)}</div>' for x in EX[i:i+3])+'</div>' for i in range(0,21,3))
def bottom_strip():
 nums=''.join(f'<span class="number-item">{x}</span>' for x in ARABIC_NUMERALS);names=''.join(f'<span class="name-review-item">{x}</span>' for x in NAME_REVIEW)
 return f'<section class="learning-strip"><div class="number-review">{nums}</div><div class="strip-divider"></div><div class="name-review">{names}</div></section>'
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 9mm 2.5mm;display:grid;grid-template-rows:17mm 18mm 1fr 3mm 19mm 2mm 12mm;overflow:hidden}}.header{{position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{display:flex;align-items:center;justify-content:center;gap:16mm;font:43pt/1.25 "{FONT}";direction:rtl;overflow:visible}}.grid{{min-height:0;display:grid;grid-template-rows:repeat(7,minmax(0,1fr));row-gap:2.2mm;padding:2.2mm 0;overflow:visible}}.row{{display:grid;grid-template-columns:repeat(3,34mm);column-gap:7mm;direction:rtl;align-items:center;justify-content:center;overflow:visible}}.practice{{width:34mm;display:flex;align-items:center;justify-content:center;font:36pt/1.25 "{FONT}";white-space:nowrap;overflow:visible}}.run{{display:inline-flex;direction:rtl;align-items:center;gap:3.2mm;overflow:visible}}.glyph{{display:inline-block;overflow:visible}}.learning-strip{{border-top:.35mm solid #b9b9b9;display:grid;grid-template-columns:1fr 1px 32mm;align-items:center;column-gap:3mm;padding:.3mm 2mm .5mm;overflow:visible}}.number-review{{display:flex;direction:rtl;align-items:center;justify-content:space-between;gap:1.4mm;height:100%;font:25pt/1.1 Arial,"{FONT}"}}.number-item{{display:flex;align-items:center;justify-content:center;min-width:5.5mm;white-space:nowrap}}.strip-divider{{height:14mm;background:#c9c9c9}}.name-review{{display:flex;direction:rtl;align-items:center;justify-content:space-between;gap:2mm;font:25pt/1.3 "{FONT}"}}.name-review-item{{display:flex;align-items:center;justify-content:center;min-width:5mm}}.safe{{min-height:2mm}}.footer{{display:flex;justify-content:space-between;align-items:center;padding-bottom:1mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1 · PENGAYAAN</div><div class="pageno">45</div></header><section class="presentation"><span>مَ</span><span>مِ</span><span>مُ</span></section><section class="grid">{rows()}</section><div></div>{bottom_strip()}<div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P045-PENGAYAAN-02-CANDIDATE-V1.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  g=await p.evaluate("()=>{let page=document.querySelector('.page').getBoundingClientRect(),grid=document.querySelector('.grid').getBoundingClientRect(),strip=document.querySelector('.learning-strip').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),rows=[...document.querySelectorAll('.row')].map(e=>e.getBoundingClientRect()),last=[...document.querySelectorAll('.row:last-child .glyph')].map(e=>e.getBoundingClientRect());return {gridBottom:grid.bottom,lastRowBottom:rows.at(-1).bottom,lastGlyphToStrip:strip.top-Math.max(...last.map(x=>x.bottom)),stripBottom:strip.bottom,footerTop:footer.top,footerBottom:footer.bottom,pageBottom:page.bottom}}")
  if g['lastRowBottom']>g['gridBottom']+1 or g['lastGlyphToStrip']<5:raise RuntimeError('P045_LAYOUT_FAIL '+str(g))
  if g['stripBottom']>g['footerTop'] or g['footerBottom']>g['pageBottom']+1:raise RuntimeError('P045_BOTTOM_FLOW_FAIL '+str(g))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P045-PENGAYAAN-02-CANDIDATE-V1.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h));print('QJ1_P045_ENRICHMENT=PASS');print('PAGE_TYPE=FINAL_FATHAH_KASRAH_DAMMAH_ENRICHMENT');print('HARAKAT_BALANCE=21|21|21');print('KASRAH_HAMZAH=إِ');print('BOTTOM_STRIP_PRIMARY=ARABIC_NUMERALS');print('JILID1_TARGET_END=P045');print('PDF='+str(pdf.relative_to(ROOT)))
