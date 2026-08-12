#!/usr/bin/env python3
# QURBATA Jilid 1 P008 — طَ ظَ; content-verified standalone page over stable P004 shell.
from pathlib import Path
import importlib.util, argparse, asyncio, sys
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v19_kfgqpc as kfgloader
BASE=ROOT/'tools/render_qurbata_jilid1_p004_clean_v1.py'
spec=importlib.util.spec_from_file_location('p004shell',BASE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
OUT=ROOT/'dist/qurbata-print-ready/jilid-1/pages/P008'
FOCUS={'طَ','ظَ'}
REVIEW={'ءَ','أَ','بَ','تَ','ثَ','جَ','حَ','خَ','دَ','ذَ','رَ','زَ','سَ','شَ','صَ','ضَ'}
EXERCISES=['طَ ءَ','ظَ أَ','طَ بَ','ظَ تَ','ثَ طَ','جَ ظَ','حَ طَ','خَ ظَ','طَ دَ طَ','ظَ ذَ ظَ','طَ رَ طَ','ظَ زَ ظَ','طَ سَ طَ','ظَ شَ ظَ','طَ صَ طَ','ظَ ضَ ظَ','ءَ طَ ءَ','أَ ظَ أَ','بَ طَ بَ','تَ ظَ تَ','ثَ طَ ثَ','جَ ظَ جَ','حَ طَ حَ','خَ ظَ خَ']

def audit():
    rendered=EXERCISES[:-1];ts=[x for e in rendered for x in e.split()];f=sum(x in FOCUS for x in ts);r=len(ts)-f
    if len(EXERCISES)!=24 or len(rendered)!=23 or len(ts)!=61: raise RuntimeError('P008_SOURCE_COUNT_FAIL')
    if any(x not in FOCUS|REVIEW for x in ts): raise RuntimeError('P008_WHITELIST_FAIL')
    if (f,r)!=(31,30): raise RuntimeError(f'P008_RENDER_BALANCE_FAIL focus={f} review={r}')
    if any(not (set(e.split()) & FOCUS) for e in EXERCISES[:8]): raise RuntimeError('P008_FIRST_TWO_ROWS_MISSING_FOCUS')

def doc(font_uri):
    # Critical: inject P008 exercises into the shell BEFORE HTML is built.
    m.EXERCISES=EXERCISES
    s=m.doc(font_uri)
    s=s.replace('<div class="pageno">04</div>','<div class="pageno">08</div>')
    s=s.replace('<section class="presentation"><span>دَ</span><span>ذَ</span></section>','<section class="presentation"><span>طَ</span><span>ظَ</span></section>')
    # Same accepted 40pt + group spacing; compress vertical allocation only for safe area.
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
    raise RuntimeError('P008_NO_FREE_OUTPUT')

async def render(h):
    pdf=free(OUT/'QURBATA-JILID-1-P008-TA-ZA-CANDIDATE-V5-CONTENT-VERIFIED.pdf')
    png=free(OUT/'QURBATA-JILID-1-P008-TA-ZA-CANDIDATE-V5-CONTENT-VERIFIED.png')
    expected=EXERCISES[:-1]
    async with async_playwright() as pw:
        b=await pw.chromium.launch();p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(h.resolve().as_uri(),wait_until='networkidle');await p.evaluate('document.fonts.ready')
        if not await p.evaluate("()=>document.fonts.check('40pt \"QURBATA KFGQPC Uthman Taha\"','طَ ظَ')"): raise RuntimeError('P008_FONT_BINDING_FAIL')
        visible=await p.locator('.practice').evaluate_all("els=>els.map(e=>[...e.querySelectorAll('.run > span')].map(x=>x.textContent.trim()).join(' '))")
        if visible!=expected: raise RuntimeError(f'P008_RENDERED_CONTENT_MISMATCH visible={visible} expected={expected}')
        first8=visible[:8]
        if any(('طَ' not in x and 'ظَ' not in x) for x in first8): raise RuntimeError(f'P008_FIRST_TWO_ROWS_VISUAL_FOCUS_FAIL={first8}')
        geom=await p.evaluate("""()=>{const sp=document.querySelector('.bottom-safe-spacer').getBoundingClientRect(),boxes=[...document.querySelectorAll('.practice')].map(e=>e.getBoundingClientRect());const maxBottom=Math.max(...boxes.map(x=>x.bottom));const rows2=[...document.querySelectorAll('.r2')],rows3=[...document.querySelectorAll('.r3')];const gap=(rows)=>Math.min(...rows.flatMap(row=>{const cs=[...row.children].map(c=>c.getBoundingClientRect()).sort((a,b)=>a.left-b.left);return cs.slice(1).map((c,i)=>c.left-cs[i].right)}));return {ok:maxBottom<=sp.top&&sp.top-maxBottom>=6,g2:gap(rows2),g3:gap(rows3),clearance:sp.top-maxBottom,count:boxes.length}}""")
        if not geom['ok']: raise RuntimeError(f'P008_SAFE_AREA_FAIL {geom}')
        if geom['count']!=23: raise RuntimeError(f"P008_OBJECT_COUNT_FAIL={geom['count']}")
        if geom['g2']<30 or geom['g3']<30: raise RuntimeError(f'P008_GROUP_GAP_TOO_SMALL g2={geom["g2"]} g3={geom["g3"]}')
        await p.screenshot(path=str(png),full_page=True);await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await b.close()
    return pdf,geom

if __name__=='__main__':
    audit();ap=argparse.ArgumentParser();ap.add_argument('--font-file');ap.add_argument('--font-zip');a=ap.parse_args();OUT.mkdir(parents=True,exist_ok=True)
    font,src=kfgloader.discover_font(a.font_file,a.font_zip,OUT);h=OUT/'QURBATA-JILID-1-P008-TA-ZA-CANDIDATE-V5-CONTENT-VERIFIED.html';h.write_text(doc(font.resolve().as_uri()),encoding='utf-8');pdf,g=asyncio.run(render(h))
    print('QJ1_P008_TA_ZA_CONTENT_VERIFIED=PASS');print('MATERIAL_NEW=طَ|ظَ');print('FIRST_TWO_ROWS=طَ|ظَ_FOCUS_VERIFIED');print('RENDERED_CONTENT_MATCH=23_OF_23');print('PRACTICE_FONT_PT=40');print('GROUP_SPACING=PRESERVED');print('RENDER_BALANCE=31_FOCUS|30_REVIEW');print('BOTTOM_GLYPH_OVERFLOW=0');print('SAFE_CLEARANCE_PX='+str(round(g['clearance'],2)));print('PDF='+str(pdf.relative_to(ROOT)))
