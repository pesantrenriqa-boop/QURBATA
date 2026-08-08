#!/usr/bin/env python3
from __future__ import annotations
import csv
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'content/qwo/composer/output/jilid-2-v1-joined-foundation'
R=OUT/'JILID-2-READING-OBJECTS-V1.csv';M=OUT/'JILID-2-PAGE-METADATA-V1.csv'
def read(p):
 with p.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def main():
 rows=read(R);meta=read(M);issues=[]
 if len(rows)!=480:issues.append(f'ROW_COUNT actual={len(rows)} expected=480')
 if len(meta)!=20:issues.append(f'META_COUNT actual={len(meta)} expected=20')
 by=Counter(int(x['Page']) for x in rows)
 for p in range(1,21):
  if by[p]!=24:issues.append(f'PAGE_COUNT page={p} actual={by[p]} expected=24')
 pr={p:[x for x in rows if int(x['Page'])==p] for p in range(1,21)}
 for p,xs in pr.items():
  if any(int(x['UnitLength'])!=3 for x in xs):issues.append(f'UNIT_LENGTH page={p}')
  if any(x['DisplayJoinPolicy']!='ARABIC_NATIVE_JOINING' for x in xs):issues.append(f'JOIN_POLICY page={p}')
  if any(' ' in x['ArabicObject'] for x in xs):issues.append(f'SPACE_BREAKS_JOIN page={p}')
  if any(len([x[f'Base{i}'] for i in (1,2,3) if x[f'Base{i}']])!=3 for x in xs):issues.append(f'BASE_ARITY page={p}')
  if p not in (10,19,20):
   c=Counter(x['LearningState'] for x in xs)
   if c['CURRENT']!=12 or c['REVIEW']!=12:issues.append(f'RATIO page={p} current={c["CURRENT"]} review={c["REVIEW"]}')
  else:
   if any(x['LearningState']!='CUMULATIVE_REVIEW' for x in xs):issues.append(f'EVAL_STATE page={p}')
 # review blocks must be freshly generated: exact Arabic surface duplicates within a page are forbidden.
 for p,xs in pr.items():
  surfaces=[x['ArabicObject'] for x in xs]
  dup=sum(v-1 for v in Counter(surfaces).values() if v>1)
  if dup:issues.append(f'DUPLICATE_SURFACE page={p} count={dup}')
 print('JILID2_FOUNDATION_PAGES=20');print('JILID2_FOUNDATION_ROWS=480');print('JILID2_FOUNDATION_PATTERN=24xL3');print('JILID2_JOIN_POLICY=ARABIC_NATIVE_JOINING');print('JILID2_ACQUISITION_RATIO=12_CURRENT|12_REVIEW');print('JILID2_TWO_LETTER_REGRESSION=FORBIDDEN');print('JILID2_EXACT_BLOCK_REUSE=FORBIDDEN');print('JILID2_LAYOUT_BASELINE=JILID1_V22_FROZEN');print(f'JILID2_FOUNDATION_ISSUES={len(issues)}')
 for x in issues[:30]:print('ISSUE='+x)
 print('JILID2_JOINED_FOUNDATION_GATE_V1=' + ('PASS' if not issues else 'FAIL'))
 return 0 if not issues else 1
if __name__=='__main__':raise SystemExit(main())
