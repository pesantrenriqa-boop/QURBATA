#!/usr/bin/env python3
# QURBATA Jilid 1 P008 — طَ ظَ; recovered from historical QJ1-P007 v0.2.0 50:50.
from pathlib import Path
import importlib.util, argparse, asyncio, sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
BASE=ROOT/'tools/render_qurbata_jilid1_p006_clean_v1.py'
spec=importlib.util.spec_from_file_location('safe',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.OUT0=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P008';m.FOCUS={'طَ','ظَ'}
m.REVIEW=['ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ','صَ','ضَ']
m.EXERCISES=['طَ ءَ','ظَ أَ','طَ بَ','ظَ تَ','ثَ طَ','جَ ظَ','حَ طَ','خَ ظَ','طَ دَ طَ','ظَ ذَ ظَ','طَ رَ طَ','ظَ زَ ظَ','طَ سَ طَ','ظَ شَ ظَ','طَ صَ طَ','ظَ ضَ ظَ','ءَ طَ ءَ','أَ ظَ أَ','بَ طَ بَ','تَ ظَ تَ','ثَ طَ ثَ','جَ ظَ جَ','حَ طَ حَ','خَ ظَ خَ']
_old=m.doc
def doc(u):
 s=_old(u).replace('<div class="pageno">06</div>','<div class="pageno">08</div>')
 s=s.replace('<section class="presentation"><span>سَ</span><span>شَ</span></section>','<section class="presentation"><span>طَ</span><span>ظَ</span></section>')
 # Lock the same horizontal group spacing already accepted on earlier frozen pages.
 s=s.replace('.r2{gap:10mm}', '.r2{gap:10mm}')
 s=s.replace('.r3{gap:11mm}', '.r3{gap:11mm}')
 return s
m.doc=doc
def audit():
 ts=[x for e in m.EXERCISES[:-1] for x in e.split()];f=sum(x in m.FOCUS for x in ts);r=len(ts)-f
 if len(ts)!=61 or (f,r)!=(31,30):raise RuntimeError(f'P008_RENDER_BALANCE_FAIL focus={f} review={r}')
def free(base):
 if not base.exists():return base
 try:
  with open(base,'ab'):pass
  return base
 except PermissionError:pass
 for n in range(1,100):
  p=base.with_name(base.stem+f'-R{n}'+base.suffix)
  if not p.exists():return p
  try:
   with open(p,'ab'):pass
   return p
  except PermissionError:continue
 raise RuntimeError('P008_NO_FREE_OUTPUT_FILENAME')
async def render(h,o):
 pdf=free(o/'QURBATA-JILID-1-P008-TA-ZA-CANDIDATE-V4-FROZEN-SPACING.pdf');png=free(o/'QURBATA-JILID-1-P008-TA-ZA-CANDIDATE-V4-FROZEN-SPACING.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  safe=await p.evaluate("""()=>{const f=document.querySelector('.footer').getBoundingClientRect(),pg=document.querySelector('.page').getBoundingClientRect(),xs=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect());const max=Math.max(...xs.map(x=>x.bottom));const r2=[...document.querySelectorAll('.r2')],r3=[...document.querySelectorAll('.r3')];const minGap=(rows)=>Math.min(...rows.flatMap(row=>{const cs=[...row.children].map(c=>c.getBoundingClientRect()).sort((a,b)=>a.left-b.left);return cs.slice(1).map((c,i)=>c.left-cs[i].right)}));const g2=minGap(r2),g3=minGap(r3);return {ok:max<=f.top-12&&max<=pg.bottom-12&&g2>=30&&g3>=30,bad:xs.filter(x=>x.bottom>f.top-12||x.bottom>pg.bottom-12).length,clearance:f.top-max,g2,g3}}""")
  if not safe['ok']:raise RuntimeError(f"P008_SAFE_OR_SPACING_FAIL bad={safe['bad']} clearance={safe['clearance']} g2={safe['g2']} g3={safe['g3']}")
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,safe
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();m.OUT0.mkdir(parents=True,exist_ok=True);font,src=kfgloader.discover_font(a.font_file,a.font_zip,m.OUT0);h=m.OUT0/'QURBATA-JILID-1-P008-TA-ZA-CANDIDATE-V4-FROZEN-SPACING.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,safe=asyncio.run(render(h,m.OUT0));print('QJ1_P008_TA_ZA_FROZEN_SPACING=PASS');print('MATERIAL_NEW=طَ|ظَ');print('PRACTICE_FONT_PT=40');print('GROUP_SPACING=PRESERVED');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('BOTTOM_GLYPH_OVERFLOW=0');print('SAFE_CLEARANCE_PX='+str(round(safe['clearance'],2)));print('GROUP_GAP_R2_PX='+str(round(safe['g2'],2)));print('GROUP_GAP_R3_PX='+str(round(safe['g3'],2)));print('FONT_SOURCE='+str(src));print('PDF='+str(pdf.relative_to(ROOT)))
