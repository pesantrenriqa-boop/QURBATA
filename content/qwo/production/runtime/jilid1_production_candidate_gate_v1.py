#!/usr/bin/env python3
"""QURBATA Jilid 1 production-candidate verification gate.

This gate verifies candidate artifacts and core source outputs. It does not replace
human visual/pedagogical approval and therefore never declares FINAL status.
"""
from __future__ import annotations
import csv,json
from collections import Counter,defaultdict
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[4]
READING=ROOT/'content/qwo/composer/output/jilid-1-v7-micro-progression/JILID-1-READING-OBJECTS-V7.csv'
META=ROOT/'content/qwo/composer/output/jilid-1-v7-micro-progression/JILID-1-PAGE-METADATA-V7.csv'
YAML_DIR=ROOT/'books/jilid-1/data-generated-v7-native'
DIST=ROOT/'dist/jilid-1-production-candidate-v1'
OVERFLOW=DIST/'LAYOUT-OVERFLOW-REPORT-V4.json'
PDF=DIST/'QURBATA-JILID-1-CANONICAL-V4-NATIVE.pdf'
SPECIAL={20,40}
def csvrows(p):
 with p.open(encoding='utf-8-sig',newline='') as h:return list(csv.DictReader(h))
def main():
 issues=[]
 for p in (READING,META,OVERFLOW,PDF):
  if not p.exists():issues.append('MISSING:'+str(p.relative_to(ROOT)))
 if issues:
  for x in issues:print('ISSUE='+x)
  print('JILID1_PRODUCTION_CANDIDATE_GATE_V1=FAIL');return 1
 reading=csvrows(READING);meta=csvrows(META)
 if len(reading)!=912:issues.append(f'READING_ROWS={len(reading)}')
 if len(meta)!=40:issues.append(f'METADATA_ROWS={len(meta)}')
 by=defaultdict(list)
 for r in reading:by[int(r['Page'])].append(r)
 if set(by)!={p for p in range(1,41) if p not in SPECIAL}:issues.append('READING_PAGE_SET')
 for page,rows in by.items():
  if Counter(int(r['UnitLength']) for r in rows)!=Counter({1:8,2:8,3:8}):issues.append(f'LENGTH_PATTERN page={page}')
  if any(r['DisplayJoinPolicy']!='DISCONNECTED_NO_SPACE' for r in rows):issues.append(f'JOIN_POLICY page={page}')
  if any(r['QuranQuotation']!='NO' for r in rows):issues.append(f'QURAN_QUOTATION_POLICY page={page}')
 page1=sorted(by[1],key=lambda r:int(r['Slot']))
 if ''.join(r['Base1'] for r in page1 if r['UnitLength']=='1')!='ابتثابتث':issues.append('PAGE1_L1_ORDER')
 if any(r['HarakatStage']!='FATHAH' for r in page1):issues.append('PAGE1_HARAKAT')
 yaml_paths=sorted(YAML_DIR.glob('page-*.yaml'))
 if len(yaml_paths)!=40:issues.append(f'YAML_PAGE_COUNT={len(yaml_paths)}')
 else:
  for idx,p in enumerate(yaml_paths,1):
   data=yaml.safe_load(p.read_text(encoding='utf-8'))
   if int(data.get('page',0))!=idx:issues.append(f'YAML_SEQUENCE={p.name}')
   if idx in SPECIAL:
    if data.get('page_kind')!='LETTER_NAMES' or len(data.get('letter_names',[]))!=14:issues.append(f'SPECIAL_YAML page={idx}')
   else:
    objs=data.get('objects',[])
    if len(objs)!=24:issues.append(f'YAML_OBJECT_COUNT page={idx}')
    for o in objs:
     if o.get('display_join_policy')!='DISCONNECTED_NO_SPACE':issues.append(f'YAML_JOIN page={idx} slot={o.get("slot")}')
     if len(o.get('tokens',[]))!=int(o.get('unit_length',0)):issues.append(f'YAML_TOKEN_LENGTH page={idx} slot={o.get("slot")}')
 overflow=json.loads(OVERFLOW.read_text(encoding='utf-8'))
 if overflow:issues.append(f'LAYOUT_OVERFLOW_COUNT={len(overflow)}')
 print('CANDIDATE_STATUS=PRODUCTION_CANDIDATE_NOT_FINAL')
 print(f'READING_ROWS={len(reading)}')
 print(f'YAML_PAGES={len(yaml_paths)}')
 print(f'LAYOUT_OVERFLOW_COUNT={len(overflow)}')
 print(f'PDF_EXISTS={"YES" if PDF.is_file() else "NO"}')
 print(f'CANDIDATE_ISSUES={len(issues)}')
 if issues:
  for x in issues[:50]:print('ISSUE='+x)
  print('JILID1_PRODUCTION_CANDIDATE_GATE_V1=FAIL');return 1
 print('HUMAN_QA_REQUIRED=YES')
 print('JILID1_PRODUCTION_CANDIDATE_GATE_V1=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
