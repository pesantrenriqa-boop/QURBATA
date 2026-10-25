# Head-to-Head K15–K17 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent baseline:** K1–K14 draft-frozen in research layer.  
**Goal:** determine the most stable ordering among attached-pronoun recognition, conjunction recognition, and core na'at–man'ut.

## 1. Candidates

- K15-CAND — recognize dhamir muttashil as a morphological segment
- K16-CAND — recognize frequent conjunction particles
- K17-CAND — core na'at–man'ut

## 2. K15 — Attached Pronoun Recognition

### Target
Recognize a host + attached pronoun boundary without yet requiring the learner to explain the pronoun's syntactic function.

Examples of host classes:
- noun + suffix: `رَبُّهُ`
- verb + suffix: `خَلَقَهُ`
- preposition + suffix: `لَهُ`

### Dependencies
- recognition of noun / verb / preposition host according to example;
- no requirement yet to know possessive/object/prepositional-object function.

### Strength
Very low conceptual dependency at recognition level, despite high polyfunctionality later.

**Judgement:** VERY STRONG EARLY REC.

## 3. K16 — Conjunction Recognition

### Target
Recognize frequent conjunction particles in a controlled context, especially `و`, `ف`, and later `ثم` where the function is genuinely conjunctive.

### Dependencies
Minimal at recognition level.

### Main risk
Surface `و` and `ف` are multifunctional. Evidence must distinguish conjunction from other discourse/particle functions before PASS status.

### Strength
Recognition is light, but corpus annotation must be function-sensitive.

**Judgement:** STRONG EARLY REC, but annotation-sensitive.

## 4. K17 — Core Na'at–Man'ut

### Target
Recognize a two-word noun–adjective relation in the cleanest Qur'anic examples.

### Dependencies
- noun recognition;
- basic definiteness contrast;
- enough exposure to gender/number/case matching to identify the relation reliably.

### Burden
Unlike K15/K16, this is a relation, not simple token recognition. It requires agreement-sensitive interpretation.

### Clean-evidence policy
Core K17 examples must avoid:
- idhafah chains unless already allowed and not necessary to the target;
- coordination inside the target;
- attached-pronoun complexity;
- nested clauses;
- multiple adjectives until core relation is established.

**Judgement:** HIGH VALUE, but should follow the two recognition competencies.

## 5. Head-to-Head Result

| Criterion | K15 pronoun suffix REC | K16 conjunction REC | K17 na'at REL |
|---|---:|---:|---:|
| Dependency depth | low | low | moderate |
| Morphological complexity | moderate | low | low–moderate |
| Functional ambiguity | high later, low for segmentation | moderate/high by particle function | moderate |
| Relation burden | none at core | none at core | yes |
| Evidence filtering burden | moderate | moderate | high |
| Readiness for early placement | very high | high | lower than K15/K16 |

**Preferred order:** `K15 → K16 → K17`.

## 6. Why K15 Before K16

K15 is placed first because its target can be defined purely as morphological segmentation: learner identifies that the Qur'anic word contains a host plus attached pronoun. The syntactic role is deliberately withheld.

K16 is also recognition-level, but `و` and `ف` require functional disambiguation before a corpus example can be accepted as conjunction evidence. Thus its evidence validation is slightly heavier.

## 7. Na'at Evidence Expansion Strategy

Evidence for K17 should be harvested in layers:

### Layer A — clean two-token relation
Target pattern: `اسم + صفة` with no additional expansion required.

### Layer B — same relation with known nominal features
Examples may include `الـ`, tanwin, or simple number/gender distinctions already inferable from surface forms.

### Layer C — reinforcement only
Examples with multiple adjectives or larger nominal phrases are stored but not used for core teaching until their extra structures are licensed.

All candidates are retained as PASS / PREMATURE / REVIEW.

## 8. Candidate Ordering After Test

- **K15-CAND** — attached pronoun recognition
- **K16-CAND** — conjunction particle recognition
- **K17-CAND** — core na'at–man'ut
- **K18-CAND** — simple coordination relation
- **K19-CAND** — basic hidden subject / fa'il mustatir

No production registry changes.

## 9. Next Gate

1. build evidence bank for K15–K17;
2. verify conjunction-function annotation for K16;
3. expand clean na'at examples until the yield is demonstrably sufficient;
4. if stable, draft-freeze K15–K17;
5. then compare K18 simple coordination vs K19 hidden subject and the first syntactic functions of attached pronouns.
