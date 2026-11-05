# QJ6 register integrity check — 2026-11-05

## Method

Read the current CSV directly from branch `work/qj6-register-9-slot-20261028` and independently parse the quoted CSV rows. This is a **JavaScript data-level cross-check**, not execution of `audit-qj6-register.py`, and not Quranic content certification.

## Verified counts

| Check | Result |
|---|---|
| Total rows | 360 |
| Filled | 335 |
| EMPTY | 25 |
| EMPTY P017 | 7 |
| EMPTY P018 | 9 |
| EMPTY P036 | 9 |
| Rows with incorrect column count or page ID mismatch | 0 |
| Internal QJ6 source references | 84 |
| Missing referenced slot IDs | 0 |

## Priority waqf glyph checks

| Slot | Expected glyph | Found | source_verified | competency_verified | review_status |
|---|---|---|---|---|---|
| P015-S01 | ۘ (U+06D8) | YES | no | no | CANDIDATE |
| P015-S06 | ۘ (U+06D8) | YES | no | no | CANDIDATE |
| P016-S03 | ۚ (U+06DA) | YES | no | no | CANDIDATE |

**Interpretation:** structural checks pass for the examined fields. The glyphs exist in the CSV; this does not confirm their positions in the official MSI or establish safe waqf–ibtida'.

## Remaining gates

1. Run the Python audit script itself in a suitable runtime or CI and record its exit status.
2. Obtain verse-specific MSI source images for QS 6:36, 10:65, and 61:7 and verify signs with a reviewer.
3. Preserve P017/P018/P036 empty slots until curriculum-approved material and source verification exist.
4. Do not advance any CANDIDATE to print approval based on this report.
