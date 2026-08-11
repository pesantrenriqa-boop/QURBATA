#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V4.
Actual local KFGQPC font. Isolates Unicode mark order / normalization for U+06E1.
No book page is modified.
"""
from __future__ import annotations
import argparse,asyncio,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
ROWS=[
('A NFC canonical','يَكۡتُبُ   يَفۡتَحُ   يَسۡجُدُ   قُلۡ   مِنۡ   لَمۡ   هَلۡ'),
('B NFD canonical','يَكۡتُبُ   يَفۡتَحُ   يَسۡجُدُ   قُلۡ   مِنۡ   لَمۡ   هَلۡ'),
('C minimal mark load','يَكۡتُبُ   يَفۡتَحُ   قُلۡ   مِنۡ'),
('D isolated pairs','كۡ   فۡ   سۡ   لۡ   نۡ   مۡ   عۡ   بۡ'),
]
def norm_rows():
 out=[]
 for label,text in ROWS:
  form='NFD' if label.startswith('B ') else 'NFC';out.append((label,unicodedata.normalize(form,text)))
 return out
TEMPLATE='''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>
@page{{size:A5;margin:0}}*{{box-sizing:border-box}}body{{margin:0;background:#fff;color:#111;font-family:Arial,sans-serif}}.page{{width:148mm;height:210mm;padding:10mm;direction:ltr}}h1{{font:700 12pt Arial;text-align:center;margin:0 0 6mm}}.row{{border-bottom:1px solid #ddd;padding:5mm 0}}.label{{font:8pt Arial;direction:ltr;margin-bottom:2mm}}.arab{{direction:rtl;text-align:center;font-size:38pt;line-height:1.5;font-family:"QURBATA KFGQPC Uthman Taha Naskh"!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility;white-space:pre-wrap}}
@font-face{{font-family:"QURBATA KFGQPC Uthman Taha Naskh";src:url("{font_uri}") format("truetype");font-style:normal;font-weight:400;font-display:block}}</style></head><body><div class="page"><h1>SUKUN LAB V4 — KFGQPC MARK ORDER</h1>{rows}</div></body></html>'''
async def run(out,font_path,font_source):
 rows=''.join(f'<div class="row"><div class="label">{label}</div><div class="arab" lang="ar">{text}</div></div>' for label,text in norm_rows());h=out/'sukun-lab-v4.html';h.write_text(TEMPLATE.format(font_uri=font_path.as_uri(),rows=rows),encoding='utf-8')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');loaded=await p.evaluate("()=>document.fonts.check('38pt \\\"QURBATA KFGQPC Uthman Taha Naskh\\\"','كۡ')")
  if not loaded:raise RuntimeError('KFGQPC_BINDING_FAIL')
  await p.screenshot(path=str(out/'SUKUN-LAB-V4.png'),full_page=True);await p.pdf(path=str(out/'SUKUN-LAB-V4.pdf'),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 (out/'SUKUN-LAB-V4.json').write_text(json.dumps({'font':'KFGQPC','font_source':font_source,'test':'unicode_normalization_and_mark_order','rows':[x[0] for x in norm_rows()]},ensure_ascii=False,indent=2),encoding='utf-8');print('SUKUN_LAB_V4=PASS');print('FONT=ACTUAL_KFGQPC');print('TEST=UNICODE_NORMALIZATION_AND_MARK_ORDER');print('BOOK_PAGES_MODIFIED=NO')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v4');ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);fp,src=kfgloader.discover_font(a.font_file,a.font_zip,out);asyncio.run(run(out,fp,src))
if __name__=='__main__':main()
