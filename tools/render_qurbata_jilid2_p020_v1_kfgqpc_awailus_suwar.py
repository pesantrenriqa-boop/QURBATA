#!/usr/bin/env python3
"""QURBATA Jilid 2 P020 — full-page milestone with large KFGQPC typography."""
from __future__ import annotations
import csv,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P020-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P020-V1.csv'; REG=ROOT/'content/qwo/registry/JILID-2-P020-PRACTICE-REGISTRY-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with REG.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
if len(stairs)!=10 or len(rows)!=32: raise ValueError('P020_REGISTRY_INVALID')
aw=[r for r in rows if r['object_type']=='QURANIC_OPENING']; har=[r for r in rows if r['object_type']=='HARAKAT_SYMBOL']
AW_EXPECTED=['الم','الر','المر','المص','طه','طسم','طس']
if [r['text'] for r in aw] != AW_EXPECTED: raise ValueError('P020_AWAILUS_SUWAR_SET_INVALID')
if [r['meaning_id'] for r in har] != ['Fathah','Kasrah','Dhammah']: raise ValueError('P020_HARAKAT_NAME_SET_INVALID')
for r in rows:
    if r['status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P020_STATUS_GATE_FAIL='+repr(r))
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); p001.P001_ROWS=[['ا']]
ARABIC_FONT='QURBATA KFGQPC Uthman Taha Naskh'
p001.P001_CSS += f'''
.presentation{{display:none!important;height:0!important;flex:0 0 0!important;margin:0!important;padding:0!important}}
.j2-grid{{display:block!important;height:151mm!important;flex:0 0 151mm!important;padding:.4mm 0 .2mm!important;overflow:hidden!important;direction:ltr!important;box-sizing:border-box!important}}
.p020-board{{height:100%;display:grid;grid-template-rows:73mm 34mm 39mm;gap:2mm;box-sizing:border-box}}
.p020-block{{box-sizing:border-box;border:.3mm solid rgba(6,77,55,.55);border-radius:2.2mm;padding:1.2mm 1.5mm;overflow:hidden;background:#fff}}
.p020-aw{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:16.2mm;gap:.9mm 1.8mm;align-content:center}}
.p020-aw-cell{{display:flex;align-items:center;justify-content:center;gap:2mm;border-bottom:.18mm dotted rgba(6,77,55,.34);font-family:"{ARABIC_FONT}",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-size:31pt;line-height:.9;white-space:nowrap;min-width:0}}
.p020-aw-cell:last-child{{grid-column:1 / span 2;width:50%;justify-self:center}}
.p020-aw-cell .sep{{font-family:Arial,sans-serif!important;font-size:17pt;color:#555;direction:ltr}}
.p020-aw-cell .split,.p020-aw-cell .joined{{direction:rtl;unicode-bidi:isolate;font-family:"{ARABIC_FONT}",serif!important}}
.p020-aw-cell .joined{{font-size:34pt}}
.p020-harakat{{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));grid-template-rows:repeat(2,1fr);gap:.8mm 1.4mm;align-items:stretch}}
.p020-harakat-cell{{display:flex;flex-direction:column;align-items:center;justify-content:flex-start;font-family:"{ARABIC_FONT}",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-size:36pt;line-height:.74;padding-top:0;min-width:0}}
.p020-harakat-line{{width:82%;height:3.3mm;margin-top:.45mm;border-bottom:.4mm dotted #555}}
.p020-letters{{display:grid;grid-template-columns:repeat(14,minmax(0,1fr));grid-template-rows:repeat(2,1fr);gap:.8mm .4mm;align-items:center;justify-items:center;direction:rtl}}
.p020-letter{{font-family:"{ARABIC_FONT}",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-size:32pt;line-height:.86;direction:rtl;unicode-bidi:isolate}}
'''
orig=p001.build_page_html
def separated(s:str)->str: return ' '.join(list(s))
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">20</div>',1)
    ps=h.index('<section class="presentation">'); pe=h.index('</section>',ps)+len('</section>'); h=h[:ps]+'<section class="presentation"></section>'+h[pe:]
    gs=h.index('<section class="j2-grid">'); ge=h.index('</section>',gs)+len('</section>')
    aw_html=''.join(f'<div class="p020-aw-cell"><span class="split" lang="ar">{separated(x)}</span><span class="sep">=</span><span class="joined" lang="ar">{x}</span></div>' for x in AW_EXPECTED)
    hs=['َ','ِ','ُ','َ','ُ','ِ','ُ','َ','ِ','ِ','َ','ُ']; har_html=''.join(f'<div class="p020-harakat-cell"><span lang="ar">{x}</span><span class="p020-harakat-line"></span></div>' for x in hs)
    all_letters=list('ابتثجحخدذرزسشصضطظعغفقكلمنهوي')
    if len(all_letters)!=28: raise ValueError('P020_ALL_HIJAIYAH_COUNT_INVALID='+str(len(all_letters)))
    letter_html=''.join(f'<span class="p020-letter" lang="ar">{x}</span>' for x in all_letters)
    board=f'''<section class="j2-grid"><div class="p020-board"><div class="p020-block p020-aw">{aw_html}</div><div class="p020-block p020-harakat">{har_html}</div><div class="p020-block p020-letters">{letter_html}</div></div></section>'''; h=h[:gs]+board+h[ge:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    targets=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+targets+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P020-V8.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        if (await page.locator('.page-number').inner_text()).strip()!='20': raise RuntimeError('P020_PAGE_IDENTITY_FAIL')
        if await page.locator('.p020-aw-cell').count()!=7 or await page.locator('.p020-harakat-cell').count()!=12 or await page.locator('.p020-letter').count()!=28: raise RuntimeError('P020_OBJECT_COUNT_FAIL')
        families=await page.evaluate('''()=>[...document.querySelectorAll('.p020-aw-cell,.p020-harakat-cell,.p020-letter')].map(x=>getComputedStyle(x).fontFamily)''')
        if not all('QURBATA KFGQPC Uthman Taha Naskh' in x for x in families): raise RuntimeError('P020_FONT_BINDING_FAIL='+repr(families[:5]))
        issues=await page.evaluate('''()=>{const out=[];const board=document.querySelector('.p020-board'),targets=document.querySelector('.targets');if(board&&targets&&board.getBoundingClientRect().bottom>targets.getBoundingClientRect().top-2)out.push({kind:'P020_BOARD_TARGET_OVERLAP',boardBottom:board.getBoundingClientRect().bottom,targetTop:targets.getBoundingClientRect().top});for(const el of document.querySelectorAll('.p020-block')){if(el.scrollHeight>el.clientHeight+3||el.scrollWidth>el.clientWidth+3)out.push({kind:'P020_BLOCK_OVERFLOW',className:el.className,scrollHeight:el.scrollHeight,clientHeight:el.clientHeight,scrollWidth:el.scrollWidth,clientWidth:el.clientWidth})}return out}''')
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P020_LAYOUT_ISSUES='+str(len(issues))+' DETAILS='+repr(issues)+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-020.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P020-V8-KFGQPC-FULL-PAGE-LARGE.pdf'; await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return {},report,pdf
p001.render=render
def main():
    rc=v22.main(); print('JILID2_P020_RENDERER_V8=PASS'); print('PAGE=20'); print('ARABIC_FONT_PRIMARY=QURBATA KFGQPC Uthman Taha Naskh'); print('FONT_BINDING_GATE=PASS'); print('PAGE_USAGE=FULL_PROPORTIONAL'); print('BLOCK_HEIGHTS_MM=73|34|39'); print('AWAILUS_FONT_SIZE=31PT'); print('AWAILUS_JOINED_FONT_SIZE=34PT'); print('HARAKAT_FONT_SIZE=36PT'); print('BARE_LETTER_FONT_SIZE=32PT'); print('AWAILUS_LAYOUT=2_COLUMNS_PER_ROW'); print('HARAKAT_DRILL_OBJECTS=12'); print('BARE_LETTER_REVIEW_COUNT=28'); print('STATUS=P020_FULL_PAGE_LARGE_REBALANCED_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
