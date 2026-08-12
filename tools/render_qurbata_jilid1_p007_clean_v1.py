#!/usr/bin/env python3
# QURBATA Jilid 1 P007 — صَ ضَ. Stable production candidate after P001-P006 freeze.
from pathlib import Path
import importlib.util, argparse, asyncio, sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
BASE=ROOT/'tools/render_qurbata_jilid1_p004_clean_v1.py'
spec=importlib.util.spec_from_file_location('p004shell',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P007'
FOCUS={'صَ','ضَ'}
REVIEW={'ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ'}
EXERCISES=['صَ ءَ','ضَ أَ','صَ بَ','ضَ تَ','ثَ صَ','جَ ضَ','حَ صَ','خَ ضَ','صَ دَ صَ','ضَ ذَ ضَ','صَ رَ صَ','ضَ زَ ضَ','صَ سَ صَ','ضَ شَ ضَ','صَ ءَ صَ','ضَ أَ ضَ','بَ صَ بَ','تَ ضَ تَ','ثَ صَ ثَ','جَ ضَ جَ','حَ صَ حَ','خَ ضَ خَ','دَ صَ دَ','ذَ ضَ ذَ']

def audit():
    rendered=EXERCISES[:-1];ts=[x for e in rendered for x in e.split()];f=sum(x in FOCUS for x in ts);r=len(ts)-f
    if len(EXERCISES)!=24 or len(rendered)!=23 or len(ts)!=61: raise RuntimeError('P007_SOURCE_COUNT_FAIL')
    if any(x not in FOCUS|REVIEW for x in ts): raise RuntimeError('P007_WHITELIST_FAIL')
    if (f,r)!=(31,30): raise RuntimeError(f'P007_RENDER_BALANCE_FAIL focus={f} review={r}')

def doc(font_uri):
    m.EXERCISES=EXERCISES
    s=m.doc(font_uri)
    s=s.replace('<div class="pageno">04</div>','<div class="pageno">07</div>')
    s=s.replace('<section class="presentation"><span>دَ</span><span>ذَ</span></section>','<section class="presentation"><span>صَ</span><span>ضَ</span></section>')
    # Frozen visual baseline: keep 40pt practice type and original horizontal group spacing.
    # Only vertical allocation is compressed for a real bottom safe zone.
    s=s.replace('.grid{height:158mm;display:grid;', '.grid{height:142mm;flex:0 0 142mm;display:grid;')
    s=s.replace('row-gap:3.2mm','row-gap:1.4mm')
    s=s.replace('font:40pt "QURBATA KFGQPC Uthman Taha";white-space:nowrap','font:40pt/1 "QURBATA KFGQPC Uthman Taha";white-space:nowrap')
    s=s.replace('</section><footer class="footer">','</section><div class="bottom-safe-spacer" style="height:8mm;flex:0 0 8mm"></div><footer class="footer">')
    return s

def free(base):
    if not base.exists(): return base
    try:
        with open(base,'ab'): pass
        return base
    except PermissionError: pass
    for n in range(1,100):
        p=base.with_name(base.stem+f'-R{n}'+base.suffix)
        if not p.exists(): return p
    raise RuntimeError('P007_NO_FREE_OUTPUT')

async def render(h):
    pdf=free(OUT/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V2-FROZEN-SPACING.pdf')
    png=free(OUT/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V2-FROZEN-SPACING.png')
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        if not await p.evaluate("()=>document.fonts.check('40pt \"QURBATA KFGQPC Uthman Taha\"','صَ ضَ')"): raise RuntimeError('P007_FONT_BINDING_FAIL')
        geom=await p.evaluate("""()=>{const sp=document.querySelector('.bottom-safe-spacer').getBoundingClientRect(),boxes=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect());const maxBottom=Math.max(...boxes.map(x=>x.bottom));const rows2=[...document.querySelectorAll('.r2')],rows3=[...document.querySelectorAll('.r3')];const gap2=rows2.length?parseFloat(getComputedStyle(rows2[0]).gap):0;const gap3=rows3.length?parseFloat(getComputedStyle(rows3[0]).gap):0;return {ok:maxBottom<=sp.top&&sp.top-maxBottom>=6,clearance:sp.top-maxBottom,gap2,gap3,count:boxes.length}}""")
        if not geom['ok']: raise RuntimeError(f'P007_SAFE_AREA_FAIL {geom}')
        if geom['count']!=23: raise RuntimeError(f"P007_OBJECT_COUNT_FAIL={geom['count']}")
        # Explicit guard against the large-type experiment collapsing group spacing.
        if geom['gap2'] < 30 or geom['gap3'] < 30: raise RuntimeError(f'P007_GROUP_GAP_TOO_SMALL gap2={geom["gap2"]} gap3={geom["gap3"]}')
        await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    return pdf,geom

if __name__=='__main__':
    audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True)
    font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P007-SAD-DAD-CANDIDATE-V2-FROZEN-SPACING.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h))
    print('QJ1_P007_SAD_DAD_FROZEN_SPACING=PASS');print('MATERIAL_NEW=صَ|ضَ');print('PRACTICE_FONT_PT=40');print('GROUP_SPACING=PRESERVED');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('BOTTOM_GLYPH_OVERFLOW=0');print('SAFE_CLEARANCE_PX='+str(round(g['clearance'],2)));print('PDF='+str(pdf.relative_to(ROOT)))
