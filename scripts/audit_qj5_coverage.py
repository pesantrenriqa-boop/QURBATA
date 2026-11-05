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
        inactive = cells[2+capacity:18]
        if any(value not in ("", "—") for value in inactive):
            errors.append(f"{page}: inactive K slots contain data; do not count or publish")
        filled = sum(bool(c and c != "—") for c in examples)
        if page == "P013":
            # Mad farq has only a small number of Quranic occurrences.
            # Do not fill the remaining 12 slots with invented/repeated text.
            if filled > 4:
                errors.append("P013: more than four candidates; manually verify each distinct Quran locus before acceptance")
            allowed_refs = ("QS 27:59", "QS 6:143", "QS 10:59", "QS 6:144")
            seen_refs = set()
            for index, example in enumerate(examples, 1):
                if not example or example == "—":
                    continue
                # Only declared candidate sources count; a bare QS immediately
                # following its semicolon is a second unlabelled source.
                declared = re.findall(
                    r"\bKANDIDAT\s+QS\s+([^\s;\],)]+)", example
                )
                refs = ["QS " + ref for ref in declared]
                if re.search(r"\bKANDIDAT\s+QS\s+[^;\]]+;\s*QS\s+", example):
                    refs.append("ambiguous second source")
                if len(refs) != 1 or refs[0] not in allowed_refs:
                    errors.append(f"P013 K{index:02d}: expected exactly one known Mad Farq reference")
                    continue
                if refs[0] in seen_refs:
                    errors.append(f"P013 K{index:02d}: duplicate Quran locus {refs[0]}")
                seen_refs.add(refs[0])
        sah = cells[-1]
        if not re.fullmatch(r"\d+/(?:16|8)", sah):
            errors.append(f"{page}: invalid Sah counter {sah!r}")
        elif int(sah.split("/")[1]) != capacity:
            errors.append(f"{page}: Sah denominator mismatch")
        elif int(sah.split("/")[0]) > filled:
            errors.append(f"{page}: Sah count exceeds filled candidates ({filled})")
        elif page == "P013" and int(sah.split("/")[0]) > 4:
            errors.append("P013: Sah count exceeds the four distinct documented Mad Farq loci")
        results.append((page, filled, capacity, capacity-filled, sah))
    expected = {f"P{i:03d}" for i in range(1, 41)}
    if seen != expected:
        errors.append(f"missing pages: {sorted(expected-seen)}; unexpected: {sorted(seen-expected)}")
    return results, errors

def repeated_phrases(content):
    """Advisory only: exact same-page phrases, ignoring bracketed review notes."""
    groups = {}
    for line in content.splitlines():
        if not re.match(r"^\| P\d{3} \|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 19:
            continue
        page = cells[0]
        capacity = 16 if int(page[1:]) <= 20 else 8
        for index, value in enumerate(cells[2:2+capacity], 1):
            if not value or value == "—":
                continue
            phrase = value.split(" [", 1)[0].strip()
            if not phrase:
                continue
            groups.setdefault((page, phrase), []).append(f"K{index:02d}")
    return [(page, phrase, slots) for (page, phrase), slots in groups.items()
            if len(slots) > 1]

def repeated_quran_loci(content):
    """Advisory only: repeated QS references within one page."""
    groups = {}
    for line in content.splitlines():
        if not re.match(r"^\| P\d{3} \|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 19:
            continue
        page = cells[0]
        capacity = 16 if int(page[1:]) <= 20 else 8
        for index, value in enumerate(cells[2:2+capacity], 1):
            if not value or value == "—":
                continue
            # Use only the candidate's declared source, not QS mentions in review notes.
            candidate = re.search(
                r"\bKANDIDAT(?:\s+QS|\s*;\s*(?:MUROJAAH|HAFALAN UNIT)\s+QS)\s+(\d{1,3}:\d{1,3}(?:[–-]\d{1,3})?)",
                value,
            )
            if candidate:
                reference = "QS " + candidate.group(1)
                groups.setdefault((page, reference), []).append(f"K{index:02d}")
    return [(page, reference, slots) for (page, reference), slots in groups.items()
            if len(slots) > 1]

def p036_hafalan_advisory(content):
    """Report declared P036 hafalan coverage; never certify memorization."""
    line = next((s for s in content.splitlines() if s.startswith("| P036 |")), None)
    if line is None:
        return ["P036: missing hafalan row"]
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    if len(cells) != 19:
        return ["P036: malformed row; hafalan coverage cannot be assessed"]
    references = []
    for value in cells[2:10]:
        found = re.search(
            r"\bKANDIDAT\s*;\s*(?:MUROJAAH|HAFALAN UNIT)\s+QS\s+(\d{1,3}:\d{1,3})\b",
            value,
        )
        references.append(found.group(1) if found else None)
    warnings = []
    expected = ["112:1", "112:2", "112:3", "112:4",
                "113:1", "113:2", "113:3", "113:4"]
    for index, (actual, required) in enumerate(zip(references, expected), 1):
        if actual != required:
            warnings.append(
                f"P036 K{index:02d}: declared source {actual or 'missing'} "
                f"differs from documented {required}; review hafalan sequence"
            )
    if references[4:8] == ["113:1", "113:2", "113:3", "113:4"]:
        warnings.append(
            "P036: QS 113:1-4 are present, but QS 113:5 is not in the active "
            "P036 slots; do not mark Al-Falaq complete without a documented continuation"
        )
    return warnings

def qj5_alfalaq_completion_advisory(content):
    """Check declared candidate sources across Jilid 5, not QS mentions in notes."""
    declared = set()
    for line in content.splitlines():
        if not re.match(r"^\| P\d{3} \|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 19:
            continue
        capacity = 16 if int(cells[0][1:]) <= 20 else 8
        for value in cells[2:2 + capacity]:
            match = re.search(
                r"\[\s*KANDIDAT(?:\s+QS|\s*;\s*(?:MUROJAAH|HAFALAN UNIT)\s+QS)"
                r"\s+(\d{1,3}:\d{1,3})\b", value
            )
            if match:
                declared.add(match.group(1))
    if "113:5" not in declared:
        return ["Jilid 5: QS 113:5 has no declared active candidate source; "
                "audit notes alone do not establish hafalan completion"]
    return []

def qj5_alfalaq_source_locations(content):
    """List declared QS 113:5 candidate slots; not evidence of completed hafalan."""
    locations = []
    for line in content.splitlines():
        if not re.match(r"^\| P\d{3} \|", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != 19:
            continue
        page = cells[0]
        capacity = 16 if int(page[1:]) <= 20 else 8
        for index, value in enumerate(cells[2:2 + capacity], 1):
            if re.search(r"\[\s*KANDIDAT\s+QS\s+113:5\b", value):
                locations.append(f"{page} K{index:02d}")
    return locations

def main():
    if not SOURCE.is_file():
        print(f"ERROR missing {SOURCE}", file=sys.stderr)
        return 2
    content = SOURCE.read_text(encoding="utf-8")
    rows, errors = audit(content)
    print("PAGE | FILLED | CAPACITY | EMPTY | SAH")
    for page, filled, capacity, empty, sah in rows:
        print(f"{page} | {filled} | {capacity} | {empty} | {sah}")
    print(f"TOTAL: {sum(x[1] for x in rows)}/{sum(x[2] for x in rows)} filled; {sum(x[3] for x in rows)} empty")
    p013 = next((row for row in rows if row[0] == "P013"), None)
    if p013 is not None:
        print(f"P013: {p013[3]} unfilled slots; pending curriculum review. "
              "Empty slots are not permission to duplicate Quran text.")
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    duplicates = repeated_phrases(content)
    print(f"ADVISORY: {len(duplicates)} exact same-page phrase groups (not CI errors).")
    for page, phrase, slots in duplicates:
        print(f"ADVISORY {page} {','.join(slots)}: {phrase}")
    source_duplicates = repeated_quran_loci(content)
    print(f"ADVISORY: {len(source_duplicates)} repeated same-page Quran reference groups.")
    for page, reference, slots in source_duplicates:
        print(f"ADVISORY SOURCE {page} {','.join(slots)}: {reference}")
    for warning in p036_hafalan_advisory(content):
        print("ADVISORY HAFALAN:", warning)
    locations = qj5_alfalaq_source_locations(content)
    print("INFO QS 113:5 reading candidates:", ", ".join(locations) or "none",
          "(not proof of P036 hafalan completion)")
    for warning in qj5_alfalaq_completion_advisory(content):
        print("ADVISORY HAFALAN:", warning)
    print("Note: filled means nonempty candidate, NOT verified Quran text or approved Sah.")
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
