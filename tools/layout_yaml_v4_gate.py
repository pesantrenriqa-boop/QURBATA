#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'books/jilid-1/data-generated-v8-composition-v5'
SPECIAL = {20, 40}

def main():
    paths = sorted(DATA.glob('page-*.yaml'))
    issues = []
    reading = 0
    names = 0
    if len(paths) != 40:
        issues.append(f'PAGE_COUNT actual={len(paths)} expected=40')
    for expected, path in enumerate(paths, 1):
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
        page = int(data.get('page', 0))
        if page != expected:
            issues.append(f'PAGE_SEQUENCE expected={expected} actual={page}')
        if page in SPECIAL:
            if data.get('page_kind') != 'LETTER_NAMES' or data.get('objects'):
                issues.append(f'SPECIAL_CONTENT page={page}')
            count = len(data.get('letter_names', []))
            if count != 14:
                issues.append(f'LETTER_NAMES page={page} actual={count}')
            names += count
            continue
        objects = data.get('objects', [])
        reading += len(objects)
        if len(objects) != 16:
            issues.append(f'OBJECT_COUNT page={page} actual={len(objects)}')
        bands = Counter(x.get('row_band') for x in objects)
        lengths = Counter(int(x.get('unit_length', 0)) for x in objects)
        if bands != Counter({'ROW_2_L2_CURRENT': 4, 'ROWS_3_6_L3': 12}):
            issues.append(f'BANDS page={page} actual={dict(bands)}')
        if lengths != Counter({2: 4, 3: 12}):
            issues.append(f'LENGTHS page={page} actual={dict(lengths)}')
        focus = data.get('new_material', {})
        if not focus.get('label'):
            issues.append(f'FOCUS_LABEL page={page}')
        if not focus.get('tokens'):
            issues.append(f'FOCUS_TOKENS page={page}')
        for item in objects:
            if item.get('display_join_policy') != 'DISCONNECTED_NO_SPACE':
                issues.append(f'JOIN page={page} slot={item.get("slot")}')
            if item.get('render_mode') != 'qae-native-short-vowel':
                issues.append(f'RENDER_MODE page={page} slot={item.get("slot")}')
            if len(item.get('tokens', [])) != int(item.get('unit_length', 0)):
                issues.append(f'TOKENS page={page} slot={item.get("slot")}')
    print(f'YAML_PAGES={len(paths)}')
    print(f'YAML_READING_OBJECTS={reading}')
    print(f'YAML_LETTER_NAMES={names}')
    print('YAML_PAGE_PATTERN=ROW1_FOCUS|ROW2_4xL2|ROWS3_6_3x4_L3')
    print(f'YAML_V4_ISSUES={len(issues)}')
    if issues:
        for issue in issues[:30]:
            print('ISSUE=' + issue)
        print('LAYOUT_YAML_V4_GATE=FAIL')
        return 1
    print('LAYOUT_YAML_V4_GATE=PASS')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
