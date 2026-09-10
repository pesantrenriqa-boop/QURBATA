# Rescan K32–K35 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K31 DRAFT-FROZEN in research layer.  
**Purpose:** menguji `قد`, `إنّ`, `كان`, dan `ليس` sebagai recognition nodes terpisah dari efek gramatikalnya.

## 1. K32 candidate — recognition `قد`

Target: mengenali `قد` pada occurrence yang tervalidasi sebagai particle sebelum fi'il.

Strengths:
- token lokal dan tidak berinfleksi;
- dapat muncul sebelum madhi atau mudhari';
- tidak perlu langsung mengajarkan seluruh nuansa tahqiq/taqlil/expectation.

Risks:
- makna fungsional berbeda menurut konteks;
- semantic interpretation tidak boleh dijadikan satu K dengan recognition.

**Judgement:** VERY HIGH.

## 2. K33 candidate — recognition `إنّ`

Target: mengenali `إنّ` sebagai particle pada occurrence yang tervalidasi.

Strengths:
- surface form jelas;
- sangat produktif;
- construction effect dapat dikunci untuk K lain.

Risks:
- jangan otomatis mengajarkan isim `إنّ` manshub dan khabar marfu';
- perlu membedakan dari `إنْ` syarthiyyah/nafiyah sesuai tagging occurrence.

**Judgement:** VERY HIGH WITH FUNCTION DISAMBIGUATION.

## 3. K34 candidate — recognition `كان`

Target: mengenali occurrence `كان` sebagai verb/copular element tanpa mengajarkan sistem kana wa akhawatuha penuh.

Strengths:
- token verbal yang familiar;
- jalur verb recognition sudah kuat dari K6/K7/K26.

Risks:
- `كان` adalah fi'il yang membawa tense/aspect dan subject relation;
- penggunaan naqis vs tamam harus dibedakan oleh occurrence;
- effect pada isim/khabar tidak boleh ikut terbuka.

**Judgement:** HIGH, tetapi lebih berat daripada particle-only recognition.

## 4. K35 candidate — recognition `ليس`

Target: mengenali `ليس` sebagai negative copular verb pada occurrence yang tervalidasi.

Strengths:
- bentuk relatif stabil;
- fungsi khas dan penting.

Risks:
- secara struktural lebih dekat ke nawasikh verbal daripada particle recognition;
- subject/predicate relation tidak boleh otomatis dianalisis penuh.

**Judgement:** MODERATE-HIGH.

## 5. Head-to-head result

Urutan awal yang paling ringan secara dependency:

1. **K32-CAND — recognition `قد`**
2. **K33-CAND — recognition `إنّ`**
3. **K34-CAND — recognition `كان`**
4. **K35-CAND — recognition `ليس`**

Reasoning:
- `قد` dan `إنّ` adalah recognition particle nodes dengan locality sangat tinggi;
- `كان` dan `ليس` membawa verbal/copular burden yang lebih besar;
- efek i'rab dan full construction tetap dikunci.

## 6. Locked effects

### For `قد`
- detailed semantic nuance;
- interaction with aspect beyond basic recognition.

### For `إنّ`
- isim `إنّ` / khabar `إنّ` analysis;
- accusative/nominative effect;
- distinction from all `إن` homographs beyond occurrence tagging.

### For `كان`
- isim `كان` / khabar `كان` analysis;
- ناقص vs تام generalization;
- tense/aspect abstraction.

### For `ليس`
- full copular negation construction;
- isim/khabar case analysis.

## 7. Architecture rule

For high-polyfunction or nawasikh-related tokens, each evidence row must include:
- surface token;
- corpus POS/function tag;
- occurrence role;
- construction effect locked/unlocked;
- ambiguity/homograph flag.

## 8. Next

1. evidence bank K32–K33;
2. counterexample test whether `إنّ` should precede `قد` based on clean-context yield;
3. compare K34 `كان` with other lightweight recognition nodes before freezing;
4. only later open full constructions `إنّ + اسم + خبر`, `كان + اسم + خبر`, and `ليس + اسم + خبر`.