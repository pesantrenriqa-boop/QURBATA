#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V2.
Tests TRUE consonant sukun only. It deliberately does not put sukun on ya madd.
Rows B and D from V1 were visually approved; V2 verifies those models on multiple
initial/medial/final consonants before any integration into book pages.
"""
from __future__ import annotations
import argparse,asyncio,json
from pathlib import Path
from playwright.async_api import async_playwright
HTML='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
@page{size:A5;margin:0}*{box-sizing:border-box}body{margin:0;background:#fff;color:#111;font-family:Arial,sans-serif}.page{width:148mm;height:210mm;padding:10mm;direction:ltr}h1{font:700 13pt Arial;text-align:center;margin:0 0 5mm}.row{border-bottom:1px solid #ddd;padding:3.5mm 0}.label{font:8pt Arial;direction:ltr;margin-bottom:1mm}.arab{direction:rtl;text-align:center;font-size:39pt;line-height:1.35;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}.kfg{font-family:"QURBATA KFGQPC Uthman Taha Naskh","KFGQPC Uthman Taha Naskh",serif}.ami{font-family:"Amiri",serif}.note{font:7.5pt Arial;direction:ltr;margin-top:4mm}</style></head><body><div class="page"><h1>SUKUN LAB V2 — TRUE CONSONANT SUKUN</h1>
<div class="row"><div class="label">B1 · KFGQPC U+06E1 · medial consonant</div><div class="arab kfg">يَكۡتُبُ &nbsp; يَفۡتَحُ &nbsp; يَسۡجُدُ</div></div>
<div class="row"><div class="label">B2 · KFGQPC U+06E1 · final consonant</div><div class="arab kfg">قُلۡ &nbsp; مِنۡ &nbsp; لَمۡ &nbsp; هَلۡ</div></div>
<div class="row"><div class="label">B3 · KFGQPC U+06E1 · mixed positions</div><div class="arab kfg">أَنۡعَمۡتَ &nbsp; يَعۡلَمۡ &nbsp; نَعۡبُدُ</div></div>
<div class="row"><div class="label">D1 · Amiri U+06E1 · same control</div><div class="arab ami">يَكۡتُبُ &nbsp; يَفۡتَحُ &nbsp; يَسۡجُدُ</div></div>
<div class="row"><div class="label">D2 · Amiri U+06E1 · final control</div><div class="arab ami">قُلۡ &nbsp; مِنۡ &nbsp; لَمۡ &nbsp; هَلۡ</div></div>
<div class="note">No SVG · no overlay · no clipping · no manual positioning · no sukun on madd letters. Select B if KFGQPC remains visually correct; D is control only.</div></div></body></html>'''
async def run(out:Path):
 out.mkdir(parents=True,exist_ok=True);h=out/'sukun-lab-v2.html';h.write_text(HTML,encoding='utf-8')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  text=await p.locator('body').inner_text();
  if 'ِيۡ' in text or 'ُوۡ' in text or 'َاۡ' in text:raise RuntimeError('SUKUN_ON_MADD_LETTER_FORBIDDEN')
  fam=await p.evaluate("()=>[...document.querySelectorAll('.arab')].map(e=>getComputedStyle(e).fontFamily)")
  await p.screenshot(path=str(out/'SUKUN-LAB-V2.png'),full_page=True);await p.pdf(path=str(out/'SUKUN-LAB-V2.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});(out/'SUKUN-LAB-V2.json').write_text(json.dumps({'model':'TRUE_CONSONANT_SUKUN','codepoint':'U+06E1','primary':'KFGQPC','control':'Amiri','font_families':fam},ensure_ascii=False,indent=2),encoding='utf-8');await b.close()
 print('SUKUN_LAB_V2=PASS');print('SUBJECT=TRUE_CONSONANT_SUKUN_ONLY');print('CODEPOINT=U+06E1');print('PRIMARY_MODEL=B_KFGQPC_NATIVE');print('CONTROL_MODEL=D_AMIRI_NATIVE');print('SUKUN_ON_MADD_LETTERS=FORBIDDEN');print('BOOK_PAGES_MODIFIED=NO')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v2');a=ap.parse_args();asyncio.run(run(Path(a.output_dir)))
if __name__=='__main__':main()
