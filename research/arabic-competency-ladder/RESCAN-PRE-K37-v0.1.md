# Rescan Before K37 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K36 DRAFT-FROZEN.

## Purpose

Menguji kembali apakah limited family `كان` sudah menjadi node termudah berikutnya setelah K36 `لو`, atau masih ada token Qurani invariant/low-dependency yang seharusnya mendahuluinya.

## Candidates

### A. `بَلْ` recognition

Target: mengenali `بل` pada occurrence yang tervalidasi sebagai discourse/conjunction marker, tanpa mengajarkan rincian idrab/transition relation.

- invariant token;
- sangat lokal;
- tidak memerlukan paradigma;
- semantic discourse relation dapat dikunci.

**Judgement: VERY HIGH.**

### B. `لَكِنْ` / `لَكِنَّ`

Tidak boleh disatukan tanpa distinction. `لكن` dan `لكنّ` membawa analisis berbeda.

- surface recognition mungkin ringan;
- orthographic/morphosyntactic distinction penting;
- risk of conflating conjunction with ناسخ.

**Judgement: MODERATE-HIGH; requires split.**

### C. `أَوْ` recognition

Sebagai conjunction/disjunction marker.

- invariant;
- relation coordination sudah punya basis K16/K19;
- secara pedagogis bisa menjadi expansion dari conjunction inventory, bukan necessarily new structural K.

**Judgement: HIGH, but likely inventory expansion rather than independent competence.**

### D. `أَمْ` recognition

Interrogative/disjunctive behavior; depends partly on question structure and can be more complex.

**Judgement: MODERATE.**

### E. limited `كان` family recognition

Still useful and frequent, but carries inflectional family burden.

**Judgement: HIGH but heavier than invariant `بل`.**

## Decision

A lightweight node still precedes `كان`:

- **K37-CAND — recognition `بَلْ`**
- **K38-CAND — limited `كان` family recognition**

`أو` is provisionally treated as expansion under conjunction-recognition inventory unless evidence shows a genuinely new competency. This prevents artificial inflation of K count by lexical inventory alone.

`لكن/لكنّ` must be split and audited later. `أم` remains later due interrogative relation complexity.

## Important anti-inflation rule

Not every new particle receives a new K. A new K is justified only if it adds a distinct learnable operation/category/relation, not merely another lexical member of an already mastered inventory.

Therefore:
- `أو` may expand K16/K19 evidence/inventory;
- `بل` is provisionally new only if its corrective/discourse recognition is pedagogically distinct enough from simple coordination;
- final evidence gate must test this before freeze.

## Next

Head-to-head: `بل` as distinct recognition competence vs treating it as K16 inventory expansion. If it fails distinctness, K37 returns to limited `كان` family.