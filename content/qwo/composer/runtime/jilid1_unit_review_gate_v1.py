#!/usr/bin/env python3
import csv
from collections import defaultdict,Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'content/qwo/composer/output/jilid-1-v10-unit-review';SPECIAL={20,40}
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def main():
 r=rows(OUT/'JILID-1-READING-OBJECTS-V10.csv');m=rows(OUT/'JILID-1-PAGE-METADATA-V10.csv');by=defaultdict(list);meta={int(x['Page']):x for x in m};issues=[]
 for x in r:by[int(x['Page'])].append(x)
 if len(r)!=722:issues.append(f'ROWS={len(r)} expected=722')
 for p in range(1,41):
  if p in SPECIAL:continue
  pr=sorted(by[p],key=lambda x:int(x['Slot']))
  if len(pr)!=19:issues.append(f'COUNT page={p}')
  focus=set(meta[p]['NewMaterialBases'])
  # Row 2 must be current focus only.
  for x in pr[:4]:
   for i in (1,2):
    if x[f'Base{i}'] not in focus or x[f'Unit{i}State']!='CURRENT':issues.append(f'ROW2 page={p} slot={x["Slot"]}')
  # Review is audited at unit level, not object level.
  cur=rev=0
  for x in pr:
   for i in range(1,int(x['UnitLength'])+1):
    s=x[f'Unit{i}State'];cur+=s=='CURRENT';rev+=s=='REVIEW'
  if p==1:
   if rev!=0:issues.append('PAGE1_REVIEW_NONZERO')
  else:
   if cur<30 or rev<18:issues.append(f'UNIT_DOMINANCE page={p} current={cur} review={rev}')
   # No entire triple may be labeled as the review atom; mixed unit assembly is expected.
   triples=pr[4:]
   if any(x['LearningState']=='REVIEW' for x in triples):issues.append(f'BLOCK_REVIEW_STATE page={p}')
 print(f'V10_READING_ROWS={len(r)}');print('V10_REVIEW_ATOM=LETTER_PLUS_HARAKAT');print('V10_BLOCK_REVIEW=FORBIDDEN');print('V10_CURRENT_MATERIAL=DOMINANT');print(f'V10_ISSUES={len(issues)}')
 if issues:
  [print('ISSUE='+x) for x in issues[:40]];print('JILID1_UNIT_REVIEW_GATE=FAIL');return 1
 print('JILID1_UNIT_REVIEW_GATE=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
