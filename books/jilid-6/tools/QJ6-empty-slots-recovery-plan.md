# QJ6 — Recovery plan for the 25 unfilled slots

Date: 2026-11-05. Derived from the committed `QJ6-slots.csv`. **Planning only: no invented Quranic excerpts, no verification or print approval.**

## Actual unfilled inventory

| Page | Competency | Empty slot IDs | Count | Release prerequisite |
| --- | --- | --- | ---: | --- |
| P017 | Larangan/kehati-hatian waqaf — لا dan pasangan tanda | S01, S03, S05, S06, S07, S08, S09 | 7 | Direct Mushaf Standar Indonesia collation of dedicated waqf-la signs and placement; distinguish negation لا from waqf sign |
| P018 | Hafalan 1 — unit Al-Qur'an disahkan | S01–S09 | 9 | Authorized hafalan unit and verse range, age-level target, approved curricular sequence |
| P036 | Hafalan 2 — unit sah + murojaah | S01–S09 | 9 | Authorized second unit and murajaah scope, progression after P018, prerequisite approval |
| **Total** | | | **25** | **Remain EMPTY pending authoritative evidence** |

## Safe filling order

1. **P017:** Have the qualified reviewer identify a specific MSI edition, verse, actual standalone waqf-la glyph, intended teaching point, and precise excerpt for each proposed slot. Compare with existing P017-S02 and S04, whose excerpts currently lack a dedicated sign. Reject a candidate if its only evidence is the ordinary letters `لا`.
2. **P018:** Obtain the approved hafalan syllabus and assigned surah/ayah units before choosing any text. Check that nine slots are pedagogically appropriate; if not, obtain explicit curriculum authorization rather than inventing filler.
3. **P036:** Obtain the authorized second hafalan and murojaah targets, then compare with P018 and earlier jilid to avoid unintended repetition.
4. For every proposed candidate: record exact Quranic source, target-edition evidence, competency and prerequisite match, duplication check, reviewer, and decision. Only then propose a CSV change in a separately reviewable commit.
5. Re-run regression tests, inspect all release holds, and retain `print_approved=false` until independent release authorization.

## No-go rules

- Do not substitute web Quran text for verse-level MSI verification.
- Do not mark `source_verified` or `competency_verified` as `yes` on inference alone.
- Do not alter Arabic rasm or waqf symbols to make an automated test pass.
- Do not treat nine slots as a mandate to invent nine different verses.
- This plan is not evidence of tashih or approval.
