#!/usr/bin/env python3
# QURBATA Jilid 1 P005 — رَ زَ split from historical P004; uses P004 renderer shell.
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'tools/render_qurbata_jilid1_p004_clean_v1.py'
spec=importlib.util.spec_from_file_location('p004',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.OUT0=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P005'
m.FOCUS={'رَ','زَ'}
m.REVIEW=['ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ']
m.EXERCISES=['رَ ءَ','زَ أَ','رَ بَ','زَ تَ','رَ ثَ','زَ جَ','رَ حَ','زَ خَ','رَ زَ رَ','دَ رَ ذَ','زَ رَ زَ','ءَ زَ أَ','رَ رَ زَ','بَ رَ تَ','زَ زَ رَ','ثَ زَ جَ','رَ حَ زَ','خَ رَ دَ','زَ ذَ رَ','ءَ زَ بَ','رَ تَ زَ','ثَ رَ جَ','زَ حَ رَ','خَ زَ دَ']
# Replace page-specific document strings while preserving the frozen visual shell.
_old_doc=m.doc
def doc(u):
 s=_old_doc(u)
 s=s.replace('<div class="pageno">04</div>','<div class="pageno">05</div>')
 s=s.replace('<section class="presentation"><span>دَ</span><span>ذَ</span></section>','<section class="presentation"><span>رَ</span><span>زَ</span></section>')
 return s
m.doc=doc
def audit():
 ts=[x for e in m.EXERCISES for x in e.split()];allowed=m.FOCUS|set(m.REVIEW)
 if len(m.EXERCISES)!=24 or len(ts)!=64 or any(x not in allowed for x in ts):raise RuntimeError('P005_SOURCE_AUDIT_FAIL')
 if sum(x in m.FOCUS for x in ts)!=32:raise RuntimeError('P005_FOCUS_NOT_32')
async def render(h,o):
 from playwright.async_api import async_playwright
 pdf=m.free(o/'QURBATA-JILID-1-P005-RA-ZAY-CANDIDATE-V1.pdf');png=m.free(o/'QURBATA-JILID-1-P005-RA-ZAY-CANDIDATE-V1.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready');await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 import argparse,asyncio
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();m.OUT0.mkdir(parents=True,exist_ok=True);font,src=m.kfgloader.discover_font(a.font_file,a.font_zip,m.OUT0);h=m.OUT0/'QURBATA-JILID-1-P005-RA-ZAY-CANDIDATE-V1.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h,m.OUT0));print('QJ1_P005_RA_ZAY=PASS');print('MATERIAL_NEW=رَ|زَ');print('PDF='+str(pdf.relative_to(ROOT)))
