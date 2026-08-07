#!/usr/bin/env python3
"""Convert Jilid 1 Composer v8 outputs to 40-page Composition v5 YAML.

Reading-page layout contract:
- row 1: one full-width current-material focus strip (metadata, not reading object)
- row 2: 4 x L2 current-material objects
- rows 3-6: 12 x L3 objects, rendered as a 3-column x 4-row grid
- all practice objects share one common font size in the renderer
- independent Arabic units; never shape L2/L3 as connected words
"""
from __future__ import annotations
import argparse,csv
from collections import defaultdict
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
DEFAULT_INPUT=ROOT/'content/qwo/composer/output/jilid-1-v8-composition-v5'
SPECIAL={20,40}
def read(path):
    with path.open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input-dir',default=str(DEFAULT_INPUT.relative_to(ROOT)));ap.add_argument('--output-dir',default='books/jilid-1/data-generated-v8-composition-v5');a=ap.parse_args()
    inp=Path(a.input_dir);inp=inp if inp.is_absolute() else ROOT/inp
    out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out;out.mkdir(parents=True,exist_ok=True)
    reading=read(inp/'JILID-1-READING-OBJECTS-V8.csv');meta=read(inp/'JILID-1-PAGE-METADATA-V8.csv');inj=read(inp/'JILID-1-INJECTION-CONTENT-V8.csv')
    rb=defaultdict(list);ib=defaultdict(list)
    for r in reading:rb[int(r['Page'])].append(r)
    for r in inj:ib[int(r['Page'])].append(r)
    mb={int(r['Page']):r for r in meta}
    if set(mb)!=set(range(1,41)):raise ValueError('METADATA_PAGE_SET_INVALID')
    total=names=0
    for page in range(1,41):
        m=mb[page]
        focus_tokens=[x for x in m.get('NewMaterialTokens','').split('|') if x]
        data={'schema_version':4,'book':'QURBATA','volume':1,'page':page,'status':'v8-composition-v5-review-candidate','layout':'canonical-j1-composition-v5','source':str(inp).replace('\\','/'),'page_role':'LETTER_NAMES' if page in SPECIAL else 'READING','identity':{'title':'QURBATA','subtitle':f'JILID 1 • HALAMAN {page:02d}'},'targets':{'material_progress':f'{page:02d} / 40','competency_codes':m.get('CompetencyCodes',''),'competency_descriptions':m.get('CompetencyDescriptions',''),'memorization_code':m.get('MemorizationCode',''),'memorization':m.get('MemorizationDescription',''),'memorization_stage':m.get('MemorizationStage',''),'arabic_code':m.get('ArabicCode',''),'arabic_language':m.get('ArabicDescription',''),'akhlaq_code':m.get('AkhlaqCode',''),'akhlaq':m.get('AkhlaqDescription',''),'assessment_code':m.get('AssessmentCode',''),'assessment':m.get('AssessmentDescription',''),'harakat_stage':m.get('HarakatStage',''),'new_letters':m.get('NewLetters',''),'active_letters':m.get('ActiveLetters','')},'new_material':{'label':m.get('NewMaterialLabel',''),'tokens':focus_tokens},'special_injection':m.get('SpecialInjection','NONE'),'footer':{'profile':m.get('FooterProfile','J1_STANDARD_V2'),'teacher_label':'Nama Guru','date_label':'Tanggal','score_label':'Nilai'}}
        if page in SPECIAL:
            rows=sorted(ib[page],key=lambda r:int(r['Sequence']))
            if len(rows)!=14:raise ValueError(f'LETTER_NAME_COUNT page={page} actual={len(rows)}')
            data['page_kind']='LETTER_NAMES';data['objects']=[];data['letter_names']=[{'sequence':int(r['Sequence']),'letter':r['Letter'],'letter_name_arabic':r['LetterNameArabic'],'status':r.get('Status','REVIEW_CANDIDATE')} for r in rows];names+=14
        else:
            rows=sorted(rb[page],key=lambda r:int(r['Slot']))
            if len(rows)!=16:raise ValueError(f'PAGE_OBJECT_COUNT page={page} actual={len(rows)}')
            objs=[]
            for r in rows:
                length=int(r['UnitLength']);tokens=[r[f'Unit{i}'] for i in range(1,length+1)]
                if any(not x for x in tokens):raise ValueError(f'EMPTY_UNIT page={page} slot={r["Slot"]}')
                objs.append({'slot':int(r['Slot']),'object_id':r['ObjectID'],'object_type':'PRACTICE','competency_code':r['CompetencyCode'],'competency_description':r['CompetencyDescription'],'learning_state':r['LearningState'],'source_ref':r['SourceRef'],'text':r['ArabicObject'],'unit_length':length,'row_band':r['RowBand'],'display_join_policy':r['DisplayJoinPolicy'],'render_mode':'qae-native-short-vowel','tokens':tokens})
            data['page_kind']='READING';data['objects']=objs;data['letter_names']=[];total+=16
        (out/f'page-{page:03d}.yaml').write_text(yaml.safe_dump(data,allow_unicode=True,sort_keys=False),encoding='utf-8')
    print('PAGES_WRITTEN=40');print(f'READING_OBJECTS_WRITTEN={total}');print(f'LETTER_NAMES_WRITTEN={names}');print('PAGE_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_6_3x4_L3');print('LAYOUT_ADAPTER_V4=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
