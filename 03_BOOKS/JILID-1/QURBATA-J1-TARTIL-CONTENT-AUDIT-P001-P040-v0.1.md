# QURBATA Jilid 1 — Tartil Content Audit P001–P040 v0.1

**Status:** AUDIT OPEN — PDF production remains blocked  
**Branch:** `renderer/pagedjs-p001-prototype`

## Purpose

This file reconciles the content and renderer gates before Jilid 1 P001–P040 can be frozen as one production master.

## Authority

1. Frozen Tartil page registers P001–P040 remain authority for letter/harakat progression.
2. `QURBATA-J1-TARTIL-CONTENT-MASTER-P001-P020-FROZEN-v1.0.md` remains current content authority for P001–P020.
3. `QURBATA-J1-TARTIL-CONTENT-MASTER-P021-P040-WORKING-v0.1.md` remains working authority for P021–P040.
4. Renderer changes MUST NOT be used to silently repair lexical/curricular content.

## Reconciled gate status

| Gate | Status | Note |
|---|---|---|
| Register P001–P040 | PASS | Frozen page-register sequence is authoritative |
| P001–P020 allocation | PASS / lexical audit pending | Frozen v1.0 remains authority |
| P021–P039 24-group allocation | PASS | Exact allocations recorded in working master |
| P040 checkpoint inventory | PASS | 29 identities + 3 harakat names + 24 reading groups |
| Dhammah exact-form evidence | PASS | Authorized anchors: كَبُرَ، حَسُنَ، ضَعُفَ |
| HOLD candidates excluded | PASS | No HOLD item may enter production |
| 3-letter pseudo-word prohibition | PASS as rule | Production requires meaningful exact-harakat words |
| Global inherited Fathah/Kasrah lexical-source audit | **PENDING** | v0.8 correctly left this gate open; v0.9 did not supersede it |
| Detached ه two-hole visual proof | **PENDING CI/RENDERER** | Unicode U+0647 must remain unchanged |
| PDF production | **BLOCKED** | Until both pending gates pass |

## Mandatory lexical audit scope

Every unique 3-letter item inherited from P001–P020 must be checked for:

- exact Arabic spelling;
- exact printed harakat;
- Indonesian gloss;
- lexical/source status: `QURAN-CONFIRMED`, `FUSHA-VERIFIED`, or `HOLD`;
- first legal page, determined by the **actual letter carrying the newly introduced harakat**.

Priority re-check set:

`شَطَرَ` · `مَرَجَ` · `يَبَسَ` · `نَشِطَ` · `عَطِشَ` · `خَطِفَ` · `رَصَدَ` · `ضَجَرَ` · `قَرَعَ` · `شَفَعَ`

No item may be promoted from HOLD by inference.

## Renderer gate

Sentinels:

- P013: `هَ`
- P019: `هِ`
- P027: `هُ`
- P040: `ه`

PASS requires visible two-hole detached heh while preserving underlying Unicode `ه` (U+0647) and frozen KFGQPC Uthman Taha policy.

## Freeze rule

Do **not** freeze P021–P040 or unified P001–P040 until:

`GLOBAL LEXICAL PASS → HA-TWO-HOLE VISUAL PASS → UNIFIED CONTENT FREEZE → GENERATOR MIGRATION → BUILD → VISUAL AUDIT`

