#!/usr/bin/env python3
"""QURBATA Jilid 2 P024 — mad ya. Correct harakat semantics: mad ya has no sukun mark; sukun is applied only to true consonant-sukun examples."""
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
OPEN_SUKUN='ۡ'; ROUND_SUKUN='ْ'; MARKS=set(chr(c) for c in range(0x064B,0x0660))|{OPEN_SUKUN,'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in MARKS and unicodedata.category(ch)!='Mn')
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P024_REGISTRY_INVALID')
lengths={2:0,3:0}
for r in lex:
    n=len(bases(r['word'])); lengths[n]=lengths.get(n,0)+1
    if n not in (2,3): raise ValueError('P024_LENGTH_GATE_FAIL='+repr(r))
    if OPEN_SUKUN in r['word'] or ROUND_SUKUN in r['word']: raise ValueError('P024_REGISTRY_MARK_FREE_REQUIRED')
    if 'ِي' not in r['word']: raise ValueError('P024_MAD_YA_REQUIRED='+repr(r))
    if n==3 and not r['word'].endswith('ُ'): raise ValueError('P024_FINAL_DAMMA_REQUIRED='+repr(r))
if lengths!={2:16,3:16}: raise ValueError('P024_DISTRIBUTION_FAIL='+repr(lengths))
# IMPORTANT: In mad asli, the madd letter ya is ساكنة in grammar/tajwid terms but
# its mushaf sign is normally not drawn as an explicit sukun above ya. The V15/V16
# corruption came from inserting U+06E1 after every mad-ya. P024 therefore keeps
# kasra + bare ya for the mad unit. Open ras-al-kha U+06E1 is reserved for future
# actual consonant-sukun units, using the validated native KFGQPC Lab-B model.
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set(); words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''
.presentation-object{font-size:48pt}.j2-glyph{font-size:44pt}
.j2-glyph,.presentation-object .arabic-part{direction:rtl;font-family:"QURBATA KFGQPC Uthman Taha Naskh","KFGQPC Uthman Taha Naskh",serif!important;font-feature-settings:'mark' 1,'mkmk' 1;text-rendering:optimizeLegibility}
'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">24</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres='''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">دِينُ</span><span class="arrow">←</span><span class="arabic-part" lang="ar">دِي</span><span class="arrow">←</span><span class="arabic-part" lang="ar">دِ</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
async def render(h,out,debug):
    report=out/'LAYOUT-OVERFLOW-REPORT-J2-P024-V17.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); p=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2)
        await p.goto(h.resolve().as_uri(),wait_until='networkidle'); await p.evaluate('document.fonts.ready')
        if await p.locator('.j2-object').count()!=32: raise RuntimeError('P024_OBJECT_COUNT_INVALID')
        if (await p.locator('.page-number').inner_text()).strip()!='24': raise RuntimeError('P024_PAGE_IDENTITY_FAIL')
        body=await p.locator('body').inner_text()
        if OPEN_SUKUN in body or ROUND_SUKUN in body: raise RuntimeError('P024_EXPLICIT_SUKUN_FORBIDDEN_ON_MAD_YA')
        if await p.locator('[class*="sukun-"]').count(): raise RuntimeError('P024_OVERLAY_FORBIDDEN')
        metrics,issues=await p001.fit_and_inspect(p); report.write_text(json.dumps({'layout_issues':issues,'mad_ya_explicit_sukun':False,'future_consonant_sukun_model':'KFGQPC+U+06E1 native'},ensure_ascii=False,indent=2),encoding='utf-8')
        if issues: raise RuntimeError('P024_LAYOUT_ISSUES='+str(len(issues))+' REPORT='+str(report))
        await p.screenshot(path=str(png/'page-024.png'),full_page=True)
        pdf=out/'QURBATA-JILID-2-P024-V17-MAD-YA-CLEAN.pdf'; await p.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await b.close()
    return metrics,report,pdf
p001.render=render
def main():
    rc=v22.main(); print('JILID2_P024_RENDERER_V17=PASS'); print('PAGE=24'); print('MAD_YA_EXPLICIT_SUKUN=NO'); print('MAD_PATTERN=KASRA_PLUS_BARE_YA'); print('FONT=KFGQPC_UTHMAN_TAHA'); print('FUTURE_TRUE_SUKUN_MODEL=KFGQPC_PLUS_U+06E1_NATIVE'); print('OVERLAY=DISABLED'); print('STATUS=P024_MAD_YA_CLEAN_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
