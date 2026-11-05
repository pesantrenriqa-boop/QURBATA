#!/usr/bin/env python3
"""Read-only structural and publication-gate audit for QURBATA Jilid 6."""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
import unicodedata

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
    # Each nine-slot page has exactly one curriculum target and material kind.
    # This checks internal consistency, not external curriculum authorization.
    page_targets = defaultdict(set)
    page_kinds = defaultdict(set)
    for row in rows:
        page_targets[row["page_id"]].add(row["competency"].strip())
        page_kinds[row["page_id"]].add(row["kind"])
    for page_id in sorted(page_targets):
        if len(page_targets[page_id]) != 1 or "" in page_targets[page_id]:
            errors.append(f"{page_id}: inconsistent or blank page competency")
        if len(page_kinds[page_id]) != 1:
            errors.append(f"{page_id}: mixed material kinds within page")
    empty_by_page = defaultdict(int)
    text_index = defaultdict(list)
    # These three signs have online evidence but no verse-level MSI confirmation.
    msi_pending = {
        "QJ6-P015-S01": "\u06d8",
        "QJ6-P015-S06": "\u06d8",
        "QJ6-P016-S03": "\u06da",
    }
    msi_sign_checks = []
    for r in rows:
        ident, status = r["slot_id"], r["review_status"]
        if r["kind"] not in ("tartil", "hafalan", "bahasa-arab", "akhlak-hadis"):
            errors.append(f"{ident}: unknown slot kind {r['kind']!r}; fail closed")
        if status not in ("EMPTY", "CANDIDATE", "RESEARCH"):
            errors.append(f"{ident}: unknown review_status {status!r}; fail closed")
        if ident in msi_pending:
            glyph = msi_pending[ident]
            actual = [f"U+{ord(ch):04X}" for ch in r["text_uthmani"] if ch in "\u06d8\u06da"]
            msi_sign_checks.append({"slot_id": ident, "expected": f"U+{ord(glyph):04X}", "found": actual,
                                    "source_verified": r["source_verified"],
                                    "competency_verified": r["competency_verified"]})
            if glyph not in r["text_uthmani"]:
                errors.append(f"{ident}: expected online-source sign U+{ord(glyph):04X} missing; review change")
            if r["source_verified"].lower() == "yes" or r["competency_verified"].lower() == "yes":
                warnings.append(f"{ident}: verify signed MSI verse-level evidence before treating flags as approved")
        if r["text_uthmani"].strip():
            text_index[unicodedata.normalize("NFC", r["text_uthmani"].strip())].append(ident)
        # A verified flag is not evidence by itself: require traceable review metadata.
        if r["competency_verified"].lower() == "yes" and not r["reviewer"].strip():
            errors.append(f"{ident}: competency verified without reviewer")
        if r["source_verified"].lower() == "yes" and not r["source_id"].strip():
            errors.append(f"{ident}: source verified without source_id")
        if r["page_id"] != ident[:8]:
            errors.append(f"{ident}: page_id mismatch")
        if status == "EMPTY":
            empty_by_page[r["page_id"]] += 1
            if r["text_uthmani"].strip():
                errors.append(f"{ident}: EMPTY but text exists")
        elif not r["text_uthmani"].strip():
            errors.append(f"{ident}: {status} but text missing")
        allowed_flags = ("", "no") if status == "EMPTY" else ("yes", "no")
        if (r["source_verified"].lower() not in allowed_flags
                or r["competency_verified"].lower() not in allowed_flags):
            errors.append(f"{ident}: invalid verification flag for {status}; expected {allowed_flags}")
        if status in ("CANDIDATE", "RESEARCH") and (
            r["source_verified"].lower() == "yes"
            or r["competency_verified"].lower() == "yes"
        ):
            warnings.append(f"{ident}: partial verification; still not print approved")
        if r["page_id"] == "QJ6-P017" and status != "EMPTY":
            if "لا" not in r["text_uthmani"]:
                warnings.append(f"{ident}: no explicit waqf-la glyph in text")
                if (r["source_verified"].lower() == "yes"
                        or r["competency_verified"].lower() == "yes"):
                    errors.append(f"{ident}: cannot verify waqf-la without an explicit sign in the excerpt")
        if r["page_id"] in ("QJ6-P018", "QJ6-P036") and status != "EMPTY":
            warnings.append(f"{ident}: verify official hafalan unit approval")
    # Internal source references must exist and preserve the excerpt verbatim.
    # References to later pages are curricular review flags, not data errors.
    forward_references = []
    for r in rows:
        source = r["source_id"].strip()
        if not source.startswith("QJ6-P"):
            continue
        ident = r["slot_id"]
        target = index.get(source)
        if target is None:
            errors.append(f"{ident}: internal source {source} not found")
            continue
        if r["text_uthmani"].strip() and (
            unicodedata.normalize("NFC", r["text_uthmani"].strip())
            != unicodedata.normalize("NFC", target["text_uthmani"].strip())
        ):
            errors.append(f"{ident}: internal source text differs from {source}")
        try:
            own_page = int(r["page_id"].split("-P")[1])
            source_page = int(target["page_id"].split("-P")[1])
        except (IndexError, ValueError):
            errors.append(f"{ident}: invalid page number in internal source mapping")
            continue
        if source_page > own_page:
            forward_references.append({"slot_id": ident, "source_id": source})
            warnings.append(f"{ident}: cites later-page source {source}; review prerequisites")
    # Explicit, machine-readable review queue; not a substitute for MSI tashih.
    # Never imply that a clean structural audit is publication approval.
    release_holds = [
        {"slot_id": row["slot_id"], "reason": "unfilled_slot"}
        for row in rows if row["review_status"] == "EMPTY"
    ]
    release_holds.extend(
        {"slot_id": row["slot_id"], "reason": "waqf_la_glyph_missing"}
        for row in rows
        if row["page_id"] == "QJ6-P017"
        and row["review_status"] != "EMPTY"
        and "لا" not in row["text_uthmani"]
    )
    # Pending content verification remains a publication hold even if all
    # 360 slots are populated. Source and competency approval are independent.
    release_holds.extend(
        {"slot_id": row["slot_id"], "reason": "source_unverified"}
        for row in rows
        if row["review_status"] != "EMPTY"
        and row["source_verified"].lower() != "yes"
    )
    release_holds.extend(
        {"slot_id": row["slot_id"], "reason": "competency_unverified"}
        for row in rows
        if row["review_status"] != "EMPTY"
        and row["competency_verified"].lower() != "yes"
    )
    # Research cases require an explicit expert decision independent of flags.
    release_holds.extend(
        {"slot_id": row["slot_id"], "reason": "research_review_pending"}
        for row in rows if row["review_status"] == "RESEARCH"
    )
    duplicate_text_groups = [slot_ids for slot_ids in text_index.values() if len(slot_ids) > 1]
    for slot_ids in duplicate_text_groups:
        warnings.append("Repeated text (review intentional reuse): " + ", ".join(slot_ids))
    return {
        "rows": len(rows),
        "duplicate_text_groups": len(duplicate_text_groups),
        "forward_references": forward_references,
        "msi_sign_checks": msi_sign_checks,
        "release_holds": release_holds,
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
