# Final Gate K39 v1.0

**Status:** DRAFT-FROZEN — RESEARCH LAYER ONLY  
**Baseline:** K1–K38 DRAFT-FROZEN  
**Target:** simple `ليس + اسم ليس + خبر ليس`

## Competency

### K39 — REL-LAYSA-PRED
**Menganalisis konstruksi sederhana `ليس + اسم ليس + خبر ليس`.**

Siswa mampu:
- mengenali `ليس` sebagai pengubah predikasi nominal;
- menentukan اسم ليس yang eksplisit;
- menentukan خبر ليس yang eksplisit dan sederhana;
- membedakannya dari jumlah ismiyyah biasa.

## Hard dependencies

- K35 recognition `ليس`;
- K8 jumlah ismiyyah / predikasi nominal;
- fitur isim dan relasi nominal yang sudah frozen sebelumnya.

## Clean evidence boundary

### PASS-A
- explicit اسم ليس;
- explicit simple خبر;
- tidak memerlukan `بـ` الزائدة analysis;
- tidak memerlukan fa'il mustatir/subject inference;
- tidak memerlukan relative/clausal relation sesudah K39.

### PASS-B
- struktur target K39 plus hanya fitur dari K1–K38.

### REVIEW-BA
- خبر ليس dengan `بـ` atau fenomena yang memerlukan analisis tambahan.
- disimpan di corpus bank tetapi bukan core teaching evidence K39.

### REVIEW-MORPH
- bentuk persona/jumlah yang membuat subject analysis melampaui core K39.

### PREMATURE
- ellipsis berat;
- clausal/relative predicate yang belum dibuka;
- konstruksi lain yang memerlukan K40+.

## Freeze decision

K39 lolos karena:
1. operasi belajar distinct dari K35 recognition;
2. dependency graph stabil;
3. clean evidence cukup untuk mendefinisikan kompetensi tanpa mengandalkan REVIEW-BA;
4. tidak ditemukan dependency reversal yang memaksa full `كان` mendahului `ليس`;
5. quota contoh tidak dipaksakan bila merusak cumulative-only rule.

## Locked features

K39 tidak otomatis membuka:
- `باء` الزائدة في خبر ليس;
- seluruh paradigma `ليس`;
- ellipsis/omitted predicate analysis;
- clausal khabar;
- broader nawāsikh theory.

## Next frontier

- K40-CAND — simple `كان + اسم كان + خبر كان`;
- K41-CAND — basic fa'il mustatir;
- K42-CAND — isim maushul + minimal silah;
- later: special `بـ` with `ليس`, complex khabar, and other nawāsikh expansions.

## Production boundary

No production registry, AR-STG, master jilid, production page, or assessment is changed by this research freeze.