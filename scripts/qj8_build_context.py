#!/usr/bin/env python3
"""Build a QJ8 context preview from a reviewed verse-key JSON source.
Never synthesize Qur'an text. Does not change the canonical 360-slot register.
Input JSON: {"source_id":"...", "verses":{"36:51":"...",...}}.
"""
import argparse
import csv
import json
import re
from pathlib import Path

REF = re.compile(r"^\d{1,3}:\d+$")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="books/jilid-8/QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv")
    ap.add_argument("--verses", required=True, help="JSON with source_id and verses keyed 'surah:ayah'")
    ap.add_argument("--output", required=True, help="Output markdown preview (never final)")
    args = ap.parse_args()
    data = json.loads(Path(args.verses).read_text(encoding="utf-8"))
    source_id = data.get("source_id", "").strip()
    verses = data.get("verses")
    if not source_id or not isinstance(verses, dict):
        raise SystemExit("ERROR: source_id and verses map required")
    if not all(REF.fullmatch(k) and isinstance(v, str) and v.strip() for k, v in verses.items()):
        raise SystemExit("ERROR: invalid verse key or empty text")
    with Path(args.manifest).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 33:
        raise SystemExit(f"ERROR: expected 33 manifest rows, found {len(rows)}")
    output = ["# QJ8 — Pratinjau konteks ayat (BELUM TASHIH)", "", f"Source-ID: {source_id}", "Status: DRAF / HOLD. Teks ditampilkan verbatim dari input JSON, tanpa modifikasi karakter.", ""]
    complete = 0
    for row in rows:
        before = row["before_reference"]
        targets = row["target_verse_references"].split(";")
        after = row["after_reference"]
        refs = ([before] if before != "N/A" else []) + targets + [after]
        missing = [r for r in refs if r not in verses]
        output += [f"## {row['case_id']} — {row['target_reference']}", ""]
        if missing:
            output += ["**HOLD — missing source:** " + ", ".join(missing), ""]
            continue
        complete += 1
        if before != "N/A":
            output += [f"**Sebelum ({before}):**", "", verses[before], ""]
        for ref in targets:
            output += [f"**TARGET ({ref}):**", "", verses[ref], ""]
        output += [f"**Sesudah ({after}):**", "", verses[after], "", "**Status:** belum tashih target Gharib, rasm/dabt, dan jalur Hafs.", ""]
    output.insert(4, f"Kasus dengan konteks lengkap: {complete}/{len(rows)}. Sisanya HOLD.")
    Path(args.output).write_text("\n".join(output), encoding="utf-8")
    print(f"Context complete {complete}/{len(rows)}; all output remains HOLD pending tashih.")

if __name__ == "__main__":
    main()
