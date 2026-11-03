#!/usr/bin/env python3
"""Read-only Jilid 5 coverage report; never treats candidates as approved."""
from pathlib import Path
import re
import sys

SOURCE = Path("02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_5.md")

def audit(content):
    rows = [s for s in content.splitlines() if re.match(r"^\| P\d{3} \|", s)]
    errors, results = [], []
    seen = set()
    for line in rows:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        page = cells[0]
        if page in seen:
            errors.append(f"duplicate page: {page}")
        seen.add(page)
        if len(cells) != 19:
            errors.append(f"{page}: expected 19 cells, got {len(cells)}")
            continue
        number = int(page[1:])
        capacity = 16 if number <= 20 else 8
        examples = cells[2:2+capacity]
        filled = sum(bool(c and c != "—") for c in examples)
        if page == "P013":
            # Mad farq has only a small number of Quranic occurrences.
            # Do not fill the remaining 12 slots with invented/repeated text.
            if filled > 4:
                errors.append("P013: more than four candidates; manually verify each distinct Quran locus before acceptance")
            for index, example in enumerate(examples, 1):
                if example != "—" and not any(ref in example for ref in ("QS 27:59", "QS 6:143", "QS 10:59", "QS 6:144")):
                    errors.append(f"P013 K{index:02d}: missing an expected Mad Farq reference; requires review")
        sah = cells[-1]
        if not re.fullmatch(r"\d+/(?:16|8)", sah):
            errors.append(f"{page}: invalid Sah counter {sah!r}")
        elif int(sah.split("/")[1]) != capacity:
            errors.append(f"{page}: Sah denominator mismatch")
        results.append((page, filled, capacity, capacity-filled, sah))
    expected = {f"P{i:03d}" for i in range(1, 41)}
    if seen != expected:
        errors.append(f"missing pages: {sorted(expected-seen)}; unexpected: {sorted(seen-expected)}")
    return results, errors

def main():
    if not SOURCE.is_file():
        print(f"ERROR missing {SOURCE}", file=sys.stderr)
        return 2
    rows, errors = audit(SOURCE.read_text(encoding="utf-8"))
    print("PAGE | FILLED | CAPACITY | EMPTY | SAH")
    for page, filled, capacity, empty, sah in rows:
        print(f"{page} | {filled} | {capacity} | {empty} | {sah}")
    print(f"TOTAL: {sum(x[1] for x in rows)}/{sum(x[2] for x in rows)} filled; {sum(x[3] for x in rows)} empty")
    print("P013: 12 unfilled slots are an intentional pending curriculum exception, not permission to duplicate Quran text.")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    print("Note: filled means nonempty candidate, NOT verified Quran text or approved Sah.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
