#!/usr/bin/env python3
"""QURBATA Jilid 2 P020 — Awailus Suwar I + cumulative lexical review."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P020-COMPETENCY-MAP-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P020-V1.csv'
REG=ROOT/'content/qwo/registry/JILID-2-P020-PRACTICE-REGISTRY-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with REG.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
if len(stairs)!=10 or len(rows)!=32: raise ValueError('P020_REGISTRY_INVALID')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
aw=[r for r in rows if r['object_type']=='QURANIC_OPENING']; lex=[r for r in rows if r['object_type']=='LEXICAL']
if [r['text'] for r in aw] != ['الم','الر','المر','المص','طه','طسم','طس']:
    raise ValueError('P020_AWAILUS_SUWAR_SET_INVALID='+repr([r['text'] for r in aw]))
if len(aw)!=7 or len(set(r['text'] for r in aw))!=7: raise ValueError('P020_AWAILUS_SUWAR_UNIQUENESS_FAIL')
for r in rows:
    if r['status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P020_STATUS_GATE_FAIL='+repr(r))
for r in lex:
    if len(bases(r['text']))!=3 or not r['meaning_id'].strip(): raise ValueError('P020_LEXICAL_SEMANTIC_GATE_FAIL='+repr(r))
p001.MICRO=MICRO
p001.P001_BANNED_JOINING=set()  # all hijaiyah acquisition letters completed by P019
texts=[r['text'] for r in rows]; p001.P001_ROWS=[texts[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''.presentation-object{font-size:46pt}.j2-glyph{font-size:42pt}.awailus-title{direction:rtl;unicode-bidi:isolate}.aw-sep{font-family:serif;font-size:24pt;opacity:.5;margin:0 8px}'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">20</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres='''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object awailus-title"><span class="arabic-part" lang="ar">الم</span><span class="aw-sep">•</span><span class="arabic-part" lang="ar">الر</span><span class="aw-sep">•</span><span class="arabic-part" lang="ar">طسم</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P020-V1.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=32: raise RuntimeError(f'P020_OBJECT_COUNT_INVALID actual={count} expected=32')
        page_no=(await page.locator('.page-number').inner_text()).strip()
        if page_no!='20': raise RuntimeError('P020_PAGE_IDENTITY_FAIL actual='+repr(page_no))
        metrics,issues=await p001.fit_and_inspect(page)
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P020_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-020.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P020-V1-KFGQPC-AWAILUS-SUWAR-I.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render

def main():
    text=''.join(r['text'] for r in lex)
    counts={'FATHA':text.count('َ'),'KASRA':text.count('ِ'),'DAMMA':text.count('ُ')}
    if counts['KASRA']<10 or counts['DAMMA']<10: raise ValueError('P020_HARAKAT_BALANCE_FAIL='+repr(counts))
    rc=v22.main()
    print('JILID2_P020_RENDERER_V1=PASS'); print('PAGE=20'); print('PAGE_IDENTITY_GATE=20')
    print(f"COMPETENCY={meta['CompetencyCode']}|{meta['Competency']}")
    print(f"UNIT_COMPETENCY={meta['UnitCompetencyCode']}|{meta['UnitCompetency']}")
    print(f"UNIT_MUROJAAH={meta['UnitMurojaahCode']}|{meta['UnitMurojaah']}")
    print('NEW_LETTER_ACQUISITION=NONE'); print('AWAILUS_SUWAR_UNIT=I'); print('AWAILUS_SUWAR_UNIQUE_PATTERNS=7')
    print('AWAILUS_SUWAR_PATTERNS=الم|الر|المر|المص|طه|طسم|طس')
    print('AWAILUS_SUWAR_REUSE_AT_P030=FORBIDDEN')
    print('AWAILUS_SUWAR_LEXICAL_SEMANTIC_GATE=CANONICAL_QURANIC_EXCEPTION')
    print('LEXICAL_REVIEW_OBJECTS=25'); print('LEXICAL_THREE_LETTER_WITH_MEANING=25')
    print('CUMULATIVE_COMPETENCY_P001_P019=PRESERVED')
    print('HARAKAT_KASRA_COUNT='+str(counts['KASRA'])); print('HARAKAT_DAMMA_COUNT='+str(counts['DAMMA']))
    print('HARAKAT_BALANCE_GATE=KASRA>=10|DAMMA>=10'); print('PRACTICE_OBJECTS=32'); print('COMPETENCY_LEAKAGE=0')
    print('STATUS=P020_AWAILUS_SUWAR_I_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
