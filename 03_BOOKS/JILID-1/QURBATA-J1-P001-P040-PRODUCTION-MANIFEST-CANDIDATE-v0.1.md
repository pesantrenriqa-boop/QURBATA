# QURBATA Jilid 1 — P001–P040 Production Manifest Candidate

**Status:** RC / NOT FINAL / PDF BUILD BLOCKED  
**Purpose:** single handoff contract from frozen curriculum/content authorities into the production generator.

## Authority chain
1. Master curriculum: `02_MASTER_SYSTEM/QURBATA_TARTIL_J1_MASTER_CURRICULUM_FROZEN-v1.1.md`
2. Tartil Page Registers P001–P040 (frozen sequence)
3. Integration overlay: `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`
4. Tartil content P001–P020: `QURBATA-J1-TARTIL-CONTENT-MASTER-P001-P020-FROZEN-v1.1.md`
5. Tartil content P021–P040: `QURBATA-J1-TARTIL-CONTENT-MASTER-P021-P040-CANDIDATE-v1.0-rc1.md`
6. Tahfidz: frozen J1 baseline distribution; candidate v0.2 MUST NOT supersede it.
7. Visual master: P001 Build 21 / frozen visual-master rules, extended only through approved renderer rules.

## Production invariants
- Tartil remains dominant.
- No generator-created 3-letter groups.
- Every 3-letter group must come from the approved page allocation and be meaningful with the exact printed harakat.
- First-legal-page is determined by the actual letter carrying the newly introduced harakat.
- No premature connected letters, mad, tanwin, sukun, or shaddah.
- Bi'ah and Akhlak MUST come from Integration Register v1.3, not stale page-register fields.
- Tahfidz MUST come from the frozen baseline distribution.
- Detached `ه` preserves Unicode U+0647 and must visually pass the two-hole sentinel audit.
- KFGQPC Uthman Taha remains the frozen Arabic font.
- P020 and P040 implement their special checkpoint contracts.
- Footer retains Tanggal — Nilai — TTD and QR area.
- No ornament may reduce the practice area.

## Generator migration contract
The production generator MUST:
1. remove/disable random or cyclic 3-letter word construction;
2. load exact per-page Tartil allocations from the content masters;
3. load Bi'ah/Akhlak from Integration v1.3;
4. load Tahfidz from the frozen J1 baseline;
5. apply detached-heh renderer handling only as a visual layer, never as Unicode substitution;
6. preserve approved P001 visual proportions;
7. fail the build when a requested page lacks an explicit approved content allocation.

## Gate ledger
| Gate | Status |
|---|---|
| Register sequence | PASS |
| Integration v1.3 | PASS |
| P001–P020 lexical/content | PASS |
| P021–P039 allocations | PASS |
| P040 checkpoint | PASS |
| Dhammah exact anchors | PASS |
| HOLD in production allocation | 0 |
| Pseudo-word in production allocation | 0 |
| Detached-heh source wiring | PASS — including isolated heh tokens inside multi-token drills |
| Detached-heh visual proof | **PENDING** |
| Original QURBATA logo asset | **PENDING — repo currently contains traced SVG only** |\n| Unified final content freeze | **PENDING visual + logo gates** |
| Generator migration | **PASS — exact governed allocations wired through P040; P021–P027 planting sets and P028 identity rotation enforced** |
| Production PDF | **BLOCKED** |

## Release rule
No artifact may be labeled FINAL until:

`ORIGINAL-LOGO ASSET PASS → HA-TWO-HOLE VISUAL PASS → UNIFIED CONTENT FREEZE → 40-PAGE BUILD → VISUAL/CONTENT AUDIT PASS`

This candidate manifest is intentionally prepared before the visual gate so generator migration can begin immediately after the sentinel proof passes without reopening curriculum decisions.


## Migration reconciliation — 2026-09-23
- P001–P020 generator uses approved content-master allocations; random 3-letter construction is disabled.
- P021–P027 now use the exact 6 planting groups + 18 approved WORD groups per page.
- P028–P039 now use the exact 24-group allocations from the reconciled P021–P040 candidate master.
- P028 explicitly carries the full 29-letter identity rotation required by its register.
- P020 checkpoint remains Fathah + Kasrah; P040 checkpoint carries Fathah + Kasrah + Dhammah and the exact 29-letter inventory.
- Detached-heh visual handling now applies to isolated `هَ / هِ / هُ / ه` tokens even when they occur inside multi-token drills.
- Generator migration is therefore content-side PASS. Final release remains blocked by the actual visual proof and original-logo asset gate.
