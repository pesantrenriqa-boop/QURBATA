#!/usr/bin/env python3
"""Export a read-only, prioritized QJ6 human-review queue; never grants approval."""
import csv
import hashlib
import json
import importlib.util
from datetime import date
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
DECISION_FIELDS = ("decision", "reviewer_name", "review_date", "mushaf_edition",
                   "evidence_reference", "tajwid_rule", "curriculum_evidence",
                   "review_notes")
FIELDS = ("slot_id", "row_sha256", "page_id", "kind", "competency", "review_status",
          "text_uthmani", "surah", "ayah_start", "ayah_end",
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
        # Fingerprint the entire source row, not the queue-derived hold reasons.
        # A reviewer must recheck evidence if any original register field changes.
        payload = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        record["row_sha256"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()
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


def validate_review_worksheet(worksheet, register=MODULE.CSV_PATH):
    """Read-only check for stale fingerprints and unsupported decisions."""
    expected = {row["slot_id"]: row for row in build_queue(register)}
    problems = []
    with Path(worksheet).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(FIELDS + DECISION_FIELDS):
            return ["Worksheet columns differ from controlled template"]
        seen = set()
        for line_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                problems.append(f"Worksheet line {line_number}: malformed CSV field count")
                continue
            ident = row["slot_id"]
            if ident in seen:
                problems.append(f"{ident}: duplicate worksheet row")
            seen.add(ident)
            source = expected.get(ident)
            if source is None:
                problems.append(f"{ident}: not in current held-slot queue")
                continue
            for field in FIELDS:
                if row[field] != source[field]:
                    problems.append(f"{ident}: stale or changed controlled field {field}")
            decision = row["decision"].strip()
            if decision not in ("", "APPROVE", "REVISE", "REJECT"):
                problems.append(f"{ident}: invalid decision {decision!r}")
            if decision == "APPROVE" and source["review_status"] == "EMPTY":
                problems.append(f"{ident}: cannot approve an unfilled slot")
            if decision == "APPROVE" and source["review_status"] == "RESEARCH":
                problems.append(f"{ident}: research slot needs a revised register before approval")
            if decision:
                raw_date = row["review_date"].strip()
                if raw_date:
                    try:
                        if date.fromisoformat(raw_date).isoformat() != raw_date:
                            raise ValueError("noncanonical date")
                    except ValueError:
                        problems.append(f"{ident}: review_date must be a real YYYY-MM-DD date")
                required = ("reviewer_name", "review_date", "mushaf_edition",
                            "evidence_reference", "tajwid_rule", "curriculum_evidence")
                for field in required:
                    value = row[field].strip()
                    if not value:
                        problems.append(f"{ident}: decision missing {field}")
                    elif value.casefold() in ("pending", "tbd", "todo", "n/a", "none", "-", "?"):
                        problems.append(f"{ident}: placeholder is not reviewer evidence for {field}")
        missing = sorted(set(expected) - seen)
        if missing:
            problems.append(f"Worksheet missing {len(missing)} held slots")
    return problems


def export(path, register=MODULE.CSV_PATH):
    rows = build_queue(register)
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


EMPTY_EVIDENCE_FIELDS = (
    "slot_id", "page_id", "competency", "proposed_surah", "proposed_ayah_start",
    "proposed_ayah_end", "mushaf_edition", "edition_page_or_link",
    "waqf_sign_position", "hafalan_unit_approval_id",
    "prerequisite_and_duplicate_check", "reviewer_name", "decision_id", "notes",
)


def export_empty_slot_evidence(path, register=MODULE.CSV_PATH):
    """Create a blank evidence-intake sheet, never proposed Quranic text."""
    with Path(register).open(encoding="utf-8-sig", newline="") as handle:
        rows = [r for r in csv.DictReader(handle) if r["review_status"] == "EMPTY"]
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=EMPTY_EVIDENCE_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                **{field: "" for field in EMPTY_EVIDENCE_FIELDS},
                "slot_id": row["slot_id"],
                "page_id": row["page_id"],
                "competency": row["competency"],
            })
    return len(rows)


def validate_empty_slot_evidence(path, register=MODULE.CSV_PATH):
    """Check evidence-intake completeness; never authenticate Quranic text."""
    with Path(register).open(encoding="utf-8-sig", newline="") as handle:
        expected = {r["slot_id"]: r for r in csv.DictReader(handle)
                    if r["review_status"] == "EMPTY"}
    errors = []
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(EMPTY_EVIDENCE_FIELDS):
            return ["Evidence intake columns differ from controlled template"]
        seen = set()
        for line_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                errors.append(f"Evidence intake line {line_number}: malformed CSV field count")
                continue
            slot = row["slot_id"]
            if slot in seen:
                errors.append(f"{slot}: duplicate slot")
            seen.add(slot)
            source = expected.get(slot)
            if source is None:
                errors.append(f"{slot}: not an empty register slot")
                continue
            if row["page_id"] != source["page_id"] or row["competency"] != source["competency"]:
                errors.append(f"{slot}: controlled page or competency changed")
            # Any entered evidence starts a proposal; do not let partial records
            # bypass checks merely because surah/ayah fields are still blank.
            proposed = any(row[f].strip() for f in EMPTY_EVIDENCE_FIELDS[3:])
            if proposed:
                common = ("proposed_surah", "proposed_ayah_start", "proposed_ayah_end",
                          "mushaf_edition", "edition_page_or_link", "reviewer_name",
                          "decision_id", "prerequisite_and_duplicate_check")
                specialized = (("waqf_sign_position",) if source["page_id"] == "QJ6-P017"
                               else ("hafalan_unit_approval_id",))
                for field in common + specialized:
                    value = row[field].strip()
                    if not value:
                        errors.append(f"{slot}: proposed evidence missing {field}")
                    elif value.casefold() in ("pending", "tbd", "todo", "n/a", "none", "-", "?"):
                        errors.append(f"{slot}: placeholder is not evidence for {field}")
                start, end = row["proposed_ayah_start"].strip(), row["proposed_ayah_end"].strip()
                if start and end:
                    if not start.isascii() or not end.isascii() or not start.isdecimal() or not end.isdecimal():
                        errors.append(f"{slot}: ayah range must use positive ASCII integers")
                    elif int(start) < 1 or int(end) < int(start):
                        errors.append(f"{slot}: invalid ayah range")
                    elif int(end) > 286:
                        errors.append(f"{slot}: ayah number exceeds Quran-wide maximum 286; verify surah-specific limit")
                surah = row["proposed_surah"].strip()
                if surah:
                    if not surah.isascii() or not surah.isdecimal():
                        errors.append(f"{slot}: surah must be a numeric ID 1-114")
                    elif not 1 <= int(surah) <= 114:
                        errors.append(f"{slot}: surah number outside 1-114")
    missing = set(expected) - seen
    if missing:
        errors.append(f"Evidence intake missing {len(missing)} empty slots")
    return errors


def export_review_worksheet(path, register=MODULE.CSV_PATH):
    """A blank reviewer form; no verification or decision is prefilled."""
    rows = build_queue(register)
    with Path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS + DECISION_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({**row, **{field: "" for field in DECISION_FIELDS}})
    return len(rows)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path, help="Destination review CSV")
    parser.add_argument("--worksheet", type=Path, help="Optional blank reviewer decision worksheet")
    parser.add_argument("--empty-evidence", type=Path, help="Optional blank evidence intake for empty slots")
    parser.add_argument("--validate-empty-evidence", type=Path, help="Check completed empty-slot evidence intake")
    parser.add_argument("--validate-worksheet", type=Path,
                        help="Validate existing worksheet without modifying it")
    args = parser.parse_args()
    if args.validate_empty_evidence:
        if args.output or args.worksheet or args.empty_evidence or args.validate_worksheet:
            parser.error("--validate-empty-evidence cannot be combined with other options")
        issues = validate_empty_slot_evidence(args.validate_empty_evidence)
        for issue in issues:
            print("ERROR:", issue)
        if issues:
            raise SystemExit(1)
        print("Evidence intake structurally valid; Quranic evidence NOT authenticated")
    elif args.validate_worksheet:
        if args.output or args.worksheet or args.empty_evidence:
            parser.error("--validate-worksheet cannot be combined with export options")
        issues = validate_review_worksheet(args.validate_worksheet)
        for issue in issues:
            print("ERROR:", issue)
        if issues:
            raise SystemExit(1)
        print("Worksheet structurally valid against current register; NOT approved for print")
    else:
        if args.output is None:
            parser.error("output is required for export")
        count = export(args.output)
        if args.worksheet:
            assert export_review_worksheet(args.worksheet) == count
        if args.empty_evidence:
            print(f"Exported {export_empty_slot_evidence(args.empty_evidence)} empty-slot evidence requests")
        print(f"Exported {count} held slots; NOT approved for print")
