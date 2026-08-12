#!/usr/bin/env python3
# QURBATA Jilid 1 P006 — سَ شَ, shifted from historical QJ1-P005 after P004 split.
from pathlib import Path
import importlib.util, argparse, asyncio
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'tools/render_qurbata_jilid1_p004_clean_v1.py'
spec=importlib.util.spec_from_file_location('p004shell',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.OUT0=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P006'
m.FOCUS={'سَ','شَ'}
m.REVIEW=['ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ']
m.EXERCISES=['سَ ءَ','شَ أَ','سَ بَ','شَ تَ','ثَ سَ','جَ شَ','حَ سَ','خَ شَ','سَ دَ سَ','شَ ذَ شَ','سَ رَ سَ','شَ زَ شَ','سَ ءَ سَ','شَ أَ شَ','سَ بَ سَ','شَ تَ شَ','ثَ سَ ثَ','جَ شَ جَ','حَ سَ حَ','خَ شَ خَ','دَ سَ دَ','ذَ شَ ذَ','رَ سَ رَ','زَ شَ زَ']
_old_doc=m.doc
def doc(u):
 s=_old_doc(u)
 s=s.replace('<div class="pageno">04</div>','<div class="pageno">06</div>')
 s=s.replace('<section class="presentation"><span>دَ</span><span>ذَ</span></section>','<section class="presentation"><span>سَ</span><span>شَ</span></section>')
 return s
def audit():
 rendered=m.EXERCISES[:-1];ts=[x for e in rendered for x in e.split()];allowed=m.FOCUS|set(m.REVIEW);f=sum(x in m.FOCUS for x in ts);r=len(ts)-f
 if len(m.EXERCISES)!=24 or len(rendered)!=23 or len(ts)!=61 or any(x not in allowed for x in ts):raise RuntimeError('P006_SOURCE_AUDIT_FAIL')
 if (f,r)!=(31,30):raise RuntimeError(f'P006_RENDER_BALANCE_FAIL focus={f} review={r}')
async def render(h,o):
 from playwright.async_api import async_playwright
 pdf=m.free(o/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V1.pdf');png=m.free(o/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V1.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();m.OUT0.mkdir(parents=True,exist_ok=True);font,src=m.kfgloader.discover_font(a.font_file,a.font_zip,m.OUT0);h=m.OUT0/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V1.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h,m.OUT0));print('QJ1_P006_SIN_SHIN=PASS');print('HISTORICAL_SOURCE=QJ1_P005_V0.2_50_50');print('MATERIAL_NEW=سَ|شَ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('PDF='+str(pdf.relative_to(ROOT)))
