# FINAL GATE K64 v1.0

**Status:** DRAFT-FROZEN  
**Baseline:** K1–K63 DRAFT-FROZEN.

## Competency

**K64 — Mengenali relasi sebab/alasan antara dua proposisi Qurani melalui marker eksplisit yang tervalidasi, lalu menentukan proposisi yang dijelaskan dan proposisi yang menjadi sebab/alasan.**

## Learner operation

Given a validated occurrence, learner can:
1. identify the proposition being explained/justified;
2. identify the proposition that supplies the reason/grounds;
3. locate the overt validated explanatory signal;
4. state the directed reason relation.

## Included

- two proposition spans analyzable through K63;
- overt validated reason/explanatory signal;
- clear local direction of explanation;
- one cause/reason relation;
- cumulative clause/discourse analysis through K63.

## Excluded

- purpose/goal constructions requiring additional machinery;
- hidden `أن` as a new dependency;
- tafsir-only causal inference;
- ambiguous multifunctional markers without prior validation;
- advanced balaghah explanations;
- multiple competing reasons;
- omitted causal material.

## Assessment prompt

`أيُّ المعنيين هو المعلَّل؟ وأيُّهما يبيّن السبب أو العلة؟`

Expected core response identifies the explained proposition and the proposition functioning as its reason, with the overt signal.

## Gate results

- distinctness from K63: PASS;
- cause-vs-purpose containment: PASS;
- overt-evidence requirement: PASS;
- discourse-locality: PASS;
- one-relation rule: PASS.

**Decision: K64 DRAFT-FROZEN.**

## Architectural significance

The discourse-semantic layer now supports controlled recognition of:
- coordination;
- temporal sequence;
- contrast/correction;
- result/consequence;
- cause/reason.

K63 and K64 intentionally train opposite discourse directions without collapsing them into one generic 'causal relation' competency.

## Next

Rescan K65 across purpose/goal, exception/restriction, elaboration, and controlled null-reference candidates. Select by distinct learner operation and dependency cost.