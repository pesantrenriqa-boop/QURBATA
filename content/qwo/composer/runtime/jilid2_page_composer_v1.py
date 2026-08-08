#!/usr/bin/env python3
"""QURBATA Jilid 2 Composer v1.1 — joined-form foundation P001-P020.

Controlled baseline derived from QJ2-MASTER 0.25.0-id and
JILID-2-PROGRESSION-REGISTRY-V1.csv.

Policy:
- P001-P020 only; 24 reading objects per page, each exactly 3 letters;
- no isolated or two-letter regression;
- acquisition pages = 12 CURRENT + 12 REVIEW objects (50/50 by object);
- evaluation/integration pages = cumulative three-letter application;
- every surface on a page must be unique;
- uniqueness is produced by fresh letter assembly + independent short-vowel variation,
  not by weakening the gate or copying old blocks;
- ArabicObject contains no spaces so the browser/font may shape joining naturally;
- joining breakers remain in rotation as authentic interruption cases;
- this output is a CONTROLLED DRILL candidate, not a Qur'anic quotation dataset.
"""
from __future__ import annotations
import argparse,csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
REG=ROOT/'content/qwo/registry/JILID-2-PROGRESSION-REGISTRY-V1.csv'
DEFAULT_OUT=ROOT/'content/qwo/composer/output/jilid-2-v1-joined-foundation'

MARKS=('َ','ِ','ُ')
FOCUS={
 1:'ب',2:'بتث',3:'بتثني',4:'جحخ',5:'دذرز',6:'او',7:'سش',8:'صض',9:'طظ',
 10:'ابتثجحخدذرزسشصضطظ',11:'فق',12:'ك',13:'لم',14:'عغ',15:'ه',16:'تةه',17:'يى',
 18:'ءأإؤئ',19:'ابتثجحخدذرزسشصضطظعغفقكلمهوني',20:'ابتثجحخدذرزسشصضطظعغفقكلمهونيءأإؤئىة'
}
ACQ={1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18}


def read_rows(path):
 with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def write_rows(path,rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 fields=list(rows[0].keys()) if rows else []
 with path.open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def uniq(s):return ''.join(dict.fromkeys(s))
def prior_focus(page):
 s=''
 for p in range(1,page):s+=FOCUS[p]
 return uniq(s)

def marked_surface(bases:str,page:int,slot:int,variant:int)->str:
 """Independent ternary vowel code gives up to 27 surfaces for identical bases."""
 code=(page*101 + slot*17 + variant*7) % 27
 marks=[]
 for _ in range(3):
  marks.append(MARKS[code%3]);code//=3
 return ''.join(ch+marks[i] for i,ch in enumerate(bases))

def current_bases(page:int,slot:int,variant:int)->str:
 focus=uniq(FOCUS[page]);known=uniq(prior_focus(page)+focus)
 # Two positions explicitly expose current family; context position rotates cumulative pool.
 a=focus[(slot-1+variant)%len(focus)]
 b=focus[(slot+page+2*variant)%len(focus)]
 c=known[(slot*3+page+variant)%len(known)]
 return a+b+c

def review_bases(page:int,slot:int,variant:int)->str:
 # P1 legitimately bridges mastered J1 letters while remaining an L3 sequence.
 pool=prior_focus(page) or 'ابتثجحخدذرزسشصضطظعغفقكلمهوني'
 pool=uniq(pool);seed=page*7+slot*5+variant*3
 return ''.join(pool[(seed+i*(1+variant%3))%len(pool)] for i in range(3))

def cumulative_bases(page:int,slot:int,variant:int)->str:
 pool=uniq(prior_focus(page)+FOCUS[page]);seed=page*11+slot*7+variant*5
 return ''.join(pool[(seed+i*(1+(variant%4)))%len(pool)] for i in range(3))

def unique_object(page:int,slot:int,state:str,seen:set[str]):
 maker=current_bases if state=='CURRENT' else (review_bases if state=='REVIEW' else cumulative_bases)
 for variant in range(216):
  bases=maker(page,slot,variant)
  obj=marked_surface(bases,page,slot,variant)
  if obj not in seen:
   seen.add(obj);return obj,bases,variant
 raise ValueError(f'UNIQUE_SURFACE_POOL_EXHAUSTED page={page} slot={slot} state={state} seen={len(seen)}')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(DEFAULT_OUT.relative_to(ROOT)));a=ap.parse_args()
 out=Path(a.output_dir);out=out if out.is_absolute() else ROOT/out
 reg={int(r['Page']):r for r in read_rows(REG)}
 rows=[];meta=[]
 for page in range(1,21):
  r=reg[page]
  if r['UnitPattern']!='24xL3':raise ValueError(f'PATTERN_NOT_L3 page={page}')
  focus=uniq(FOCUS[page]);cur=rev=0;seen=set()
  for slot in range(1,25):
   if page in ACQ:
    state='CURRENT' if slot<=12 else 'REVIEW'
   else:
    state='CUMULATIVE_REVIEW'
   obj,bases,variant=unique_object(page,slot,state,seen)
   cur+=state=='CURRENT';rev+=state!='CURRENT'
   rows.append({
    'Jilid':2,'Page':page,'Slot':slot,'RowBand':'L3_JOINED','ObjectID':f'J2V1-P{page:02d}-S{slot:02d}',
    'ArabicObject':obj,'Base1':bases[0],'Base2':bases[1],'Base3':bases[2],'UnitLength':3,
    'DisplayJoinPolicy':'ARABIC_NATIVE_JOINING','CompetencyCode':r['Code'],'CompetencyStage':r['Stage'],
    'CompetencyFocus':r['Focus'],'LearningState':state,'AcquisitionType':r['AcquisitionType'],
    'SurfaceVariant':variant,'SourceRef':'CONTROLLED_DRILL:J2_JOINED_FOUNDATION_V1_1','QuranQuotation':'NO','Status':'COMPOSER_CANDIDATE_V1_1'
   })
  if len(seen)!=24:raise ValueError(f'PAGE_SURFACE_UNIQUENESS_DRIFT page={page} unique={len(seen)}')
  if page in ACQ and (cur,rev)!=(12,12):raise ValueError(f'RATIO_DRIFT page={page} current={cur} review={rev}')
  meta.append({
   'Page':page,'Code':r['Code'],'Stage':r['Stage'],'Focus':r['Focus'],'FocusBases':focus,'UnitPattern':'24xL3',
   'ReviewPolicy':'50_CURRENT|50_CUMULATIVE_REVIEW' if page in ACQ else '100_CUMULATIVE_APPLICATION',
   'ObjectCount':24,'UniqueSurfaceCount':24,'JoinedForms':'YES','TwoLetterRegression':'FORBIDDEN',
   'LayoutBaseline':'JILID1_V22_FROZEN','SourceStatus':r['Status'],'Status':'COMPOSER_CANDIDATE_V1_1'
  })
 write_rows(out/'JILID-2-READING-OBJECTS-V1.csv',rows);write_rows(out/'JILID-2-PAGE-METADATA-V1.csv',meta)
 print('JILID2_COMPOSER_V1_1=PASS');print('COMPOSED_PAGES=20');print(f'READING_ROWS={len(rows)}');print('PAGE_PATTERN=24xL3');print('JOIN_POLICY=ARABIC_NATIVE_JOINING');print('TWO_LETTER_REGRESSION=FORBIDDEN');print('ACQUISITION_REVIEW=12_CURRENT|12_REVIEW');print('PAGE_SURFACE_UNIQUENESS=24_OF_24');print('BLOCK_REUSE=FORBIDDEN');print('LAYOUT_BASELINE=JILID1_V22_FROZEN');return 0
if __name__=='__main__':raise SystemExit(main())
