#!/usr/bin/env python3
from __future__ import annotations
import argparse,asyncio,html,re,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path:sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
import render_qurbata_jilid2_sukun_lab_v5 as sukunlab
SRC=ROOT/'books/jilid-2/rebased';DEFAULT=ROOT/'dist/jilid-2-full-review'
def pnum(p):
 m=re.search(r'QJ2-P(\d{3})',p.name,re.I);return int(m.group(1)) if m else None
def getsrc():
 d={}
 for p in SRC.glob('QJ2-P*.md'):
  n=pnum(p)
  if n and n not in d:d[n]=p
 return d
def f(s):return html.escape(s).replace('**','')
def md(t):
 out=[]
 for line in t.splitlines():
  s=line.strip()
  if not s:continue
  if s.startswith('# '):out.append('<h1>'+f(s[2:])+'</h1>')
  elif s.startswith('## '):out.append('<h2>'+f(s[3:])+'</h2>')
  elif s.startswith('|'):out.append('<div class="row">'+f(s)+'</div>')
  elif s.startswith('- '):out.append('<div class="bullet">• '+f(s[2:])+'</div>')
  else:out.append('<p>'+f(s)+'</p>')
 return ''.join(out)
def build(src,font):
 pages=[]
 for n in range(1,41):
  p=src.get(n);body=md(p.read_text(encoding='utf-8')) if p else '<div class="missing">SOURCE MISSING</div>';name=p.name if p else 'MISSING'
  pages.append(f'<section class="sheet"><div class="inner"><div class="tag">FULL REVIEW PROOF - NOT FINAL PRINT</div><div class="folio">{n:02d}</div><div class="src">{html.escape(name)}</div>{body}</div></section>')
 css=f'''@page{{size:A5;margin:0}}*{{box-sizing:border-box}}@font-face{{font-family:q;src:url("{font}")}}body{{margin:0;background:#ddd}}.sheet{{width:148mm;height:210mm;page-break-after:always;background:#fff;padding:8mm;overflow:hidden}}.inner{{height:100%;position:relative;transform-origin:top left;font:7.2pt/1.2 q,Arial}}.tag{{font:700 5.2pt Arial;color:#777;border-bottom:.2mm solid #b98a2f;padding-bottom:1mm}}.folio{{position:absolute;right:0;top:-1mm;background:#064d37;color:white;padding:1.5mm 2mm;font:700 8pt Arial}}.src{{font:5pt Consolas;color:#999;margin:1mm 0}}h1{{font:700 10pt Arial;color:#064d37;margin:1mm 0}}h2{{font:700 8pt Arial;color:#064d37;margin:1.3mm 0 .5mm}}p,.row,.bullet{{margin:.45mm 0}}.row{{font-size:6.4pt;border-bottom:.1mm solid #ddd;padding:.25mm}}.missing{{margin-top:60mm;text-align:center;color:#b00;font:700 14pt Arial}}'''
 return '<!doctype html><html><head><meta charset="utf-8"><style>'+css+'</style></head><body>'+''.join(pages)+'''<script>(async()=>{await document.fonts.ready;for(const s of document.querySelectorAll('.sheet')){const i=s.querySelector('.inner'),a=s.clientHeight,n=i.scrollHeight;if(n>a){const z=Math.max(.46,a/n);i.style.transform=`scale(${z})`;i.style.width=`${100/z}%`}}})()</script></body></html>'
async def render(h,out):
 pdf=out/'QURBATA-JILID-2-FULL-REVIEW-P001-P040.pdf'
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584});await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');await p.wait_for_timeout(300);count=await p.locator('.sheet').count()
  if count!=40:raise RuntimeError(f'PAGE_COUNT={count}')
  await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT.relative_to(ROOT)));ap.add_argument('--font-file');ap.add_argument('--font-zip');ap.add_argument('--amiri-font');a=ap.parse_args();out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True);src=getsrc();missing=[n for n in range(1,41) if n not in src];kfg,_=kfgloader.discover_font(a.font_file,a.font_zip,out);am=sukunlab.discover_amiri(a.amiri_font,out);hy=out/'_runtime_font'/'KFGQPC-QURBATA-REVIEW-FROZEN-SUKUN.ttf';sukunlab.patch_font(kfg,am,hy,-1700);h=out/'QURBATA-JILID-2-FULL-REVIEW.html';h.write_text(build(src,hy.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h,out));print('QURBATA_JILID2_FULL_REVIEW=PASS');print(f'SOURCE_PAGES_FOUND={len(src)}');print('MISSING='+(','.join(f'P{x:03d}' for x in missing) if missing else 'NONE'));print('ARTIFACT=REVIEW_PROOF_NOT_FINAL_PRINT');print(f'PDF={pdf.relative_to(ROOT)}')
if __name__=='__main__':main()
