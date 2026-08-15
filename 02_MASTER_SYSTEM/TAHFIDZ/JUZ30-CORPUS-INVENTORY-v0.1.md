# QURBATA TAHFIDZ — JUZ 30 CORPUS INVENTORY v0.1

**Document ID:** QTS-T1B-001  
**Status:** DRAFT ANALYTICAL INVENTORY / NOT FROZEN  
**Date:** 15 August 2026  
**Parent:** `QURBATA-TAHFIDZ-SYSTEM-BASELINE-v0.1.md` (content baseline currently v0.2)

## 1. Purpose

T1B inventories the candidate Juz 30 corpus before assigning targets to QURBATA pages. The purpose is to prevent arbitrary distribution such as `1 ayah = 1 page`.

Verified corpus boundary: Surah 78 An-Naba through Surah 114 An-Nas, 37 surahs and 564 ayat.

## 2. Corpus Inventory

| # | Surah | Ayat | Relative load | Initial pedagogical note |
|---:|---|---:|---|---|
| 114 | An-Nas | 6 | very light | strong entry candidate |
| 113 | Al-Falaq | 5 | very light | strong entry candidate |
| 112 | Al-Ikhlas | 4 | very light | strong entry candidate |
| 111 | Al-Masad/Al-Lahab | 5 | light | short but vocabulary less familiar |
| 110 | An-Nasr | 3 | light | short verses, moderate phrase length |
| 109 | Al-Kafirun | 6 | light | repetition supports retention |
| 108 | Al-Kawthar | 3 | very light | strong early candidate |
| 107 | Al-Ma'un | 7 | light | gradual increase |
| 106 | Quraysh | 4 | light | compact but connected phrases |
| 105 | Al-Fil | 5 | light | narrative sequence helps retention |
| 104 | Al-Humazah | 9 | light–medium | phonetic/vocabulary load rises |
| 103 | Al-Asr | 3 | light | ayah 3 substantially longer |
| 102 | At-Takathur | 8 | light | compact sequence |
| 101 | Al-Qari'ah | 11 | light–medium | repetition plus later longer ayat |
| 100 | Al-Adiyat | 11 | medium | rapid phonetic sequence |
| 99 | Az-Zalzalah | 8 | medium | several medium-length phrases |
| 98 | Al-Bayyinah | 8 | heavy | several very long ayat; requires splitting |
| 97 | Al-Qadr | 5 | light–medium | compact, familiar pattern |
| 96 | Al-Alaq | 19 | medium–heavy | mixed lengths; later ayat increase load |
| 95 | At-Tin | 8 | light–medium | gradual phrase growth |
| 94 | Ash-Sharh/Al-Inshirah | 8 | light | repetition/familiarity advantage |
| 93 | Ad-Duha | 11 | medium | later verses longer |
| 92 | Al-Layl | 21 | medium | many short ayat, cumulative load |
| 91 | Ash-Shams | 15 | medium | repeated oath structure supports chunking |
| 90 | Al-Balad | 20 | medium–heavy | mixed lengths and lexical load |
| 89 | Al-Fajr | 30 | heavy | long surah, mixed unit lengths |
| 88 | Al-Ghashiyah | 26 | medium–heavy | many manageable ayat but sizable corpus |
| 87 | Al-A'la | 19 | medium | relatively rhythmic sequence |
| 86 | At-Tariq | 17 | medium | compact opening, longer closing section |
| 85 | Al-Buruj | 22 | medium–heavy | mixed lengths and narrative/thematic shifts |
| 84 | Al-Inshiqaq | 25 | medium–heavy | multiple medium/long units |
| 83 | Al-Mutaffifin | 36 | heavy | long corpus with several long ayat |
| 82 | Al-Infitar | 19 | medium | mostly manageable but cumulative |
| 81 | At-Takwir | 29 | medium–heavy | many short rhythmic ayat; cumulative load |
| 80 | Abasa | 42 | heavy | high ayah count with mixed lengths |
| 79 | An-Nazi'at | 46 | very heavy | highest ayah count in Juz 30; mixed lengths |
| 78 | An-Naba | 40 | heavy | large corpus, mixed lengths |

**Important:** `Relative load` is a curriculum-engineering draft classification, not a religious classification and not yet a measured word-count score.

## 3. Quantitative Finding

Juz 30 contains **564 ayat**, while the current QURBATA planning baseline has approximately **320 page/meeting slots**.

Therefore:

- simple `1 ayah = 1 slot` is mathematically impossible for the complete Juz 30;
- the system must combine multiple very short ayat into one target where appropriate;
- some long ayat must consume more than one slot;
- therefore ayah count alone is not an adequate load metric.

This finding strengthens the need for a word/phrase-based pedagogical unit model.

## 4. Proposed Load Engine

For the next simulation, each ayah/unit should receive:

- `WC`: word count;
- `PC`: phrase/chunk count;
- `TL`: tartil complexity relative to current QURBATA level;
- `RL`: repetition/familiarity benefit;
- `SC`: semantic cut suitability for long ayat;
- `UL`: resulting pedagogical unit load.

Draft principle:

`Unit Load = text volume + articulation/reading complexity - repetition benefit`, with semantic boundaries controlling where splitting is allowed.

No numeric coefficient is frozen yet.

## 5. Initial Sequence Hypothesis

The first simulation should run **from the end of the mushaf backward**, but not blindly. Proposed starting sequence:

An-Nas → Al-Falaq → Al-Ikhlas → Al-Kawthar → An-Nasr → Al-Kafirun → Al-Masad → Al-Ma'un → Quraysh → Al-Fil → ...

Reason: this provides a low-load entry and familiar worship-use corpus. After the early cluster, sequencing may be adjusted by measured load rather than strictly descending surah number.

**NOT FROZEN.**

## 6. Key Design Consequence

The objective should not be phrased as “finish 564 ayat in 320 pages.” The correct objective is:

> distribute the complete candidate corpus into approximately 320 pedagogical units whose size grows with the learner's QURBATA tartil competence.

This means early pages can carry extremely small targets while later pages can carry several short ayat or larger phrases.

## 7. Preliminary Feasibility Assessment

**Juz 30 remains feasible enough to continue simulation**, but it cannot yet be declared the final target. The decisive test is whether measured word/phrase volume can fit into 8 jilid while reserving sufficient space for retention and without causing a sharp load jump in later jilid.

Three possible outcomes after page-level simulation:

1. **FIT** — Juz 30 fits with healthy progression and retention room.
2. **TIGHT** — Juz 30 fits technically but harms retention; reduce corpus or change allocation.
3. **OVERLOAD** — Juz 30 does not fit pedagogically; set a smaller QURBATA terminal corpus and leave the remainder for the 30-juz continuation program.

## 8. Next Output

T1C/T2 must produce a first **J1–J8 macro allocation**, followed by a page-level map.

Before freezing any page target, the map must be audited against the actual tartil content of each QURBATA page.

## 9. Source Verification Notes

Corpus boundary and total were cross-checked against Quran.com Juz 30 and secondary corpus/list sources on 15 August 2026. Surah ayah counts used here follow the standard 37-surah Juz 30 inventory.

---

**State:** ACTIVE WORKING DOCUMENT  
**Next:** QTS-T1C/T2 — macro sequence and volume distribution.