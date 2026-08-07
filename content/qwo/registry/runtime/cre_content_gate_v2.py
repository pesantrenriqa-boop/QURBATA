#!/usr/bin/env python3
"""Validate Jilid 1 page-content registry v2 against domain registries."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PAGE_REGISTRY = ROOT / "content/qwo/registry/JILID-1-PAGE-CONTENT-REGISTRY-V2.csv"
MEM_REGISTRY = ROOT / "content/qwo/registry/JILID-1-MEMORIZATION-REGISTRY-V1.csv"
AR_REGISTRY = ROOT / "content/qwo/registry/JILID-1-ARABIC-REGISTRY-V1.csv"
AK_REGISTRY = ROOT / "content/qwo/registry/JILID-1-AKHLAQ-REGISTRY-V1.csv"
AS_REGISTRY = ROOT / "content/qwo/registry/JILID-1-ASSESSMENT-REGISTRY-V1.csv"


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    pages = rows(PAGE_REGISTRY)
    mem = {r["MemorizationCode"]: r for r in rows(MEM_REGISTRY)}
    arabic = {r["ArabicCode"]: r for r in rows(AR_REGISTRY)}
    akhlaq = {r["AkhlaqCode"]: r for r in rows(AK_REGISTRY)}
    assessments = {r["AssessmentCode"]: r for r in rows(AS_REGISTRY)}

    issues: list[str] = []
    if len(pages) != 40:
        issues.append(f"PAGE_COUNT expected=40 actual={len(pages)}")
    if [int(r["Page"]) for r in pages] != list(range(1, 41)):
        issues.append("PAGE_SEQUENCE_MUST_BE_1_TO_40")

    assessment_pages: list[int] = []
    for row in pages:
        page = int(row["Page"])
        mcode = row["MemorizationCode"].strip()
        acode = row["ArabicCode"].strip()
        kcode = row["AkhlaqCode"].strip()
        scode = row["AssessmentCode"].strip()

        if mcode not in mem:
            issues.append(f"UNKNOWN_MEMORIZATION page={page} code={mcode}")
        else:
            m = mem[mcode]
            if not (int(m["StartPage"]) <= page <= int(m["MasteryPage"])):
                issues.append(f"MEMORIZATION_PAGE_RANGE page={page} code={mcode}")

        if acode not in arabic:
            issues.append(f"UNKNOWN_ARABIC page={page} code={acode}")
        else:
            a = arabic[acode]
            if not (int(a["StartPage"]) <= page <= int(a["EndPage"])):
                issues.append(f"ARABIC_PAGE_RANGE page={page} code={acode}")

        if kcode not in akhlaq:
            issues.append(f"UNKNOWN_AKHLAQ page={page} code={kcode}")
        else:
            k = akhlaq[kcode]
            if not (int(k["StartPage"]) <= page <= int(k["EndPage"])):
                issues.append(f"AKHLAQ_PAGE_RANGE page={page} code={kcode}")

        if scode != "NONE":
            assessment_pages.append(page)
            if scode not in assessments:
                issues.append(f"UNKNOWN_ASSESSMENT page={page} code={scode}")
            elif int(assessments[scode]["TargetPage"]) != page:
                issues.append(f"ASSESSMENT_PAGE_MISMATCH page={page} code={scode}")

        for field in ("MemorizationDescription", "ArabicDescription", "AkhlaqDescription", "AssessmentDescription"):
            if not row[field].strip():
                issues.append(f"DESCRIPTION_MISSING page={page} field={field}")

    if assessment_pages != [10, 20, 30, 40]:
        issues.append(f"ASSESSMENT_PAGES expected=10,20,30,40 actual={assessment_pages}")

    pending_mem_text = sum(r["ContentStatus"].strip().upper() != "VERIFIED" for r in mem.values())

    print(f"CRE_V2_PAGES={len(pages)}")
    print(f"MEMORIZATION_TARGETS={len(mem)}")
    print(f"ARABIC_TARGETS={len(arabic)}")
    print(f"AKHLAQ_TARGETS={len(akhlaq)}")
    print(f"ASSESSMENT_TARGETS={len(assessments)}")
    print(f"ASSESSMENT_PAGES={','.join(map(str, assessment_pages))}")
    print(f"MEMORIZATION_TEXT_PENDING={pending_mem_text}")
    print(f"CRE_V2_ISSUES={len(issues)}")
    if issues:
        for issue in issues[:50]:
            print("ISSUE=" + issue)
        print("CRE_CONTENT_GATE_V2=FAIL")
        return 1
    print("CRE_CONTENT_GATE_V2=PASS_REVIEW_CANDIDATE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
