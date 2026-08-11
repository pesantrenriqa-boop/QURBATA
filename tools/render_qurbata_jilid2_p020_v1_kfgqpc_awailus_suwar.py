#!/usr/bin/env python3
"""QURBATA Jilid 2 P020 — Awailus Suwar I, harakat names, and bare-letter name review."""
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
aw=[r for r in rows if r['object_type']=='QURANIC_OPENING']; har=[r for r in rows if r['object_type']=='HARAKAT_SYMBOL']; letters=[r for r in rows if r['object_type']=='HURUF_BARE']
if [r['text'] for r in aw] != ['الم','الر','المر','المص','طه','طسم','طس']: raise ValueError('P020_AWAILUS_SUWAR_SET_INVALID')
if [r['meaning_id'] for r in har] != ['Fathah','Kasrah','Dhammah']: raise ValueError('P020_HARAKAT_NAME_SET_INVALID')
if len(letters)!=22 or any(any(ch in r['text'] for ch in 'ًٌٍَُِّْ') for r in letters): raise ValueError('P020_BARE_LETTER_GATE_FAIL')
for r in rows:
    if r['status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P020_STATUS_GATE_FAIL='+repr(r))
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set()
texts=[r['text'] for r in rows]; p001.P001_ROWS=[texts[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''
.presentation-object{font-size:42pt}.j2-glyph{font-size:40pt}
.p020-section-label{font-family:Arial,sans-serif;font-size:8pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#555;text-align:center;margin:1mm 0 .5mm}
.p020-harakat-names{display:flex;justify-content:center;gap:8mm;align-items:center;font-family:Arial,sans-serif;font-size:10pt;font-weight:700;margin-top:1mm}
.p020-harakat-names b{font-family:"KFGQPC Uthman Taha Naskh",serif;font-size:28pt;font-weight:400;margin-right:2mm}
'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">20</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres='''<section class="presentation"><div class="p020-section-label">Awailus Suwar</div><div class="presentation-object-wrap"><div class="presentation-object" dir="rtl"><span lang="ar">الم</span> &nbsp; <span lang="ar">الر</span> &nbsp; <span lang="ar">المر</span> &nbsp; <span lang="ar">المص</span> &nbsp; <span lang="ar">طه</span> &nbsp; <span lang="ar">طسم</span> &nbsp; <span lang="ar">طس</span></div></div><div class="p020-section-label">Nama Harakat</div><div class="p020-harakat-names"><span><b>َ</b>Fathah</span><span><b>ِ</b>Kasrah</span><span><b>ُ</b>Dhammah</span></div><div class="p020-section-label">Murojaah Nama Huruf — tanpa harakat</div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P020-V2.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=32: raise RuntimeError('P020_OBJECT_COUNT_INVALID')
        if (await page.locator('.page-number').inner_text()).strip()!='20': raise RuntimeError('P020_PAGE_IDENTITY_FAIL')
        metrics,issues=await p001.fit_and_inspect(page); report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P020_LAYOUT_ISSUES='+str(len(issues)))
        await page.screenshot(path=str(png/'page-020.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P020-V2-KFGQPC-MILESTONE-REVIEW.pdf'; await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render
def main():
    rc=v22.main(); print('JILID2_P020_RENDERER_V2=PASS'); print('PAGE=20'); print('PAGE_IDENTITY_GATE=20'); print('NEW_LETTER_ACQUISITION=NONE'); print('P020_BLOCK_1=AWAILUS_SUWAR_I'); print('AWAILUS_SUWAR_PATTERNS=الم|الر|المر|المص|طه|طسم|طس'); print('P020_BLOCK_2=HARAKAT_NAMES'); print('HARAKAT_NAMES=FATHAH|KASRAH|DHAMMAH'); print('P020_BLOCK_3=BARE_LETTER_NAME_REVIEW'); print('BARE_LETTERS_WITH_HARAKAT=0'); print('CONNECTED_HARAKAT_LEXICAL_EXAMPLES=0'); print('CUMULATIVE_COMPETENCY_P001_P019=PRESERVED'); print('STATUS=P020_MILESTONE_REVIEW_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
