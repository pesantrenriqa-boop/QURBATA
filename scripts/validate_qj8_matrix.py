#!/usr/bin/env python3
"""Read-only structural QA for QJ8's consolidated draft matrix (not Qur'an tashih)."""
import argparse
import collections
import pathlib
import re
import sys

SLOT_RE = re.compile(r"^QJ8-P(\d{3})-K(\d{2})$")
REF_RE = re.compile(r"^\d+:\d+$")
SPECIAL = {18, 28, 36, 38}
EVALUATIONS = {10, 20, 30, 40}
BAD_7616 = "قَوَارِيرَ"
GOOD_7616 = "قَوَارِيرَا۟"

def parse_matrix(path):
    entries = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.startswith("| QJ8-P"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) < 5:
            raise ValueError(f"line {line_no}: expected at least 5 columns")
        slot, arabic, ref, status, source = parts[:5]
        if not SLOT_RE.fullmatch(slot):
            raise ValueError(f"line {line_no}: invalid slot ID {slot!r}")
        entries.append((slot, arabic, ref, status, source))
    return entries

def audit(entries):
    errors, warnings = [], []
    ids = [e[0] for e in entries]
    counter = collections.Counter(ids)
    duplicates = [slot for slot, n in counter.items() if n > 1]
    if duplicates:
        errors.append(f"duplicate IDs: {duplicates[:10]}")
    expected = {f"QJ8-P{p:03d}-K{k:02d}" for p in range(1, 41) for k in range(1, 10)}
    missing, extra = expected - set(ids), set(ids) - expected
    if missing:
        errors.append(f"missing slots: {len(missing)}")
    if extra:
        errors.append(f"unexpected slots: {len(extra)}")
    if len(entries) != 360:
        errors.append(f"expected 360 slots; found {len(entries)}")
    multi_ref = 0
    bad_7616 = []
    for slot, arabic, ref, status, source in entries:
        if not arabic or not ref or not source:
            errors.append(f"{slot}: empty text/reference/source")
        if not REF_RE.fullmatch(ref):
            multi_ref += 1
        if ref == "76:16" and BAD_7616 in arabic and GOOD_7616 not in arabic:
            bad_7616.append(slot)
    if bad_7616:
        errors.append(f"76:16 legacy orthography in {bad_7616}")
    page = lambda slot: int(SLOT_RE.fullmatch(slot).group(1))
    special = sum(page(slot) in SPECIAL for slot in ids)
    evaluation = sum(page(slot) in EVALUATIONS for slot in ids)
    warnings.append("ALL excerpts remain DRAFT/HOLD: no mushaf, Hafs, reviewer, or academic approval inferred.")
    warnings.append(f"special-master-page slots: {special}; evaluation slots: {evaluation}; non-atomic references: {multi_ref}")
    return errors, warnings

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("matrix", nargs="?", default="books/jilid-8/QJ8-MATRIKS-SINKRON-360-SLOT-2026-10-29.md")
    args = parser.parse_args()
    path = pathlib.Path(args.matrix)
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    try:
        entries = parse_matrix(path)
        errors, warnings = audit(entries)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(f"QJ8 STRUCTURAL QA: {len(entries)} entries, {len(set(e[0] for e in entries))} unique IDs")
    for item in warnings:
        print(f"HOLD: {item}")
    for item in errors:
        print(f"FAIL: {item}")
    print("STRUCTURE PASS (NOT TASHIH)" if not errors else "STRUCTURE FAIL")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
