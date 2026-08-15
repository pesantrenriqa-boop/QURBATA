# QURBATA TAHFIDZ — JILID 1 TARTIL ALIGNMENT AUDIT v0.1

**Document ID:** QTS-J1-ALIGN-001  
**Status:** ACTIVE AUDIT / NOT FROZEN  
**Date:** 15 August 2026  
**Tahfidz input:** `QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.1.md`  
**Repository evidence:** QURBATA Jilid 1 curriculum/book commit history and recovered page sources

---

## 1. Purpose

Audit the proposed Tahfidz Jilid 1 P001–P040 map against the actual pedagogical progression of QURBATA Tartil Jilid 1 before page targets are frozen or printed.

This audit deliberately distinguishes two modes:

- **READ-ALIGNED:** learner can reasonably decode the tahfidz target using competencies already introduced;
- **TALQIN-ALIGNED:** learner may memorize the target by listening/imitation even though the written Qur'anic form exceeds current decoding competence.

For Jilid 1, full Qur'anic text will normally exceed the learner's independent reading competence. Therefore Tahfidz is allowed to begin through talqin, but the book must not falsely imply independent reading mastery.

---

## 2. Repository Evidence Recovered

Commit history confirms that Jilid 1 is fundamentally an early harakat/letter-recognition volume, not yet a full Qur'anic decoding volume.

Key evidence:

- P002: hamza–alif page (`df8ff884...`)
- P003: jim-family page (`d1e3a28e...`)
- P010: fathah evaluation (`d2ad616c...`)
- P011: kaf–lam page (`571e1da1...`)
- P012: mim–nun page (`6201a799...`)
- P020: fathah–kasrah evaluation (`5b7d15f7...`)
- P021: heavy-letter kasrah (`7c869c31...`)
- P022: fa–qaf–kaf–lam kasrah (`2085e63c...`)
- P023: mim–nun–waw–ya kasrah (`5aa38f76...`)
- P024: kasrah integration (`a89904cb...`)
- P025: fathah–kasrah contrast (`5444aae1...`)
- P026: initial dhammah (`8b045a11...`)
- P027: throat-letter dhammah (`f24f8f83...`)
- P029: dal–shin dhammah (`d0747a65...`)
- P030: three-harakat evaluation (`a4ceaa64...`)
- P031: emphatic dhammah (`16a66d04...`)
- P032: fa–lam dhammah (`c7f0154d...`)
- P034: completion of a two-page harakat cycle (`28dca72f...`)
- P033–P040 are registered as the closing Jilid-1 page block (`87efef15...`), with the master completed through P040 (`c820ca4c...`).

Recovery history also shows P001–P040 were actively recovered/audited, so Tahfidz integration must bind to the canonical/recovered J1 content rather than create a competing tartil sequence.

---

## 3. Main Audit Finding

### Finding A — Tahfidz may start at P001, but as TALQIN

The learner at the start of J1 does not yet possess the reading competencies required to independently decode normal Qur'anic orthography. Therefore the early tahfidz target must be presented as **hafalan melalui talqin**, not as a reading exercise.

### Finding B — Tahfidz text must not control the tartil syllabus

The selected surah/ayah can contain sukun, shaddah, mad, tanwin, hamzah forms, connected script, waqf signs, and other features not yet taught in J1. This is acceptable for memorization-by-listening, but those features must not be counted as J1 tartil competencies.

### Finding C — Alignment should become progressively stronger

As J1 progresses through fathah → kasrah → dhammah and cumulative harakat integration, the learner's visual familiarity with the memorized text increases. Nevertheless, full independent mushaf reading remains a later-QURBATA outcome.

### Finding D — Evaluation pages require a different tahfidz policy

Repository history explicitly identifies at least P010, P020, and P030 as evaluation points. These pages should not automatically carry the same new-hifz burden as ordinary instruction pages. They are natural candidates for **zero/light new target + cumulative murojaah/validation**.

This finding changes the earlier assumption that all 40 pages should receive equal new-hifz capacity.

---

## 4. Alignment Bands for Jilid 1

| Page band | Tartil state from repository evidence | Tahfidz mode | New-hifz policy |
|---|---|---|---|
| P001–P009 | early letter/fathah foundation | TALQIN-DOMINANT | very light |
| P010 | fathah evaluation | REVIEW GATE | zero/light new hifz |
| P011–P019 | continued letters + kasrah development | TALQIN + VISUAL FAMILIARITY | light |
| P020 | fathah–kasrah evaluation | REVIEW GATE | zero/light new hifz |
| P021–P025 | kasrah integration/contrast | TALQIN + VISUAL FAMILIARITY | light → moderate |
| P026–P029 | dhammah introduced/developed | TALQIN + THREE-HARAKAT AWARENESS | moderate |
| P030 | three-harakat evaluation | REVIEW GATE | zero/light new hifz |
| P031–P039 | closing cumulative harakat block | TALQIN + STRONGER VISUAL LINK | moderate |
| P040 | terminal J1 consolidation | TERMINAL REVIEW GATE | preferably no new corpus; consolidate J1 |

**P040 terminal-review treatment is a design recommendation pending page-type confirmation; it is not yet frozen.**

---

## 5. Consequence for Existing P001–P040 Tahfidz Draft

The existing `QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.1.md` remains useful as a **corpus sequence draft**, but its one-target-per-page distribution must be revised.

Required revision rules:

1. preserve the approved hybrid corpus architecture;
2. preserve the initial functional priority of An-Nas / short surahs / Al-Fatihah unless later corpus audit changes it;
3. reduce or remove new-hifz load on evaluation gates P010, P020, P030;
4. strongly consider P040 as terminal consolidation rather than new target;
5. redistribute displaced ayat across adjacent ordinary pages only if the per-page load remains appropriate;
6. early pages use explicit `TALQIN` status;
7. do not require the student to read the tahfidz target independently;
8. do not use the tahfidz target to introduce untaught tartil rules prematurely.

---

## 6. Proposed Book Metadata

Each Tahfidz box should eventually carry machine-readable metadata even if only part is visually printed:

`TAHFIDZ_TARGET`
`TAHFIDZ_MODE = TALQIN | READ_ASSISTED | READ_ALIGNED`
`NEW_HIFZ_LOAD = VERY_LIGHT | LIGHT | MODERATE | ...`
`MUROJAAH_SET`
`VALIDATION_MODE`
`TARTIL_ALIGNMENT = PREVIEW | PARTIAL | ALIGNED`

Example for an early page:

`TAHFIDZ: QS. An-Nas [114]: 1`
`MODE: TALQIN`
`TARTIL_ALIGNMENT: PREVIEW`

The printed student page does not necessarily need to display all technical fields; they can live in the source data / teacher system.

---

## 7. Important Design Principle Discovered

Tahfidz QURBATA should be **synchronized with tartil without being imprisoned by tartil**.

If memorization were restricted only to text the learner can already decode independently, J1 tahfidz would become unnaturally small. Conversely, if tahfidz text is treated as reading material, it leaks higher tartil competencies into J1.

The solution is dual-channel learning:

**Tartil channel:** what the learner is formally learning to decode/read.  
**Tahfidz channel:** authentic Qur'anic corpus memorized primarily through talqin, gradually converging with reading competence.

This dual-channel principle is recommended for the entire J1–J8 system and should later be considered for freeze.

---

## 8. Audit Gate Result

| Gate | Result |
|---|---|
| Tahfidz can begin at J1-P001 | PASS, via TALQIN |
| Existing J1 corpus sequence can be retained as draft | PASS WITH REVISION |
| Existing equal page allocation can be frozen | FAIL |
| Evaluation pages need special handling | PASS |
| Tahfidz and tartil must use separate competency semantics | PASS |
| J1 page map ready for final freeze | NOT YET |

**Overall:** `PASS WITH REQUIRED REDISTRIBUTION`

---

## 9. Next Artifact

Create:

`QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.2.md`

The v0.2 map must:
- reserve P010/P020/P030 as review/evaluation gates;
- test P040 as terminal consolidation;
- redistribute new memorization across instructional pages;
- mark TALQIN/preview alignment;
- preserve a realistic cumulative J1 corpus;
- explicitly separate `hafalan baru` from `murojaah`.

Only after v0.2 is checked against the final canonical J1 page types should a J1 Tahfidz page map be frozen.

---

**Audit state:** COMPLETE v0.1  
**Freeze state:** NOT FROZEN  
**Next:** J1 Tahfidz Map v0.2 redistribution