#!/usr/bin/env python3
"""Hard gate for QURBATA Jilid 1 50:50 NEW/REVIEW competency distribution."""
import csv
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
READING=ROOT/'content/qwo/composer/output/jilid-1-v7-micro-progression/JILID-1-READING-OBJECTS-V7.csv'
SPECIAL={20,40}
def main():
 with READING.open(encoding='utf-8-sig',newline='') as h: rows=list(csv.DictReader(h))
 by=defaultdict(list)
 for r in rows:by[int(r['Page'])].append(r)
 issues=[];exact_duplicates=0
 for page in sorted(by):
  pr=by[page]; states=Counter(r['LearningState'] for r in pr)
  if page==1:
   if states!=Counter({'FOUNDATION':24}):issues.append(f'PAGE1_STATE actual={dict(states)}')
  else:
   if states['NEW']!=12 or states['REVIEW']!=12:issues.append(f'RATIO page={page} new={states["NEW"]} review={states["REVIEW"]}')
   for length in (1,2,3):
    band=[r for r in pr if int(r['UnitLength'])==length];bc=Counter(r['LearningState'] for r in band)
    if bc['NEW']!=4 or bc['REVIEW']!=4:issues.append(f'BAND_RATIO page={page} L{length} new={bc["NEW"]} review={bc["REVIEW"]}')
 # Exact surface duplicates are checked across earlier pages only; unavoidable L1 repeats are excluded.
 seen=set()
 for r in sorted(rows,key=lambda x:(int(x['Page']),int(x['Slot']))):
  if int(r['UnitLength'])==1:continue
  key=(r['HarakatStage'],r['ArabicObject'])
  if key in seen: exact_duplicates+=1
  seen.add(key)
 print(f'REVIEW_PAGES={len(by)}')
 print('REVIEW_TARGET=50_NEW|50_REVIEW')
 print('REVIEW_BAND_TARGET=L1:4|4,L2:4|4,L3:4|4')
 print(f'EXACT_MULTIUNIT_REUSE_OBSERVED={exact_duplicates}')
 print(f'REVIEW_DISTRIBUTION_ISSUES={len(issues)}')
 if issues:
  for x in issues[:30]:print('ISSUE='+x)
  print('JILID1_REVIEW_DISTRIBUTION_GATE_V1=FAIL');return 1
 print('JILID1_REVIEW_DISTRIBUTION_GATE_V1=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
