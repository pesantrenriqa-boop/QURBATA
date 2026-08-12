#!/usr/bin/env python3
from __future__ import annotations
import argparse, asyncio, html, sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
LOGO=ROOT/'books/shared/assets/qurbata-logo.svg'; OUT0=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P004'; FONT='QURBATA KFGQPC Uthman Taha'
FOCUS={'دَ','ذَ'}; REVIEW=['ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ']
EXERCISES=['دَ ءَ','ذَ أَ','دَ بَ','ذَ تَ','دَ ثَ','ذَ جَ','دَ حَ','ذَ خَ','دَ ذَ دَ','ءَ دَ أَ','ذَ دَ ذَ','بَ ذَ تَ','دَ دَ ذَ','ثَ دَ جَ','ذَ ذَ دَ','حَ ذَ خَ','دَ ءَ ذَ','أَ دَ بَ','ذَ تَ دَ','ثَ ذَ جَ','دَ حَ ذَ','خَ دَ ءَ','ذَ أَ دَ','بَ ذَ تَ']
def toks(s):return s.split()
def obj(s):return '<span class="run">'+''.join(f'<span>{html.escape(x)}</span>' for x in toks(s))+'</span>'
def audit():
 ts=[x for e in EXERCISES for x in toks(e)]; allowed=FOCUS|set(REVIEW)
 if len(EXERCISES)!=24 or len(ts)!=64 or any(x not in allowed for x in ts):raise RuntimeError('P004_SOURCE_AUDIT_FAIL')
 if sum(x in FOCUS for x in ts)!=32:raise RuntimeError('P004_FOCUS_NOT_32')
def rows():
 items=EXERCISES[:-1];out=[]
 for i in range(0,8,4):out.append('<div class="row r2">'+''.join(f'<div class="practice l2">{obj(x)}</div>' for x in items[:8][i:i+4])+'</div>')
 for i in range(0,15,3):out.append('<div class="row r3">'+''.join(f'<div class="practice l3">{obj(x)}</div>' for x in items[8:][i:i+3])+'</div>')
 return ''.join(out)
def doc(u):
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:"{FONT}";src:url("{u}") format("truetype")}}html,body{{margin:0}}.page{{width:148mm;height:210mm;padding:3.6mm 8mm 2.5mm;display:flex;flex-direction:column;overflow:hidden}}.header{{height:17mm;flex:0 0 17mm;position:relative;display:flex;align-items:center;justify-content:center}}.logo{{position:absolute;left:0;width:32mm;height:17mm}}.title{{position:absolute;left:50%;transform:translateX(-50%);color:#064d37;font:700 6.2pt Georgia;letter-spacing:.16em}}.pageno{{position:absolute;right:0;top:0;width:12mm;background:#064d37;color:white;border-bottom:1mm solid #b98a2f;text-align:center;font:700 12pt Arial;padding:2.2mm 1mm 3mm;border-radius:0 0 3mm 3mm}}.presentation{{height:20mm;display:flex;align-items:center;justify-content:center;gap:18mm;font:46pt "{FONT}";direction:rtl}}.grid{{height:158mm;display:grid;grid-template-rows:repeat(7,1fr);row-gap:3.2mm}}.row{{display:flex;direction:rtl;align-items:center;justify-content:center}}.r2{{gap:10mm}}.r3{{gap:11mm}}.practice{{display:flex;justify-content:center;font:40pt "{FONT}";white-space:nowrap}}.l2{{width:23mm}}.l3{{width:35mm}}.run{{display:inline-flex;direction:rtl}}.l2 .run{{gap:2.8mm}}.l3 .run{{gap:2.4mm}}.footer{{height:12mm;display:flex;justify-content:space-between;align-items:center;padding-bottom:2.2mm;color:#173a2d}}.ar{{font:10.3pt "{FONT}";direction:rtl}}'''
 return f'''<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body><main class="page"><header class="header"><img class="logo" src="{LOGO.resolve().as_uri()}"><div class="title">QURBATA · JILID 1</div><div class="pageno">04</div></header><section class="presentation"><span>دَ</span><span>ذَ</span></section><section class="grid">{rows()}</section><footer class="footer"><span class="ar">قُرْآنٌ · لُغَةٌ · أَدَبٌ</span><span class="ar">تَعَلَّمْ · اِعْمَلْ · عَلِّمْ</span></footer></main></body></html>'''
def free(b):
 if not b.exists():return b
 try:open(b,'ab').close();return b
 except PermissionError:pass
 for n in range(1,100):
  p=b.with_name(b.stem+f'-R{n}'+b.suffix)
  if not p.exists():return p
 raise RuntimeError('NO_FREE_OUTPUT')
async def render(h,o):
 pdf=free(o/'QURBATA-JILID-1-P004-DAL-DHAL-CANDIDATE-V2.pdf');png=free(o/'QURBATA-JILID-1-P004-DAL-DHAL-CANDIDATE-V2.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT0.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT0);h=OUT0/'QURBATA-JILID-1-P004-DAL-DHAL-CANDIDATE-V2.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h,OUT0));print('QJ1_P004_DAL_DHAL=PASS');print('MATERIAL_NEW=دَ|ذَ');print('PDF='+str(pdf.relative_to(ROOT)))
