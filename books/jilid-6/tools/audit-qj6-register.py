#!/usr/bin/env python3
"""Read-only structural and publication-gate audit for QURBATA Jilid 6."""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

CSV_PATH = Path(__file__).with_name("QJ6-slots.csv")
EXPECTED_FIELDS = [
    "slot_id", "page_id", "competency", "kind", "text_uthmani",
    "surah", "ayah_start", "ayah_end", "source_id", "source_verified",
    "competency_verified", "reviewer", "review_status", "notes",
]


def audit(path=CSV_PATH):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_FIELDS:
            raise ValueError(f"Unexpected columns: {reader.fieldnames}")
        rows = list(reader)
    errors = []
    warnings = []
    if len(rows) != 360:
        errors.append(f"Expected 360 rows, found {len(rows)}")
    ids = [r["slot_id"] for r in rows]
    for ident, count in Counter(ids).items():
        if count != 1:
            errors.append(f"Duplicate slot_id {ident}: {count}")
    index = {r["slot_id"]: r for r in rows}
    missing = []
    for page in range(1, 41):
        for slot in range(1, 10):
            ident = f"QJ6-P{page:03d}-S{slot:02d}"
            if ident not in index:
                missing.append(ident)
    if missing:
        errors.append(f"Missing expected slot IDs: {missing}")
    empty_by_page = defaultdict(int)
    for r in rows:
        ident, status = r["slot_id"], r["review_status"]
        if r["page_id"] != ident[:8]:
            errors.append(f"{ident}: page_id mismatch")
        if status == "EMPTY":
            empty_by_page[r["page_id"]] += 1
            if r["text_uthmani"].strip():
                errors.append(f"{ident}: EMPTY but text exists")
        elif not r["text_uthmani"].strip():
            errors.append(f"{ident}: {status} but text missing")
        if status in ("CANDIDATE", "RESEARCH") and (
            r["source_verified"].lower() == "yes"
            or r["competency_verified"].lower() == "yes"
        ):
            warnings.append(f"{ident}: partial verification; still not print approved")
        if r["page_id"] == "QJ6-P017" and status != "EMPTY":
            if "لا" not in r["text_uthmani"]:
                warnings.append(f"{ident}: no explicit waqf-la glyph in text")
        if r["page_id"] in ("QJ6-P018", "QJ6-P036") and status != "EMPTY":
            warnings.append(f"{ident}: verify official hafalan unit approval")
    return {
        "rows": len(rows),
        "filled": len(rows) - sum(empty_by_page.values()),
        "empty": sum(empty_by_page.values()),
        "empty_by_page": dict(sorted(empty_by_page.items())),
        "errors": errors,
        "warnings": warnings,
        "print_approved": False,
    }


if __name__ == "__main__":
    result = audit()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if result["errors"] else 0)
