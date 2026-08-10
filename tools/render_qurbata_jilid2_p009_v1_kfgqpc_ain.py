#!/usr/bin/env python3
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P009-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P009-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P009-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
ARABIC_MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def base_letters(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in ARABIC_MARKS and unicodedata.category(ch)!='Mn')
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P009_REGISTRY_COUNT_INVALID')
issues=[(r['slot'],r['word']) for r in lex if len(base_letters(r['word']))!=3 or not r['meaning_id'].strip()]
if issues: raise ValueError('P009_THREE_LETTER_SEMANTIC_GATE_FAIL='+repr(issues))
p001.MICRO=MICRO; p001.P001_BANNED_JOINING=set('ظغفقكلمنيه'); words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]; p001.P001_CSS+=r'''.presentation-object{font-size:46pt}.j2-glyph{font-size:42pt}'''
_orig=p001.build_page_html
def build(debug):
 h=_orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">09</div>',1); s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>'); pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">{p001.arabic_html('عَبَرَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('رَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('بَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('عَ')}</span></div></div></section>'''; h=h[:s]+pres+h[e:]; s=h.index('<section class="targets">'); e=h.index('</section>',s)+len('</section>'); t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''; return h[:s]+t+h[e:]
p001.build_page_html=build
async def render(h,out,debug):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P009-V1.json'; png=out/'png'; png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  b=await pw.chromium.launch(); page=await b.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2); await page.goto(h.resolve().as_uri(),wait_until='networkidle'); await page.evaluate('document.fonts.ready'); metrics,li=await p001.fit_and_inspect(page); report.write_text(json.dumps(li,ensure_ascii=False,indent=2),encoding='utf-8')
  if li: raise RuntimeError('P009_LAYOUT_ISSUES='+str(len(li))+' REPORT='+str(report))
  await page.screenshot(path=str(png/'page-009.png'),full_page=True); pdf=out/'QURBATA-JILID-2-P009-V1-KFGQPC-AIN-CUMULATIVE.pdf'; await page.pdf(path=str(pdf),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'}); await b.close()
 return metrics,report,pdf
p001.render=render
def main():
 leaks=[(r['word'],''.join(sorted(p001.P001_BANNED_JOINING.intersection(r['word'])))) for r in lex if p001.P001_BANNED_JOINING.intersection(r['word'])]
 if leaks: raise ValueError('P009_COMPETENCY_LEAKAGE='+repr(leaks))
 current=[r for r in lex if r['function']=='CURRENT']; missing=[r['word'] for r in current if 'ع' not in base_letters(r['word'])]
 if missing: raise ValueError('P009_CURRENT_OBJECT_MISSING_AIN='+repr(missing))
 text=''.join(r['word'] for r in lex); counts={'FATHA':text.count('َ'),'KASRA':text.count('ِ'),'DAMMA':text.count('ُ')}
 if counts['KASRA']<10 or counts['DAMMA']<10: raise ValueError('P009_HARAKAT_BALANCE_FAIL='+repr(counts))
 rc=v22.main(); print('JILID2_P009_RENDERER_V1=PASS'); print('PAGE=9'); print('ACQUISITION_LETTERS=ع'); print('CUMULATIVE_HARAKAT=FATHA|KASRA|DAMMA'); print('HARAKAT_FATHA_COUNT='+str(counts['FATHA'])); print('HARAKAT_KASRA_COUNT='+str(counts['KASRA'])); print('HARAKAT_DAMMA_COUNT='+str(counts['DAMMA'])); print('HARAKAT_BALANCE_GATE=KASRA>=10|DAMMA>=10'); print('CUMULATIVE_COMPETENCY_P001_P008=PRESERVED'); print('PRACTICE_OBJECTS=32'); print('CURRENT_LEXICAL_OBJECTS='+str(len(current))); print('MUROJAAH_LEXICAL_OBJECTS='+str(32-len(current))); print('THREE_LETTER_WITH_MEANING=32'); print('MEANINGLESS_THREE_LETTER_OBJECTS=0'); print('COMPETENCY_LEAKAGE=0'); print('STATUS=P009_CUMULATIVE_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
