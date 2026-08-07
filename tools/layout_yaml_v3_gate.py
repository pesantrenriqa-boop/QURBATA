#!/usr/bin/env python3
import yaml
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'books/jilid-1/data-generated-v7-native'
def main():
 paths=sorted(DATA.glob('page-*.yaml'));issues=[];reading=names=0;states=Counter()
 if len(paths)!=40:issues.append(f'PAGE_COUNT={len(paths)}')
 for path in paths:
  d=yaml.safe_load(path.read_text(encoding='utf-8'));page=int(d['page'])
  if page in {20,40}:
   if d.get('page_kind')!='LETTER_NAMES' or d.get('objects') or len(d.get('letter_names',[]))!=14:issues.append(f'SPECIAL_PAGE={page}')
   names+=len(d.get('letter_names',[]));continue
  objs=d.get('objects',[])
  if len(objs)!=24:issues.append(f'OBJECT_COUNT page={page} actual={len(objs)}')
  lengths=Counter(int(x['unit_length']) for x in objs)
  if lengths!=Counter({1:8,2:8,3:8}):issues.append(f'LENGTH_PATTERN page={page} actual={dict(lengths)}')
  for x in objs:
   length=int(x['unit_length']);tokens=x.get('tokens',[])
   if len(tokens)!=length:issues.append(f'TOKEN_LENGTH page={page} slot={x.get("slot")}')
   if x.get('display_join_policy')!='DISCONNECTED_NO_SPACE':issues.append(f'JOIN_POLICY page={page} slot={x.get("slot")}')
   if x.get('render_mode')!='qae-native-short-vowel':issues.append(f'RENDER_MODE page={page} slot={x.get("slot")}')
   states[x.get('learning_state','')]+=1
  reading+=len(objs)
 print(f'YAML_PAGES={len(paths)}');print(f'YAML_READING_OBJECTS={reading}');print(f'YAML_LETTER_NAMES={names}');print('YAML_SLOT_PATTERN=8_L1|8_L2|8_L3');print('YAML_JOIN_POLICY=DISCONNECTED_NO_SPACE');print(f'YAML_V3_ISSUES={len(issues)}')
 if issues:
  for x in issues[:30]:print('ISSUE='+x)
  print('LAYOUT_YAML_V3_GATE=FAIL');return 1
 print('LAYOUT_YAML_V3_GATE=PASS');return 0
if __name__=='__main__':raise SystemExit(main())
