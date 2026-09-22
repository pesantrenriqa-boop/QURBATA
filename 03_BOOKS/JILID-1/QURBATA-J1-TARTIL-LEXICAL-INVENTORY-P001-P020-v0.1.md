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
