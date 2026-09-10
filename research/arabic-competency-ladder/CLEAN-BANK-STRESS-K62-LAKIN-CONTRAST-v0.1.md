# Clean Bank + Stress Test K62 — Overt Contrast Relation with `لكن` v0.1

**Status:** PRE-FREEZE STRESS TEST  
**Baseline:** K1–K61 DRAFT-FROZEN.

## Operation under test

Learner recognizes two already-analyzable Qur'anic propositions linked by an overt, validated `لكن` and identifies the second proposition as correcting, restricting, or contrasting with an expectation established by the first.

Core representation:

`[proposition A] + لكن + [proposition B]`

The new operation is **semantic contrast/correction recognition across propositions**, not mere particle spotting.

## PASS requirements

- both proposition spans are independently analyzable using ≤ K61;
- `لكن` is overt and occurrence-specifically validated in the target function;
- contrast/correction relation is locally clear;
- no competing syntactic parse changes the relation;
- no hidden proposition is needed;
- no full taxonomy of `لكن` is required;
- the learner can state what expectation/claim is being corrected or limited.

## Evidence classes

### PASS-A — direct correction/contrast
Proposition A establishes an expectation or claim; overt `لكن` introduces proposition B that clearly corrects or restricts it.

### PASS-B — cumulative-clean contrast
One or both propositions contain earlier mastered complexity, but the contrastive relation remains transparent.

### REVIEW-FUNCTION
`لكن` is overt, but distinguishing its precise grammatical function requires later syntax.

### REVIEW-SEM
The structure is grammatical, but the contrast is too discourse-dependent or interpretively subtle for core teaching.

### PREMATURE
- omitted contrast term;
- nested contrast;
- multiple competing discourse relations;
- cases where `لكن` classification itself is disputed;
- examples requiring a full chapter on particles before the learner can solve the relation.

## Stress test 1 — Is this just K58 coordination with a different conjunction?

No. K58 asks whether two clauses are coordinated at the same structural level. K62 asks what **semantic relation** holds between the propositions: B counters, corrects, or restricts an expectation from A.

The learner must identify relational meaning, not only structural linkage.

## Stress test 2 — Must the learner distinguish every type of `لكن`?

No. Core K62 is occurrence-specific. Full distinctions among grammatical subtypes, governing behavior, and all traditional conditions remain outside the competency.

## Stress test 3 — Is 'contrast' too vague?

K62 requires a concrete answer format:
- what does proposition A make the reader expect?
- what does proposition B correct/restrict?

If that cannot be answered locally and stably, the occurrence is not clean-bank evidence.

## Stress test 4 — Why not use `ف` for result first?

Because `ف` carries a much larger disambiguation burden and overlaps with earlier `فاء جواب الشرط`. `لكن` offers a cleaner one-marker/one-relation core for introducing proposition-level semantic relation.

## Assessment design

Core prompt:

`ما القضية الأولى؟ وما القضية الثانية؟ وما الذي تصححه أو تستدركه الثانية بعد لكن؟`

Expected response identifies both proposition spans and states the correction/contrast relation.

## Verdict

**PASS WITH OVERT-`لكن` RESTRICTED SCOPE.**

K62 is distinct, semantically meaningful, and preserves the one-new-operation rule when examples are limited to locally transparent contrast/correction.

## Freeze recommendation

> **K62 — Mengenali relasi pertentangan/koreksi antara dua proposisi Qurani melalui `لكن` eksplisit yang tervalidasi, dengan menjelaskan apa yang dibatasi atau dikoreksi oleh proposisi kedua.**

## Next frontier

After freeze, rescan K63 across:
- tightly filtered result/consequence relation;
- omitted `العائد` only if a low-dependency subtype emerges;
- other explicit discourse relations;
- cohesion/reference operations beyond relative clauses.

Do not turn every discourse particle into a separate K automatically.