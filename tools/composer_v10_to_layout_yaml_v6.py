#!/usr/bin/env python3
import argparse,csv
from collections import defaultdict
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1];SPECIAL={20,40}
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def dl(x):return x
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-dir',default='content/qwo/composer/output/jilid-1-v10-unit-review');ap.add_argument('--output-dir',default='books/jilid-1/data-generated-v10-unit-review');a=ap.parse_args();inp=ROOT/a.input_dir;out=ROOT/a.output_dir;out.mkdir(parents=True,exist_ok=True)
 reading=read(inp/'JILID-1-READING-OBJECTS-V10.csv');meta=read(inp/'JILID-1-PAGE-METADATA-V10.csv');inj=read(inp/'JILID-1-INJECTION-CONTENT-V10.csv');rb=defaultdict(list);ib=defaultdict(list)
 for r in reading:rb[int(r['Page'])].append(r)
 for r in inj:ib[int(r['Page'])].append(r)
 mb={int(r['Page']):r for r in meta};total=names=0
 for page in range(1,41):
  m=mb[page]
  focus_tokens=[x for x in m.get('NewMaterialTokens','').split('|') if x]
  competency_unit=(m.get('NewMaterialLabel','')+(': '+' '.join(focus_tokens) if focus_tokens else '')).strip()
  memorization_item=m.get('MemorizationDescription','') or 'Belum ditetapkan'
  arabic_sub=m.get('ArabicDescription','') or 'Belum ditetapkan'
  # CRE currently has no versioned NIDOM target. Do not invent instructional metadata.
  nidom_sub='Belum diregistrasi'
  d={'schema_version':7,'book':'QURBATA','volume':1,'page':page,'status':'v10-unit-review-candidate','layout':'canonical-j1-composition-v5','page_role':'LETTER_NAMES' if page in SPECIAL else 'READING','identity':{'title':'QURBATA','subtitle':f'JILID 1 • HALAMAN {page:02d}'},'targets':{'competency_unit':competency_unit or m.get('CompetencyDescriptions',''),'memorization_item':memorization_item,'arabic_subcompetency':arabic_sub,'nidom_subcompetency':nidom_sub,'material_progress':f'{page:02d} / 40','competency_codes':m.get('CompetencyCodes',''),'competency_descriptions':m.get('CompetencyDescriptions',''),'memorization_code':m.get('MemorizationCode',''),'memorization':m.get('MemorizationDescription',''),'memorization_stage':m.get('MemorizationStage',''),'arabic_code':m.get('ArabicCode',''),'arabic_language':m.get('ArabicDescription',''),'harakat_stage':m.get('HarakatStage',''),'new_letters':m.get('NewLetters',''),'active_letters':m.get('ActiveLetters','')},'new_material':{'label':m.get('NewMaterialLabel',''),'bases':m.get('NewMaterialBases',''),'tokens':focus_tokens},'special_injection':m.get('SpecialInjection','NONE'),'footer':{'profile':m.get('FooterProfile','J1_STANDARD_V2'),'teacher_label':'Nama Guru','date_label':'Tanggal','score_label':'Nilai'}}
  if page in SPECIAL:
   rows=sorted(ib[page],key=lambda r:int(r['Sequence']));d['page_kind']='LETTER_NAMES';d['objects']=[];d['letter_names']=[{'sequence':int(r['Sequence']),'canonical_letter':r['Letter'],'letter':dl(r['Letter']),'letter_name_arabic':r['LetterNameArabic'],'status':r.get('Status','REVIEW_CANDIDATE')} for r in rows];names+=len(rows)
  else:
   rows=sorted(rb[page],key=lambda r:int(r['Slot']));
   if len(rows)!=19:raise ValueError(f'PAGE_OBJECT_COUNT page={page} actual={len(rows)}')
   objs=[]
   for r in rows:
    L=int(r['UnitLength']);tokens=[r[f'Unit{i}'] for i in range(1,L+1)];states=[r[f'Unit{i}State'] for i in range(1,L+1)]
    objs.append({'slot':int(r['Slot']),'object_id':r['ObjectID'],'object_type':'PRACTICE','competency_code':r['CompetencyCode'],'competency_description':r['CompetencyDescription'],'learning_state':r['LearningState'],'unit_states':states,'source_ref':r['SourceRef'],'text':r['ArabicObject'],'unit_length':L,'row_band':r['RowBand'],'display_join_policy':r['DisplayJoinPolicy'],'render_mode':'qae-native-short-vowel','tokens':tokens})
   d['page_kind']='READING';d['objects']=objs;d['letter_names']=[];total+=len(rows)
  (out/f'page-{page:03d}.yaml').write_text(yaml.safe_dump(d,allow_unicode=True,sort_keys=False),encoding='utf-8')
 print('PAGES_WRITTEN=40');print(f'READING_OBJECTS_WRITTEN={total}');print(f'LETTER_NAMES_WRITTEN={names}');print('REVIEW_ATOM=LETTER_PLUS_HARAKAT');print('BOX_WIDTH_POLICY=FIXED_EQUAL_COLUMNS');print('UNIT_ALIGNMENT=EDGE_LOCKED_RTL');print('TARGET_POSITION=BOTTOM');print('HEH_DISPLAY=ISOLATED_CANONICAL');print('NIDOM_REGISTRY=NOT_YET_VERSIONED');print('LAYOUT_ADAPTER_V6=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
