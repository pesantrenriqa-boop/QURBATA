#!/usr/bin/env python3
from pathlib import Path
import argparse,asyncio,sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P032';LOGO=ROOT/'books/shared/assets/qurbata-logo.svg';FONT='QURBATA KFGQPC Uthman Taha';HA='ﮪ';HA_F='ﮪَ'
FOCUS={'كِ','لِ'}
OLD_KASRAH={'ءِ','إِ','بِ','تِ','ثِ','جِ','حِ','خِ','دِ','ذِ','رِ','زِ','سِ','شِ','صِ','ضِ','طِ','ظِ','عِ','غِ','فِ','قِ'}
FATHAH_POOL={'ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ','صَ','ضَ','طَ','ظَ','عَ','غَ','فَ','قَ','كَ','لَ','مَ','نَ',HA_F,'وَ','يَ'}
# 61 tokens = 31 focus + 30 review; review = 15 old kasrah + 15 fathah.
EX=['كِ ءَ','لِ أَ','كِ بَ','لِ تَ','كِ ثَ','لِ جَ','كِ حَ','لِ خَ',
    'كِ فِ كِ','لِ قِ لِ','كِ عِ كِ','لِ غِ لِ','كِ طِ كِ','لِ ظِ لِ','كِ صِ كِ','لِ ضِ لِ',
    'كِ سِ دَ','لِ شِ ذَ','كِ رِ رَ','لِ زِ زَ','كِ دِ سَ','لِ ذِ شَ','كِ حِ وَ']
NAMES=['ا','ث','ج','ح','خ','ر','س','ص','ع','غ',HA,'ي']
def run(s):return '<span class="run">'+''.join(f'<span>{x}</span>' for x in s.split())+'</span>'
def audit():
 ts=[x for e in EX for x in e.split()];f=sum(x in FOCUS for x in ts);old=sum(x in OLD_KASRAH for x in ts);fa=sum(x in FATHAH_POOL for x in ts)
 if (len(ts),f,old+fa)!=(61,31,30):raise RuntimeError(f'P032_BALANCE_FAIL tokens={len(ts)} focus={f} review={old+fa}')
 if (old,fa)!=(15,15):raise RuntimeError(f'P032_REVIEW_SPLIT_FAIL kasrah={old} fathah={fa}')
 if 'ه' in NAMES or 'هَ' in ts:raise RuntimeError('P032_ONE_HOLE_HA_FORBIDDEN')
 if HA not in NAMES:raise RuntimeError('P032_TWO_HOLE_HA_REQUIRED')
def rows():
 o=[]
 for i in range(0,8,4):o.append('<div class="row r2">'+''.join(f'<div class="practice l2">{run(x)}</div>' for x in EX[i:i+4])+'</div>')
 for i in range(8,23,3):o.append('<div class="row r3">'+''.join(f'<div class="practice l3">{run(x)}</div>' for x in EX[i:i+3])+'</div>')
 return ''.join(o)
def doc(u):
 names=''.join(f'<span>{x}</span>' for x in NAMES)
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:18mm;display:flex;align-items:center;justify-content:center;gap:18mm;font:46pt "{FONT}";direction:rtl}}.grid{{height:121mm;display:grid;grid-template-rows:repeat(7,1fr);row-gap:.8mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;justify-content:center;font:39pt/1 "{FONT}";white-space:nowrap}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.name-strip{{height:23mm;margin-top:1mm;border-top:.35mm solid #b9b9b9;display:flex;align-items:center;justify-content:space-between;direction:rtl;font:39pt/1.35 "{FONT}";padding:1mm 4mm 2mm;overflow:visible}}.name-strip>span{{display:inline-block;overflow:visible}}.safe{{height:5mm}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">32</div></header><section class="presentation"><span>كِ</span><span>لِ</span></section><section class="grid">{rows()}</section><section class="name-strip">{names}</section><div class="safe"></div><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
async def render(h):
 pdf=OUT/'QURBATA-JILID-1-P032-KASRAH-12-CANDIDATE-V1-BALANCED.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');names=await p.locator('.name-strip span').all_text_contents()
  if names!=NAMES:raise RuntimeError('P032_NAME_ROW_MISMATCH')
  g=await p.evaluate("()=>{let n=document.querySelector('.name-strip').getBoundingClientRect(),a=[...document.querySelectorAll('.name-strip>span')].map(e=>e.getBoundingClientRect());return {left:Math.min(...a.map(x=>x.left))-n.left,right:n.right-Math.max(...a.map(x=>x.right)),top:Math.min(...a.map(x=>x.top))-n.top,bottom:n.bottom-Math.max(...a.map(x=>x.bottom))}}")
  if g['left']<8 or g['right']<8 or g['top']<0 or g['bottom']<0:raise RuntimeError('P032_NAME_SAFEAREA_FAIL '+str(g))
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,g
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P032-KASRAH-12-CANDIDATE-V1-BALANCED.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h));print('QJ1_P032_KASRAH=PASS');print('MAIN_COMPETENCY=KASRAH');print('MATERIAL_NEW=كِ|لِ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('REVIEW_SPLIT=15_OLD_KASRAH|15_FATHAH');print('HA_GLYPH=TWO_HOLE_ONLY');print('NAME_ROW_SAFEAREA=PASS');print('PDF='+str(pdf.relative_to(ROOT)))
