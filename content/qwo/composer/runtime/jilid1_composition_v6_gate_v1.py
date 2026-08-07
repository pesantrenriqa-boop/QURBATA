#!/usr/bin/env python3
import csv
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];OUT=ROOT/'content/qwo/composer/output/jilid-1-v9-composition-v6';SPECIAL={20,40};ORDER='ابتثجحخدذرزسشصضطظعغفقكلمهوني';EXPECTED={1:'اب',2:'تث',3:'جحخ',4:'دذ',5:'رز',6:'سش',7:'صض',8:'طظ',9:'عغ',10:'فق',11:'ك',12:'ل',13:'م',14:'ه',15:'و',16:'ني'}
def rows(p):
 with p.open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def main():
 r=rows(OUT/'JILID-1-READING-OBJECTS-V9.csv');m=rows(OUT/'JILID-1-PAGE-METADATA-V9.csv');issues=[];by=defaultdict(list);meta={int(x['Page']):x for x in m}
 for x in r:by[int(x['Page'])].append(x)
 if len(r)!=722:issues.append(f'ROWS={len(r)} expected=722')
 for p in range(1,41):
  if p in SPECIAL:continue
  pr=sorted(by[p],key=lambda x:int(x['Slot']));bands=Counter(x['RowBand'] for x in pr)
  if len(pr)!=19 or bands!=Counter({'ROW_2_L2_CURRENT':4,'ROWS_3_7_L3':15}):issues.append(f'PATTERN page={p}')
  if p<=16 and meta[p]['NewLetters']!=EXPECTED[p]:issues.append(f'FAMILY page={p}')
  focus=set(meta[p]['NewMaterialBases'])
  for x in pr[:4]:
   if x['Base1'] not in focus or x['Base2'] not in focus:issues.append(f'ROW2_SOURCE page={p} slot={x["Slot"]}')
  if meta[p]['ActiveLetters']!=''.join(ch for ch in ORDER if ch in set(meta[p]['ActiveLetters'])):issues.append(f'ACTIVE_ORDER page={p}')
  if meta[p]['HarakatStage']=='KASRAH':
   for x in pr[4:]:
    marks=''.join(ch for ch in x['ArabicObject'] if ch in 'َُِ')
    if marks.count('َ')!=2 or marks.count('ِ')!=1:issues.append(f'KASRAH_MIX page={p} slot={x["Slot"]}')
  if meta[p]['HarakatStage']=='DHAMMAH':
   for x in pr[4:]:
    marks=''.join(ch for ch in x['ArabicObject'] if ch in 'َُِ')
    if marks.count('ُ')!=1:issues.append(f'DHAMMAH_MIX page={p} slot={x["Slot"]}')
 print(f'V9_READING_ROWS={len(r)}');print('V9_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_7_15xL3');print('V9_ORDER_POLICY=VISUAL_FAMILY_DIFFICULTY');print('V9_NUN_YA=DEFERRED_END');print('V9_KASRAH_TRIPLES=2_FATHAH_1_KASRAH');print('V9_DHAMMAH_TRIPLES=ONE_DHAMMAH_WITH_PRIOR_MARKS');print(f'V9_ISSUES={len(issues)}')
 if issues:
  [print('ISSUE='+x) for x in issues[:40]];print('JILID1_COMPOSITION_V6_GATE=FAIL');return 1
 print('JILID1_COMPOSITION_V6_GATE=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
