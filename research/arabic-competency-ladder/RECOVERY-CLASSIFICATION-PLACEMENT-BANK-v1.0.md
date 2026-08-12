# Recovery Classification — Placement Bank v1.0

**Status:** ACTIVE  
**Scope:** 180 historical placement slots

## 1. Evidence rule

A slot may be classified R1 only when its complete historical wording can be recovered from repository evidence. Search failure or a summary reference is not enough.

## 2. Current confirmed classes

### R0 — FULL
All item records reproduced in full in the currently accessible checkpoint files/patches are R0 and may proceed to normalization, subject to quality disposition.

### R2 — SUMMARY-ONLY
Representative searches for L04-P01 and L10-P01 did not recover independent item records or matching commits. The consolidated files explicitly preserve early ranges only by summary/reference. Those slots are therefore treated as R2 unless later repository evidence proves otherwise.

Known summary-only ranges from consolidated sources include:
- L04 P01–P30
- L10 P01–P24
- L13 P01–P24

For L19 and L21, earlier batches exist as separate source files, so they are not automatically R2; they require direct file-level normalization.

### R3 — UNRESOLVED
No slot is assigned R3 merely because code search fails. R3 is reserved for cases where neither historical recovery nor safe replacement construction is possible after canonical K/evidence review.

## 3. Replacement policy for R2

R2 slots retain their historical slot ID but receive a new replacement record only after fresh authoring from:
1. canonical competency definition;
2. prerequisite graph;
3. verified Qur'anic evidence;
4. feature-ceiling rules;
5. duplicate-function controls.

Replacement IDs use version `v2.0` to make the break from unrecoverable historical wording explicit.

Example:
`historical_slot=L04-P01` → `canonical_item_id=ARB-PL-L04-P001-v2.0`

## 4. Production policy

R2 replacement items start with:
- `quality_status=DRAFT-REPLACEMENT`
- `reviewer_status=UNREVIEWED`
- `pilot_status=NOT-PILOTED`
- `production_enabled=false`

No reconstructed item may inherit PASS status from the lost historical slot.

## 5. Normalization priorities

1. Normalize R0 L19/L21 earlier-batch files directly.
2. Normalize fully reproduced late-batch records from all checkpoints.
3. Build R2 replacements checkpoint-by-checkpoint, starting L04.
4. Run duplicate-function audit against R0 records before accepting each replacement.
5. Quality review replacements as new items.

## 6. Decision

**L04 P01–P30, L10 P01–P24, and L13 P01–P24 are provisionally classified R2 SUMMARY-ONLY.**

This classification can be upgraded to R1 only if later repository evidence recovers the full historical record verbatim.