# Late-Ladder Source Conflict Resolution — K58–K67 v1.0

**Status:** GOVERNANCE CORRECTION — ACTIVE  
**Scope:** late-ladder evidence numbering and placement alignment  
**Authoritative source:** `CANONICAL-REGISTRY-K58-K67-v0.1.md` as recovered from PR #4.

## Conflict discovered

`EVIDENCE-MATURITY-AUDIT-K58-K65-v1.0.md` explicitly states that it was produced under an earlier **K01–K65** architecture and remaps legacy discovery nodes after duplicate transfer nodes were removed. Its row numbering therefore does not equal the later authoritative K01–K67 registry numbering.

Example conflict:
- authoritative current K60 = Relative-Clause Boundary (`صلة الموصول`);
- stale maturity audit K60 = Contrast/Correction;
- authoritative current K63 = Result/Consequence;
- stale maturity audit K63 = Exception/Restriction;
- authoritative current K64 = Cause/Reason;
- stale maturity audit K64 = Purpose/Goal.

These are numbering-version conflicts, not necessarily conceptual contradictions.

## Supersession rule

For placement canonicalization, all K-ID assignments MUST use the authoritative K58–K67 registry:

- K58 — Simple Inter-Clausal Coordination
- K59 — Temporal Sequencing with `ثم`
- K60 — Relative-Clause Boundary (`صلة الموصول`)
- K61 — Explicit Relative Resumptive (`العائد`)
- K62 — Contrast / Correction
- K63 — Result / Consequence
- K64 — Cause / Reason
- K65 — Exception / Restriction with `إلا`
- K66 — Purpose / Goal
- K67 — Concession / Counterexpectation

Older K01–K65 evidence artifacts remain valid as research provenance only after **conceptual remapping by competency identity**, never by numeric K-ID alone.

## Consequence for K63/K64 closure

The old maturity audit cannot be used to claim that current K63/K64 have normalized placement occurrences. Its current-number rows refer to different concepts.

For current K63 Result/Consequence and K64 Cause/Reason, the valid sources recovered so far are:
- current conceptual rescan records;
- evidence gates;
- clean-bank/stress-test definitions;
- final gates;
- authoritative K58–K67 registry.

Those sources establish competency identity and admission criteria but do not expose a normalized, occurrence-level PASS record with complete `surah:ayah + exact span + validated marker/function + proposition boundaries` in the retrieved material.

Therefore current K63 and K64 remain:

`HOLD-EVIDENCE-NORMALIZATION`

until an occurrence-level source is recovered or newly validated through Arabic-content review.

## Governance rule for all future evidence reuse

When reusing any pre-K67 artifact:
1. match by **competency definition/operation**, not old number;
2. record the legacy K-ID separately;
3. map to current canonical K-ID;
4. verify prerequisites against current graph;
5. never auto-promote an old occurrence solely because its numeric label equals a current K-ID.

## Progress consequence

- authoritative definition coverage K01–K67: preserved;
- historical placement-slot recovery: preserved;
- L21 current canonical candidate coverage: 8/10;
- K63/K64: evidence-normalization debt remains explicit;
- production_enabled: false.

This correction prevents silent evidence migration across incompatible ladder-numbering versions.