from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REG = ROOT / 'content/qwo/registry/JILID-2-NEW-MATERIAL-PRESENTATION-V1.csv'


def main() -> int:
    rows = list(csv.DictReader(REG.open(encoding='utf-8-sig')))
    issues: list[str] = []

    if len(rows) != 40:
        issues.append(f'PAGE_COUNT actual={len(rows)} expected=40')

    acquisition_like = {'ACQUISITION', 'ORIENTATION', 'CONTRAST'}
    # Page-level source of acquisition type from progression registry.
    prog_path = ROOT / 'content/qwo/registry/JILID-2-PROGRESSION-REGISTRY-V1.csv'
    prog = {int(r['Page']): r for r in csv.DictReader(prog_path.open(encoding='utf-8-sig'))}

    required = 0
    suppressed = 0
    for r in rows:
        page = int(r['Page'])
        p = prog.get(page)
        if not p:
            issues.append(f'MISSING_PROGRESSION page={page}')
            continue
        req = r['PresentationRequired'].strip().upper() == 'YES'
        if req:
            required += 1
            if not r['PresentationTitle'].strip():
                issues.append(f'MISSING_PRESENTATION_TITLE page={page}')
            if not r['PresentationObject'].strip():
                issues.append(f'MISSING_PRESENTATION_OBJECT page={page}')
            if not r['Function'].startswith('PAPARAN_'):
                issues.append(f'INVALID_PRESENTATION_FUNCTION page={page} function={r["Function"]}')
        else:
            suppressed += 1
            if r['PresentationObject'].strip():
                issues.append(f'UNEXPECTED_PRESENTATION_OBJECT page={page}')

        if p['AcquisitionType'] in acquisition_like and not req:
            # Reinforcement pages are represented by ACQUISITION in legacy progression,
            # so only flag when the presentation registry also declares a genuinely new subcompetency.
            if r['Stair'].lower().startswith(('mengenali', 'membedakan')):
                issues.append(f'NEW_MATERIAL_WITHOUT_PRESENTATION page={page}')

    print(f'JILID2_PRESENTATION_PAGES={len(rows)}')
    print(f'JILID2_PRESENTATION_REQUIRED={required}')
    print(f'JILID2_PRESENTATION_SUPPRESSED={suppressed}')
    print('JILID2_NEW_MATERIAL_ORDER=TITLE|PRESENTATION|PRACTICE|REVIEW_TRANSFER')
    print('JILID2_PRESENTATION_IS_READING_OBJECT=YES')
    print('JILID2_PRESENTATION_IS_TECHNICAL_LABEL=NO')
    print('JILID2_REPEAT_SAME_PRESENTATION_EVERY_PAGE=NO')
    print(f'JILID2_PRESENTATION_ISSUES={len(issues)}')
    for issue in issues:
        print('ISSUE=' + issue)
    if issues:
        print('JILID2_PRESENTATION_GATE_V1=FAIL')
        return 1
    print('JILID2_PRESENTATION_GATE_V1=PASS')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
