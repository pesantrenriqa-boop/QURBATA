# EVIDENCE SCAN K62 — CONTRAST vs RESULT v0.1

**Status:** MARKER-SPECIFIC CANDIDATE FILTER  
**Baseline:** K1–K61 DRAFT-FROZEN.

## Goal

Select a K62 relation that:
- has an overt marker;
- links two spans already analyzable through K61;
- adds exactly one semantic relation;
- avoids simultaneous marker disambiguation burden;
- does not expand into a full conjunction inventory.

---

## Candidate A — contrast/correction with overt `لكن`

Potential core operation:

`proposition A + لكن + proposition B → recognize B as contrast/correction against A`

### Strengths
- overt semantic marker;
- relation is conceptually distinct from K58 coordination and K59 sequencing;
- learner can classify the discourse relation without reconstructing a hidden element;
- contrast can be assessed by identifying what expectation/statement is being revised or opposed.

### Main risk
`لكن` is not uniform across all occurrences. Its morphosyntactic behavior and attachment can vary. Therefore K62 cannot be “all uses of لكن”.

### Clean-core policy
Admit only occurrences where:
- `لكن` is overt;
- the two compared spans are clearly recoverable;
- the second span functions as an explicit correction/contrast;
- no advanced `لكنّ` governance analysis is required merely to understand the relation;
- no ellipsis is needed to reconstruct the first or second proposition.

### Verdict
**PASS AS A NARROW CORE CANDIDATE.**

---

## Candidate B — result/consequence with filtered `ف`

Potential core operation:

`proposition/event A + ف + proposition/event B → identify B as direct consequence/result`

### Strengths
- highly useful Qur'anic relation;
- overt connector;
- natural extension beyond temporal sequencing.

### Main risks
- `ف` is highly multifunctional;
- K48/K54 already established `فاء جواب الشرط`;
- a learner may need to first decide “which fā’ is this?” before analyzing result;
- close temporal succession and consequence often overlap;
- one K could accidentally require two operations: disambiguate marker + classify relation.

### Clean-core policy challenge
A valid K62 item would need a subset where the result relation is obvious without teaching a new taxonomy of fā’ functions. Current architecture does not yet guarantee this cheaply.

### Verdict
**DEFER.** The relation is important, but not yet the cleanest K62 entry point.

---

## Direct comparison

### Contrast with `لكن`
Learner operation:
1. identify proposition/span A;
2. identify overt contrast marker;
3. identify proposition/span B;
4. classify B as correction/contrast relative to A.

### Result with `ف`
Learner operation often becomes:
1. identify A;
2. disambiguate the function of `ف`;
3. identify B;
4. decide whether the relation is sequence/result/condition-link/etc.

This violates the preference for one new operation per K.

---

# Selection

## K62-CAND

> **Mengenali relasi pertentangan/koreksi antara dua proposisi Qurani melalui marker `لكن` yang eksplisit dan tervalidasi dalam konstruksi sederhana.**

Core representation:

`[proposisi A] + لكن + [proposisi B]`

## Included
- overt `لكن`;
- two locally clear spans/propositions;
- explicit contrast/correction relation;
- cumulative internal syntax through K61;
- no requirement for full particle-governance theory.

## Excluded
- all uses of `لكن/لكنّ` as one inventory;
- ellipsis-dependent contrast;
- advanced governance as prerequisite;
- ambiguous discourse scope;
- multiple contrast markers;
- contrast mixed with nested condition/relative structures.

## Assessment prompt

`ما القضية الأولى؟ وما الذي خالفها أو صححها بعد لكن؟`

Expected learner operation: identify the two propositions and explain the contrast/correction relation.

## Decision

**Advance contrast-with-`لكن` to K62 distinctness/clean-bank gate.**

Keep filtered result/consequence with `ف` in the frontier queue for later testing.