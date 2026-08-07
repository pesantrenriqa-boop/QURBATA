#!/usr/bin/env python3
"""QURBATA Jilid 1 Composer v4.

Major changes from v3:
- pages 20 and 40 are dedicated LETTER_NAMES pages with zero reading objects;
- reading rows exist on 38 pages only (38 x 24 = 912);
- L1/L2 candidates must pass the authoritative pedagogical rule matrix, preventing
  non-canonical early-letter forms from entering merely because Unicode parsing succeeds;
- new/review ratios use JILID-1-COMPOSITION-MATRIX-V2.csv;
- letter-name content is sourced from JILID-1-LETTER-NAME-REGISTRY-V1.csv;
- Awailus Suwar remains forbidden.

This remains REVIEW_CANDIDATE content.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
LPE_PATH = ROOT / "content/qwo/lpe/runtime/lpe_engine_v1.py"
PUE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_unit_engine.py"
PED_ENGINE_PATH = ROOT / "content/qwo/pedagogy/runtime/pedagogical_engine.py"
RULES_PATH = ROOT / "content/qwo/pedagogy/PEDAGOGICAL-RULE-MATRIX-V1.csv"
DEFAULT_PROGRESSION = ROOT / "content/qwo/lpe/JILID-1-40-PAGE-PROGRESSION-V2.csv"
DEFAULT_COMPOSITION = ROOT / "content/qwo/lpe/JILID-1-COMPOSITION-MATRIX-V2.csv"
DEFAULT_FOUNDATION = ROOT / "content/qwo/production/generated/JILID-1-FOUNDATION-OBJECTS-PUE-V1.csv"
DEFAULT_CORPUS = ROOT / "content/qwo/corpus/quran-uthmani.txt"
DEFAULT_LETTER_NAMES = ROOT / "content/qwo/lpe/JILID-1-LETTER-NAME-REGISTRY-V1.csv"
SPECIAL_PAGES = {20, 40}
MARK_TO_COMPETENCY = {"َ": "C0002", "ِ": "C0003", "ُ": "C0004"}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


LPE = load_module(LPE_PATH, "qurbata_lpe_v1_v4")
PUE = load_module(PUE_PATH, "qurbata_pue_v1_v4")
PED = load_module(PED_ENGINE_PATH, "qurbata_pedagogical_engine_v4")
PED_RULES = PED.load_rules(RULES_PATH)


@dataclass(frozen=True)
class Candidate:
    key: str
    object_type: str
    text: str
    source_ref: str
    unit_length: int
    competency: str


def load_rule_descriptions() -> dict[str, str]:
    with RULES_PATH.open(encoding="utf-8-sig", newline="") as handle:
        return {row["CompetencyID"].strip(): row["Notes"].strip() for row in csv.DictReader(handle) if row.get("CompetencyID")}


def load_composition(path: Path, progression: dict[int, Any]) -> dict[int, dict[str, int]]:
    rows: dict[int, dict[str, int]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            page = int(row["Page"])
            values = {key: int(row[key]) for key in ("L1New", "L1Review", "L2New", "L2Review", "L3New", "L3Review")}
            total = int(row["TotalSlots"])
            if sum(values.values()) != total:
                raise ValueError(f"COMPOSITION_TOTAL_MISMATCH page={page}")
            expected_total = 0 if page in SPECIAL_PAGES else 24
            if total != expected_total:
                raise ValueError(f"COMPOSITION_SLOT_POLICY page={page} expected={expected_total} actual={total}")
            if page in SPECIAL_PAGES and progression[page].special_injection != "LETTER_NAMES":
                raise ValueError(f"SPECIAL_PAGE_INJECTION_MISMATCH page={page}")
            rows[page] = values
    if sorted(rows) != list(range(1, 41)):
        raise ValueError("COMPOSITION_MUST_DEFINE_PAGES_1_TO_40")
    return rows


def foundation_candidates(path: Path) -> list[Candidate]:
    result: list[Candidate] = []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            text = unicodedata.normalize("NFC", row["Text"].strip())
            units = PUE.grapheme_units(text)
            length = len(units)
            if length not in {1, 2}:
                continue
            if length == 1:
                decision = PUE.validate_short_vowel_unit(units[0])
                if not decision.passed:
                    continue
                competency = MARK_TO_COMPETENCY.get(decision.marks[0])
                if not competency:
                    continue
                if not PED.validate(text, "LETTER", competency, PED_RULES).passed:
                    continue
                object_type = "LETTER"
            else:
                passed, _ = PUE.validate_short_vowel_fragment(text)
                if not passed:
                    continue
                competency = "C0005" if PUE.has_nonconnector_transition(text) else "C0006"
                if not PED.validate(text, "WORD_FRAGMENT", competency, PED_RULES).passed:
                    continue
                object_type = "WORD_FRAGMENT"
            result.append(Candidate(row["CanonicalKey"], object_type, text, row["SourceRef"], length, competency))
    # Deduplicate visible surface objects before composition.
    unique: dict[tuple[int, str], Candidate] = {}
    for item in result:
        unique.setdefault((item.unit_length, item.text), item)
    return sorted(unique.values(), key=lambda item: (item.unit_length, item.text, item.source_ref, item.key))


def triple_word_candidates(corpus: Path) -> list[Candidate]:
    result: dict[str, Candidate] = {}
    with corpus.open(encoding="utf-8-sig") as handle:
        for raw in handle:
            line = raw.rstrip("\r\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("|", 2)
            if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
                continue
            surah, ayah, ayah_text = parts
            for word in ayah_text.split():
                word = unicodedata.normalize("NFC", word)
                units = PUE.grapheme_units(word)
                if len(units) != 3:
                    continue
                if not all(PUE.validate_short_vowel_unit(unit).passed for unit in units):
                    continue
                if not PED.validate(word, "WORD", "C0007", PED_RULES).passed:
                    continue
                result.setdefault(word, Candidate(f"C0007-{surah}-{ayah}-{len(result)+1:05d}", "WORD", word, f"{surah}:{ayah}", 3, "C0007"))
    return sorted(result.values(), key=lambda item: (item.text, item.source_ref))


def load_letter_names(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 28:
        raise ValueError(f"LETTER_NAME_REGISTRY_COUNT expected=28 actual={len(rows)}")
    page_counts = Counter(int(row["TargetPage"]) for row in rows)
    if page_counts != Counter({20: 14, 40: 14}):
        raise ValueError(f"LETTER_NAME_PAGE_DISTRIBUTION actual={dict(page_counts)}")
    return rows


def take_new(pool: list[Candidate], seen_texts: set[str], count: int) -> list[Candidate]:
    if count < 0:
        raise ValueError(f"NEW_COUNT_NEGATIVE count={count}")
    if count == 0:
        return []
    selected: list[Candidate] = []
    for candidate in pool:
        if candidate.text in seen_texts:
            continue
        selected.append(candidate)
        seen_texts.add(candidate.text)
        if len(selected) == count:
            break
    if len(selected) != count:
        raise ValueError(f"NEW_POOL_SHORTAGE requested={count} actual={len(selected)}")
    return selected


def take_review(previous: list[Candidate], count: int, page: int, length: int) -> list[Candidate]:
    if count == 0:
        return []
    if not previous:
        raise ValueError(f"REVIEW_BEFORE_INTRODUCTION page={page} length={length}")
    if count > len(previous):
        raise ValueError(f"REVIEW_UNIQUE_POOL_SHORTAGE page={page} length={length} requested={count} available={len(previous)}")
    start = ((page - 1) * 7 + length * 11) % len(previous)
    return (previous[start:] + previous[:start])[:count]


def compose(args: argparse.Namespace) -> None:
    progression = LPE.load_progression(args.progression)
    issues = LPE.validate_blueprint(progression)
    if issues:
        raise ValueError("LPE_BLUEPRINT_INVALID " + " | ".join(issues))
    composition = load_composition(Path(args.composition), progression)
    descriptions = load_rule_descriptions()
    letter_names = load_letter_names(Path(args.letter_names))

    foundation = foundation_candidates(Path(args.foundation))
    triples = triple_word_candidates(Path(args.corpus))
    pools = {1: [x for x in foundation if x.unit_length == 1], 2: [x for x in foundation if x.unit_length == 2], 3: triples}
    required_new = {length: sum(composition[p][f"L{length}New"] for p in range(1, 41)) for length in (1, 2, 3)}
    for length in (1, 2, 3):
        available = len({item.text for item in pools[length]})
        if available < required_new[length]:
            raise ValueError(f"L{length}_NEW_POOL_SHORTAGE required={required_new[length]} actual={available}")

    seen: dict[int, list[Candidate]] = {1: [], 2: [], 3: []}
    seen_texts: dict[int, set[str]] = {1: set(), 2: set(), 3: set()}
    reading_rows: list[dict[str, Any]] = []
    metadata_rows: list[dict[str, Any]] = []

    for page in range(1, 41):
        rule = progression[page]
        plan = composition[page]
        if page in SPECIAL_PAGES:
            metadata_rows.append({
                "Page": page, "PageRole": rule.page_role,
                "CompetencyCodes": "LETTER_NAMES",
                "CompetencyDescriptions": "Mengenal dan menyebut nama huruf hijaiyah.",
                "MemorizationCode": "UNASSIGNED",
                "MemorizationDescription": "Belum ditetapkan; menunggu registri hafalan Jilid 1.",
                "ArabicCode": "UNASSIGNED",
                "ArabicDescription": "Belum ditetapkan; menunggu registri Bahasa Arab Jilid 1.",
                "SpecialInjection": "LETTER_NAMES", "Status": "REVIEW_CANDIDATE",
            })
            continue

        previous = {length: list(seen[length]) for length in (1, 2, 3)}
        page_selected: list[tuple[Candidate, str]] = []
        for length in (1, 2, 3):
            new_count, review_count = plan[f"L{length}New"], plan[f"L{length}Review"]
            if (new_count or review_count) and length not in rule.allowed_unit_lengths:
                raise ValueError(f"COMPOSITION_VIOLATES_LPE page={page} length={length}")
            new_items = take_new(pools[length], seen_texts[length], new_count)
            review_items = take_review(previous[length], review_count, page, length)
            page_selected.extend((item, "NEW") for item in new_items)
            page_selected.extend((item, "REVIEW") for item in review_items)
            seen[length].extend(new_items)

        if len(page_selected) != 24:
            raise ValueError(f"PAGE_SLOT_COUNT page={page} actual={len(page_selected)}")
        if len({item.text for item, _ in page_selected}) != 24:
            raise ValueError(f"DUPLICATE_WITHIN_PAGE page={page}")

        competency_codes: list[str] = []
        for slot, (candidate, state) in enumerate(page_selected, 1):
            object_issues = LPE.validate_page_object(page=page, object_type=candidate.object_type, unit_length=candidate.unit_length, rules=progression)
            if object_issues:
                raise ValueError("LPE_OBJECT_REJECTED " + " | ".join(object_issues))
            if candidate.competency not in competency_codes:
                competency_codes.append(candidate.competency)
            reading_rows.append({
                "Jilid": 1, "Page": page, "PageRole": rule.page_role, "Slot": slot,
                "ObjectID": f"J1V4-P{page:02d}-S{slot:02d}", "CanonicalKey": candidate.key,
                "ObjectType": candidate.object_type, "ArabicObject": candidate.text,
                "UnitLength": candidate.unit_length, "LearningState": state,
                "CompetencyCode": candidate.competency,
                "CompetencyDescription": descriptions.get(candidate.competency, ""),
                "SourceRef": candidate.source_ref, "SpecialInjection": rule.special_injection,
                "Status": "LPE_REVIEW_CANDIDATE_V4",
            })

        code_display = " | ".join(competency_codes)
        desc_display = " | ".join(descriptions.get(code, "") for code in competency_codes)
        metadata_rows.append({
            "Page": page, "PageRole": rule.page_role, "CompetencyCodes": code_display,
            "CompetencyDescriptions": desc_display, "MemorizationCode": "UNASSIGNED",
            "MemorizationDescription": "Belum ditetapkan; menunggu registri hafalan Jilid 1.",
            "ArabicCode": "UNASSIGNED", "ArabicDescription": "Belum ditetapkan; menunggu registri Bahasa Arab Jilid 1.",
            "SpecialInjection": rule.special_injection, "Status": "REVIEW_CANDIDATE",
        })

    injection_rows = [{
        "Page": int(row["TargetPage"]), "Sequence": int(row["Sequence"]), "ContentType": "LETTER_NAME",
        "Letter": row["Letter"], "LetterNameArabic": row["LetterNameArabic"], "Status": row.get("Status", "REVIEW_CANDIDATE")
    } for row in letter_names]

    output_dir = Path(args.output_dir); output_dir.mkdir(parents=True, exist_ok=True)
    def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys())); writer.writeheader(); writer.writerows(rows)

    reading_output = output_dir / "JILID-1-READING-OBJECTS-V4.csv"
    metadata_output = output_dir / "JILID-1-PAGE-METADATA-V4.csv"
    injection_output = output_dir / "JILID-1-INJECTION-CONTENT-V4.csv"
    write_csv(reading_output, reading_rows); write_csv(metadata_output, metadata_rows); write_csv(injection_output, injection_rows)

    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in reading_rows: grouped[int(row["Page"])].append(row)
    audit_rows: list[dict[str, Any]] = []
    for page in range(1, 41):
        page_rows = grouped.get(page, [])
        lengths = Counter(int(row["UnitLength"]) for row in page_rows)
        states = Counter(str(row["LearningState"]) for row in page_rows)
        audit_rows.append({"Page": page, "ObjectCount": len(page_rows), "L1": lengths[1], "L2": lengths[2], "L3": lengths[3], "New": states["NEW"], "Review": states["REVIEW"], "SpecialInjection": progression[page].special_injection, "DuplicateWithinPage": len(page_rows)-len({str(r["ArabicObject"]) for r in page_rows}), "Status": "PASS"})
    audit_output = output_dir / "JILID-1-PAGE-AUDIT-SUMMARY-V4.csv"; write_csv(audit_output, audit_rows)

    report = output_dir / "JILID-1-COMPOSER-REPORT-V4.txt"
    report.write_text("\n".join([
        "QURBATA JILID 1 COMPOSER V4", "STATUS=LPE_REVIEW_CANDIDATE_PASS", "INSTRUCTIONAL_PAGES=40",
        "READING_PAGES=38", "DEDICATED_LETTER_NAME_PAGES=20|40", f"TOTAL_READING_ROWS={len(reading_rows)}",
        f"LETTER_NAME_ROWS={len(injection_rows)}", f"UNIQUE_L1_INTRODUCED={len(seen_texts[1])}",
        f"UNIQUE_L2_INTRODUCED={len(seen_texts[2])}", f"UNIQUE_L3_INTRODUCED={len(seen_texts[3])}",
        "AWAILUS_SUWAR=FORBIDDEN", f"READING_OUTPUT={reading_output}", f"METADATA_OUTPUT={metadata_output}",
        f"INJECTION_OUTPUT={injection_output}", f"AUDIT_OUTPUT={audit_output}"]) + "\n", encoding="utf-8")

    print("JILID1_COMPOSER_V4=PASS")
    print("INSTRUCTIONAL_PAGES=40")
    print("READING_PAGES=38")
    print(f"TOTAL_READING_ROWS={len(reading_rows)}")
    print(f"LETTER_NAME_ROWS={len(injection_rows)}")
    print("PAGE20_READING_OBJECTS=0")
    print("PAGE40_READING_OBJECTS=0")
    print("AWAILUS_SUWAR=FORBIDDEN")
    print(f"READING_OUTPUT={reading_output}")
    print(f"METADATA_OUTPUT={metadata_output}")
    print(f"INJECTION_OUTPUT={injection_output}")
    print(f"AUDIT_OUTPUT={audit_output}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--progression", default=str(DEFAULT_PROGRESSION.relative_to(ROOT)))
    parser.add_argument("--composition", default=str(DEFAULT_COMPOSITION.relative_to(ROOT)))
    parser.add_argument("--foundation", default=str(DEFAULT_FOUNDATION.relative_to(ROOT)))
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS.relative_to(ROOT)))
    parser.add_argument("--letter-names", default=str(DEFAULT_LETTER_NAMES.relative_to(ROOT)))
    parser.add_argument("--output-dir", default="content/qwo/composer/output/jilid-1-v4-lpe")
    args = parser.parse_args()
    for name in ("progression", "composition", "foundation", "corpus", "letter_names", "output_dir"):
        value = Path(getattr(args, name)); setattr(args, name, value if value.is_absolute() else ROOT / value)
    compose(args); return 0

if __name__ == "__main__":
    raise SystemExit(main())
