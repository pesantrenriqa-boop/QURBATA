#!/usr/bin/env python3
"""Gate for Jilid 1 Composition v5 / Composer v8."""
import csv
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'content/qwo/composer/output/jilid-1-v8-composition-v5'
READING=OUT/'JILID-1-READING-OBJECTS-V8.csv'; META=OUT/'JILID-1-PAGE-METADATA-V8.csv'; INJ=OUT/'JILID-1-INJECTION-CONTENT-V8.csv'
SPECIAL={20,40}
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def main():
 r=rows(READING);m=rows(META);inj=rows(INJ);issues=[];by=defaultdict(list);meta={int(x['Page']):x for x in m}
 for x in r:by[int(x['Page'])].append(x)
 if len(r)!=608:issues.append(f'READING_ROWS actual={len(r)} expected=608')
 if len(m)!=40:issues.append(f'METADATA_ROWS actual={len(m)} expected=40')
 if len(inj)!=28:issues.append(f'LETTER_NAMES actual={len(inj)} expected=28')
 expected={p for p in range(1,41) if p not in SPECIAL}
 if set(by)!=expected:issues.append('READING_PAGE_SET_INVALID')
 for p in sorted(by):
  pr=sorted(by[p],key=lambda x:int(x['Slot']))
  if [int(x['Slot']) for x in pr]!=list(range(1,17)):issues.append(f'SLOT_SEQUENCE page={p}')
  bands=Counter(x['RowBand'] for x in pr); lengths=Counter(int(x['UnitLength']) for x in pr)
  if bands!=Counter({'ROW_2_L2_CURRENT':4,'ROWS_3_6_L3':12}):issues.append(f'ROW_PATTERN page={p} actual={dict(bands)}')
  if lengths!=Counter({2:4,3:12}):issues.append(f'LENGTH_PATTERN page={p} actual={dict(lengths)}')
  row2=pr[:4]; triples=pr[4:]
  if any(x['LearningState'] not in ({'FOUNDATION'} if p==1 else {'CURRENT'}) for x in row2):issues.append(f'ROW2_NOT_CURRENT page={p}')
  if p==1:
   if Counter(x['LearningState'] for x in pr)!=Counter({'FOUNDATION':16}):issues.append('PAGE1_FOUNDATION_STATE')
  else:
   states=Counter(x['LearningState'] for x in pr)
   if states['CURRENT']!=8 or states['REVIEW']!=8:issues.append(f'PAGE_RATIO page={p} current={states["CURRENT"]} review={states["REVIEW"]}')
   ts=Counter(x['LearningState'] for x in triples)
   if ts['CURRENT']!=4 or ts['REVIEW']!=8:issues.append(f'TRIPLE_RATIO page={p} current={ts["CURRENT"]} review={ts["REVIEW"]}')
  active=set(meta[p]['ActiveLetters']);new=set(meta[p]['NewLetters'])
  for x in pr:
   L=int(x['UnitLength']); bases=[x[f'Base{i}'] for i in range(1,L+1)]
   if any(b not in active for b in bases):issues.append(f'FUTURE_LETTER page={p} slot={x["Slot"]}')
   if x['DisplayJoinPolicy']!='DISCONNECTED_NO_SPACE':issues.append(f'JOIN_POLICY page={p} slot={x["Slot"]}')
  if new:
   for x in row2:
    bases=[x['Base1'],x['Base2']]
    if any(b not in new for b in bases):issues.append(f'ROW2_NOT_NEW_MATERIAL page={p} slot={x["Slot"]}')
  if not meta[p].get('NewMaterialLabel'):issues.append(f'NEW_MATERIAL_LABEL_EMPTY page={p}')
  if not meta[p].get('NewMaterialTokens'):issues.append(f'NEW_MATERIAL_TOKENS_EMPTY page={p}')
 if any(int(x['Page']) in SPECIAL for x in r):issues.append('SPECIAL_PAGE_HAS_READING')
 print(f'V8_READING_ROWS={len(r)}');print('V8_PAGE_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_6_12xL3');print('V8_COMMON_PRACTICE_FONT=REQUIRED');print('V8_REVIEW_TARGET=8_CURRENT|8_REVIEW');print(f'V8_COMPOSITION_ISSUES={len(issues)}')
 if issues:
  for x in issues[:40]:print('ISSUE='+x)
  print('JILID1_COMPOSITION_V5_GATE_V1=FAIL');return 1
 print('JILID1_COMPOSITION_V5_GATE_V1=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
