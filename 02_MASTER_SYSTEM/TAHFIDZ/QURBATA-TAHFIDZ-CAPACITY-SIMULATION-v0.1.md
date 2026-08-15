# QURBATA TAHFIDZ — CAPACITY SIMULATION v0.1

**Document ID:** QTS-CAPACITY-SIM-001  
**Status:** ACTIVE ANALYTICAL SIMULATION / NOT FROZEN  
**Date:** 15 August 2026  
**Parent:** `QURBATA-TAHFIDZ-CORPUS-MASTER-v0.1.md`

---

## 1. Purpose

This simulation estimates how much Qur'anic corpus can realistically fit into QURBATA Jilid 1–8 before page-level allocation is frozen.

The purpose is to test H3/H4/H5/HX under different retention-reserve assumptions while preserving the frozen Hybrid Corpus architecture.

---

## 2. Planning Envelope

Working planning envelope:

- 8 jilid;
- approximately 40 learning pages/meetings per jilid;
- approximately 320 pedagogical units total.

The 320 units are not equal-sized memorization units. Load must increase as tartil competence and memorization independence grow.

---

## 3. Volume Proxy

For v0.1, the simulation uses **Mushaf-page equivalent** as a transparent volume proxy rather than pretending that ayah count represents equal memorization burden.

A sequential juz is treated as approximately 20 Mushaf pages for planning purposes. The exact final model will later be replaced/refined by word-count and phrase/chunk data.

Quran.com confirms that Juz 30 begins in the An-Naba section around Mushaf page 582 and that Juz 27 begins in the Adh-Dhariyat section, supporting the use of standard page-based juz segmentation as a practical first-pass corpus-volume proxy.

This page-equivalent model is **not a final pedagogical formula**.

---

## 4. Progressive Load Curve v0.1

To avoid underusing later learner capacity, the simulation assigns increasing relative load across the eight jilid.

| Jilid | Relative factor | Draft average new-hifz load per meeting |
|---|---:|---:|
| J1 | 1.0x | 2.0 lines |
| J2 | 1.4x | 2.8 lines |
| J3 | 1.9x | 3.8 lines |
| J4 | 2.5x | 5.0 lines |
| J5 | 3.2x | 6.4 lines |
| J6 | 4.0x | 8.0 lines |
| J7 | 4.8x | 9.6 lines |
| J8 | 5.5x | 11.0 lines |

For simulation only, a 15-line Mushaf-page equivalent is used.

Across 40 meetings per jilid, this produces an unconstrained gross capacity of approximately:

`1,944 lines ≈ 129.6 Mushaf pages ≈ 6.48 juz-equivalent`

This is the **gross theoretical capacity before retention reserve**.

---

## 5. Retention Reserve Scenarios

The model protects part of capacity for consolidation, evaluation, recovery, and real-school variability.

| Scenario | Protected capacity | Net new-hifz capacity | Approx. juz-equivalent |
|---|---:|---:|---:|
| R20 | 20% | 80% | 5.18 juz |
| R30 | 30% | 70% | 4.54 juz |
| R40 | 40% | 60% | 3.89 juz |

Interpretation:

- R20 represents an ambitious but still protected model;
- R30 is the current balanced-school candidate;
- R40 is a conservative model for environments with limited contact time or weaker out-of-class support.

---

## 6. Scenario Test

### H3 — Foundation + 3 sequential juz

Expected sequential coverage:

`Juz 30 + Juz 29 + Juz 28`

plus Al-Fatihah special priority and limited selected passages.

Result:
- PASS under R20;
- PASS under R30;
- PASS under R40.

Assessment: **robust but probably under-ambitious as the terminal target**.

### H4 — Foundation + 4 sequential juz

Expected sequential coverage:

`Juz 30 + Juz 29 + Juz 28 + Juz 27`

plus Al-Fatihah; selected corpus must be controlled by unique coverage and capacity.

Result:
- PASS under R20;
- PASS under R30;
- BORDERLINE-to-PASS under R40 depending on selected additions and actual page-level load.

Assessment: **strong current baseline candidate**.

### H5 — Foundation + 5 sequential juz

Expected sequential coverage:

`Juz 30 → Juz 26`

plus Al-Fatihah and only very limited selected additions.

Result:
- PASS/BORDERLINE under R20;
- TIGHT under R30;
- FAIL under R40.

Assessment: **stretch target, not yet robust enough to freeze**.

### HX — Maximum sustainable hybrid

The gross curve suggests more than five juz is mathematically conceivable if later jilid carry high volume, but this would consume nearly all flexibility and is not currently defensible for ordinary school implementation.

Assessment: **do not freeze beyond H5 without empirical trial data**.

---

## 7. Core Wajib and Selected Corpus Effect

Al-Fatihah is outside the Juz 30→ sequence and therefore adds unique corpus volume.

Some high-value selected candidates may already fall inside sequential coverage:

- Al-Mulk is contained in Juz 29;
- Al-Hashr 22–24 is contained in Juz 28.

These must not be double-counted.

Non-overlapping candidates such as Yasin, Ar-Rahman, Al-Waqi'ah, Ayat al-Kursi, Al-Baqarah 285–286, and selected Al-Kahf passages consume additional unique capacity.

Therefore a hybrid target must choose between:

`more sequential juz` **or** `more selected high-value corpus`.

The design should not pretend both are free.

---

## 8. v0.1 Recommendation

### Robust baseline candidate

**4 sequential juz-equivalent as the core backbone**, beginning:

`Juz 30 → Juz 29 → Juz 28 → Juz 27`

plus:
- Al-Fatihah as CORE WAJIB;
- selected passages only through F/E/M/T/C scoring and capacity replacement logic.

This is the best current balance between ambition, sequential continuity, and retention protection.

### Stretch candidate

**5 sequential juz-equivalent** through Juz 26 can remain a stretch scenario, especially for schools/classes with:

- stronger meeting frequency;
- more home repetition;
- digital/peer validation support;
- stronger teacher infrastructure;
- higher learner entry competence.

It should not yet be the universal minimum.

---

## 9. Important Interpretation

The recommendation **does not mean every graduate must be capped at exactly four juz**.

The system can use tiered attainment:

- **QURBATA Tahfidz Standard:** robust corpus target;
- **QURBATA Tahfidz Plus:** extended sequential/selected corpus;
- **QURBATA Tahfidz Accelerated:** stretch capacity leading into the 30-juz continuation program.

This allows one book system to serve ordinary schools and stronger tahfidz environments without lowering the baseline quality standard.

---

## 10. Candidate Terminal Architecture for Next Simulation

The next page-allocation simulation should test:

### STANDARD
- Al-Fatihah;
- Juz 30;
- Juz 29;
- Juz 28;
- Juz 27;
- selected corpus only where capacity remains or where it replaces lower-priority sequential load.

### PLUS
- STANDARD;
- expand toward Juz 26 and/or selected high-value surahs.

### ACCELERATED
- continue sequentially beyond the Standard target based on learner performance.

This tiering is **DRAFT**, not frozen.

---

## 11. Next Gate

Before freezing the terminal corpus, complete two additional checks:

1. **Corpus Detail Audit** — word/phrase volume for Juz 30–26 and selected candidates;
2. **Jilid Load Distribution** — determine where each sequential juz can realistically enter without making J1–J3 too heavy or J7–J8 overloaded.

After those checks, the project may freeze the Standard target and begin definitive `J1-P001 → J8-P040` mapping.

---

## 12. Decision Register v0.1

| ID | Finding | Status |
|---|---|---|
| QTS-SIM-001 | Juz 30 alone materially underuses the 8-jilid capacity | SUPPORTED |
| QTS-SIM-002 | H3 passes all reserve scenarios | SUPPORTED |
| QTS-SIM-003 | H4 is the current robust baseline candidate | RECOMMENDED / NOT FROZEN |
| QTS-SIM-004 | H5 is a stretch target | RECOMMENDED AS STRETCH / NOT FROZEN |
| QTS-SIM-005 | R30 is the current balanced reserve scenario | WORKING BASELINE |
| QTS-SIM-006 | Selected corpus must compete for unique capacity | ACTIVE |
| QTS-SIM-007 | Tiered Standard/Plus/Accelerated structure merits testing | DRAFT |

---

**State:** ACTIVE ANALYTICAL SIMULATION  
**Version:** 0.1  
**Next:** Corpus Detail Audit + Jilid Load Distribution