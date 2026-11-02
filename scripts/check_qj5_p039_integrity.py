#!/usr/bin/env python3
"""Read-only structural guard for QURBATA Jilid 5 P039.

Run from repository root: python3 scripts/check_qj5_p039_integrity.py
Does not edit the register, validate Quran text, or grant tashih.
"""
from pathlib import Path
import sys

REGISTER = Path("02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_5.md")
EXPECTED = {
    5: ("QS 12:16", "وَجَاءُوا أَبَاهُمْ"),
    8: ("QS 51:7", "وَالسَّمَاءِ"),
}
# 0-based indices of Markdown table cells; K01 starts at index 2.
def main() -> int:
    if not REGISTER.is_file():
        print(f"FAIL: missing {REGISTER}", file=sys.stderr)
        return 2
    lines = REGISTER.read_text(encoding="utf-8").splitlines()
    matches = [line for line in lines if line.startswith("| P039 |")]
    if len(matches) != 1:
        print(f"FAIL: expected exactly one P039 row; found {len(matches)}")
        return 1
    row = matches[0]
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    problems = []
    if len(cells) != 19:
        problems.append(f"expected 19 cells, found {len(cells)}")
    if cells[0] != "P039":
        problems.append("first cell is not P039")
    if cells[-1] != "0/8":
        problems.append(f"Sah changed from 0/8: {cells[-1]!r}; review before release")
    for idx, (reference, phrase) in EXPECTED.items():
        if len(cells) > idx and (reference not in cells[idx] or phrase not in cells[idx]):
            problems.append(f"cell {idx} changed from the archived candidate; review patch and tashih")
    if problems:
        for problem in problems:
            print("REVIEW REQUIRED:", problem)
        return 1
    print("PASS: P039 has 19 cells, original K04/K07 and Sah 0/8.")
    print("This is a structural check only; not an approval to publish.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
