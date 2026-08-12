#!/usr/bin/env python3
# QURBATA Jilid 1 P007 — صَ ضَ, shifted from historical QJ1-P006 after page split.
from pathlib import Path
import importlib.util, argparse, asyncio
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'tools/render_qurbata_jilid1_p006_clean_v1.py'
spec=importlib.util.spec_from_file_location('p006shell',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.OUT0=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P007'
m.FOCUS={'صَ','ضَ'}
m.REVIEW=['ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ']
m.EXERCISES=['صَ ءَ','ضَ أَ','صَ بَ','ضَ تَ','ثَ صَ','جَ ضَ','حَ صَ','خَ ضَ','صَ دَ صَ','ضَ ذَ ضَ','صَ رَ صَ','ضَ زَ ضَ','صَ سَ صَ','ضَ شَ ضَ','صَ ءَ صَ','ضَ أَ ضَ','بَ صَ بَ','تَ ضَ تَ','ثَ صَ ثَ','جَ ضَ جَ','حَ صَ حَ','خَ ضَ خَ','دَ صَ دَ','ذَ ضَ ذَ']
_old_doc=m.doc
def doc(u):
 s=_old_doc(u)
 s=s.replace('<div class="pageno">06</div>','<div class="pageno">07</div>')
 s=s.replace('<section class="presentation"><span>سَ</span><span>شَ</span></section>','<section class="presentation"><span>صَ</span><span>ضَ</span></section>')
 return s
def audit():
 rendered=m.EXERCISES[:-1];ts=[x for e in rendered for x in e.split()];allowed=m.FOCUS|set(m.REVIEW);f=sum(x in m.FOCUS for x in ts);r=len(ts)-f
 if len(m.EXERCISES)!=24 or len(rendered)!=23 or len(ts)!=61 or any(x not in allowed for x in ts):raise RuntimeError('P007_SOURCE_AUDIT_FAIL')
 if (f,r)!=(31,30):raise RuntimeError(f'P007_RENDER_BALANCE_FAIL focus={f} review={r}')
async def render(h,o):
 from playwright.async_api import async_playwright
 pdf=m.m.free(o/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V1-SAFEAREA.pdf') if hasattr(m,'m') else m.free(o/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V1-SAFEAREA.pdf')
 png=m.m.free(o/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V1-SAFEAREA.png') if hasattr(m,'m') else m.free(o/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V1-SAFEAREA.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  safe=await p.evaluate('''()=>{const footer=document.querySelector('.footer').getBoundingClientRect(),rows=[...document.querySelectorAll('.practice')].map(x=>x.getBoundingClientRect());const maxBottom=Math.max(...rows.map(r=>r.bottom));const clearance=footer.top-maxBottom;return {ok:clearance>=20,clearance,maxBottom,footerTop:footer.top}}''')
  if not safe['ok']:raise RuntimeError(f"P007_SAFE_AREA_FAIL clearance={safe['clearance']} maxBottom={safe['maxBottom']} footerTop={safe['footerTop']}")
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,safe['clearance']
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();m.m.OUT0.mkdir(parents=True,exist_ok=True) if hasattr(m,'m') else m.OUT0.mkdir(parents=True,exist_ok=True);loader=m.m.kfgloader if hasattr(m,'m') else m.kfgloader;out=m.m.OUT0 if hasattr(m,'m') else m.OUT0;font,src=loader.discover_font(a.font_file,a.font_zip,out);h=out/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V1-SAFEAREA.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,clearance=asyncio.run(render(h,out));print('QJ1_P007_SAD_DAD_SAFEAREA=PASS');print('HISTORICAL_SOURCE=QJ1_P006_V0.2_50_50');print('MATERIAL_NEW=صَ|ضَ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('BOTTOM_GLYPH_OVERFLOW=0');print(f'SAFE_CLEARANCE_PX={clearance}');print('PDF='+str(pdf.relative_to(ROOT)))
