# Clean Bank + Stress Test K58 — Simple Clause Coordination v0.1

**Status:** PRE-FREEZE STRESS TEST  
**Baseline:** K1–K57 DRAFT-FROZEN.

## Operation under test

Learner recognizes two independently analyzable clauses connected at the same structural level by one overt coordinator, beginning with transparent Qur'anic `و`.

Core representation:

`[جملة 1] + رابط عطف ظاهر + [جملة 2]`

The new operation is **inter-clausal coordination recognition**, not memorization of the full `حروف العطف` inventory.

## Core entry policy

Use `و` first because it provides the least additional semantic burden. The learner must first establish that both sides are clauses, then identify the overt connector as linking them at clause level.

## PASS requirements

- both conjuncts are independently analyzable using ≤ K57;
- both are genuine clauses rather than isolated words/phrases;
- coordinator is overt;
- attachment scope is locally clear;
- no omitted clause is required;
- no nested coordination;
- no disputed discourse attachment;
- the item does not require advanced semantic distinctions among coordinators.

## Evidence classes

### PASS-A — transparent `و`
Two simple clauses + overt `و` + unambiguous same-level coordination.

### PASS-B — cumulative-clean extension
One or both clauses contain previously mastered internal complexity, but their boundaries and coordination remain transparent.

### REVIEW-SCOPE
The connector is overt but its attachment could be phrase-level or clause-level without later analysis.

### REVIEW-SEM
Coordination is clear, but the connector's interpretation requires a semantic relation not yet mastered.

### PREMATURE
- ellipsis across conjuncts;
- nested coordination;
- coordination mixed with oath/condition ambiguity;
- disputed clause boundary;
- several new discourse relations at once.

## Stress test 1 — Distinctness from phrase-level `عطف`

K58 core requires each side to form a clause. If the connector merely joins nouns, adjectives, or other phrase-level constituents, the occurrence is not evidence for K58.

## Stress test 2 — Distinctness from K47 conditional linkage

Conditional linkage is asymmetric:
`شرط → جواب`.

K58 coordination is structurally peer-like:
`clause ↔ clause` linked by an overt coordinator.

The learner therefore makes a new relation judgment.

## Stress test 3 — Does every coordinator need a new K?

No. `ف`, `ثم`, and other coordinators may later be added as application breadth only when the core operation remains clause-level coordination. A new K is justified only if the learner must infer a genuinely new relation beyond coordination recognition.

## Stress test 4 — Is `و` always coordination?

No. Surface `و` alone never passes. The occurrence must be validated as an actual coordinator linking the two target clauses. Other functions of wāw are excluded from the clean bank.

## Assessment design

Core prompt:

`أين الجملة الأولى؟ وأين الجملة الثانية؟ وما الرابط بينهما؟`

Expected response identifies both clause spans and the overt coordinator.

## Verdict

**PASS WITH `و`-FIRST SCOPE.**

K58 is distinct and teachable if evidence is restricted to genuine, same-level, overt inter-clausal coordination.

## Freeze recommendation

> **K58 — Mengenali koordinasi dua klausa Qurani yang sama-sama utuh melalui satu penghubung eksplisit, dimulai dari `و` yang tervalidasi sebagai koordinator antarklausa.**

## Next

After freeze, rescan K59 across:
- semantic sequencing with `ف` / `ثم` if it adds a new learner operation;
- subordinate clause relations;
- relative-clause structure;
- other corpus-driven inter-clausal relations.

Do not convert the inventory of conjunctions into an inventory of K numbers.