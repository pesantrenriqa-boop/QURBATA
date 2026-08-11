#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V3.
Tests TRUE consonant sukun using the ACTUAL local KFGQPC Uthman Taha font file.
No book page is modified.
"""
from __future__ import annotations
import argparse,asyncio,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader

TEMPLATE='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
@page{{size:A5;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#111;font-family:Arial,sans-serif}}.page{{width:148mm;height:210mm;padding:10mm;direction:ltr}}h1{{font:700 13pt Arial;text-align:center;margin:0 0 5mm}}.row{{border-bottom:1px solid #ddd;padding:3.5mm 0}}.label{{font:8pt Arial;direction:ltr;margin-bottom:1mm}}.arab{{direction:rtl;text-align:center;font-size:39pt;line-height:1.35;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}}
@font-face{{font-family:"QURBATA KFGQPC Uthman Taha Naskh";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block;}}
.kfg{{font-family:"QURBATA KFGQPC Uthman Taha Naskh",serif!important}}.ami{{font-family:"Amiri",serif}}.note{{font:7.5pt Arial;direction:ltr;margin-top:4mm}}</style></head><body><div class="page"><h1>SUKUN LAB V3 — TRUE KFGQPC FONT BINDING</h1>
<div class="row"><div class="label">B1 · ACTUAL KFGQPC + U+06E1 · medial</div><div class="arab kfg">يَكۡتُبُ &nbsp; يَفۡتَحُ &nbsp; يَسۡجُدُ</div></div>
<div class="row"><div class="label">B2 · ACTUAL KFGQPC + U+06E1 · final</div><div class="arab kfg">قُلۡ &nbsp; مِنۡ &nbsp; لَمۡ &nbsp; هَلۡ</div></div>
<div class="row"><div class="label">B3 · ACTUAL KFGQPC + U+06E1 · mixed</div><div class="arab kfg">أَنۡعَمۡتَ &nbsp; يَعۡلَمۡ &nbsp; نَعۡبُدُ</div></div>
<div class="row"><div class="label">D1 · Amiri + U+06E1 · control</div><div class="arab ami">يَكۡتُبُ &nbsp; يَفۡتَحُ &nbsp; يَسۡجُدُ</div></div>
<div class="row"><div class="label">D2 · Amiri + U+06E1 · final control</div><div class="arab ami">قُلۡ &nbsp; مِنۡ &nbsp; لَمۡ &nbsp; هَلۡ</div></div>
<div class="note">KFGQPC is injected from the same local TTF/ZIP loader used by Jilid 2. No SVG, overlay, clipping, or manual positioning.</div></div></body></html>'''

async def run(out:Path,font_path:Path,font_source:str):
 out.mkdir(parents=True,exist_ok=True); h=out/'sukun-lab-v3.html';h.write_text(TEMPLATE.format(font_uri=font_path.as_uri()),encoding='utf-8')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  loaded=await p.evaluate("()=>document.fonts.check('39pt \\\"QURBATA KFGQPC Uthman Taha Naskh\\\"','يَكۡتُبُ')")
  if not loaded: raise RuntimeError('SUKUN_LAB_KFGQPC_FONT_BINDING_FAIL')
  text=await p.locator('body').inner_text()
  if 'ِيۡ' in text or 'ُوۡ' in text or 'َاۡ' in text:raise RuntimeError('SUKUN_ON_MADD_LETTER_FORBIDDEN')
  fam=await p.evaluate("()=>[...document.querySelectorAll('.arab')].map(e=>getComputedStyle(e).fontFamily)")
  await p.screenshot(path=str(out/'SUKUN-LAB-V3.png'),full_page=True);await p.pdf(path=str(out/'SUKUN-LAB-V3.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});(out/'SUKUN-LAB-V3.json').write_text(json.dumps({'model':'TRUE_CONSONANT_SUKUN','codepoint':'U+06E1','primary':'ACTUAL_LOCAL_KFGQPC','control':'Amiri','font_source':font_source,'font_file':font_path.name,'font_binding':loaded,'font_families':fam},ensure_ascii=False,indent=2),encoding='utf-8');await b.close()
 print('SUKUN_LAB_V3=PASS');print('SUBJECT=TRUE_CONSONANT_SUKUN_ONLY');print('CODEPOINT=U+06E1');print('PRIMARY_FONT=ACTUAL_KFGQPC_UTHMAN_TAHA');print('FONT_BINDING_GATE=PASS');print('FONT_SOURCE='+font_source);print('FONT_FILE_NAME='+font_path.name);print('BOOK_PAGES_MODIFIED=NO')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v3');ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);font_path,font_source=kfgloader.discover_font(a.font_file,a.font_zip,out);asyncio.run(run(out,font_path,font_source))
if __name__=='__main__':main()
