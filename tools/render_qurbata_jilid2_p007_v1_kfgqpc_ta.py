#!/usr/bin/env python3
"""QURBATA Jilid 2 P007 — acquisition of ط with cumulative P001-P006 review."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001

MAP=ROOT/'content/qwo/registry/JILID-2-P007-COMPETENCY-MAP-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P007-V1.csv'
LEX=ROOT/'content/qwo/registry/JILID-2-P007-LEXICAL-FOUNDATION-V1.csv'
SEMANTIC_POLICY=ROOT/'content/qwo/policies/JILID-2-THREE-LETTER-SEMANTIC-LEXEME-POLICY-V1.md'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10: raise ValueError('P007_MICRO_STAIRS_INVALID')
if len(lex)!=32: raise ValueError('P007_LEXICAL_COUNT_INVALID')
if any(r['competency_status']!='ALLOWED' for r in lex): raise ValueError('P007_LEXICAL_COMPETENCY_NOT_ALLOWED')
if not SEMANTIC_POLICY.is_file(): raise ValueError('THREE_LETTER_SEMANTIC_POLICY_MISSING')

ARABIC_MARKS=set(chr(c) for c in range(0x064B,0x0660)) | {'ـ'}
def base_letters(s:str)->str:
    return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in ARABIC_MARKS and unicodedata.category(ch)!='Mn')

semantic_issues=[]
for r in lex:
    bases=base_letters(r['word']); meaning=(r.get('meaning_id') or '').strip()
    if len(bases)!=3: semantic_issues.append((r['slot'],r['word'],'BASE_LETTER_COUNT_'+str(len(bases))))
    if not meaning: semantic_issues.append((r['slot'],r['word'],'MISSING_MEANING'))
    if (r.get('lexical_status') or '').strip() not in {'CURATED','VERIFIED','MEANING_VERIFIED'}:
        semantic_issues.append((r['slot'],r['word'],'LEXICAL_STATUS_NOT_ACCEPTED'))
if semantic_issues: raise ValueError('P007_THREE_LETTER_SEMANTIC_GATE_FAIL='+repr(semantic_issues))

# Through P007 acquired joining letters are ب ت ث ج ح خ س ش ص ض ط; nonjoiners ا د ذ ر ز و are review.
p001.MICRO=MICRO
p001.P001_BANNED_JOINING=set('ظعغفقكلمنيه')
words=[r['word'] for r in lex]
p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''.presentation-object{font-size:46pt}.j2-glyph{font-size:42pt}'''
_original_build=p001.build_page_html

def build_p007(debug:bool):
    h=_original_build(debug)
    h=h.replace('<div class="page-number">01</div>','<div class="page-number">07</div>',1)
    start=h.index('<section class="presentation">'); end=h.index('</section>',start)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">{p001.arabic_html('رَطُبَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('بَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('طُ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('رَ')}</span></div></div></section>'''
    h=h[:start]+pres+h[end:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    targets=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+targets+h[te:]
p001.build_page_html=build_p007

async def render_p007(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P007-V1.json'; png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(); page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready')
        count=await page.locator('.j2-object').count()
        if count!=32: raise RuntimeError(f'P007_OBJECT_COUNT_INVALID actual={count} expected=32')
        metrics,layout_issues=await p001.fit_and_inspect(page)
        report.write_text(json.dumps(layout_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if layout_issues:
            kinds={}
            for x in layout_issues:kinds[x['kind']]=kinds.get(x['kind'],0)+1
            raise RuntimeError('P007_LAYOUT_ISSUES='+str(len(layout_issues))+' TYPES='+','.join(f'{k}:{v}' for k,v in sorted(kinds.items()))+f' REPORT={report}')
        await page.screenshot(path=str(png/'page-007.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P007-V1-KFGQPC-TA-CUMULATIVE.pdf'
        await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await browser.close()
    return metrics,report,pdf
p001.render=render_p007

def main():
    leaks=[]
    for r in lex:
        hit=p001.P001_BANNED_JOINING.intersection(r['word'])
        if hit: leaks.append((r['word'],''.join(sorted(hit))))
    if leaks: raise ValueError('P007_COMPETENCY_LEAKAGE='+repr(leaks))
    current=[r for r in lex if r['function']=='CURRENT']
    missing=[r['word'] for r in current if 'ط' not in base_letters(r['word'])]
    if missing: raise ValueError('P007_CURRENT_OBJECT_MISSING_TA='+repr(missing))
    required_harakat={'َ':'FATHA','ِ':'KASRA','ُ':'DAMMA'}
    all_text=''.join(r['word'] for r in lex)
    harakat_counts={name:all_text.count(mark) for mark,name in required_harakat.items()}
    missing_harakat=[name for name,count in harakat_counts.items() if count==0]
    if missing_harakat: raise ValueError('P007_CUMULATIVE_HARAKAT_MISSING='+repr(missing_harakat))
    rc=v22.main()
    n=sum(1 for r in lex if len(base_letters(r['word']))==3); m=sum(1 for r in lex if len(base_letters(r['word']))==3 and r['meaning_id'].strip())
    review=sum(1 for r in lex if r['function']=='MUROJAAH')
    print('JILID2_P007_RENDERER_V1=PASS'); print('PAGE=7')
    print(f"COMPETENCY={meta['CompetencyCode']}|{meta['Competency']}")
    print(f"UNIT_COMPETENCY={meta['UnitCompetencyCode']}|{meta['UnitCompetency']}")
    print(f"SUBCOMPETENCY={meta['SubCompetencyCode']}|{meta['SubCompetency']}")
    print(f"UNIT_MUROJAAH={meta['UnitMurojaahCode']}|{meta['UnitMurojaah']}")
    print(f"STAIR_RANGE={stairs[0]['StairCode']}-{stairs[-1]['StairCode']}")
    print('ACQUISITION_LETTERS=ط'); print('REVIEW_LETTERS=ب|ت|ث|ج|ح|خ|س|ش|ص|ض|ا|د|ذ|ر|ز|و')
    print('CUMULATIVE_HARAKAT=FATHA|KASRA|DAMMA')
    print('HARAKAT_FATHA_COUNT='+str(harakat_counts['FATHA'])); print('HARAKAT_KASRA_COUNT='+str(harakat_counts['KASRA'])); print('HARAKAT_DAMMA_COUNT='+str(harakat_counts['DAMMA']))
    print('CUMULATIVE_COMPETENCY_P001_P006=PRESERVED')
    print('PRACTICE_OBJECTS=32'); print(f'CURRENT_LEXICAL_OBJECTS={len(current)}'); print(f'MUROJAAH_LEXICAL_OBJECTS={review}')
    print('THREE_LETTER_SEMANTIC_POLICY=REQUIRED'); print(f'THREE_LETTER_OBJECTS={n}'); print(f'THREE_LETTER_WITH_MEANING={m}'); print(f'MEANINGLESS_THREE_LETTER_OBJECTS={n-m}')
    print('COMPETENCY_LEAKAGE=0'); print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh'); print('PRACTICE_FONT_SIZE=42PT'); print('PRESENTATION_FONT_SIZE=46PT'); print('STATUS=P007_CUMULATIVE_CANDIDATE_NOT_FROZEN')
    return rc
if __name__=='__main__': raise SystemExit(main())
