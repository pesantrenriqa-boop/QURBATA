#!/usr/bin/env python3
"""QURBATA Jilid 2 P006 — paired acquisition ط ظ for joining-form recognition."""
from __future__ import annotations
import csv,json,sys,unicodedata
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p001_v22_kfgqpc_lexical as v22
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P006-COMPETENCY-MAP-V1.csv';MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P006-V1.csv';LEX=ROOT/'content/qwo/registry/JILID-2-P006-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f:meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f:stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f:lex=list(csv.DictReader(f))
if len(stairs)!=10:raise ValueError('P006_MICRO_STAIRS_INVALID')
if len(lex)!=32:raise ValueError('P006_LEXICAL_COUNT_INVALID')
ARABIC_MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def base_letters(s:str)->str:return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in ARABIC_MARKS and unicodedata.category(ch)!='Mn')
p001.MICRO=MICRO;p001.P001_BANNED_JOINING=set('عغفقكلمنيه')
words=[r['word'] for r in lex[:28]];p001.P001_ROWS=[words[i:i+4] for i in range(0,28,4)]
p001.P001_CSS+=r'''.presentation-object{font-size:34pt!important;direction:ltr!important;flex-direction:row-reverse!important;unicode-bidi:isolate!important;gap:1.7mm!important;}.presentation-object .arabic-part{direction:rtl!important;unicode-bidi:isolate!important;line-height:1.15!important;padding:.35mm .3mm!important;}.presentation-object .arrow{direction:ltr!important;unicode-bidi:isolate!important;font-size:15pt!important;}.j2-glyph{font-size:39pt!important;}.j2-grid{grid-template-rows:repeat(8,minmax(0,1fr))!important;}.p006-enrichment-row{grid-column:1/-1!important;grid-row:8!important;display:grid!important;grid-template-columns:1fr 1fr!important;gap:10mm!important;padding:.55mm 6mm .35mm!important;border-top:.28mm solid #111!important;box-sizing:border-box!important;background:#fff!important;}.p006-enrichment-row .micro{display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;text-align:center!important;min-width:0!important;}.p006-enrichment-row .micro-label{font-family:Arial,sans-serif!important;font-size:6.2pt!important;font-weight:700!important;margin:0 0 .7mm!important;white-space:nowrap!important;}.glyph-run{display:flex!important;align-items:center!important;justify-content:center!important;gap:1.45mm!important;direction:ltr!important;white-space:nowrap!important;}.glyph-run.num .eg{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:20pt!important;line-height:1!important;width:4mm!important;text-align:center!important;direction:rtl!important;}.glyph-run.nonjoin .eg{font-family:'KFGQPC Uthman Taha Naskh','Amiri Quran','Amiri',serif!important;font-size:21pt!important;line-height:1!important;width:5mm!important;text-align:center!important;direction:rtl!important;}'''
_base_build=p001.build_page_html
def build_p006(debug:bool):
 h=_base_build(debug);h=h.replace('<div class="page-number">01</div>','<div class="page-number">06</div>',1);start=h.index('<section class="presentation">');end=h.index('</section>',start)+len('</section>');pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('طَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('طَرَبَ')}</span><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ظَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar" dir="rtl">{p001.arabic_html('ظَهَرَ')}</span></div></div></section>''';h=h[:start]+pres+h[end:];ts=h.index('<section class="targets">');te=h.index('</section>',ts)+len('</section>');targets=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>''';h=h[:ts]+targets+h[te:];nums=''.join(f'<span class="eg">{x}</span>' for x in '٠١٢٣٤٥٦٧٨٩');njs=''.join(f'<span class="eg">{x}</span>' for x in 'ادذرزو');enrichment=f'''<div class="p006-enrichment-row"><div class="micro"><div class="micro-label">ANGKA ARAB</div><div class="glyph-run num">{nums}</div></div><div class="micro"><div class="micro-label">PEMUTUS SAMBUNGAN</div><div class="glyph-run nonjoin">{njs}</div></div></div>''';gs=h.find('<section class="j2-grid">');ge=h.find('</section>',gs);return h[:ge]+enrichment+h[ge:]
p001.build_page_html=build_p006
async def _write_pdf(page,out:Path):
 names=[out/'QURBATA-JILID-2-P006-V3-TA-ZA-BOTTOMROW.pdf']+[out/f'QURBATA-JILID-2-P006-V3-TA-ZA-BOTTOMROW-LOCK-SAFE-{i:02d}.pdf' for i in range(1,100)]
 for idx,p in enumerate(names):
  try:await page.pdf(path=str(p),format='A5',print_background=True,margin={'top':'0','right':'0','bottom':'0','left':'0'});return p,('DIRECT_P006_V3' if idx==0 else f'LOCK_FALLBACK_P006_V3_{idx:02d}')
  except PermissionError:pass
 raise RuntimeError('P006_NO_AVAILABLE_PDF_NAME')
async def render_p006(h:Path,out:Path,debug:bool):
 report=out/'LAYOUT-OVERFLOW-REPORT-J2-P006-V3.json';png=out/'png';png.mkdir(parents=True,exist_ok=True)
 async with async_playwright() as pw:
  browser=await pw.chromium.launch();page=await browser.new_page(viewport={'width':1120,'height':1584},device_scale_factor=2);await page.goto(h.resolve().as_uri(),wait_until='networkidle');await page.evaluate('document.fonts.ready')
  if await page.locator('.j2-object').count()!=28:raise RuntimeError('P006_CORE_OBJECT_COUNT_INVALID')
  metrics,issues=await p001.fit_and_inspect(page);report.write_text(json.dumps(issues,ensure_ascii=False,indent=2),encoding='utf-8')
  if issues:raise RuntimeError('P006_LAYOUT_ISSUES='+repr(issues))
  await page.screenshot(path=str(png/'page-006-v3.png'),full_page=True);pdf,mode=await _write_pdf(page,out);await browser.close()
 return metrics,report,pdf,mode
p001.render=render_p006
def main():
 current=[r for r in lex if r['function']=='CURRENT'];ta=[r for r in current if 'ط' in base_letters(r['word'])];za=[r for r in current if 'ظ' in base_letters(r['word'])]
 if len(ta)<8 or len(za)<8:raise ValueError(f'P006_PAIR_GATE_FAIL ta={len(ta)} za={len(za)} required_each=8')
 premature=[]
 for r in lex:
  hit=set(base_letters(r['word'])).intersection(set('اأإآءؤئى'))
  if hit:premature.append((r['word'],''.join(sorted(hit))))
 if premature:raise ValueError('P006_PREMATURE_MADD_OR_HAMZAH='+repr(premature))
 leaks=[]
 for r in lex:
  hit=p001.P001_BANNED_JOINING.intersection(base_letters(r['word']))
  if hit:leaks.append((r['word'],''.join(sorted(hit))))
 if leaks:raise ValueError('P006_FUTURE_LETTER_LEAKAGE='+repr(leaks))
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P006'])
 rc=v22.main();print('JILID2_P006_RENDERER_V3_TA_ZA=PASS');print('PAGE=6');print('ACQUISITION_LETTERS=ط|ظ');print('TITLE_VISUAL_RIGHT_TO_LEFT=طَ←طَرَبَ|ظَ←ظَهَرَ');print('PAIRING_POLICY=SHAPE_FAMILY_SAME_PAGE');print(f'CURRENT_TA_OBJECTS={len(ta)}');print(f'CURRENT_ZA_OBJECTS={len(za)}');print('PREMATURE_MADD_OR_HAMZAH=0');print('FUTURE_LETTER_LEAKAGE=0');print('CORE_PRACTICE_ROWS=7');print('CORE_PRACTICE_OBJECTS=28');print('PRESENTATION_FONT_SIZE=34PT');print('PRACTICE_FONT_SIZE=39PT');print('ENRICHMENT_GRID_ROW=8_NATIVE');print('OUTPUT_DIR=dist/qurbata-print-ready/jilid-2/pages/P006');return rc
if __name__=='__main__':raise SystemExit(main())
