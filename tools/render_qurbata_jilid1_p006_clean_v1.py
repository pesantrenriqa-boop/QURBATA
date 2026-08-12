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
 # True bottom safe zone. Keep 40pt practice glyphs; compress only vertical allocation.
 s=s.replace('.grid{height:158mm;display:grid;', '.grid{height:142mm;flex:0 0 142mm;display:grid;')
 s=s.replace('row-gap:3.2mm', 'row-gap:1.4mm')
 s=s.replace('font:40pt "QURBATA KFGQPC Uthman Taha";white-space:nowrap', 'font:40pt/1 "QURBATA KFGQPC Uthman Taha";white-space:nowrap')
 # Add an explicit spacer between practice and footer so combining marks never touch trim/footer area.
 s=s.replace('</section><footer class="footer">', '</section><div class="bottom-safe-spacer" style="height:8mm;flex:0 0 8mm"></div><footer class="footer">')
 return s
def audit():
 rendered=m.EXERCISES[:-1];ts=[x for e in rendered for x in e.split()];allowed=m.FOCUS|set(m.REVIEW);f=sum(x in m.FOCUS for x in ts);r=len(ts)-f
 if len(m.EXERCISES)!=24 or len(rendered)!=23 or len(ts)!=61 or any(x not in allowed for x in ts):raise RuntimeError('P006_SOURCE_AUDIT_FAIL')
 if (f,r)!=(31,30):raise RuntimeError(f'P006_RENDER_BALANCE_FAIL focus={f} review={r}')
async def render(h,o):
 from playwright.async_api import async_playwright
 pdf=m.free(o/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V3-SAFEAREA.pdf');png=m.free(o/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V3-SAFEAREA.png')
 async with async_playwright() as pw:
  b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
  safe=await p.evaluate('''()=>{const page=document.querySelector('.page').getBoundingClientRect(),footer=document.querySelector('.footer').getBoundingClientRect(),sp=document.querySelector('.bottom-safe-spacer').getBoundingClientRect();const boxes=[...document.querySelectorAll('.practice')].map(x=>x.getBoundingClientRect());const maxBottom=Math.max(...boxes.map(r=>r.bottom));const bad=boxes.filter(r=>r.bottom>sp.top).length;return {ok:bad===0&&maxBottom<=sp.top,bad,maxBottom,safeTop:sp.top,footerTop:footer.top,pageBottom:page.bottom,clearance:sp.top-maxBottom}}''')
  if not safe['ok']:raise RuntimeError(f"P006_SAFE_AREA_FAIL bad={safe['bad']} maxBottom={safe['maxBottom']} safeTop={safe['safeTop']} clearance={safe['clearance']}")
  if safe['clearance'] < 6:raise RuntimeError(f"P006_CLEARANCE_TOO_SMALL px={safe['clearance']}")
  await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
 return pdf,safe
if __name__=='__main__':
 audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();m.OUT0.mkdir(parents=True,exist_ok=True);font,src=m.kfgloader.discover_font(a.font_file,a.font_zip,m.OUT0);h=m.OUT0/'QURBATA-JILID-1-P006-SIN-SHIN-CANDIDATE-V3-SAFEAREA.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,safe=asyncio.run(render(h,m.OUT0));print('QJ1_P006_SIN_SHIN_SAFEAREA=PASS');print('MATERIAL_NEW=سَ|شَ');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('PRACTICE_FONT_PT=40');print('GRID_HEIGHT_MM=142');print('ROW_GAP_MM=1.4');print('BOTTOM_SAFE_SPACER_MM=8');print('BOTTOM_GLYPH_OVERFLOW=0');print('SAFE_CLEARANCE_PX='+str(round(safe['clearance'],2)));print('PDF='+str(pdf.relative_to(ROOT)))
