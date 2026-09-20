# EVIDENCE MATURITY FRAMEWORK — K01–K65 v1.0

**Status:** FROZEN FRAMEWORK / BANK EXPANSION CONTINUES  
**Parent architecture:** `LADDER-ARCHITECTURE-v1.0.md`

## 1. Purpose

Architecture maturity and evidence-bank maturity are separate. A competency can be architecturally frozen while its Qur'anic example bank continues to grow.

## 2. Evidence maturity scale

- **E0 — DEFINITION:** competency identity exists, but no canonical anchor bank is locked.
- **E1 — ANCHOR:** at least one clean canonical Qur'anic anchor validates the operation.
- **E2 — SMALL CLEAN BANK:** several clean examples establish repeatability.
- **E3 — DIVERSIFIED VALIDATED BANK:** examples vary in lexical/surface form while preserving the same target operation; false positives and boundary cases are documented.
- **E4 — TEACHING READY:** bank is sufficient for explanation, guided practice, independent practice, and controlled transfer without importing later competencies.
- **E5 — ASSESSMENT READY:** bank supports parallel assessment forms, distractor design, scoring criteria, and reliable mastery decisions.

## 3. Required metadata per evidence item

Each canonical evidence record should eventually contain:
- K ID;
- surah:ayah;
- exact target span;
- target operation;
- prerequisite features present;
- forbidden/later features absent or controlled;
- occurrence-specific function validation;
- difficulty band;
- use type: anchor / guided / independent / transfer / assessment;
- ambiguity note;
- validation status.

## 4. Maturity rule

A higher number of examples does not automatically mean higher maturity. Diversity, cleanliness, independent assessability, and absence of hidden later dependencies matter more than raw count.

## 5. Current architecture-level evidence posture

The discovery process used anchor evidence, clean-bank checks, stress tests, and final gates to freeze the identities of K01–K65. Therefore the architecture is not evidence-free. However, this framework deliberately does **not** claim E4/E5 globally until a dedicated per-K bank audit is completed.

Conservative operational status for downstream work:

- architecture identity: **FROZEN**;
- evidence existence: **CONFIRMED across the discovery process**;
- uniform production maturity: **NOT YET CLAIMED**;
- next evidence objective: promote each K through explicit E-level audits rather than inventing new competencies.

## 6. Promotion gates

### E1 → E2
Require multiple clean occurrences with the same operation and no hidden later dependency.

### E2 → E3
Require lexical/form diversity, documented exclusions, and successful boundary-case discrimination.

### E3 → E4
Require a teaching sequence: anchor → guided practice → independent practice → transfer, with cumulative-clean progression.

### E4 → E5
Require parallel assessment items, mastery threshold, scoring rubric, and evidence that the item tests the target K rather than vocabulary or a later K.

## 7. Evidence-bank workstream priority

Priority A: K01–K25 foundational high-frequency structures.  
Priority B: K38–K57 structurally sensitive operator/mood subsystem.  
Priority C: K58–K65 discourse-semantic relations, because marker multifunctionality requires strong occurrence-level validation.  
Priority D: recognition nodes K26–K37 for breadth and false-positive control.

Priority is about bank development, not competence importance.

## 8. Integration rule

Downstream curriculum and RIQA OS should store at minimum:

`canonical_k_id`, `architecture_version`, `evidence_maturity`, `evidence_record_id`, `surah`, `ayah`, `target_span`, `difficulty_band`, `validation_status`.

Legacy discovery IDs must be stored separately where historical traceability is needed.

## 9. Freeze verdict

**EVIDENCE MATURITY MODEL: FROZEN v1.0**  
**BANK CONTENT: LIVING / VERSIONED**  
**ARCHITECTURE K01–K65: NOT TO BE REOPENED merely because more examples are discovered.**