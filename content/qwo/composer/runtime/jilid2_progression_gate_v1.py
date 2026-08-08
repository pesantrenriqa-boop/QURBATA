#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path

ROOT=Path(__file__).resolve().parents[4]
REG=ROOT/'content/qwo/registry/JILID-2-PROGRESSION-REGISTRY-V1.csv'

EXPECTED_STAGE={
    **{p:'JOINED_FORMS' for p in range(1,21)},
    **{p:'TANWIN' for p in range(21,25)},
    25:'MAD',
    **{p:'MAD_ALIF' for p in range(26,31)},
    **{p:'MAD_YA' for p in range(31,35)},
    **{p:'MAD_WAW' for p in range(35,39)},
    39:'MAD_INTEGRATION',40:'MAD_INTEGRATION'
}


def rows():
    with REG.open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))


def main():
    data=rows();issues=[]
    if len(data)!=40:issues.append(f'PAGE_COUNT actual={len(data)} expected=40')
    pages=[int(r['Page']) for r in data]
    if pages!=list(range(1,41)):issues.append('PAGE_SEQUENCE_INVALID')

    for r in data:
        p=int(r['Page']);stage=r['Stage'];pattern=r['UnitPattern']
        if stage!=EXPECTED_STAGE.get(p):issues.append(f'STAGE page={p} actual={stage} expected={EXPECTED_STAGE.get(p)}')
        expected='24xL3' if p<=20 else '8xL3|16xL4'
        if pattern!=expected:issues.append(f'UNIT_PATTERN page={p} actual={pattern} expected={expected}')
        if 'L2' in pattern or 'L1' in pattern:issues.append(f'REGRESSION_UNIT page={p} pattern={pattern}')
        if r['ReviewPolicy']!='CUMULATIVE_COMPETENCY_REVIEW':issues.append(f'REVIEW_POLICY page={p}')

    for p in range(21,25):
        if data[p-1]['Status']!='BLOCKED_ORTHOGRAPHY_GATE':issues.append(f'TANWIN_STATUS page={p}')
    for p in range(25,41):
        if data[p-1]['Status']!='PENDING_REGENERATION':issues.append(f'MAD_STATUS page={p}')

    print('JILID2_PAGES='+str(len(data)))
    print('JILID2_P001_P020_PATTERN=24xL3')
    print('JILID2_P021_P040_PATTERN=8xL3|16xL4')
    print('JILID2_TWO_LETTER_REGRESSION=FORBIDDEN')
    print('JILID2_REVIEW_POLICY=CUMULATIVE_COMPETENCY_REVIEW')
    print('JILID2_LAYOUT_BASELINE=JILID1_V22_FROZEN')
    print('JILID2_TANWIN_GATE=P021-P024_BLOCKED_ORTHOGRAPHY')
    print('JILID2_MAD_REGENERATION=P025-P040_PENDING')
    print('JILID2_PROGRESSION_ISSUES='+str(len(issues)))
    for x in issues[:50]:print('ISSUE='+x)
    if issues:
        print('JILID2_PROGRESSION_GATE_V1=FAIL');return 1
    print('JILID2_PROGRESSION_GATE_V1=PASS');return 0

if __name__=='__main__':raise SystemExit(main())
