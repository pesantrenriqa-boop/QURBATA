# Rescan K46 — Simple Shart vs Clausal Predicate v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Baseline:** K1–K45 DRAFT-FROZEN.

## Purpose

Menentukan operasi belajar paling ringan berikutnya setelah K45, dengan fokus pada dua frontier besar yang kini tersisa:
1. hubungan syarth sederhana;
2. khabar berbentuk klausa.

K46 harus tetap atomic, cumulative-only, dan dapat didukung contoh Qurani tanpa memaksa dependency lebih tinggi.

---

## Candidate A — simple conditional linkage

### New operation
Learner can identify:
- a validated conditional marker;
- the condition/protasis clause;
- the response/apodosis clause;
- the basic semantic dependency between them.

### Strength
- distinct and highly meaningful;
- opens a major Qur'anic clause relation;
- many examples available in principle.

### Burden
- two-clause boundary;
- particle ambiguity;
- jawab markers may vary;
- verbal mood/jazm may become relevant;
- some occurrences use omitted/implicit response;
- conditional markers do not all behave identically.

To keep atomicity, K46 cannot teach all أدوات الشرط or all jazm rules at once.

**Judgement: HIGH value, but structurally heavy.**

---

## Candidate B — clausal khabar in simple jumlah ismiyyah

### New operation
Learner recognizes that the khabar slot of an already-mastered nominal sentence may be filled by a complete simple clause rather than a single noun/adjective/PP.

Possible core form:

`مبتدأ + [جملة فعلية خبر]`

or one narrowly chosen sub-type only.

### Foundation
- K8 nominal predication;
- K10 basic verbal relation;
- K41 basic fa'il mustatir;
- K42–K45 clause-boundary discipline from relative structures.

### Strength
- one host construction rather than two linked independent clauses;
- can be restricted to a simple verbal-clause predicate;
- directly expands an already-frozen syntactic slot.

### Burden
- رابط between mubtada' and clausal khabar may be required;
- the inner clause must be fully analyzable;
- nominal-clause khabar would be a separate subtype and should not be merged immediately.

**Judgement: VERY HIGH if K46 is narrowed to verbal-clause khabar only.**

---

## Head-to-head result

A narrowly defined **verbal-clause khabar** is lighter than full conditional linkage because it introduces one embedded predicate slot inside a known structure, whereas syarth requires coordinating two clauses plus marker behavior.

### Provisional decision

- **K46-CAND — jumlah fi'liyyah sederhana sebagai khabar mubtada'**
- **K47-CAND — simple conditional linkage**, subject to rescan after K46

## K46 provisional definition

Learner can identify a simple nominal sentence whose khabar is a **short verbal clause**, with all internal clause relations already analyzable through K1–K45.

## Hard exclusions

K46 does not yet include:
- jumlah ismiyyah as khabar;
- clausal khabar under `إنّ`, `كان`, or `ليس`;
- nested clauses;
- conditional clauses;
- complex discourse linkage;
- cases where the required رابط is omitted or disputed;
- advanced semantic interpretation.

## Evidence policy for next gate

### PASS-A
- explicit mubtada';
- short verbal-clause khabar;
- clear linkage to mubtada';
- internal grammar ≤ K45;
- no new clause relation beyond K46.

### PASS-B
Additional cumulative material only.

### REVIEW-RABIT
Khabar clause is clear but the رابط mechanism itself requires a new operation not securely frozen.

### PREMATURE
Nested clause, syarth, clausal khabar under nawāsikh, disputed boundary, or additional new construction.

## Decision

Open evidence gate for K46 as **simple verbal-clause khabar of a mubtada'**. Do not freeze until the `رابط` issue is explicitly stress-tested.