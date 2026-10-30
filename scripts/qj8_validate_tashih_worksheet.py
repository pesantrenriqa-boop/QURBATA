#!/usr/bin/env python3
"""Fail closed: validate the manual Saktah tashih worksheet; never auto-approve."""
import csv
from pathlib import Path
from qj8_validate_canonical_saktah import EXPECTED

FILE=Path(__file__).resolve().parents[1]/"books/jilid-8/QJ8-LEMBAR-TASHIH-SAKTAH-2026-10-30.csv"
FIELDS={"case_id","target_refs","context_refs","rasm_uthmani_verified",
"waqf_saktah_verified","hafs_recitation_verified","source_sha256_checked",
"reviewer","review_date","decision","notes"}

def main():
    with FILE.open(encoding="utf-8-sig",newline="") as f:
        reader=csv.DictReader(f)
        assert FIELDS.issubset(reader.fieldnames or []), "Worksheet columns missing"
        rows=list(reader)
    assert len(rows)==4 and {r["case_id"] for r in rows}==set(EXPECTED), "Exactly four Saktah cases required"
    for row in rows:
        before,targets,after=EXPECTED[row["case_id"]]
        refs=([before] if before!="N/A" else [])+list(targets)+([after] if after!="N/A" else [])
        assert row["target_refs"]==";".join(targets), "Target mismatch"
        assert row["context_refs"]==";".join(refs), "Context mismatch"
        checks=[row[k] for k in ("rasm_uthmani_verified","waqf_saktah_verified",
                                  "hafs_recitation_verified","source_sha256_checked")]
        assert all(v in ("YES","NO") for v in checks), "Invalid check state"
        if row["decision"]=="APPROVED":
            assert all(v=="YES" for v in checks) and row["reviewer"] and row["review_date"], "Unreviewed case cannot be approved"
        else:
            assert row["decision"]=="HOLD", "Unexpected decision"
    print("PASS: 4 Saktah worksheet rows structurally consistent")
    print("NOTE: structural checks cannot replace independent Quranic tashih")

if __name__=="__main__":main()
