#!/usr/bin/env python3
"""Build a QJ8 context preview from a reviewed verse-key JSON source.
Never synthesize Qur'an text. Does not change the canonical 360-slot register.
Input JSON: {"source_id":"...", "verses":{"36:51":"...",...}}.
"""
import argparse
import csv
import json
import re
from qj8_validate_context_manifest import parse, validate
from pathlib import Path


def context_refs(before, targets, after):
    """Return only existing verse references, respecting surah boundaries."""
    return ([before] if before != "N/A" else []) + list(targets) + ([after] if after != "N/A" else [])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="books/jilid-8/QJ8-MANIFEST-KONTEKS-AYAT-2026-10-29.csv")
    ap.add_argument("--verses", required=True, help="JSON with source_id and verses keyed 'surah:ayah'")
    ap.add_argument("--output", required=True, help="Output markdown preview (never final)")
    args = ap.parse_args()
    if Path(args.output).resolve() == Path(args.verses).resolve() or Path(args.output).resolve() == Path(args.manifest).resolve():
        raise SystemExit("ERROR: output cannot overwrite source or manifest")
    data = json.loads(Path(args.verses).read_text(encoding="utf-8"))
    source_id = data.get("source_id")
    source_sha256 = data.get("source_sha256")
    source_status = data.get("status")
    verses = data.get("verses")
    if not isinstance(source_id, str) or not source_id.strip() or not isinstance(verses, dict):
        raise SystemExit("ERROR: source_id and verses map required")
    if not isinstance(source_sha256, str) or not re.fullmatch(r"[0-9a-f]{64}", source_sha256):
        raise SystemExit("ERROR: authentic source SHA-256 metadata required")
    if source_id != "TANZIL-UTHMANI-LOCAL-" + source_sha256[:16]:
        raise SystemExit("ERROR: source_id and source_sha256 mismatch")
    if data.get("source_url") != "https://tanzil.net/pub/download/index.php":
        raise SystemExit("ERROR: unexpected source provenance URL")
    if source_status != "SOURCE_IMPORTED_NOT_TASHIH":
        raise SystemExit("ERROR: source must be explicitly marked unreviewed")
    if not all(isinstance(k, str) and isinstance(v, str) and v and v == v.strip() for k, v in verses.items()):
        raise SystemExit("ERROR: invalid or altered verse text")
    try:
        for ref in verses:
            parse(ref)
        validate(args.manifest)
    except ValueError as e:
        raise SystemExit(f"ERROR: invalid references: {e}")
    with Path(args.manifest).open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 33:
        raise SystemExit(f"ERROR: expected 33 manifest rows, found {len(rows)}")
    output = ["# QJ8 — Pratinjau konteks ayat (BELUM TASHIH)", "", f"Source-ID: {source_id}", f"SHA-256 sumber (klaim metadata, belum diverifikasi ulang): {source_sha256}", "Status: DRAF / HOLD. Metadata sumber tidak membuktikan keaslian teks tanpa berkas asli dan tashih.", ""]
    complete = 0
    for row in rows:
        before = row["before_reference"]
        targets = row["target_verse_references"].split(";")
        after = row["after_reference"]
        refs = context_refs(before, targets, after)
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
        if after != "N/A":
            output += [f"**Sesudah ({after}):**", "", verses[after], ""]
        output += ["**Status:** belum tashih target Gharib, rasm/dabt, dan jalur Hafs.", ""]
    output.insert(5, f"Kasus dengan konteks lengkap: {complete}/{len(rows)}. Sisanya HOLD.")
    destination = Path(args.output)
    if destination.exists():
        raise SystemExit(f"ERROR: refusing to overwrite existing preview: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as preview:
        preview.write("\n".join(output))
    print(f"Context complete {complete}/{len(rows)}; all output remains HOLD pending tashih.")

if __name__ == "__main__":
    main()
