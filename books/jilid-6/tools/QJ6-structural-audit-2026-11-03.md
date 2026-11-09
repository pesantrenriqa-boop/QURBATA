# QURBATA Jilid 6 — Structural audit snapshot (2026-11-03)

Branch: `work/qj6-register-9-slot-20261028`  
Register: `books/jilid-6/tools/QJ6-slots.csv`

## Results

| Check | Result |
|---|---|
| Register data rows | 360 / 360 |
| Missing slot IDs | 0 |
| Duplicate slot IDs | 0 |
| Page-ID mismatches | 0 |
| Empty rows containing text | 0 |
| Filled rows lacking text | 0 |
| Filled | 335 |
| EMPTY | 25 |

Empty by page: P017 = 7, P018 = 9, P036 = 9.

## Warnings (not structural failures)

- `QJ6-P017-S02`: candidate text does not include the explicit `لا` waqf glyph.
- `QJ6-P017-S04`: candidate text does not include the explicit `لا` waqf glyph.
- P018 and P036: memorization units still lack official approval; all 18 slots remain EMPTY.

## Method and limits

This report records a direct structural scan of the latest fetched CSV: all expected slot IDs (P001–P040, S01–S09), field counts, unique keys, page mapping, EMPTY/text consistency, and the two waqf-la glyph warnings. The repository Python audit script was inspected, but **was not itself executed in the repository's CI**. This audit is not a mushaf-source collation, tashih, semantic waqaf–ibtida approval, or publication approval. Preserve CANDIDATE/RESEARCH status pending human verification.
