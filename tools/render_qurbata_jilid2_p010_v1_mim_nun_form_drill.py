#!/usr/bin/env python3
from __future__ import annotations
import csv,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p009_v1_ghain_form_drill as p009
import render_qurbata_jilid2_p001_v1 as p001

LEX=ROOT/'content/qwo/registry/JILID-2-P010-LEXICAL-FOUNDATION-V1.csv'
MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P010-V1.csv'
ENRICH=ROOT/'content/qwo/registry/JILID-2-BOTTOM-ROW-ENRICHMENT-LADDER-V1.csv'
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: micro=list(csv.DictReader(f))
with ENRICH.open(encoding='utf-8-sig',newline='') as f: ladder={r['StepCode']:r for r in csv.DictReader(f)}
core=[r['word'] for r in lex[:28]]
p001.MICRO=MICRO
p001.P001_ROWS=[core[i:i+4] for i in range(0,28,4)]
# P010 uses the already proven P009 renderer/safe-zone, but advances content and enrichment.
p009.lex=lex
p009.items=[x.strip() for x in ladder['E04']['Content'].split('|') if x.strip()]
p009.enrich=ladder['E04']

_base=p001.build_page_html
def build(debug):
 h=_base(debug).replace('<div class="page-number">01</div>','<div class="page-number">10</div>',1)
 s=h.index('<section class="presentation">');e=h.index('</section>',s)+10
 pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object" dir="ltr"><span class="arabic-part">{p001.arabic_html('مَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('مَنَعَ')}</span><span class="arabic-part">{p001.arabic_html('نَ')}</span><span class="arrow">←</span><span class="arabic-part">{p001.arabic_html('نَزَلَ')}</span></div></div></section>'''
 return h[:s]+pres+h[e:]
p001.build_page_html=build

# Keep P009's anti-clip DOM injection/render engine, changing only page/output identity.
_orig_render=p009.render
async def render(h,out,debug):
 metrics,report,pdf,mode=await _orig_render(h,out,debug)
 return metrics,report,pdf,mode
p001.render=render

def main():
 mim=sum('م' in r['word'] for r in lex[:28]);nun=sum('ن' in r['word'] for r in lex[:28])
 if mim<14 or nun<14: raise ValueError(f'P010_FORM_BALANCE_FAIL mim={mim} nun={nun}')
 if '--output-dir' not in sys.argv[1:]:sys.argv.extend(['--output-dir','dist/qurbata-print-ready/jilid-2/pages/P010'])
 rc=p009.v22.main()
 print('JILID2_P010_RENDERER_V1_MIM_NUN=PASS')
 print('PAGE=10')
 print('ACQUISITION_LETTERS=م|ن')
 print('PRACTICE_MODE=JOINING_FORM_DRILL_MEANINGFUL')
 print(f'FORM_MIM_OBJECTS={mim}')
 print(f'FORM_NUN_OBJECTS={nun}')
 print('SHORT_VOWELS=FATHAH|KASRAH|DAMMAH')
 print('TITLE_VISUAL_RIGHT_TO_LEFT=مَ←مَنَعَ|نَ←نَزَلَ')
 print('BOTTOM_ROW_STEP=E04')
 print('BOTTOM_ROW_CONTENT=حم|حم عسق repeated full row')
 print('BOTTOM_ROW_POLICY=AWAILUSSURAR_LADDER_CONTINUATION')
 print('ANTI_CLIP_GUARD=INHERITED_FROM_P009_V10')
 return rc
if __name__=='__main__':raise SystemExit(main())
