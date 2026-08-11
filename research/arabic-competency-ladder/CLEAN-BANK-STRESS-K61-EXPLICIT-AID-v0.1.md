# Clean Bank + Stress Test K61 — Explicit `العائد` Reference Resolution v0.1

**Status:** PRE-FREEZE STRESS TEST  
**Baseline:** K1–K60 DRAFT-FROZEN.

## Operation under test

Learner identifies one overt resumptive pronoun (`العائد`) inside an already-recognized `صلة الموصول` and resolves that pronoun back to the overt `اسم الموصول`.

Core representation:

`اسم موصول → صلة الموصول → ضمير عائد ظاهر → مرجعه اسم الموصول`

The new operation is **local anaphoric reference resolution**.

## PASS requirements

- `اسم الموصول` is overt and familiar;
- `صلة الموصول` boundary is already clear through K60;
- exactly one relevant overt pronoun functions as the resumptive element;
- antecedent is local and unique;
- pronoun form is already familiar;
- no omitted resumptive is needed;
- no competing antecedent requires discourse-level inference;
- no nested relative clause.

## Evidence classes

### PASS-A — direct explicit resumptive
Short relative clause + one overt attached or independent pronoun + unique relative antecedent.

### PASS-B — cumulative-clean extension
Additional internal syntax is ≤ K60, but the resumptive dependency remains locally obvious.

### REVIEW-REF
Pronoun is overt, but more than one plausible antecedent exists.

### REVIEW-FUNCTION
Pronoun is present, but identifying it specifically as `العائد` requires an unmastered grammatical dependency.

### PREMATURE
- `العائد المحذوف`;
- multiple competing pronouns;
- long-distance reference;
- nested relative structures;
- reference resolution requiring discourse context outside the local construction;
- disputed parsing.

## Stress test 1 — Is K61 merely “spot a pronoun”?

No. Pronoun recognition alone is insufficient. The learner must answer both:
1. which pronoun is the resumptive element?
2. what antecedent does it refer back to?

The competency is relational, not lexical.

## Stress test 2 — Distinctness from K60

K60 establishes the relative-clause span.

K61 establishes the **internal referential bridge** that reconnects the relative clause to the relative antecedent.

Thus K61 adds reference resolution rather than another boundary operation.

## Stress test 3 — Should subject/object/prepositional resumptives be separate K?

No. Their local grammatical positions differ, but the learner operation remains:

`identify overt pronoun → resolve reference to relative antecedent`.

They belong to internal staging unless future evidence reveals a genuinely distinct cognitive operation.

## Stress test 4 — Must omitted `العائد` be introduced here?

No. Omitted resumptives require reconstruction and therefore add a second inferential operation. They remain outside core K61 and may become a later candidate only if pedagogically distinct.

## Assessment design

Core prompt:

`أين العائد في صلة الموصول؟ وعلى أي اسم موصول يعود؟`

Expected response identifies the overt pronoun and its relative antecedent.

## Verdict

**PASS WITH EXPLICIT-ONLY SCOPE.**

K61 is independently assessable, cumulative, and distinct if restricted to overt, local, unambiguous resumptive dependencies.

## Freeze recommendation

> **K61 — Mengenali `العائد` eksplisit di dalam `صلة الموصول` dan menghubungkannya kembali kepada `اسم الموصول` dalam konstruksi Qurani sederhana.**

## Next

After freeze, rescan K62 across:
- omitted resumptive reconstruction;
- cause/result clause relation;
- filtered `ف` sequencing;
- other Qur'anic reference/cohesion operations.

Do not automatically turn every resumptive position into a new competency.