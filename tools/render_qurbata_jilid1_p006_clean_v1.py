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
 # A5 vertical budget: previous shell used 158mm grid and exceeded the physical page.
 # Keep all Arabic base glyphs and combining marks safely above the footer/page edge.
 s=s.replace('.grid{height:158mm;', '.grid{height:151mm;flex:0 0 151mm;')
 s=s.replace('row-gap:3.2mm', 'row-gap:2.2mm')
 return s
def audit():
 rendered=m.EXERCISES[:-1];ts=[x for e in rendered for x in e.split()];allowed=m.FOCUS|set(m.REVIEW);f=sum(x in m.FOCUS for x in ts);r=len(ts)-f
 if len(m.EXERCISES)!=24 or len(rendered)!=23 or len(ts)!=61 or any(x not in allowed for x in ts):raise RuntimeError('P006_SOURCE_AUDIT_FAIL')
 if (f,r)!=(31,30):raise RuntimeError(f'P006_RENDER_BALANCE_FAIL focus={f} review={r}')
async def render(h,o):
 from playwright.async_api import async_playwright
 pdf=m.free(o/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V2-SAFEAREA.pdf');png=m.free(o/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V2-SAFEAREA.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  # Reject any practice glyph box that reaches the footer or physical page edge.
  safe=await p.evaluate('''()=>{const page=document.querySelector('.page').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect();const bad=[...document.querySelectorAll('.practice')].filter(x=>{const r=x.getBoundingClientRect();return r.bottom>=footer.top||r.bottom>page.bottom});return {ok:bad.length===0,bad:bad.length,pageBottom:page.bottom,footerTop:footer.top}}''')
  if not safe['ok']:raise RuntimeError(f"P006_SAFE_AREA_FAIL bad={safe['bad']} footerTop={safe['footerTop']} pageBottom={safe['pageBottom']}")
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();m.OUT0.mkdir(parents=True,exist_ok=True);font,src=m.kfgloader.discover_font(a.font_file,a.font_zip,m.OUT0);h=m.OUT0/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V2-SAFEAREA.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf=asyncio.run(render(h,m.OUT0));print('QJ1_P006_SIN_SHIN_SAFEAREA=PASS');print('MATERIAL_NEW=سَ|شَ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('GRID_HEIGHT_MM=151');print('ROW_GAP_MM=2.2');print('BOTTOM_GLYPH_OVERFLOW=0');print('PDF='+str(pdf.relative_to(ROOT)))
