#!/usr/bin/env python3
"""QURBATA Jilid 2 P015 — acquisition of م with cumulative P001-P014 review."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P015-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P015-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P015-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P015_REGISTRY_INVALID')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
for r in lex:
    if len(bases(r['word']))!=3 or not r['meaning_id'].strip() or r['lexical_status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P015_SEMANTIC_GATE_FAIL='+repr(r))
p001.MICRO=MICRO
# Future letters after mim: ن ه ي; ظ remains not yet acquired.
p001.P001_BANNED_JOINING=set('ظنهي')
words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''.presentation-object{font-size:46pt}.j2-glyph{font-size:42pt}'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">15</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">{p001.arabic_html('مَلَكَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('لَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('مَ')}</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P015-V1.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=32: raise RuntimeError(f'P015_OBJECT_COUNT_INVALID actual={count} expected=32')
        metrics,issues=await p001.fit_and_inspect(page)
        report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P015_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        page_no=(await page.locator('.page-number').inner_text()).strip()
        if page_no!='15': raise RuntimeError('P015_PAGE_IDENTITY_FAIL actual='+repr(page_no))
        await page.screenshot(path=str(png/'page-015.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P015-V1-KFGQPC-MIM-CUMULATIVE.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render

def main():
    leaks=[]
    for r in lex:
        hit=p001.P001_BANNED_JOINING.intersection(bases(r['word']))
        if hit: leaks.append((r['word'],''.join(sorted(hit))))
    if leaks: raise ValueError('P015_COMPETENCY_LEAKAGE='+repr(leaks))
    current=[r for r in lex if r['function']=='CURRENT']; missing=[r['word'] for r in current if 'م' not in bases(r['word'])]
    if missing: raise ValueError('P015_CURRENT_OBJECT_MISSING_MIM='+repr(missing))
    text=''.join(r['word'] for r in lex); counts={'FATHA':text.count('َ'),'KASRA':text.count('ِ'),'DAMMA':text.count('ُ')}
    if counts['KASRA']<10 or counts['DAMMA']<10: raise ValueError('P015_HARAKAT_BALANCE_FAIL='+repr(counts))
    rc=v22.main()
    print('JILID2_P015_RENDERER_V1=PASS'); print('PAGE=15'); print('PAGE_IDENTITY_GATE=15'); print(f"COMPETENCY={meta['CompetencyCode']}|{meta['Competency']}"); print(f"UNIT_COMPETENCY={meta['UnitCompetencyCode']}|{meta['UnitCompetency']}"); print(f"UNIT_MUROJAAH={meta['UnitMurojaahCode']}|{meta['UnitMurojaah']}"); print(f"STAIR_RANGE={stairs[0]['StairCode']}-{stairs[-1]['StairCode']}"); print('ACQUISITION_LETTERS=م'); print('CUMULATIVE_HARAKAT=FATHA|KASRA|DAMMA'); print('HARAKAT_FATHA_COUNT='+str(counts['FATHA'])); print('HARAKAT_KASRA_COUNT='+str(counts['KASRA'])); print('HARAKAT_DAMMA_COUNT='+str(counts['DAMMA'])); print('HARAKAT_BALANCE_GATE=KASRA>=10|DAMMA>=10'); print('CUMULATIVE_COMPETENCY_P001_P014=PRESERVED'); print('PRACTICE_OBJECTS=32'); print('CURRENT_LEXICAL_OBJECTS='+str(len(current))); print('MUROJAAH_LEXICAL_OBJECTS='+str(32-len(current))); print('THREE_LETTER_WITH_MEANING=32'); print('MEANINGLESS_THREE_LETTER_OBJECTS=0'); print('COMPETENCY_LEAKAGE=0'); print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh'); print('STATUS=P015_CUMULATIVE_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
