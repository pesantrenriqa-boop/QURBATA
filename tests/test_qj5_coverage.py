"""Regression tests for the read-only Jilid 5 coverage auditor."""
import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("qj5_coverage", ROOT / "scripts/audit_qj5_coverage.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

REGISTER = ROOT / "02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_5.md"

class CoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = REGISTER.read_text(encoding="utf-8")

    def test_p040_tashih_worksheet_matches_current_candidate_sources(self):
        # Guard against a stale human-review worksheet after register edits.
        worksheet_path = ROOT / (
            "02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/"
            "LEMBAR_TASHIH_P040_JILID_5.md"
        )
        worksheet = worksheet_path.read_text(encoding="utf-8")
        register_row = next(
            line for line in self.original.splitlines()
            if line.startswith("| P040 |")
        )
        cells = [cell.strip() for cell in register_row.strip("|").split("|")]
        for index, candidate in enumerate(cells[2:10], 1):
            with self.subTest(slot=index):
                match = __import__("re").search(
                    r"\[KANDIDAT QS (\d{1,3}:\d{1,3})(?![\w:–-])",
                    candidate,
                )
                self.assertIsNotNone(match, "P040 source label missing")
                slot = f"K{index:02d}"
                worksheet_rows = [
                    line for line in worksheet.splitlines()
                    if line.startswith(f"| {slot} |")
                ]
                self.assertEqual(len(worksheet_rows), 1)
                source = worksheet_rows[0].split("|")[2].strip()
                self.assertEqual(source, "QS " + match.group(1))
        self.assertIn("Izin pembaruan register:", worksheet)
        self.assertIn("Status Sah:", worksheet)

    def test_p040_sah_stays_zero_until_worksheet_authorizes_update(self):
        # Never certify Quran candidates while human tashih approval is pending.
        worksheet = (ROOT / "02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/"
                     "LEMBAR_TASHIH_P040_JILID_5.md").read_text(encoding="utf-8")
        row = next(line for line in self.original.splitlines()
                   if line.startswith("| P040 |"))
        sah = row.strip("|").split("|")[-1].strip()
        if "Izin pembaruan register: **BELUM DIBERIKAN**" in worksheet:
            self.assertEqual(
                sah, "0/8",
                "P040 Sah must stay zero until human approval is documented"
            )

    def test_original_has_40_pages_and_consistent_capacity(self):
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        self.assertEqual(len(rows), 40)
        self.assertEqual(sum(r[2] for r in rows), 480)
        self.assertEqual(sum(r[1] + r[3] for r in rows), 480)
        self.assertEqual(next(r for r in rows if r[0] == "P013")[2], 16)
        # Do not hardcode 468/12: valid future candidate edits must not break CI.

    def test_non_quran_sources_remain_explicitly_classified(self):
        # P028 is Arabic-language practice; P038 K01-K03 are hadith.
        # Neither category should be mislabeled as Quranic verse evidence.
        rows = {
            line.split("|")[1].strip(): [
                cell.strip() for cell in line.strip().strip("|").split("|")
            ]
            for line in self.original.splitlines()
            if line.startswith("| P028 |") or line.startswith("| P038 |")
        }
        self.assertEqual(set(rows), {"P028", "P038"})
        for index, example in enumerate(rows["P028"][2:10], 1):
            with self.subTest(page="P028", slot=index):
                self.assertIn("BAHASA ARAB", example)
                self.assertIn("BUKAN AYAT", example)
                self.assertNotIn("KANDIDAT QS", example)
        for index, example in enumerate(rows["P038"][2:5], 1):
            with self.subTest(page="P038", slot=index):
                self.assertIn("KANDIDAT HADIS", example)
                self.assertNotIn("KANDIDAT QS", example)

        for index, example in enumerate(rows["P038"][5:10], 4):
            with self.subTest(page="P038", slot=index):
                self.assertIn("KANDIDAT QS", example)
                self.assertNotIn("KANDIDAT HADIS", example)

    def test_duplicate_page_rejected(self):
        line = next(s for s in self.original.splitlines() if s.startswith("| P013 |"))
        _, errors = module.audit(self.original + "\n" + line)
        self.assertTrue(any("duplicate page" in e for e in errors))

    def test_unreferenced_p013_candidate_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                # K03 is a blank cell; replace only that slot.
                self.assertEqual(cells[5].strip(), "—")
                cells[5] = " kandidat tanpa rujukan "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_duplicate_mad_farq_locus_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                # Duplicate the known QS 27:59 reference in K03.
                cells[5] = " آللَّهُ خَيْرٌ [KANDIDAT QS 27:59] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("duplicate Quran locus" in e for e in errors))

    def test_sah_cannot_exceed_filled_candidates(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                lines[i] = line.replace("| 0/16 |", "| 5/16 |")
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("Sah count exceeds filled candidates" in e for e in errors))

    def test_inactive_slot_on_later_page_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                self.assertEqual(cells[11].strip(), "—")
                cells[11] = " kandidat tidak aktif "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("inactive K slots contain data" in e for e in errors))

    def test_p013_rejects_unapproved_quran_locus(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:590] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_multiple_references_in_one_slot(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59; QS 6:143] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_reference_with_letter_suffix(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59abc] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_reference_with_extra_colon(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59:2] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_p013_rejects_hidden_malformed_second_reference(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = " contoh uji [KANDIDAT QS 27:59; QS 27:590] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("expected exactly one known Mad Farq reference" in e for e in errors))

    def test_repeated_phrases_are_advisory_only(self):
        groups = module.repeated_phrases(self.original)
        self.assertTrue(any(page == "P016" and slots == ["K03", "K04"]
                            for page, _, slots in groups))
        self.assertTrue(any(page == "P013" and slots == ["K02", "K07"]
                            for page, _, slots in groups))
        _, errors = module.audit(self.original)
        self.assertFalse(errors, errors)

    def test_repeated_phrases_ignore_inactive_and_review_notes(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [review A]"
                cells[4] = "نَصٌّ [review B]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_phrases("\n".join(lines))
        self.assertTrue(any(page == "P040" and slots == ["K01", "K02"]
                            for page, _, slots in groups))

    def test_repeated_quran_loci_are_advisory(self):
        groups = module.repeated_quran_loci(self.original)
        self.assertTrue(any(page == "P016" and reference == "QS 106:3"
                            and {"K03", "K04", "K05"}.issubset(set(slots))
                            for page, reference, slots in groups))
        self.assertTrue(any(page == "P011" and reference == "QS 80:33"
                            and {"K04", "K12"}.issubset(set(slots))
                            for page, reference, slots in groups))
        _, errors = module.audit(self.original)
        self.assertFalse(errors, errors)

    def test_source_advisory_ignores_review_note_cross_references(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [KANDIDAT QS 17:70; AUDIT: lihat QS 2:2]"
                cells[4] = "نَصٌّ آخر [KANDIDAT QS 2:3; AUDIT: lihat QS 2:2]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups))

    def test_source_advisory_is_not_a_sah_decision(self):
        groups = module.repeated_quran_loci(self.original)
        self.assertTrue(groups)
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        self.assertEqual(next(row for row in rows if row[0] == "P013")[4], "0/16")

    def test_current_duplicate_baseline_requires_review_not_auto_replacement(self):
        # Snapshot of advisory group counts for the current 40-page register.
        # Any future change must be reviewed; counts are not acceptance criteria.
        text_groups = module.repeated_phrases(self.original)
        source_groups = module.repeated_quran_loci(self.original)
        self.assertEqual(len(text_groups), 9)
        self.assertEqual(len(source_groups), 18)
        self.assertTrue(any(page == "P040" and reference == "QS 17:70"
                            and slots == ["K03", "K06"]
                            for page, reference, slots in source_groups))

    def test_p040_identical_exam_items_remain_visible_for_human_review(self):
        # A repeated final-exam item is an advisory, never automatic permission
        # to replace Quran text or increase Sah.
        duplicates = module.repeated_phrases(self.original)
        self.assertTrue(any(
            page == "P040" and slots == ["K03", "K06"]
            for page, _phrase, slots in duplicates
        ))
        source_duplicates = module.repeated_quran_loci(self.original)
        self.assertTrue(any(
            page == "P040" and reference == "QS 17:70"
            and slots == ["K03", "K06"]
            for page, reference, slots in source_duplicates
        ))
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        self.assertEqual(next(row for row in rows if row[0] == "P040")[4], "0/8")

    def test_source_advisory_rejects_malformed_reference_suffixes(self):
        # A malformed source label must not inflate a duplicate-QS advisory.
        for malformed in ("17:70a", "17:70:1", "17:70_1"):
            with self.subTest(reference=malformed):
                lines = self.original.splitlines()
                for index, line in enumerate(lines):
                    if line.startswith("| P040 |"):
                        cells = line.split("|")
                        cells[5] = f"نَصٌّ [KANDIDAT QS {malformed}]"  # K03: split includes leading empty cell
                        lines[index] = "|".join(cells)
                        break
                duplicates = module.repeated_quran_loci("\n".join(lines))
                self.assertFalse(any(
                    page == "P040" and reference == "QS 17:70"
                    and slots == ["K03", "K06"]
                    for page, reference, slots in duplicates
                ))

    def test_source_advisory_ignores_quoted_candidate_label(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [AUDIT: tulisan KANDIDAT QS 2:2 hanya kutipan]"
                cells[4] = "نَصٌّ آخر [AUDIT: tulisan KANDIDAT QS 2:2 hanya kutipan]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups), groups)

    def test_source_advisory_does_not_count_bare_qs_in_notes(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "نَصٌّ [AUDIT: QS 2:2; tanpa label KANDIDAT]"
                cells[4] = "نَصٌّ آخر [AUDIT: QS 2:2; tanpa label KANDIDAT]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups))

    def test_source_advisory_does_not_read_inactive_slots(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[11] = "uji [KANDIDAT QS 2:2]"
                cells[12] = "uji [KANDIDAT QS 2:2]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertFalse(any(page == "P040" and reference == "QS 2:2"
                             for page, reference, _ in groups))
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("inactive K slots" in e for e in errors))

    def test_source_advisory_finds_candidate_after_audit_note(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "أَوَّلٌ [AUDIT: periksa waqaf; KANDIDAT QS 2:2]"
                cells[4] = "ثَانٍ [AUDIT: periksa rasm; KANDIDAT QS 2:2]"
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertTrue(any(page == "P040" and reference == "QS 2:2"
                            and slots == ["K01", "K02"]
                            for page, reference, slots in groups))

    def test_p016_first_slot_source_label_after_audit_note(self):
        # The real register starts K01's annotation with AUDIT, not KANDIDAT.
        line = next(line for line in self.original.splitlines()
                    if line.startswith("| P016 |"))
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        self.assertIn("AUDIT:", cells[2])
        self.assertIn("KANDIDAT QS 106:1", cells[2])
        # Reuse its genuine annotation in K02 to prove source detection.
        lines = self.original.splitlines()
        for i, row in enumerate(lines):
            if row.startswith("| P016 |"):
                parts = row.split("|")
                parts[4] = parts[3]
                lines[i] = "|".join(parts)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertTrue(any(page == "P016" and reference == "QS 106:1"
                            and slots == ["K01", "K02"]
                            for page, reference, slots in groups))

    def test_murajaah_source_recognized_but_not_hadith(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[4] = cells[3]  # Repeat the genuine P036 K01 MUROJAAH source in K02
                lines[i] = "|".join(cells)
                break
        groups = module.repeated_quran_loci("\n".join(lines))
        self.assertTrue(any(page == "P036" and reference == "QS 112:1"
                            and slots == ["K01", "K02"]
                            for page, reference, slots in groups))
        self.assertFalse(any(page == "P038" and "BUKHARI" in reference
                             for page, reference, _ in groups))

    def test_current_register_source_families_are_explicit(self):
        # Snapshot of source metadata, not a claim of Quranic or hadith validity.
        counts = {"quran": 0, "arabic": 0, "hadith": 0}
        for line in self.original.splitlines():
            if not line.startswith("| P") or not line[3:6].isdigit():
                continue
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if len(cells) != 19:
                continue
            capacity = 16 if int(cells[0][1:]) <= 20 else 8
            for value in cells[2:2 + capacity]:
                if not value or value == "—":
                    continue
                if "BAHASA ARAB" in value:
                    counts["arabic"] += 1
                elif "KANDIDAT HADIS" in value:
                    counts["hadith"] += 1
                elif "KANDIDAT QS " in value or (
                    "KANDIDAT;" in value
                    and ("MUROJAAH QS " in value or "HAFALAN UNIT QS " in value)
                ):
                    counts["quran"] += 1
                else:
                    self.fail("Unclassified source marker in register: " + cells[0])
        self.assertEqual(counts, {"quran": 457, "arabic": 8, "hadith": 3})

    def test_p013_ignores_qs_cross_reference_in_review_note(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = cells[3].replace(
                    "KANDIDAT QS 27:59",
                    "AUDIT: bandingkan QS 6:143; KANDIDAT QS 27:59",
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertFalse(any("P013 K01: expected exactly one" in error
                             for error in errors), errors)

    def test_p013_rejects_two_declared_sources(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = cells[3].replace(
                    "KANDIDAT QS 27:59",
                    "KANDIDAT QS 27:59; KANDIDAT QS 6:143",
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("P013 K01: expected exactly one" in error
                            for error in errors), errors)

    def test_p013_allows_audit_cross_reference_after_declared_source(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = cells[3].replace(
                    "KANDIDAT QS 27:59",
                    "KANDIDAT QS 27:59; AUDIT: bandingkan QS 6:143",
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertFalse(any("P013 K01: expected exactly one" in e
                             for e in errors), errors)

    def test_p036_hafalan_incomplete_surah_is_advisory(self):
        warnings = module.p036_hafalan_advisory(self.original)
        self.assertTrue(any("QS 113:5" in warning for warning in warnings))
        self.assertFalse(any("differs from documented" in warning
                             for warning in warnings), warnings)
        _, errors = module.audit(self.original)
        self.assertFalse(errors, errors)

    def test_p036_hafalan_advisory_handles_missing_page(self):
        content = "\n".join(
            line for line in self.original.splitlines()
            if not line.startswith("| P036 |")
        )
        self.assertTrue(any("missing" in warning
                            for warning in module.p036_hafalan_advisory(content)))

    def test_p036_warns_when_hafalan_sources_are_swapped(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[3], cells[4] = cells[4], cells[3]
                lines[i] = "|".join(cells)
                break
        warnings = module.p036_hafalan_advisory("\n".join(lines))
        self.assertTrue(any("P036 K01:" in w for w in warnings), warnings)
        self.assertTrue(any("P036 K02:" in w for w in warnings), warnings)

    def test_p036_warns_when_hafalan_source_is_missing(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[8] = " — "  # K06, originally QS 113:2
                lines[i] = "|".join(cells)
                break
        warnings = module.p036_hafalan_advisory("\n".join(lines))
        self.assertTrue(any("P036 K06:" in w for w in warnings), warnings)

    def test_jilid5_alfalaq_source_exists_in_reading_practice(self):
        warnings = module.qj5_alfalaq_completion_advisory(self.original)
        self.assertFalse(warnings, warnings)
        rows = [line for line in self.original.splitlines()
                if line.startswith("| P001 |") or line.startswith("| P018 |")]
        self.assertEqual(len(rows), 2)
        self.assertTrue(all("KANDIDAT QS 113:5" in row for row in rows))

    def test_jilid5_alfalaq_missing_source_is_advisory(self):
        changed = self.original.replace("KANDIDAT QS 113:5",
                                        "AUDIT: QS 113:5", 2)
        warnings = module.qj5_alfalaq_completion_advisory(changed)
        self.assertTrue(any("QS 113:5" in warning for warning in warnings))

    def test_jilid5_alfalaq_notes_are_not_candidate_sources(self):
        changed = self.original.replace("KANDIDAT QS 113:5",
                                        "AUDIT: QS 113:5", 2)
        changed = changed.replace("AUDIT HAFALAN:",
                                  "AUDIT HAFALAN: catatan QS 113:5;", 1)
        warnings = module.qj5_alfalaq_completion_advisory(changed)
        self.assertTrue(any("QS 113:5" in warning for warning in warnings))

    def test_qs1135_locations_are_active_declared_candidates(self):
        locations = module.qj5_alfalaq_source_locations(self.original)
        self.assertEqual(locations, ["P001 K13", "P018 K15"])
        self.assertFalse(any(item.startswith("P036 K") for item in locations))

    def test_alfalaq_advisory_accepts_source_after_audit_note(self):
        # Both source-location reporting and advisory must share the same rule.
        changed = self.original.replace(
            "[KANDIDAT QS 113:5;",
            "[AUDIT: periksa rasm; KANDIDAT QS 113:5;",
        )
        self.assertEqual(
            module.qj5_alfalaq_source_locations(changed),
            ["P001 K13", "P018 K15"],
        )
        self.assertEqual(module.qj5_alfalaq_completion_advisory(changed), [])

    def test_qs1135_location_scan_finds_declaration_after_audit_note(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P040 |"):
                cells = line.split("|")
                cells[3] = "وَمِنْ شَرِّ حَاسِدٍ إِذَا حَسَدَ [AUDIT: periksa; KANDIDAT QS 113:5]"
                lines[i] = "|".join(cells)
                break
        locations = module.qj5_alfalaq_source_locations("\n".join(lines))
        self.assertIn("P040 K01", locations)

    def test_qs1135_location_scan_ignores_notes(self):
        changed = self.original.replace("KANDIDAT QS 113:5",
                                        "AUDIT: QS 113:5", 2)
        self.assertEqual(module.qj5_alfalaq_source_locations(changed), [])

    def test_qs1135_location_scan_rejects_note_only_and_other_verse(self):
        # A note mentioning QS 113:5 is not a declared Quran source.
        changed = self.original.replace(
            "KANDIDAT QS 113:5", "AUDIT: lihat QS 113:5", 2
        )
        self.assertEqual(module.qj5_alfalaq_source_locations(changed), [])
        self.assertTrue(module.qj5_alfalaq_completion_advisory(changed))
        # Word boundaries must not confuse verse 5 with verse 50.
        changed = self.original.replace("KANDIDAT QS 113:5", "KANDIDAT QS 113:50", 2)
        self.assertEqual(module.qj5_alfalaq_source_locations(changed), [])
        self.assertTrue(module.qj5_alfalaq_completion_advisory(changed))

    def test_qs1135_scan_rejects_malformed_source_suffixes(self):
        for invalid_ref in ("113:5:1", "113:5-6", "113:5–6", "113:5a", "113:5A", "113:5_1"):
            with self.subTest(source=invalid_ref):
                changed = self.original.replace("KANDIDAT QS 113:5",
                                                f"KANDIDAT QS {invalid_ref}", 2)
                self.assertEqual(module.qj5_alfalaq_source_locations(changed), [])
                self.assertTrue(module.qj5_alfalaq_completion_advisory(changed))

    def test_p013_pending_count_comes_from_audited_rows(self):
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        p013 = next(row for row in rows if row[0] == "P013")
        self.assertEqual(p013[1] + p013[3], p013[2])
        # Remove one existing candidate in a synthetic copy: the pending count
        # must increase by one, without changing the real register.
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                self.assertNotIn(cells[3].strip(), ("", "—"))
                cells[3] = " — "
                lines[i] = "|".join(cells)
                break
        changed_rows, changed_errors = module.audit("\n".join(lines))
        self.assertFalse(changed_errors, changed_errors)
        changed = next(row for row in changed_rows if row[0] == "P013")
        self.assertEqual(changed[1], p013[1] - 1)
        self.assertEqual(changed[3], p013[3] + 1)

    def test_qs1135_scan_ignores_inactive_slots(self):
        changed = self.original.replace("KANDIDAT QS 113:5",
                                        "AUDIT: QS 113:5", 2)
        lines = changed.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[11] = "KANDIDAT QS 113:5"  # K09: inactive on P036
                lines[i] = "|".join(cells)
                break
        content = "\n".join(lines)
        self.assertEqual(module.qj5_alfalaq_source_locations(content), [])
        self.assertTrue(module.qj5_alfalaq_completion_advisory(content))
        _, errors = module.audit(content)
        self.assertTrue(any("inactive K slots contain data" in e for e in errors))

    def test_qs1135_scan_rejects_candidate_label_quoted_in_audit_note(self):
        changed = self.original.replace("KANDIDAT QS 113:5",
                                        "AUDIT: QS 113:5", 2)
        changed = changed.replace(
            "AUDIT: QS 113:5",
            "AUDIT: contoh label KANDIDAT QS 113:5 bukan sumber",
            1,
        )
        self.assertEqual(module.qj5_alfalaq_source_locations(changed), [])
        self.assertTrue(module.qj5_alfalaq_completion_advisory(changed))

    def test_p036_quoted_hafalan_marker_in_note_is_not_declared_source(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                cells[3] = (
                    "catatan audit mengutip KANDIDAT; MUROJAAH QS 112:1 "
                    "tanpa deklarasi kandidat [AUDIT: perlu sumber sah]"
                )
                lines[i] = "|".join(cells)
                break
        warnings = module.p036_hafalan_advisory("\n".join(lines))
        self.assertTrue(any("P036 K01:" in w and "missing" in w
                            for w in warnings), warnings)

    def test_p036_reading_source_does_not_complete_hafalan(self):
        # QS 113:5 in reading practice is not evidence that P036 hafalan
        # includes the fifth verse or that any memorization was assessed.
        self.assertEqual(
            module.qj5_alfalaq_source_locations(self.original),
            ["P001 K13", "P018 K15"],
        )
        self.assertFalse(module.qj5_alfalaq_completion_advisory(self.original))
        self.assertTrue(
            any("QS 113:5" in warning
                for warning in module.p036_hafalan_advisory(self.original))
        )
        rows, errors = module.audit(self.original)
        self.assertFalse(errors, errors)
        self.assertEqual(next(row for row in rows if row[0] == "P036")[4], "0/8")

    def test_p036_malformed_row_does_not_certify_hafalan(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P036 |"):
                cells = line.split("|")
                del cells[10]  # Drop K08, leaving a malformed table row.
                lines[i] = "|".join(cells)
                break
        content = "\n".join(lines)
        warnings = module.p036_hafalan_advisory(content)
        self.assertTrue(any("malformed row" in w for w in warnings), warnings)
        _, errors = module.audit(content)
        self.assertTrue(any("P036: expected 19 cells" in e for e in errors), errors)

    def test_duplicate_p036_page_is_structural_error_even_with_valid_hafalan(self):
        original_row = next(line for line in self.original.splitlines()
                            if line.startswith("| P036 |"))
        content = self.original + "\n" + original_row
        rows, errors = module.audit(content)
        self.assertTrue(any("duplicate page: P036" in e for e in errors), errors)
        self.assertEqual(sum(row[0] == "P036" for row in rows), 2)
        # A clean-looking hafalan sequence cannot override structural failure.
        warnings = module.p036_hafalan_advisory(content)
        self.assertTrue(any("duplicate hafalan rows (2)" in w
                            for w in warnings), warnings)

    def test_invalid_structure_never_reports_valid_coverage_total(self):
        # A duplicated page must invalidate the displayed aggregate.
        duplicated = next(line for line in self.original.splitlines()
                          if line.startswith("| P036 |"))
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "register.md"
            source.write_text(self.original + "\n" + duplicated, encoding="utf-8")
            output, errors = io.StringIO(), io.StringIO()
            with patch.object(module, "SOURCE", source):
                with redirect_stdout(output), redirect_stderr(errors):
                    code = module.main()
        self.assertEqual(code, 1)
        self.assertIn("TOTAL: INVALID STRUCTURE", output.getvalue())
        self.assertNotIn("TOTAL: 476/488", output.getvalue())
        self.assertIn("duplicate page: P036", errors.getvalue())

    def test_valid_structure_reports_real_total_and_returns_success(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "register.md"
            source.write_text(self.original, encoding="utf-8")
            output, errors = io.StringIO(), io.StringIO()
            with patch.object(module, "SOURCE", source):
                with redirect_stdout(output), redirect_stderr(errors):
                    code = module.main()
        self.assertEqual(code, 0, errors.getvalue())
        rows, structural_errors = module.audit(self.original)
        self.assertFalse(structural_errors, structural_errors)
        expected = (
            f"TOTAL: {sum(row[1] for row in rows)}/"
            f"{sum(row[2] for row in rows)} filled; "
            f"{sum(row[3] for row in rows)} empty"
        )
        self.assertIn(expected, output.getvalue())
        self.assertNotIn("TOTAL: INVALID STRUCTURE", output.getvalue())

    def test_p013_rejects_unbracketed_source_label(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = "contoh tanpa anotasi KANDIDAT QS 27:59"
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(
            any("P013 K03: expected exactly one known Mad Farq reference" in e
                for e in errors), errors
        )

    def test_p013_reference_only_slot_is_rejected(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = " [KANDIDAT QS 27:59] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(
            any("P013 K01: missing Quranic example text" in e
                for e in errors), errors
        )

    def test_p013_punctuation_only_is_not_quranic_example(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[3] = " ... 123 [KANDIDAT QS 27:59] "
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(
            any("P013 K01: missing Quranic example text" in e
                for e in errors), errors
        )

    def test_p013_quoted_label_in_audit_note_is_not_source(self):
        lines = self.original.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("| P013 |"):
                cells = line.split("|")
                cells[5] = (
                    "آللَّهُ [AUDIT: contoh tulisan KANDIDAT QS 27:59 "
                    "hanya kutipan, belum deklarasi]"
                )
                lines[i] = "|".join(cells)
                break
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(
            any("P013 K03: expected exactly one known Mad Farq reference" in e
                for e in errors), errors
        )

    def test_swapped_pages_rejected_even_when_all_pages_exist(self):
        lines = self.original.splitlines()
        first = next(i for i, line in enumerate(lines)
                     if line.startswith("| P001 |"))
        second = next(i for i, line in enumerate(lines)
                      if line.startswith("| P002 |"))
        lines[first], lines[second] = lines[second], lines[first]
        rows, errors = module.audit("\n".join(lines))
        self.assertEqual(len(rows), 40)
        self.assertTrue(any("page order mismatch" in e for e in errors),
                        errors)

    def test_missing_page_rejected(self):
        lines = [s for s in self.original.splitlines() if not s.startswith("| P040 |")]
        _, errors = module.audit("\n".join(lines))
        self.assertTrue(any("missing pages" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
