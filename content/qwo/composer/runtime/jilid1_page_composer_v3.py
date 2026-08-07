#!/usr/bin/env python3
"""Compose QURBATA Jilid 1 from the executable LPE contract.

V3 differences from the technical V2 prototype:
- exactly 40 instructional pages;
- page composition is controlled by the LPE composition matrix;
- 1-, 2-, and 3-unit reading objects are mixed according to progression;
- review repetition is intentional across pages but forbidden within a page;
- Awailus Suwar is forbidden;
- page 20 and 40 expose LETTER_NAMES injection metadata;
- competency codes are always paired with human-readable descriptions.

This remains a REVIEW_CANDIDATE build, not final book content.
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
DEFAULT_COMPOSITION = ROOT / "content/qwo/lpe/JILID-1-COMPOSITION-MATRIX-V1.csv"
DEFAULT_FOUNDATION = ROOT / "content/qwo/production/generated/JILID-1-FOUNDATION-OBJECTS-PUE-V1.csv"
DEFAULT_CORPUS = ROOT / "content/qwo/corpus/quran-uthmani.txt"

MARK_TO_COMPETENCY = {"َ": "C0002", "ِ": "C0003", "ُ": "C0004"}


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"MODULE_IMPORT_FAILED: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


LPE = load_module(LPE_PATH, "qurbata_lpe_v1")
PUE = load_module(PUE_PATH, "qurbata_pue_v1")
PED = load_module(PED_ENGINE_PATH, "qurbata_pedagogical_engine")


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
        return {
            row["CompetencyID"].strip(): row["Notes"].strip()
            for row in csv.DictReader(handle)
            if row.get("CompetencyID")
        }


def load_composition(path: Path) -> dict[int, dict[str, int]]:
    if not path.is_file():
        raise FileNotFoundError(path)
    rows: dict[int, dict[str, int]] = {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            page = int(row["Page"])
            values = {
                key: int(row[key])
                for key in ("L1New", "L1Review", "L2New", "L2Review", "L3New", "L3Review")
            }
            if sum(values.values()) != int(row["TotalSlots"]):
                raise ValueError(f"COMPOSITION_TOTAL_MISMATCH page={page}")
            if int(row["TotalSlots"]) != 24:
                raise ValueError(f"COMPOSITION_SLOTS_MUST_BE_24 page={page}")
            rows[page] = values
    if sorted(rows) != list(range(1, 41)):
        raise ValueError("COMPOSITION_MUST_DEFINE_PAGES_1_TO_40")
    return rows


def foundation_candidates(path: Path) -> list[Candidate]:
    if not path.is_file():
        raise FileNotFoundError(path)
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
                object_type = "LETTER"
            else:
                passed, _ = PUE.validate_short_vowel_fragment(text)
                if not passed:
                    continue
                competency = "C0005" if PUE.has_nonconnector_transition(text) else "C0006"
                object_type = "WORD_FRAGMENT"
            result.append(Candidate(row["CanonicalKey"], object_type, text, row["SourceRef"], length, competency))
    result.sort(key=lambda item: (item.unit_length, item.text, item.source_ref, item.key))
    return result


def triple_word_candidates(corpus: Path) -> list[Candidate]:
    if not corpus.is_file():
        raise FileNotFoundError(corpus)
    rules = PED.load_rules(RULES_PATH)
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
                decision = PED.validate(word, "WORD", "C0007", rules)
                if not decision.passed:
                    continue
                result.setdefault(
                    word,
                    Candidate(
                        key=f"C0007-{surah}-{ayah}-{len(result)+1:05d}",
                        object_type="WORD",
                        text=word,
                        source_ref=f"{surah}:{ayah}",
                        unit_length=3,
                        competency="C0007",
                    ),
                )
    return sorted(result.values(), key=lambda item: (item.text, item.source_ref))


def take_new(pool: list[Candidate], seen_texts: set[str], count: int) -> list[Candidate]:
    if count < 0:
        raise ValueError(f"NEW_COUNT_INVALID: {count}")
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
        # Cycling is pedagogically valid across pages, but duplicates within a page are not.
        raise ValueError(f"REVIEW_UNIQUE_POOL_SHORTAGE page={page} length={length} requested={count} available={len(previous)}")
    start = ((page - 1) * 7 + length * 11) % len(previous)
    ordered = previous[start:] + previous[:start]
    return ordered[:count]


def compose(args: argparse.Namespace) -> None:
    progression = LPE.load_progression(args.progression)
    blueprint_issues = LPE.validate_blueprint(progression)
    if blueprint_issues:
        raise ValueError("LPE_BLUEPRINT_INVALID " + " | ".join(blueprint_issues))
    composition = load_composition(Path(args.composition))
    descriptions = load_rule_descriptions()

    foundation = foundation_candidates(Path(args.foundation))
    triples = triple_word_candidates(Path(args.corpus))
    pools = {
        1: [item for item in foundation if item.unit_length == 1],
        2: [item for item in foundation if item.unit_length == 2],
        3: triples,
    }
    required_new = {
        length: sum(composition[p][f"L{length}New"] for p in range(1, 41))
        for length in (1, 2, 3)
    }
    for length in (1, 2, 3):
        if len({item.text for item in pools[length]}) < required_new[length]:
            raise ValueError(
                f"L{length}_NEW_POOL_SHORTAGE required={required_new[length]} actual={len({item.text for item in pools[length]})}"
            )

    seen: dict[int, list[Candidate]] = {1: [], 2: [], 3: []}
    seen_texts: dict[int, set[str]] = {1: set(), 2: set(), 3: set()}
    rows: list[dict[str, Any]] = []
    metadata_rows: list[dict[str, Any]] = []

    for page in range(1, 41):
        rule = progression[page]
        plan = composition[page]
        page_selected: list[tuple[Candidate, str]] = []

        # Snapshot at page start so REVIEW always means material introduced on an earlier page.
        previous = {length: list(seen[length]) for length in (1, 2, 3)}

        for length in (1, 2, 3):
            new_count = plan[f"L{length}New"]
            review_count = plan[f"L{length}Review"]
            if (new_count or review_count) and length not in rule.allowed_unit_lengths:
                raise ValueError(f"COMPOSITION_VIOLATES_LPE page={page} length={length}")
            new_items = take_new(pools[length], seen_texts[length], new_count)
            review_items = take_review(previous[length], review_count, page, length)
            page_selected.extend((item, "NEW") for item in new_items)
            page_selected.extend((item, "REVIEW") for item in review_items)
            seen[length].extend(new_items)

        if len(page_selected) != 24:
            raise ValueError(f"PAGE_SLOT_COUNT page={page} actual={len(page_selected)}")
        page_texts = [item.text for item, _ in page_selected]
        if len(page_texts) != len(set(page_texts)):
            raise ValueError(f"DUPLICATE_WITHIN_PAGE page={page}")

        competency_codes: list[str] = []
        for slot, (candidate, learning_state) in enumerate(page_selected, start=1):
            object_issues = LPE.validate_page_object(
                page=page,
                object_type=candidate.object_type,
                unit_length=candidate.unit_length,
                rules=progression,
            )
            if object_issues:
                raise ValueError("LPE_OBJECT_REJECTED " + " | ".join(object_issues))
            if candidate.competency not in competency_codes:
                competency_codes.append(candidate.competency)
            rows.append({
                "Jilid": 1,
                "Page": page,
                "PageRole": rule.page_role,
                "Slot": slot,
                "ObjectID": f"J1V3-P{page:02d}-S{slot:02d}",
                "CanonicalKey": candidate.key,
                "ObjectType": candidate.object_type,
                "ArabicObject": candidate.text,
                "UnitLength": candidate.unit_length,
                "LearningState": learning_state,
                "CompetencyCode": candidate.competency,
                "CompetencyDescription": descriptions.get(candidate.competency, ""),
                "SourceRef": candidate.source_ref,
                "SpecialInjection": rule.special_injection,
                "Status": "LPE_REVIEW_CANDIDATE_V3",
            })

        code_display = " | ".join(competency_codes)
        desc_display = " | ".join(descriptions.get(code, "") for code in competency_codes)
        metadata_issues = LPE.validate_metadata(
            page=page,
            competency_code=code_display,
            competency_description=desc_display,
            memorization_code="UNASSIGNED",
            memorization_description="Belum ditetapkan; menunggu registri hafalan Jilid 1.",
            arabic_code="UNASSIGNED",
            arabic_description="Belum ditetapkan; menunggu registri Bahasa Arab Jilid 1.",
            rules=progression,
        )
        if metadata_issues:
            raise ValueError("LPE_METADATA_REJECTED " + " | ".join(metadata_issues))
        metadata_rows.append({
            "Page": page,
            "PageRole": rule.page_role,
            "CompetencyCodes": code_display,
            "CompetencyDescriptions": desc_display,
            "MemorizationCode": "UNASSIGNED",
            "MemorizationDescription": "Belum ditetapkan; menunggu registri hafalan Jilid 1.",
            "ArabicCode": "UNASSIGNED",
            "ArabicDescription": "Belum ditetapkan; menunggu registri Bahasa Arab Jilid 1.",
            "SpecialInjection": rule.special_injection,
            "Status": "REVIEW_CANDIDATE",
        })

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    reading_output = output_dir / "JILID-1-READING-OBJECTS-V3.csv"
    reading_fields = list(rows[0].keys())
    with reading_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=reading_fields)
        writer.writeheader(); writer.writerows(rows)

    metadata_output = output_dir / "JILID-1-PAGE-METADATA-V3.csv"
    with metadata_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(metadata_rows[0].keys()))
        writer.writeheader(); writer.writerows(metadata_rows)

    audit_rows: list[dict[str, Any]] = []
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[int(row["Page"])].append(row)
    for page in range(1, 41):
        page_rows = grouped[page]
        lengths = Counter(int(row["UnitLength"]) for row in page_rows)
        states = Counter(str(row["LearningState"]) for row in page_rows)
        audit_rows.append({
            "Page": page,
            "ObjectCount": len(page_rows),
            "L1": lengths[1], "L2": lengths[2], "L3": lengths[3],
            "New": states["NEW"], "Review": states["REVIEW"],
            "SpecialInjection": progression[page].special_injection,
            "DuplicateWithinPage": len(page_rows) - len({str(row["ArabicObject"]) for row in page_rows}),
            "Status": "PASS",
        })
    audit_output = output_dir / "JILID-1-PAGE-AUDIT-SUMMARY-V3.csv"
    with audit_output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(audit_rows[0].keys()))
        writer.writeheader(); writer.writerows(audit_rows)

    report_output = output_dir / "JILID-1-COMPOSER-REPORT-V3.txt"
    report_output.write_text(
        "\n".join([
            "QURBATA JILID 1 COMPOSER V3",
            "STATUS=LPE_REVIEW_CANDIDATE_PASS",
            "PAGES=40",
            "OBJECTS_PER_PAGE=24",
            f"TOTAL_OBJECT_ROWS={len(rows)}",
            f"UNIQUE_L1_INTRODUCED={len(seen_texts[1])}",
            f"UNIQUE_L2_INTRODUCED={len(seen_texts[2])}",
            f"UNIQUE_L3_INTRODUCED={len(seen_texts[3])}",
            "AWAILUS_SUWAR=FORBIDDEN",
            "PAGE20_INJECTION=LETTER_NAMES",
            "PAGE40_INJECTION=LETTER_NAMES",
            f"READING_OUTPUT={reading_output}",
            f"METADATA_OUTPUT={metadata_output}",
            f"AUDIT_OUTPUT={audit_output}",
        ]) + "\n",
        encoding="utf-8",
    )

    print("JILID1_COMPOSER_V3=PASS")
    print("PAGES=40")
    print(f"TOTAL_OBJECT_ROWS={len(rows)}")
    print(f"UNIQUE_L1_INTRODUCED={len(seen_texts[1])}")
    print(f"UNIQUE_L2_INTRODUCED={len(seen_texts[2])}")
    print(f"UNIQUE_L3_INTRODUCED={len(seen_texts[3])}")
    print("AWAILUS_SUWAR=FORBIDDEN")
    print("PAGE20_INJECTION=LETTER_NAMES")
    print("PAGE40_INJECTION=LETTER_NAMES")
    print(f"READING_OUTPUT={reading_output}")
    print(f"METADATA_OUTPUT={metadata_output}")
    print(f"AUDIT_OUTPUT={audit_output}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--progression", default=str(DEFAULT_PROGRESSION.relative_to(ROOT)))
    parser.add_argument("--composition", default=str(DEFAULT_COMPOSITION.relative_to(ROOT)))
    parser.add_argument("--foundation", default=str(DEFAULT_FOUNDATION.relative_to(ROOT)))
    parser.add_argument("--corpus", default=str(DEFAULT_CORPUS.relative_to(ROOT)))
    parser.add_argument("--output-dir", default="content/qwo/composer/output/jilid-1-v3-lpe")
    args = parser.parse_args()
    for name in ("progression", "composition", "foundation", "corpus", "output_dir"):
        value = Path(getattr(args, name))
        setattr(args, name, value if value.is_absolute() else ROOT / value)
    compose(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
