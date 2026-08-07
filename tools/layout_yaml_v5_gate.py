#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import yaml
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'books/jilid-1/data-generated-v9-composition-v6';SPECIAL={20,40}
def main():
 paths=sorted(DATA.glob('page-*.yaml'));issues=[];reading=names=0
 if len(paths)!=40:issues.append(f'PAGE_COUNT actual={len(paths)} expected=40')
 for expected,path in enumerate(paths,1):
  d=yaml.safe_load(path.read_text(encoding='utf-8'));page=int(d.get('page',0))
  if page!=expected:issues.append(f'PAGE_SEQUENCE expected={expected} actual={page}')
  if page in SPECIAL:
   if d.get('page_kind')!='LETTER_NAMES' or d.get('objects'):issues.append(f'SPECIAL_CONTENT page={page}')
   n=len(d.get('letter_names',[]));names+=n
   if n!=14:issues.append(f'LETTER_NAMES page={page} actual={n}')
   continue
  objs=d.get('objects',[]);reading+=len(objs)
  if len(objs)!=19:issues.append(f'OBJECT_COUNT page={page} actual={len(objs)}')
  bands=Counter(x.get('row_band') for x in objs);lengths=Counter(int(x.get('unit_length',0)) for x in objs)
  if bands!=Counter({'ROW_2_L2_CURRENT':4,'ROWS_3_7_L3':15}):issues.append(f'BANDS page={page} actual={dict(bands)}')
  if lengths!=Counter({2:4,3:15}):issues.append(f'LENGTHS page={page} actual={dict(lengths)}')
  focus=d.get('new_material',{})
  if not focus.get('tokens'):issues.append(f'FOCUS_TOKENS page={page}')
  for x in objs:
   if x.get('display_join_policy')!='DISCONNECTED_NO_SPACE':issues.append(f'JOIN page={page} slot={x.get("slot")}')
   if x.get('render_mode')!='qae-native-short-vowel':issues.append(f'RENDER page={page} slot={x.get("slot")}')
   if len(x.get('tokens',[]))!=int(x.get('unit_length',0)):issues.append(f'TOKENS page={page} slot={x.get("slot")}')
 print(f'YAML_PAGES={len(paths)}');print(f'YAML_READING_OBJECTS={reading}');print(f'YAML_LETTER_NAMES={names}');print('YAML_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_7_15xL3');print(f'YAML_V5_ISSUES={len(issues)}')
 if issues:
  [print('ISSUE='+x) for x in issues[:30]];print('LAYOUT_YAML_V5_GATE=FAIL');return 1
 print('LAYOUT_YAML_V5_GATE=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
