#!/usr/bin/env python3
"""QURBATA Jilid 2 P022 — mad-alif transfer review using only 3/4/5-letter words that retain mad alif."""
from __future__ import annotations
import csv,json,sys,unicodedata
from collections import Counter
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P022-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P022-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P022-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P022_REGISTRY_INVALID')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}; FORBIDDEN_MARKS=set('ًٌٍّْ')
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
def has_mad_alif(word):
    chars=list(word)
    return any(ch=='ا' and i>=2 and chars[i-1]=='َ' for i,ch in enumerate(chars))
lengths=Counter()
for r in lex:
    b=bases(r['word']); n=len(b); lengths[n]+=1
    if n not in (3,4,5): raise ValueError('P022_LENGTH_CLASS_FAIL='+repr(r))
    if str(n)!=r['length_class']: raise ValueError('P022_LENGTH_METADATA_FAIL='+repr(r))
    if not r['meaning_id'].strip() or r['lexical_status']!='CURATED' or r['competency_status']!='ALLOWED' or r['function']!='MUROJAAH': raise ValueError('P022_SEMANTIC_STATUS_FAIL='+repr(r))
    if not has_mad_alif(r['word']): raise ValueError('P022_MAD_ALIF_REQUIRED='+repr(r))
    if any(m in r['word'] for m in FORBIDDEN_MARKS): raise ValueError('P022_UPPER_COMPETENCY_MARK_LEAKAGE='+repr(r))
if lengths!={3:12,4:10,5:10}: raise ValueError('P022_LENGTH_DISTRIBUTION_FAIL='+repr(dict(lengths)))
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''.presentation-object{font-size:44pt}.j2-glyph{font-size:39pt}.mad-transfer{display:inline-block;direction:rtl;unicode-bidi:isolate;font-family:"QURBATA KFGQPC Uthman Taha Naskh",serif!important;font-feature-settings:"mark" 1,"mkmk" 1}'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">22</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres='''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part mad-transfer" lang="ar">تَعَاوَنَ</span><span class="arrow">←</span><span class="arabic-part mad-transfer" lang="ar">كَاتَبَ</span><span class="arrow">←</span><span class="arabic-part mad-transfer" lang="ar">قَالَ</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P022-V1.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=32: raise RuntimeError('P022_OBJECT_COUNT_INVALID')
        if (await page.locator('.page-number').inner_text()).strip()!='22': raise RuntimeError('P022_PAGE_IDENTITY_FAIL')
        fam=await page.locator('.mad-transfer').first.evaluate("e=>getComputedStyle(e).fontFamily")
        if 'QURBATA KFGQPC Uthman Taha Naskh' not in fam: raise RuntimeError('P022_FONT_BINDING_FAIL='+repr(fam))
        metrics,issues=await p001.fit_and_inspect(page); report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P022_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-022.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P022-V1-KFGQPC-MAD-ALIF-TRANSFER-3-5.pdf'; await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render
def main():
    rc=v22.main(); print('JILID2_P022_RENDERER_V1=PASS'); print('PAGE=22'); print('UNIT_TYPE=MAD_ALIF_TRANSFER_MUROJAAH'); print('ALL_OBJECTS_RETAIN_MAD_ALIF=YES'); print('SHORT_THREE_LETTER_WITHOUT_MAD=0'); print('WORD_LENGTH_3_COUNT=12'); print('WORD_LENGTH_4_COUNT=10'); print('WORD_LENGTH_5_COUNT=10'); print('PRACTICE_OBJECTS=32'); print('MEANINGFUL_WORDS=32'); print('UPPER_COMPETENCY_MARKS=SUKUN|TANWIN|SHADDA_FORBIDDEN'); print('ARABIC_FONT_PRIMARY=QURBATA KFGQPC Uthman Taha Naskh'); print('FONT_BINDING_GATE=PASS'); print('STATUS=P022_MAD_ALIF_TRANSFER_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
