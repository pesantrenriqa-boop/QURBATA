#!/usr/bin/env python3
"""QURBATA Jilid 2 P024 — K2 U02 mad ya: KFGQPC base glyphs + isolated native open sukun mark."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P024-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P024-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P024-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P024_REGISTRY_INVALID')
OPEN_SUKUN='ۡ'  # U+06E1 ARABIC SMALL HIGH DOTLESS HEAD OF KHAH
ROUND_SUKUN='ْ'
FORBIDDEN_MARKS=set('ًٌٍّ')
MARKS=set(chr(c) for c in range(0x064B,0x0660))|{OPEN_SUKUN,'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
def has_mad_ya(text):
    chars=list(text); return any(ch=='ي' and i>=1 and chars[i-1]=='ِ' for i,ch in enumerate(chars))
def add_open_sukun(text:str)->str:
    out=[]
    for i,ch in enumerate(text):
        out.append(ch)
        if ch=='ي' and i>=1 and text[i-1]=='ِ': out.append(OPEN_SUKUN)
    return ''.join(out)
lengths={2:0,3:0}
for r in lex:
    n=len(bases(r['word']))
    if n not in lengths: raise ValueError('P024_LENGTH_GATE_FAIL='+repr(r))
    lengths[n]+=1
    if r['function']!='CURRENT' or r['lexical_status']!='CURATED' or r['competency_status']!='ALLOWED': raise ValueError('P024_STATUS_GATE_FAIL='+repr(r))
    if ROUND_SUKUN in r['word'] or OPEN_SUKUN in r['word']: raise ValueError('P024_REGISTRY_MUST_REMAIN_MARK_FREE='+repr(r))
    if not has_mad_ya(r['word']): raise ValueError('P024_MAD_YA_REQUIRED='+repr(r))
    if n==3 and (not r['meaning_id'].strip() or not r['word'].endswith('ُ')): raise ValueError('P024_THREE_LETTER_SEMANTIC_OR_FINAL_DAMMA_FAIL='+repr(r))
    if any(m in r['word'] for m in FORBIDDEN_MARKS): raise ValueError('P024_UPPER_COMPETENCY_MARK_LEAKAGE='+repr(r))
if lengths!={2:16,3:16}: raise ValueError('P024_LADDER_DISTRIBUTION_FAIL='+repr(lengths))
# V11: preserve the established KFGQPC/Uthman Taha chain for ALL Arabic base glyphs.
# U+06E1 stays inline as a combining mark. Browser/font fallback is allowed ONLY for
# that unsupported mark; do not switch the whole word to Amiri (V10 regression).
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); words=[add_open_sukun(r['word']) for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''
.presentation-object{font-size:48pt}
.j2-glyph{font-size:44pt}
.j2-glyph,.presentation-object,.presentation-object .arabic-part,.mad-unit{font-family:"QURBATA KFGQPC Uthman Taha Naskh","KFGQPC Uthman Taha Naskh",'Amiri Quran','Amiri',serif!important;font-feature-settings:'mark' 1,'mkmk' 1;font-kerning:normal;text-rendering:optimizeLegibility}
.mad-unit{display:inline-block;direction:rtl;unicode-bidi:isolate}
'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">24</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part mad-unit" lang="ar">{add_open_sukun('دِينُ')}</span><span class="arrow">←</span><span class="arabic-part mad-unit" lang="ar">{add_open_sukun('دِي')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">دِ</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P024-V11.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
        if await page.locator('.j2-object').count()!=32: raise RuntimeError('P024_OBJECT_COUNT_INVALID')
        if (await page.locator('.page-number').inner_text()).strip()!='24': raise RuntimeError('P024_PAGE_IDENTITY_FAIL')
        body=await page.locator('body').inner_text();open_count=body.count(OPEN_SUKUN);round_count=body.count(ROUND_SUKUN)
        if open_count!=34: raise RuntimeError(f'P024_NATIVE_OPEN_SUKUN_COUNT_FAIL actual={open_count} expected=34')
        if round_count!=0: raise RuntimeError(f'P024_ROUND_SUKUN_FORBIDDEN actual={round_count}')
        if await page.locator('[class*="sukun-"]').count()!=0: raise RuntimeError('P024_OVERLAY_ARTIFACT_FORBIDDEN')
        # Guard the regression reported in V10: the whole word must resolve to the
        # KFGQPC-first family stack, never an Amiri-first override.
        families=await page.evaluate("""()=>[...document.querySelectorAll('.j2-glyph,.presentation-object .arabic-part')].map(e=>getComputedStyle(e).fontFamily)""")
        if not families or any(not f.lstrip().startswith(('"QURBATA KFGQPC Uthman Taha Naskh"','QURBATA KFGQPC Uthman Taha Naskh')) for f in families): raise RuntimeError('P024_BASE_FONT_REGRESSION='+repr(families[:4]))
        metrics,issues=await p001.fit_and_inspect(page);report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P024_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await page.screenshot(path=str(png/'page-024.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P024-V11-KFGQPC-BASE-NATIVE-OPEN-SUKUN.pdf';await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});await browser.close()
    return metrics,report,pdf
p001.render=render
def main():
    rc=v22.main();print('JILID2_P024_RENDERER_V11=PASS');print('PAGE=24');print('HEADER_SEQUENCE=دِ|دِيۡ|دِيۡنُ');print('P024_STAGE=TWO_TO_THREE_LETTER_LADDER');print('TWO_LETTER_OBJECTS=16');print('THREE_LETTER_OBJECTS=16');print('BASE_ARABIC_FONT=KFGQPC_UTHMAN_TAHA');print('SUKUN_CODEPOINT=U+06E1');print('SUKUN_STYLE=NATIVE_OPEN_DOTLESS_HEAD_OF_KHAH');print('SUKUN_RENDER_MODE=INLINE_OPENTYPE_WITH_MARK_FALLBACK_ONLY');print('WHOLE_WORD_AMIRI_OVERRIDE=DISABLED');print('SVG_OVERLAY=DISABLED');print('MANUAL_POSITIONING=DISABLED');print('ROUND_SUKUN_U+0652=FORBIDDEN');print('NATIVE_OPEN_SUKUN_COUNT=34');print('STATUS=P024_KFGQPC_BASE_OPEN_SUKUN_CANDIDATE_NOT_FROZEN');return rc
if __name__=='__main__': raise SystemExit(main())
