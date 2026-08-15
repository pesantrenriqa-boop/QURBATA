# QURBATA TAHFIDZ — J1–J8 MACRO ALLOCATION v0.1

**Document ID:** QTS-T1C-T2-001  
**Status:** WORKING SIMULATION / NOT FROZEN  
**Date:** 15 August 2026  
**Parent:** `JUZ30-CORPUS-INVENTORY-v0.1.md`  

## 1. Purpose

This document creates the first macro distribution of the Juz 30 candidate corpus across QURBATA Jilid 1–8 before page-level assignment.

The corpus contains 37 surahs / 564 ayat. QURBATA currently uses a planning baseline of approximately 40 pages per jilid, or ±320 page/meeting slots in eight jilid.

The allocation below is a pedagogical simulation. It is deliberately arranged from easier/shorter/familiar surahs toward larger and more complex surahs, rather than mechanically following mushaf order.

## 2. Macro Allocation v0.1

| Jilid | Candidate Surahs | Surah Count | Ayat Count | Main Function |
|---|---|---:|---:|---|
| J1 | An-Nas, Al-Falaq, Al-Ikhlas, Al-Kawthar, An-Nasr, Al-Kafirun | 6 | 27 | entry, talqin, very short/familiar corpus |
| J2 | Al-Masad, Al-Ma'un, Quraysh, Al-Fil, Al-Asr, At-Takathur, Al-Humazah | 7 | 41 | short-surah consolidation and load growth |
| J3 | Al-Qari'ah, Al-Adiyat, Az-Zalzalah, Al-Qadr, Ash-Sharh, At-Tin | 6 | 51 | transition to medium units |
| J4 | Ad-Duha, Ash-Shams, Al-Layl, Al-A'la | 4 | 66 | medium corpus; reading-hifz linkage strengthens |
| J5 | Al-Alaq, At-Tariq, Al-Infitar, Al-Balad | 4 | 75 | mixed-length verses and stronger lexical load |
| J6 | Al-Ghashiyah, Al-Buruj, Al-Inshiqaq | 3 | 73 | sustained medium/long surahs |
| J7 | Al-Fajr, At-Takwir, Al-Bayyinah, Al-Mutaffifin | 4 | 103 | advanced load; long-ayah splitting required |
| J8 | Abasa, An-Naba, An-Nazi'at | 3 | 128 | terminal corpus and transition toward advanced hifz |
| **TOTAL** | **Juz 30 candidate corpus** | **37** | **564** | |

## 3. Critical Finding

The raw ayah distribution becomes strongly back-loaded: J1 has only 27 ayat while J8 has 128. This is not automatically a defect because later learners can memorize larger units, and many late-Juz-30 verses are short. However, the jump is large enough that **ayah count cannot be used as the balancing metric**.

The next page simulation must balance text volume, not just verse count.

## 4. Page-Slot Strategy

Each jilid is provisionally treated as 40 slots. The 40 slots are not all required to introduce new ayat.

A slot may be:

- `N` — new memorization target;
- `C` — continuation of a long ayah;
- `K` — consolidation target / no new text;
- `E` — evaluation checkpoint.

This distinction is essential. A page may still display a tahfidz instruction even when its primary function is consolidation/evaluation.

## 5. Load Growth Principle

### J1
Extremely small targets. Talqin dominates. One short ayah may occupy a full meeting where necessary.

### J2
One or more short ayat per target as learner stability improves.

### J3
Short ayat may be grouped; medium verses normally remain one unit.

### J4
Target volume rises and begins to rely more strongly on the learner's tartil competence.

### J5
Mixed-length verses. Some long verses may require semantic chunking.

### J6
Sustained surah memorization. Several short rhythmic verses can form one unit.

### J7
Advanced load. Long verses such as portions of Al-Bayyinah and Al-Mutaffifin must be split by valid phrase/meaning boundaries.

### J8
Highest QURBATA load. Learner should be substantially more independent in reading and memorization. Several short verses may be assigned together, while long verses remain chunked.

## 6. Important Correction to the 320-Slot Model

The objective is **not** to force all 564 ayat into 320 equal targets. The correct model is:

`text volume → pedagogical chunks → distribute chunks according to learner level → reserve consolidation/evaluation space`

Therefore, before freezing the J1–J8 allocation, the system needs a page-level simulation and an audit of actual QURBATA tartil competencies.

## 7. Proposed First Page-Level Work Order

Page-level mapping will proceed in controlled batches:

1. J1-P001–P040
2. audit J1 load and tartil alignment
3. J2-P001–P040
4. audit cumulative retention pressure
5. continue sequentially through J8

This avoids generating 320 arbitrary rows and discovering structural problems only at the end.

## 8. Jilid 1 Candidate Sequence for Page Mapping

The first page-level simulation will use this candidate order:

1. An-Nas — 6 ayat
2. Al-Falaq — 5 ayat
3. Al-Ikhlas — 4 ayat
4. Al-Kawthar — 3 ayat
5. An-Nasr — 3 ayat
6. Al-Kafirun — 6 ayat

Total = 27 ayat.

Because J1 has approximately 40 pages, this cluster intentionally leaves substantial room for very small entry targets, repetition, consolidation, and evaluation. It is therefore suitable for testing the QURBATA principle that tahfidz follows beginner tartil rather than racing through a juz.

## 9. Status Assessment

**Macro result:** PLAUSIBLE, NOT YET FROZEN.

The complete Juz 30 target remains possible as a working hypothesis, but J7–J8 are the stress-test zones. If page-level modeling shows unhealthy load concentration, some terminal surahs must move to the post-QURBATA 30-juz program rather than compressing targets unnaturally.

## 10. Next Action

Create `JILID-1-PAGE-MAP-v0.1.md` containing all P001–P040 rows with:

`Page | Surah | Ayah | Part | Target Type | Relative Load | Rationale | Status`

The J1 map will be the first real test of the system and will later be compared against the actual tartil material on each QURBATA Jilid 1 page.

---

**State:** ACTIVE WORKING SIMULATION  
**Next:** QTS-T3-J1 — Jilid 1 page-level tahfidz map