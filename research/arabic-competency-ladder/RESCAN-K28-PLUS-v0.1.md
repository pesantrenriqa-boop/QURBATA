# Rescan K28+ v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K27 DRAFT-FROZEN in research layer.  
**Purpose:** mencari node recognition/integration paling ringan sebelum masuk ke struktur inferensial seperti fa'il mustatir.

## Candidates audited

### A. `هَلْ` — interrogative marker recognition

Target: mengenali `هل` sebagai penanda pertanyaan pada occurrence yang tervalidasi.

Strengths:
- token sangat lokal;
- tidak memiliki inflection;
- tidak perlu langsung menganalisis struktur jawaban;
- tidak perlu menyatukan seluruh أدوات الاستفهام.

Risk:
- clause sesudah `هل` dapat kompleks, sehingga core unit recognition hanya token + metadata occurrence; contoh pedagogis harus dipilih dari konteks yang dependency-nya <= current K.

**Judgement: VERY HIGH.**

### B. Hamzah istifham `أَ` — recognition

Strengths:
- sangat produktif;
- fungsi interrogative penting.

Risks:
- clitic segmentation;
- surface `أ` dapat berdekatan dengan bentuk lain dan membutuhkan occurrence-specific tagging;
- scope pertanyaan sering meliputi struktur lebih besar.

**Judgement: HIGH, after `هل`.**

### C. `يَا` — nida' marker recognition

Target recognition saja, belum membahas i'rab munada atau jenis munada.

Strengths:
- sangat lokal;
- fungsi surface cukup jelas pada occurrence nida';
- banyak contoh Qurani.

Risks:
- konstruksi sesudah `يا` dapat proper noun, `أيها`, idhafah, atau bentuk lain; relation nida' belum boleh otomatis diajarkan penuh.

**Judgement: VERY HIGH.**

### D. Future markers `سـ` / `سوف`

Target recognition marker future.

Strengths:
- mengintegrasikan K7 mudhari' recognition;
- `سوف` token-level relatif jelas.

Risks:
- prefixed `سـ` requires segmentation;
- semantic future/modality should not be overgeneralized without occurrence evidence.

**Judgement: HIGH.**

## Head-to-head

`هل` and `يا` are the two strongest immediate candidates. Both are recognition nodes with minimal hard dependencies.

Pedagogical tie-break:
- `هل` extends clause-level communicative recognition but clause after it may be complex;
- `يا` introduces discourse/address marker but relation to munada can be held.

Because K28 was already opened as interrogative frontier and `هل` is atomically cleaner than the broader istifham family, keep:

- **K28-CAND — recognition `هل` as interrogative marker**
- **K29-CAND — recognition `يا` as nida' marker**
- **K30-CAND — recognition hamzah istifham `أَ`**
- **K31-CAND — recognition future markers `سـ/سوف`**, subject to segmentation audit

Fa'il mustatir moves behind these lightweight nodes.

## Critical architecture rule

Recognition K does not unlock the full construction automatically.

Examples:
- K28 recognizes `هل`; question-clause analysis remains locked.
- K29 recognizes `يا`; munada types/i'rab remain locked.
- K30 recognizes interrogative hamzah; scope analysis remains locked.
- K31 recognizes future marking; verbal subject analysis remains separate.

## Next

1. evidence bank K28–K29;
2. test whether `يا` should actually precede `هل` based on clean-context yield;
3. audit hamzah segmentation for K30;
4. only then return to fa'il mustatir and silah maushul.