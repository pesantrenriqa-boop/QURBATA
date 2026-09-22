# QURBATA Jilid 1 — Tartil Content Audit P001–P040 v0.1

**Status:** AUDIT OPEN — PDF production remains blocked  
**Branch:** `renderer/pagedjs-p001-prototype`

## Purpose

This file reconciles the content and renderer gates before Jilid 1 P001–P040 can be frozen as one production master.

## Authority

1. Frozen Tartil page registers P001–P040 remain authority for letter/harakat progression.
2. `QURBATA-J1-TARTIL-CONTENT-MASTER-P001-P020-FROZEN-v1.0.md` remains current content authority for P001–P020.
3. `QURBATA-J1-TARTIL-CONTENT-MASTER-P021-P040-WORKING-v0.1.md` remains working authority for P021–P040.
4. Renderer changes MUST NOT be used to silently repair lexical/curricular content.

## Reconciled gate status

| Gate | Status | Note |
|---|---|---|
| Register P001–P040 | PASS | Frozen page-register sequence is authoritative |
| P001–P020 allocation | PASS / lexical audit pending | Frozen v1.0 remains authority |
| P021–P039 24-group allocation | PASS | Exact allocations recorded in working master |
| P040 checkpoint inventory | PASS | 29 identities + 3 harakat names + 24 reading groups |
| Dhammah exact-form evidence | PASS | Authorized anchors: كَبُرَ، حَسُنَ، ضَعُفَ |
| HOLD candidates excluded | PASS | No HOLD item may enter production |
| 3-letter pseudo-word prohibition | PASS as rule | Production requires meaningful exact-harakat words |
| Global inherited Fathah/Kasrah lexical-source audit | **PENDING** | v0.8 correctly left this gate open; v0.9 did not supersede it |
| Detached ه two-hole visual proof | **PENDING CI/RENDERER** | Unicode U+0647 must remain unchanged |
| PDF production | **BLOCKED** | Until both pending gates pass |

## Mandatory lexical audit scope

Every unique 3-letter item inherited from P001–P020 must be checked for:

- exact Arabic spelling;
- exact printed harakat;
- Indonesian gloss;
- lexical/source status: `QURAN-CONFIRMED`, `FUSHA-VERIFIED`, or `HOLD`;
- first legal page, determined by the **actual letter carrying the newly introduced harakat**.

Priority re-check set:

`شَطَرَ` · `مَرَجَ` · `يَبَسَ` · `نَشِطَ` · `عَطِشَ` · `خَطِفَ` · `رَصَدَ` · `ضَجَرَ` · `قَرَعَ` · `شَفَعَ`

No item may be promoted from HOLD by inference.

## Renderer gate

Sentinels:

- P013: `هَ`
- P019: `هِ`
- P027: `هُ`
- P040: `ه`

PASS requires visible two-hole detached heh while preserving underlying Unicode `ه` (U+0647) and frozen KFGQPC Uthman Taha policy.

## Freeze rule

Do **not** freeze P021–P040 or unified P001–P040 until:

`GLOBAL LEXICAL PASS → HA-TWO-HOLE VISUAL PASS → UNIFIED CONTENT FREEZE → GENERATOR MIGRATION → BUILD → VISUAL AUDIT`



## Lexical audit pass A — priority re-check set

External dictionary verification was performed for the priority set. Production classification is conservative: an item is not promoted unless the exact vocalized form is supported.

| Item | Audit status | Meaning / note | Production decision |
|---|---|---|---|
| شَطَرَ | FUSHA-VERIFIED | berpisah/menjauh; also verb under root شطر | KEEP |
| مَرَجَ | HOLD | exact fully-vocalized production form not yet independently closed in this pass | HOLD |
| يَبَسَ | **REJECT EXACT FORM** | authoritative dictionary gives perfect **يَبِسَ**, “menjadi kering” | REMOVE/REPLACE if present as verb |
| نَشِطَ | FUSHA-VERIFIED | giat/bersemangat | KEEP |
| عَطِشَ | FUSHA-VERIFIED | haus | KEEP |
| خَطِفَ | HOLD | exact vocalization still requires authoritative closure | HOLD |
| رَصَدَ | FUSHA-VERIFIED | mengamati/mengintai | KEEP |
| ضَجَرَ | HOLD | exact vocalization/source closure pending | HOLD |
| قَرَعَ | HOLD | exact vocalization/source closure pending | HOLD |
| شَفَعَ | HOLD | exact vocalization/source closure pending | HOLD |

### Correction required

The P013 allocation in frozen v1.0 currently lists `يَبَسَ`. This cannot remain as an exact-harakat verb under the strict v1.6.4 rule. The verified Form-I perfect is `يَبِسَ`, whose kasrah on ب makes it illegal on P013 (Fathah stage). Therefore:

- do **not** silently alter frozen v1.0;
- issue a v1.1 correction before unified freeze;
- replace the P013 `يَبَسَ` slot with a previously verified, page-legal Fathah word or controlled repetition;
- `يَبِسَ` may only be considered on/after the page where بِ is legal.

### Gate impact

Global inherited Fathah/Kasrah lexical-source audit remains **PENDING**. This pass found one concrete exact-harakat defect (`يَبَسَ`) and four HOLD items requiring closure. Unified content freeze remains blocked.


## Lexical audit pass B — authoritative dictionary closure

Using Cairo Arabic Language Academy dictionary evidence:

- `خَطِفَ` — **FUSHA-VERIFIED**. The dictionary explicitly records `خَطِفَ` as a Form-I perfect variant with meaning equivalent to `خَطَفَ`. **KEEP**.
- `قَرَعَ` — **FUSHA-VERIFIED**. Exact perfect is explicitly recorded, including “ضربه / طرق الباب”. **KEEP**.
- `يَبَسَ` — remains **REJECT EXACT FORM**; correction to `يَبِسَ` remains required and page legality must be recalculated.
- `مَرَجَ`, `ضَجَرَ`, `شَفَعَ` — remain **HOLD** until exact-vocalization evidence is attached.

### Priority-set status after pass B

KEEP: `شَطَرَ، نَشِطَ، عَطِشَ، رَصَدَ، خَطِفَ، قَرَعَ`

REJECT: `يَبَسَ`

HOLD: `مَرَجَ، ضَجَرَ، شَفَعَ`

Unified freeze remains blocked until HOLD=0 and the P013 correction is issued as a versioned master amendment.


## Lexical audit pass C — close remaining HOLD set

Authoritative/lexicographic evidence closes the remaining priority HOLD set:

| Item | Result | Note | Decision |
|---|---|---|---|
| مَرَجَ | FUSHA-VERIFIED | exact form recorded; among meanings: mixed/released/let graze | KEEP |
| شَفَعَ | FUSHA-VERIFIED | exact form recorded; interceded / joined a like thing to it | KEEP |
| ضَجَرَ | **REJECT EXACT FORM AS VERB** | dictionaries identify the verb as ضَجِرَ; ضَجَر is its verbal noun | REMOVE/REPLACE |

### Priority re-check closure

Priority HOLD count is now **0**.

- KEEP: `شَطَرَ، مَرَجَ، نَشِطَ، عَطِشَ، خَطِفَ، رَصَدَ، قَرَعَ، شَفَعَ`
- REJECT exact form: `يَبَسَ، ضَجَرَ`

### Versioned correction requirement

The frozen P001–P020 v1.0 must not be edited in place. A corrected v1.1 must:

1. replace `يَبَسَ` with a page-legal verified Fathah item or controlled repetition;
2. replace `ضَجَرَ` with a page-legal verified Fathah item or controlled repetition;
3. retain `يَبِسَ` and `ضَجِرَ` only for a later page where the actual Kasrah-bearing letter is legal;
4. preserve all other register constraints.

This closes the **priority-set** lexical audit only. The book-level global unique-word inventory still requires an explicit machine-readable audit table before GLOBAL LEXICAL PASS can be declared.
