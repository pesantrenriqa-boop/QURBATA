#!/usr/bin/env python3
"""Read-only P022 Hafs source verifier. Python 3 standard library only."""
import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

EXPECTED_SHA256 = "227e6b1564d980f2bd09c2c35ebfb0330ac268c79a7c247cd1ab665bc635f245"
REFERENCES = ["105:4","88:22","50:45","6:107","2:8","34:8","83:17","29:22","21:27","2:167","2:102","11:19","7:45","27:3","6:150","21:36"]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_dataset_in_archive(archive, data):
    """Reject extracted files not byte-identical to a member of the verified ZIP."""
    if not zipfile.is_zipfile(archive):
        sys.exit("HOLD: archive is not ZIP; dataset provenance cannot be established")
    digest = sha256(data)
    with zipfile.ZipFile(archive) as z:
        for info in z.infolist():
            if info.is_dir():
                continue
            if info.file_size != data.stat().st_size:
                continue
            h = hashlib.sha256()
            with z.open(info) as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    h.update(chunk)
            if h.hexdigest() == digest:
                return info.filename
    sys.exit("HOLD: supplied dataset is not byte-identical to a member of verified archive")

def read_rows(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        if path.suffix.lower() == ".json":
            data = json.load(f)
            if isinstance(data, dict):
                data = next((v for v in data.values() if isinstance(v, list)), [])
            return data
        return list(csv.DictReader(f))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--archive", required=True, type=Path, help="Unmodified official download, for SHA-256")
    p.add_argument("--data", required=True, type=Path, help="Extracted official CSV or JSON with aya_text_unicode")
    p.add_argument("--register", required=True, type=Path, help="Jilid 4 Markdown register")
    p.add_argument("--output", required=True, type=Path, help="New JSON report")
    a = p.parse_args()
    if a.output.exists():
        sys.exit("HOLD: output report already exists; choose a fresh path to prevent stale or overwritten evidence")
    digest = sha256(a.archive)
    if digest.lower() != EXPECTED_SHA256:
        sys.exit("HOLD: SHA-256 mismatch; refusing to compare unverified source")
    source_member = verify_dataset_in_archive(a.archive, a.data)
    try:
        rows = read_rows(a.data)
    except (UnicodeError, csv.Error, json.JSONDecodeError) as exc:
        sys.exit(f"HOLD: unreadable or malformed source dataset: {exc}")
    if not isinstance(rows, list) or not rows or any(not isinstance(row, dict) for row in rows):
        sys.exit("HOLD: source dataset must contain a nonempty list of verse objects")
    index = {}
    for row in rows:
        try:
            key = (int(row["sura_no"]), int(row["aya_no"]))
            value = row["aya_text_unicode"]
        except (KeyError, TypeError, ValueError) as exc:
            sys.exit(f"HOLD: invalid source dataset row: {exc}")
        if not isinstance(value, str) or not value.strip():
            sys.exit(f"HOLD: missing Unicode verse at {key}")
        if key in index:
            sys.exit(f"HOLD: duplicate verse reference in dataset: {key}")
        index[key] = value
    lines = a.register.read_text(encoding="utf-8").splitlines()
    candidates = [x for x in lines if x.startswith("| P022 | Ikhfa syafawi |")
                  and len(x.split("|")) >= 19]
    if len(candidates) != 1:
        sys.exit(f"HOLD: expected exactly one 16-slot main P022 row; found {len(candidates)}")
    match = candidates[0]
    cells = [x.strip() for x in match.split("|")[3:19]]
    if len(cells) != 16:
        sys.exit("HOLD: expected 16 slots")
    results = []
    for i, (cell, ref) in enumerate(zip(cells, REFERENCES), 1):
        passage = cell.split(" [", 1)[0].strip()
        if not passage or passage == "—":
            sys.exit(f"HOLD: empty or placeholder slot K{i:02d}")
        cited = re.search(r"\bQS\s+(\d+):(\d+)\b", cell)
        if cited is None or f"{int(cited.group(1))}:{int(cited.group(2))}" != ref:
            sys.exit(f"HOLD: source reference mismatch at K{i:02d}; expected QS {ref}")
        verse = index.get(tuple(map(int, ref.split(":"))))
        exact = verse is not None and passage in verse
        results.append({"slot": f"K{i:02d}", "reference": ref, "exact_unicode_substring": exact,
                        "source_present": verse is not None, "status": "EXACT_MATCH" if exact else "HOLD_REVIEW"})
    a.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        with a.output.open("x", encoding="utf-8") as report:
            json.dump({"sha256_verified": True, "archive_member": source_member,
                       "screening_only": True, "print_approved": False, "slots": results},
                      report, ensure_ascii=False, indent=2)
    except FileExistsError:
        sys.exit("HOLD: output report already exists; refusing to overwrite audit evidence")
    print(f"Report saved: {a.output}; exact matches: {sum(x['exact_unicode_substring'] for x in results)}/16")
    print("Exact substring matching is a screening gate, not final rasm or print approval.")

if __name__ == "__main__":
    main()
