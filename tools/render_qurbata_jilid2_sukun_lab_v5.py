#!/usr/bin/env python3
"""QURBATA Jilid 2 — SUKUN LAB V6.
Render an atlas of the exact zero-advance mark glyph candidates discovered in the
local KFGQPC TTF. This avoids guessing which internal glyph is the approved open sukun.
No book page or source font is modified.
"""
from __future__ import annotations
import argparse,asyncio,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
CANDIDATES=['afii57451','.notdef.3','uni0654','uni0655','.notdef.5','.notdef.6','.notdef.7','afii57453','afii57457','afii57454','.notdef.4','afii57456']
TEST_BASES=['ب','ك','ل','م']
def make_probe_font(src:Path,dst:Path,candidate:str):
 from fontTools.ttLib import TTFont
 import copy
 f=TTFont(str(src));cmap={}
 for t in f['cmap'].tables:
  if t.isUnicode():cmap.update(t.cmap)
 target=cmap.get(0x0652)
 if not target:raise RuntimeError('U0652_NOT_FOUND')
 if candidate not in f.getGlyphOrder():raise RuntimeError('CANDIDATE_NOT_FOUND='+candidate)
 if 'glyf' not in f:raise RuntimeError('NOT_TRUETYPE_GLYF')
 f['glyf'][target]=copy.deepcopy(f['glyf'][candidate]);dst.parent.mkdir(parents=True,exist_ok=True);f.save(str(dst));return target
async def run(out,src,srcdesc):
 fonts=[]
 for i,c in enumerate(CANDIDATES,1):
  fp=out/'_candidate_fonts'/f'candidate-{i:02d}.ttf';make_probe_font(src,fp,c);fonts.append((i,c,fp))
 faces=''.join(f'@font-face{{font-family:"Cand{i}";src:url("{fp.resolve().as_uri()}") format("truetype");font-display:block}}' for i,c,fp in fonts)
 cards=''.join(f'<div class="card"><div class="label">{i:02d} · {c}</div><div class="arab" style="font-family:Cand{i}">{" &nbsp; ".join(x+"ْ" for x in TEST_BASES)}</div><div class="mark" style="font-family:Cand{i}">بْ</div></div>' for i,c,fp in fonts)
 html=f'''<!doctype html><html><head><meta charset="utf-8"><style>@page{{size:A4;margin:0}}{faces}*{{box-sizing:border-box}}body{{margin:0;font-family:Arial}}.page{{padding:10mm;display:grid;grid-template-columns:1fr 1fr;gap:3mm}}h1{{grid-column:1/-1;font-size:13pt;text-align:center}}.card{{border:1px solid #bbb;padding:3mm;min-height:39mm}}.label{{font-size:8pt}}.arab{{direction:rtl;text-align:center;font-size:31pt;line-height:1.35}}.mark{{direction:rtl;text-align:center;font-size:43pt;line-height:1.1}}</style></head><body><div class="page"><h1>SUKUN LAB V6 — KFGQPC INTERNAL MARK ATLAS</h1>{cards}</div></body></html>'''
 h=out/'sukun-lab-v6.html';h.write_text(html,encoding='utf-8')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1584,'height':2240},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');await p.screenshot(path=str(out/'SUKUN-LAB-V6.png'),full_page=True);await p.pdf(path=str(out/'SUKUN-LAB-V6.pdf'),format='A4',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 (out/'SUKUN-LAB-V6.json').write_text(json.dumps({'source_font':src.name,'source':srcdesc,'candidates':CANDIDATES,'instruction':'Choose the numbered candidate whose mark is the approved open sukun shape. No book page modified.'},ensure_ascii=False,indent=2),encoding='utf-8');print('SUKUN_LAB_V6=PASS');print('MODE=INTERNAL_GLYPH_ATLAS');print('CANDIDATE_COUNT='+str(len(CANDIDATES)));print('BOOK_PAGES_MODIFIED=NO')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='dist/jilid-2-sukun-lab-v6');ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);fp,src=kfgloader.discover_font(a.font_file,a.font_zip,out);asyncio.run(run(out,fp,src))
if __name__=='__main__':main()
