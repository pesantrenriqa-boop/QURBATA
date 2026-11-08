#!/usr/bin/env python3
"""Export a read-only, prioritized QJ6 human-review queue; never grants approval."""
import csv
import importlib.util
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("qj6_audit", HERE / "audit-qj6-register.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PRIORITY = (
    "unfilled_slot", "waqf_la_msi_review_pending",
    "msi_sign_collation_pending", "research_review_pending",
    "waqf_la_glyph_missing", "source_unverified", "competency_unverified",
)
FIELDS = ("slot_id", "page_id", "kind", "competency", "review_status",
          "source_id", "source_verified", "competency_verified",
          "hold_reasons", "reviewer", "notes")


def build_queue(register=MODULE.CSV_PATH):
    report = MODULE.audit(register)
    if report["errors"]:
        raise ValueError("Structural audit failed; review queue not exported")
    reasons = defaultdict(set)
    for hold in report["release_holds"]:
        reasons[hold["slot_id"]].add(hold["reason"])
    with Path(register).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result = []
    for row in rows:
        slot_reasons = reasons.get(row["slot_id"], set())
        if not slot_reasons:
            continue
        record = {field: row.get(field, "") for field in FIELDS}
        record["hold_reasons"] = ";".join(
            sorted(slot_reasons, key=lambda reason: (
                PRIORITY.index(reason) if reason in PRIORITY else len(PRIORITY), reason
            ))
        )
        result.append(record)
    result.sort(key=lambda row: (
        min(PRIORITY.index(reason) if reason in PRIORITY else len(PRIORITY)
            for reason in row["hold_reasons"].split(";")),
        row["slot_id"],
    ))
    return result


def export(path, register=MODULE.CSV_PATH):
    rows = build_queue(register)
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Destination review CSV")
    args = parser.parse_args()
    print(f"Exported {export(args.output)} held slots; NOT approved for print")
