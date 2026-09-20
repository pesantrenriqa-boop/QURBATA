# EVIDENCE MATURITY AUDIT — K11–K20 v1.0

**Status:** COMPLETED CONSERVATIVE AUDIT  
**Architecture:** K01–K65 FROZEN  
**Sources:** `FINAL-GATE-K11-K14-v1.0.md`, `FINAL-GATE-K15-K17-v1.0.md`, `FINAL-GATE-K18-K20-v1.0.md`  
**Rule:** maturity credit is limited to evidence explicitly preserved in authoritative discovery records; no Qur'anic reference is invented during audit.

## Audit matrix

| K | Competency | Evidence preserved in authoritative source | Maturity | Decision |
|---|---|---|---|---|
| K11 | detached pronoun as mubtada' | final gate confirms dedicated evidence bank/stress test, but no explicit surah:ayah anchor appears in the final-gate record | E1- | evidence existence confirmed; anchor metadata recovery required |
| K12 | PP as khabar | dedicated evidence bank/stress test confirmed, no explicit cited anchor in final gate | E1- | recover canonical anchor + clean spans |
| K13 | simple two-noun idhafah | dedicated evidence bank/stress test confirmed, no explicit cited anchor in final gate | E1- | recover canonical anchor + diversity |
| K14 | overt direct object | dedicated evidence bank/stress test confirmed; strict evidence filter noted; no explicit cited anchor in final gate | E1- | recover clean anchor and boundary cases |
| K15 | attached-pronoun segmentation | evidence expansion artifact explicitly cited; host_type/pronoun_form metadata required; no explicit cited anchor in final gate | E1- | recover cited occurrences + host diversity |
| K16 | validated conjunction recognition | core forms `و`, `ف`, `ثم` specified and occurrence-function validation required; no explicit cited anchor in final gate | E1- | normalize at least one cited occurrence per core function/form where possible |
| K17 | simple na'at–man'ut | evidence expansion artifact cited; agreement dimensions defined; no explicit cited anchor in final gate | E1- | recover anchor + agreement-diverse clean bank |
| K18 | attached pronoun as mudhaf ilaih | counterexample stress artifact cited; core function and exclusions stable; example Qur'anic reference not preserved in final gate | E1- | recover cited anchor + host variety |
| K19 | nominal coordination | counterexample stress artifact cited; validated conjunction required; no explicit cited anchor in final gate | E1- | recover anchor and distinguish from phrase/clause ambiguity |
| K20 | preposition + attached pronoun | explicit clean-form patterns preserved: `له`, `به`, `فيه`, `عليه`, `منه`, `إليه`; no surah:ayah attached in final gate | E1- | normalize cited occurrences before E2 |

## Interpretation

Unlike K01–K07, K11–K20 have stronger evidence provenance because their final-gate records explicitly name prior evidence-bank, evidence-expansion, stress-test, or counterexample artifacts. This is enough to credit **evidence existence**, but not enough to claim E2/E3 production maturity until exact Qur'anic references and item-level metadata are normalized.

Therefore the conservative status is `E1-` rather than E0: anchor/evidence work demonstrably existed during discovery, but canonical referenced anchor records are not yet surfaced in this audit layer.

## Strongest preserved evidence signals

### K15
Evidence schema already requires:
- `host_type`;
- `pronoun_form`.

This is useful for future E3 diversification because attached pronouns must be tested across host classes rather than counted as one undifferentiated token type.

### K16
The core form family is explicitly constrained to validated coordinating occurrences of:
- `و`;
- `ف`;
- `ثم`.

The same surface form with another function is negative/boundary evidence, not a clean positive example.

### K17
Agreement dimensions are already identified:
- gender;
- number;
- definiteness;
- case, where visible/relevant.

E3 promotion should require diversity across these dimensions without importing later syntax.

### K20
Existing clean-form queue:
- `لَهُ`
- `بِهِ`
- `فِيهِ`
- `عَلَيْهِ`
- `مِنْهُ`
- `إِلَيْهِ`

These spans should be normalized to exact surah:ayah and tagged by preposition + pronoun form.

## Recovery queue

1. fetch parent evidence artifacts named by the final gates;
2. extract exact surah:ayah + target span;
3. assign canonical evidence IDs;
4. tag prerequisite load;
5. separate PASS / REVIEW / PREMATURE examples;
6. promote K11–K20 from `E1-` to E1/E2 only after normalized records exist.

## Batch verdict

- K11–K20 architecture audited: **10/10**;
- evidence provenance confirmed: **10/10**;
- normalized fully cited canonical anchor surfaced in this audit file: **0/10**;
- explicit reusable clean-form queue preserved: strongest at K16/K20;
- next maturity action: source recovery, not new competency discovery.

**K11–K20 AUDIT: COMPLETE.**  
**NEXT: audit K21–K25 to complete Wave A architecture/evidence triage, while source-recovery continues for K01–K20.**