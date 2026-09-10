# Clean Bank + Stress Test K59 — `ثم` Sequencing v0.1

**Status:** PRE-FREEZE STRESS TEST  
**Baseline:** K1–K58 DRAFT-FROZEN.

## Operation under test

Learner recognizes two independently analyzable clauses linked by validated `ثم` and interprets the second clause as occurring **after** the first in an ordered sequence.

Core representation:

`[جملة 1] + ثم + [جملة 2] → ترتيب بين الحدثين`

The new operation is not merely detecting coordination, but extracting an overt sequencing relation from the connector.

## PASS requirements

- both sides are genuine clauses and independently analyzable ≤ K58;
- `ثم` is overt and validated as the connector between them;
- the occurrence supports a clear sequential reading;
- no rhetorical reinterpretation is required;
- no nested coordination or ellipsis is needed;
- no disputed scope.

## Evidence classes

### PASS-A — direct temporal/event sequence
Clause 2 is clearly subsequent to clause 1 and `ثم` overtly marks the relation.

### PASS-B — cumulative-clean sequence
Additional internal syntax is present but does not obscure clause boundaries or the ordering relation.

### REVIEW-RHET
The occurrence contains `ثم`, but understanding it requires rhetorical/discourse analysis beyond straightforward sequencing.

### REVIEW-SCOPE
Attachment of `ثم` is not locally transparent.

### PREMATURE
- nested sequencing;
- ellipsis across the coordinator;
- disputed event order;
- rhetorical escalation whose analysis would introduce another competence;
- multiple coordination relations at once.

## Stress test 1 — Distinctness from K58

K58 asks whether two clauses are linked as peers by an overt coordinator.

K59 adds one semantic relation:

`coordination + ordered succession`.

Therefore a learner can pass K58 but fail K59 by identifying the connector without recognizing the ordering relation.

## Stress test 2 — Does K59 require full `التراخي` theory?

No. Core K59 only requires **subsequent ordering**. Quantifying the delay, contrasting temporal vs rhetorical distance, and defining classical `التراخي` are later mastery-depth issues.

## Stress test 3 — Should `ف` be bundled with `ثم`?

No. `ف` has a broader functional load and often requires finer distinction among sequencing, consequence, response, and discourse functions. K59 therefore establishes the sequencing operation first through the cleaner `ثم` evidence family.

`ف` may later be tested as transfer or as a separate competence only if a genuinely new learner operation is demonstrated.

## Stress test 4 — Is this merely vocabulary knowledge of `ثم`?

No. Assessment must require the learner to identify the two clause spans and state the relation between their events. Translation of `ثم` alone is insufficient.

## Assessment design

Core prompt:

`أين الجملة الأولى؟ وأين الجملة الثانية؟ وأيهما وقع بعد الآخر؟ وما الرابط؟`

Expected response identifies both clause spans, `ثم`, and the ordered relation.

## Verdict

**PASS.**

K59 is independently assessable and cumulative-clean when restricted to clear inter-clausal sequencing with overt `ثم`.

## Freeze recommendation

> **K59 — Mengenali urutan kejadian antara dua klausa Qurani yang utuh melalui `ثم` yang tervalidasi sebagai penghubung sekuensial.**

## Next frontier

After freeze, rescan K60 across:
- immediate/close sequencing with `ف`;
- relative-clause structure;
- causal/result subordination;
- other corpus-discovered inter-clausal relations.

Do not automatically assign K60 to `ف` without a distinctness and ambiguity test.