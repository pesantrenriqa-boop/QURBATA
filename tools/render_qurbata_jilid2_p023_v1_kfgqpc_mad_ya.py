#!/usr/bin/env python3
"""QURBATA Jilid 2 P023 — K2 U02 pure acquisition of mad ya."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P023-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P023-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P023-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P023_REGISTRY_INVALID')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}; FORBIDDEN_MARKS=set('ًٌٍّْ')
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
def has_mad_ya(word):
    chars=list(word)
    return any(ch=='ي' and i>=1 and chars[i-1]=='ِ' for i,ch in enumerate(chars))
for r in lex:
    n=len(bases(r['word']))
    if n<3 or n>5 or not r['meaning_id'].strip() or r['lexical_status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P023_SEMANTIC_GATE_FAIL='+repr(r))
    if r['function']!='CURRENT': raise ValueError('P023_MIXED_REVIEW_FORBIDDEN='+repr(r))
    if not has_mad_ya(r['word']): raise ValueError('P023_MAD_YA_REQUIRED='+repr(r))
    if any(m in r['word'] for m in FORBIDDEN_MARKS): raise ValueError('P023_UPPER_COMPETENCY_MARK_LEAKAGE='+repr(r))
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''.presentation-object{font-size:46pt}.j2-glyph{font-size:42pt}.mad-unit{display:inline-block;direction:rtl;unicode-bidi:isolate;font-family:"QURBATA KFGQPC Uthman Taha Naskh",serif!important;font-feature-settings:"mark" 1,"mkmk" 1}'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">23</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres='''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">بِيعَ</span><span class="arrow">←</span><span class="arabic-part mad-unit" lang="ar">بِي</span><span class="arrow">←</span><span class="arabic-part" lang="ar">بِ</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P023-V1.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=32: raise RuntimeError('P023_OBJECT_COUNT_INVALID')
        if (await page.locator('.page-number').inner_text()).strip()!='23': raise RuntimeError('P023_PAGE_IDENTITY_FAIL')
        family=await page.locator('.mad-unit').evaluate("e=>getComputedStyle(e).fontFamily")
        if 'QURBATA KFGQPC Uthman Taha Naskh' not in family: raise RuntimeError('P023_FONT_BINDING_FAIL='+repr(family))
        metrics,issues=await p001.fit_and_inspect(page); report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P023_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-023.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P023-V1-KFGQPC-MAD-YA-FOCUS.pdf'; await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render
def main():
    lengths={3:0,4:0,5:0}
    for r in lex: lengths[len(bases(r['word']))]+=1
    rc=v22.main(); print('JILID2_P023_RENDERER_V1=PASS'); print('PAGE=23'); print('K_SEQUENCE=K2'); print('UK_SEQUENCE=J2.K2.U02'); print('HEADER_SEQUENCE=بِ|بِي|بِيعَ'); print('NEW_COMPETENCY=MAD_YA'); print('MAD_PATTERN=KASRA_PLUS_YA'); print('MAD_LENGTH=2_HARAKAT'); print('CURRENT_OBJECTS=32'); print('MUROJAAH_OBJECTS=0'); print('WORD_LENGTH_3_COUNT='+str(lengths[3])); print('WORD_LENGTH_4_COUNT='+str(lengths[4])); print('WORD_LENGTH_5_COUNT='+str(lengths[5])); print('UPPER_COMPETENCY_MARKS=SUKUN|TANWIN|SHADDA_FORBIDDEN'); print('PREVIOUS_K2_U01_MAD_ALIF=PREREQUISITE_PRESERVED'); print('ARABIC_FONT_PRIMARY=QURBATA KFGQPC Uthman Taha Naskh'); print('FONT_BINDING_GATE=PASS'); print('STATUS=P023_K2_U02_MAD_YA_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
