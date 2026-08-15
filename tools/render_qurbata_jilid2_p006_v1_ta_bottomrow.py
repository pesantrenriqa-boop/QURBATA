#!/usr/bin/env python3
"""QURBATA Jilid 2 P006 — acquisition of ط with continued bottom-row enrichment.

Project lexical gate: a new acquisition letter must have at least 8 CURRENT,
meaningful, curated lexical objects before it may be taught on a page. ظ was
removed from P006 because its safe corpus did not meet this threshold.
"""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001

MAP=ROOT/'content/qwo/registry/JILID-2-P006-COMPETENCY-MAP-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P006-V1.csv'
LEX=ROOT/'content/qwo/registry/JILID-2-P006-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10: raise ValueError('P006_MICRO_STAIRS_INVALID')
if len(lex)!=32: raise ValueError('P006_LEXICAL_COUNT_INVALID')

ARABIC_MARKS=set(chr(c) for c in range(0x064B,0x0660)) | {'ـ'}
def base_letters(s:str)->str:
    return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in ARABIC_MARKS and unicodedata.category(ch)!='Mn')

p001.MICRO=MICRO
p001.P001_BANNED_JOINING=set('ظعغفقكلمنيه')
words=[r['word'] for r in lex[:28]]
p001.P001_ROWS=[words[i:i+4] for i in range(0,28,4)]
p001.P001_CSS += r'''
.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;unicode-bidi:isolate!important;gap:1.7mm!important;}
.presentation-object .arabic-part{direction:rtl!important;unicode-bidi:isolate!important;line-height:1.15!important;padding:.35mm .3mm!important;}
.presentation-object .arrow{direction:ltr!important;unicode-bidi:isolate!important;font-size:15pt!important;}
.j2-glyph{font-size:39pt!important;}
.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;}
.p006-enrichment-row{grid-column:1/-1!important;grid-row:8!important;display:grid!important;grid-template-columns:1fr 1fr!important;gap:10mm!important;padding:.55mm 6mm .35mm!important;border-top:.28mm solid #111!important;box-sizing:border-box!important;background:#fff!important;}
.p006-enrichment-row .micro{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;min-width:0!important;}
.p006-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:6.2pt!important;font-weight:700!important;margin:0 0 .7mm!important;white-space:nowrap!important;}
.glyph-run{display:flex!important;align-items:center!important;justify-content:center!important;gap:1.45mm!important;direction:ltr!important;white-space:nowrap!important;}
.glyph-run.num .eg{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:20pt!important;line-height:1!important;width:4mm!important;text-align:center!important;direction:rtl!important;}
.glyph-run.nonjoin .eg{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:21pt!important;line-height:1!important;width:5mm!important;text-align:center!important;direction:rtl!important;}
'''

_base_build=p001.build_page_html

def build_p006(debug:bool):
    h=_base_build(debug)
    h=h.replace('<div class="page-number">01</div>','<div class="page-number">06</div>',1)
    start=h.index('<section class="presentation">');end=h.index('</section>',start)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('طَ')}</span><span class="arrow" dir="ltr">←</span><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('طَرَبَ')}</span></div></div></section>'''
    h=h[:start]+pres+h[end:]
    ts=h.index('<section class="targets">');te=h.index('</section>',ts)+len('</section>')
    targets=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    h=h[:ts]+targets+h[te:]
    nums=''.join(f'<span class="eg">{x}</span>' for x in '٠١٢٣٤٥٦٧٨٩')
    njs=''.join(f'<span class="eg">{x}</span>' for x in 'ادذرزو')
    enrichment=f'''<div class="p006-enrichment-row" data-enrichment-row="8"><div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="glyph-run num">{nums}</div></div><div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="glyph-run nonjoin">{njs}</div></div></div>'''
    gs=h.find('<section class="j2-grid">');ge=h.find('</section>',gs)
    return h[:ge]+enrichment+h[ge:]

p001.build_page_html=build_p006

async def _write_pdf(page,out:Path):
    names=[out/'QURBATA-JILID-2-P006-V2-TA-LEXICAL-GATE.pdf']+[out/f'QURBATA-JILID-2-P006-V2-TA-LEXICAL-GATE-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
    last=None
    for idx,p in enumerate(names):
        try:
            await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'})
            return p,('DIRECT_P006_V2' if idx==0 else f'LOCK_FALLBACK_P006_V2_{idx:02d}')
        except PermissionError as e:last=e
    raise RuntimeError('P006_NO_AVAILABLE_PDF_NAME') from last

async def render_p006(h:Path,out:Path,debug:bool):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P006-V2.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=28:raise RuntimeError('P006_CORE_OBJECT_COUNT_INVALID')
        metrics,issues=await p001.fit_and_inspect(page)
        extra=await page.evaluate('''()=>{const e=document.querySelector('.p006-enrichment-row'),g=document.querySelector('.j2-grid'),f=document.querySelector('.footer'),out=[];if(!e||!g)return[{kind:'P006_ENRICHMENT_MISSING'}];const er=e.getBoundingClientRect(),gr=g.getBoundingClientRect();if(er.left<gr.left-1||er.right>gr.right+1||er.bottom>gr.bottom+1)out.push({kind:'P006_ENRICHMENT_OUTSIDE_GRID'});if(f&&er.bottom>f.getBoundingClientRect().top-2)out.push({kind:'P006_ENRICHMENT_FOOTER_COLLISION'});return out}''')
        all_issues=[*issues,*extra];report.write_text(json.dumps(all_issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if all_issues:raise RuntimeError('P006_LAYOUT_ISSUES='+repr(all_issues))
        await page.screenshot(path=str(png/'page-006-v2.png'),full_page=True)
        pdf,mode=await _write_pdf(page,out);await browser.close()
    return metrics,report,pdf,mode

p001.render=render_p006

def main():
    current=[r for r in lex if r['function']=='CURRENT']
    current_ta=[r for r in current if 'ط' in base_letters(r['word'])]
    if len(current_ta)<8:raise ValueError(f'P006_LEXICAL_ACQUISITION_GATE_FAIL letter=ط count={len(current_ta)} required=8')
    if any('ظ' in base_letters(r['word']) for r in current):raise ValueError('P006_ZA_FORBIDDEN_UNTIL_LEXICAL_GATE')
    missing=[r['word'] for r in current if 'ط' not in base_letters(r['word'])]
    if missing:raise ValueError('P006_CURRENT_MISSING_TA='+repr(missing))
    leaks=[]
    for r in lex:
        hit=p001.P001_BANNED_JOINING.intersection(base_letters(r['word']))
        if hit:leaks.append((r['word'],''.join(sorted(hit))))
    if leaks:raise ValueError('P006_COMPETENCY_LEAKAGE='+repr(leaks))
    if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P006'])
    rc=v22.main()
    print('JILID2_P006_RENDERER_V2_LEXICAL_GATE=PASS');print('PAGE=6');print('ACQUISITION_LETTERS=ط');print('TITLE_VISUAL_RIGHT_TO_LEFT=طَ←طَرَبَ')
    print('LEXICAL_ACQUISITION_GATE=MIN_8_CURRENT_PER_NEW_LETTER');print(f'CURRENT_TA_OBJECTS={len(current_ta)}');print('ZA_STATUS=DEFERRED_UNTIL_CORPUS_GATE_PASS')
    print('CORE_PRACTICE_ROWS=7');print('CORE_PRACTICE_OBJECTS=28');print('REGISTRY_OBJECTS=32_PRESERVED')
    print('PRESENTATION_FONT_SIZE=34PT');print('PRACTICE_FONT_SIZE=39PT');print('ENRICHMENT_GRID_ROW=8_NATIVE')
    print('ENRICHMENT_BLOCK_POLICY=CONTINUE_UNTIL_MASTERY');print('ENRICHMENT_CATEGORY=E02|E06');print('ENRICHMENT_LAYOUT=INDIVIDUAL_FIXED_WIDTH_GLYPHS')
    print('OUTPUT_DIR=dist/qurbata-print-ready/jilid-2/pages/P006');return rc
if __name__=='__main__':raise SystemExit(main())
