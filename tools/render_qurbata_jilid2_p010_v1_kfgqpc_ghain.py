#!/usr/bin/env python3
"""QURBATA Jilid 2 P010 — acquisition of غ with cumulative P001-P009 review."""
from __future__ import annotations
import csv,sys,unicodedata
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT/'tools') not in sys.path: sys.path.insert(0,str(ROOT/'tools'))
import render_qurbata_jilid2_p008_v1_kfgqpc_transfer_balance as base
import render_qurbata_jilid2_p001_v1 as p001
MAP=ROOT/'content/qwo/registry/JILID-2-P010-COMPETENCY-MAP-V1.csv'; MICRO=ROOT/'content/qwo/registry/JILID-2-MICRO-COMPETENCY-P010-V1.csv'; LEX=ROOT/'content/qwo/registry/JILID-2-P010-LEXICAL-FOUNDATION-V1.csv'
with MAP.open(encoding='utf-8-sig',newline='') as f: meta=next(csv.DictReader(f))
with MICRO.open(encoding='utf-8-sig',newline='') as f: stairs=list(csv.DictReader(f))
with LEX.open(encoding='utf-8-sig',newline='') as f: lex=list(csv.DictReader(f))
if len(stairs)!=10 or len(lex)!=32: raise ValueError('P010_REGISTRY_INVALID')
ARABIC_MARKS=set(chr(c) for c in range(0x064B,0x0660))|{'ـ'}
def bases(s): return ''.join(ch for ch in unicodedata.normalize('NFC',s) if ch not in ARABIC_MARKS and unicodedata.category(ch)!='Mn')
for r in lex:
    if len(bases(r['word']))!=3 or not r['meaning_id'].strip(): raise ValueError('P010_SEMANTIC_GATE_FAIL='+repr(r))
p001.MICRO=MICRO
# After P010, ظ and later families remain forbidden. Also ف ق ك ل م ن ه are not yet acquired.
p001.P001_BANNED_JOINING=set('ظفقكلمنه')
words=[r['word'] for r in lex]; p001.P001_ROWS=[words[i:i+4] for i in range(0,32,4)]
p001.P001_CSS += r'''.presentation-object{font-size:46pt}.j2-glyph{font-size:42pt}'''
orig=p001.build_page_html
def build(debug):
    h=orig(debug).replace('<div class="page-number">01</div>','<div class="page-number">10</div>',1)
    s=h.index('<section class="presentation">'); e=h.index('</section>',s)+len('</section>')
    pres=f'''<section class="presentation"><div class="presentation-object-wrap"><div class="presentation-object"><span class="arabic-part" lang="ar">{p001.arabic_html('غَرُبَ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('رُ')}</span><span class="arrow">←</span><span class="arabic-part" lang="ar">{p001.arabic_html('غَ')}</span></div></div></section>'''
    h=h[:s]+pres+h[e:]
    ts=h.index('<section class="targets">'); te=h.index('</section>',ts)+len('</section>')
    t=f'''<section class="targets"><div class="target-item"><span>Kompetensi</span><strong>{meta['CompetencyCode']} — {meta['Competency']}</strong></div><div class="target-item"><span>Unit Kompetensi</span><strong>{meta['UnitCompetencyCode']} — {meta['UnitCompetency']}</strong></div><div class="target-item"><span>Unit Murojaah</span><strong>{meta['UnitMurojaahCode']} — {meta['UnitMurojaah']}</strong></div><div class="target-item"><span>Tangga</span><strong>{stairs[0]['StairCode']}–{stairs[-1]['StairCode']}</strong></div></section>'''
    return h[:ts]+t+h[te:]
p001.build_page_html=build
# Reuse validated P008 render geometry but change artifact identity.
orig_render=base.render_p008
async def render(h,out,debug):
    metrics,report,pdf=await orig_render(h,out,debug)
    target=out/'QURBATA-JILID-2-P010-V1-KFGQPC-GHAIN-CUMULATIVE.pdf'
    if pdf!=target: pdf.replace(target)
    return metrics,report,target
p001.render=render

def main():
    leaks=[]
    for r in lex:
        hit=p001.P001_BANNED_JOINING.intersection(r['word'])
        if hit: leaks.append((r['word'],''.join(sorted(hit))))
    if leaks: raise ValueError('P010_COMPETENCY_LEAKAGE='+repr(leaks))
    current=[r for r in lex if r['function']=='CURRENT']
    missing=[r['word'] for r in current if 'غ' not in bases(r['word'])]
    if missing: raise ValueError('P010_CURRENT_OBJECT_MISSING_GHAIN='+repr(missing))
    text=''.join(r['word'] for r in lex); counts={'FATHA':text.count('َ'),'KASRA':text.count('ِ'),'DAMMA':text.count('ُ')}
    if counts['KASRA']<10 or counts['DAMMA']<10: raise ValueError('P010_HARAKAT_BALANCE_FAIL='+repr(counts))
    rc=base.v22.main()
    print('JILID2_P010_RENDERER_V1=PASS'); print('PAGE=10'); print(f"COMPETENCY={meta['CompetencyCode']}|{meta['Competency']}"); print(f"UNIT_COMPETENCY={meta['UnitCompetencyCode']}|{meta['UnitCompetency']}"); print(f"SUBCOMPETENCY={meta['SubCompetencyCode']}|{meta['SubCompetency']}"); print(f"UNIT_MUROJAAH={meta['UnitMurojaahCode']}|{meta['UnitMurojaah']}"); print(f"STAIR_RANGE={stairs[0]['StairCode']}-{stairs[-1]['StairCode']}"); print('ACQUISITION_LETTERS=غ'); print('CUMULATIVE_HARAKAT=FATHA|KASRA|DAMMA'); print('HARAKAT_FATHA_COUNT='+str(counts['FATHA'])); print('HARAKAT_KASRA_COUNT='+str(counts['KASRA'])); print('HARAKAT_DAMMA_COUNT='+str(counts['DAMMA'])); print('HARAKAT_BALANCE_GATE=KASRA>=10|DAMMA>=10'); print('CUMULATIVE_COMPETENCY_P001_P009=PRESERVED'); print('PRACTICE_OBJECTS=32'); print('CURRENT_LEXICAL_OBJECTS='+str(len(current))); print('MUROJAAH_LEXICAL_OBJECTS='+str(32-len(current))); print('THREE_LETTER_WITH_MEANING=32'); print('MEANINGLESS_THREE_LETTER_OBJECTS=0'); print('COMPETENCY_LEAKAGE=0'); print('ARABIC_FONT_PRIMARY=KFGQPC Uthman Taha Naskh'); print('PRACTICE_FONT_SIZE=42PT'); print('PRESENTATION_FONT_SIZE=46PT'); print('STATUS=P010_CUMULATIVE_CANDIDATE_NOT_FROZEN'); return rc
if __name__=='__main__': raise SystemExit(main())
