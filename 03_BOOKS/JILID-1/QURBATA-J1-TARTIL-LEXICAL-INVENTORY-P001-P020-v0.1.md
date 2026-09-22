# QURBATA J1 — Lexical Inventory Audit P001–P020 v0.1

**Status:** GLOBAL AUDIT IN PROGRESS  
**Authority:** Content Master P001–P020 FROZEN v1.1 candidate  
**Rule:** exact spelling + exact harakat + meaning + first-legal-page must pass.

## Audit ledger

### Corrected defects
| Form | Status | Action |
|---|---|---|
| يَبَسَ | REJECT | Intended verb is يَبِسَ; removed from Fathah-stage P013 |
| ضَجَرَ | REJECT | Intended verb is ضَجِرَ; removed from Fathah inventory |

### Priority forms closed
| Form | Status |
|---|---|
| شَطَرَ | FUSHA-VERIFIED |
| مَرَجَ | FUSHA-VERIFIED |
| نَشِطَ | FUSHA-VERIFIED |
| عَطِشَ | FUSHA-VERIFIED |
| خَطِفَ | FUSHA-VERIFIED |
| رَصَدَ | FUSHA-VERIFIED |
| قَرَعَ | FUSHA-VERIFIED |
| شَفَعَ | FUSHA-VERIFIED |

## First-legal-page rule

Legality follows the actual letter carrying the newly introduced harakat, not every letter in the word.

Examples:
- يَبِسَ requires بِ, therefore cannot be used on P013 Fathah stage.
- ضَجِرَ requires جِ, therefore cannot be used before جِ is legal.
- كَبُرَ is Dhammah-legal from P021 because the Dhammah carrier is بُ.

## Global audit batches

To avoid silently treating the old frozen list as verified, all unique 3-letter items are audited in batches:

1. P003–P006 Fathah inventory
2. P007–P010 Fathah inventory
3. P011–P013 Fathah inventory
4. P014–P018 Kasrah inventory
5. P019–P020 curated cumulative inventory

Each item must receive one of:
- QURAN-CONFIRMED
- FUSHA-VERIFIED
- HOLD
- REJECT

**Freeze condition:** HOLD=0, REJECT items removed from v1.1, and all first-legal-page checks PASS.

## Current gate

Priority-set audit: PASS  
Versioned correction v1.1: PASS  
Global unique-word audit: IN PROGRESS  
Unified P001–P040 freeze: BLOCKED


## Batch 1 — P003–P006 Fathah inventory

Audit target is the exact-harakat inventory actually used by the v1.1 candidate.

### P003
| Form | Gloss | Status | First-legal note |
|---|---|---|---|
| بَحَثَ | mencari / meneliti | FUSHA-VERIFIED | P003: بَ، حَ، ثَ legal |

### P004
| Form | Gloss | Status | First-legal note |
|---|---|---|---|
| جَحَدَ | mengingkari | FUSHA-VERIFIED | P004 |
| حَذَرَ | waspada / takut | FUSHA-VERIFIED | P004 |
| بَدَأَ | memulai | FUSHA-VERIFIED | P004 |
| أَخَذَ | mengambil | QURAN-CONFIRMED | P004 |
| خَبَرَ | mengetahui / menguji (lexical senses) | FUSHA-VERIFIED | P004 |
| بَرَزَ | tampil / keluar | FUSHA-VERIFIED | P004 |
| حَرَثَ | membajak / mengolah tanah | FUSHA-VERIFIED | P004 |

### P005 additions
| Form | Gloss | Status | First-legal note |
|---|---|---|---|
| دَرَسَ | belajar / mempelajari | FUSHA-VERIFIED | P005 |
| سَجَدَ | bersujud | QURAN-CONFIRMED | P005 |
| حَسَدَ | dengki | FUSHA-VERIFIED | P005 |
| حَبَسَ | menahan | FUSHA-VERIFIED | P005 |
| حَرَسَ | menjaga | FUSHA-VERIFIED | P005 |
| سَبَحَ | berenang / bergerak melaju | FUSHA-VERIFIED | P005 |
| شَرَحَ | menjelaskan / melapangkan | FUSHA-VERIFIED | P005 |
| شَرَدَ | lari / menyimpang | FUSHA-VERIFIED | P005 |
| شَرَبَ | minum | QURAN-CONFIRMED | P005 |
| سَحَبَ | menarik | FUSHA-VERIFIED | P005 |

### P006 additions
| Form | Gloss | Status | First-legal note |
|---|---|---|---|
| صَبَرَ | bersabar | FUSHA-VERIFIED | P006 |
| ضَرَبَ | memukul / membuat perumpamaan (context-dependent) | QURAN-CONFIRMED | P006 |
| حَصَدَ | menuai | FUSHA-VERIFIED | P006 |
| رَصَدَ | mengamati / mengintai | FUSHA-VERIFIED | P006 |
| صَرَخَ | berteriak | FUSHA-VERIFIED | P006 |
| صَدَرَ | keluar / terbit | FUSHA-VERIFIED | P006 |
| ضَحَكَ | tertawa | QURAN-CONFIRMED | P006 |

### Batch 1 decision

- Unique forms audited: **25**
- HOLD: **0**
- REJECT: **0**
- First-legal-page conflicts: **0**
- Batch 1: **PASS**

Note: QURAN-CONFIRMED is used only for items whose exact form is established; the remainder are conservatively classified FUSHA-VERIFIED rather than being promoted merely because their roots occur in the Qur'an.
