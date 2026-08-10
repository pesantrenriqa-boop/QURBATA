# Head-to-Head K28–K29 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K27 draft-frozen.  
**Candidates:** recognition `هَلْ` vs recognition `يَا`.

## 1. K28 Candidate A — `هَلْ` Interrogative Recognition

Target:
- mengenali `هَلْ` sebagai penanda pertanyaan pada occurrence yang tervalidasi;
- belum menganalisis scope pertanyaan atau struktur jawabannya.

Strengths:
- token berdiri sendiri dan tidak berinfleksi;
- fungsi interrogative relatif stabil;
- tidak menuntut i'rab baru;
- dapat diisolasi sebagai recognition node.

Risks:
- clause sesudahnya sering kompleks;
- teaching evidence harus memilih konteks yang seluruh dependency-nya <= current K;
- recognition token tidak sama dengan penguasaan jumlah istifhamiyyah.

**Structural score:** VERY HIGH.

## 2. K29 Candidate B — `يَا` Nida' Recognition

Target:
- mengenali `يَا` sebagai marker nida' pada occurrence yang tervalidasi;
- belum menganalisis jenis munada atau i'rab munada.

Strengths:
- token berdiri sendiri dan sangat lokal;
- fungsi discourse/address kuat dan mudah dikenali;
- tidak membutuhkan teori kasus pada tahap recognition.

Risks:
- unsur sesudah `يا` sangat bervariasi: proper noun, idhafah, `أيها`, noun phrase kompleks;
- bila contoh pedagogis mengambil seluruh phrase, dependency cepat naik;
- relation nida' penuh harus tetap locked.

**Structural score:** VERY HIGH.

## 3. Clean-Context Comparison

Kedua node sama-sama ringan. Tie-break dilakukan dengan prinsip `minimal valid pedagogical context`.

### `هَلْ`
Recognition dapat diajarkan pada token itu sendiri, tetapi secara fungsi ia selalu membuka scope proposisional; konteks penuh sering lebih panjang.

### `يَا`
Recognition juga dapat diajarkan pada token itu sendiri, dan fungsi vocative dapat diketahui tanpa perlu menganalisis seluruh struktur sesudahnya.

Namun `يا` sering menempel pada konstruksi munada yang secara pedagogis mudah disalahpahami sebagai sudah dikuasai jika phrase ditampilkan tanpa lock metadata.

## 4. Preliminary Ordering

Tidak ada dependency reversal. Karena K28 sebelumnya sudah dibuka sebagai frontier istifham atomik dan `هل` sangat stabil secara category recognition, urutan dipertahankan:

- **K28-CAND — recognition `هَلْ` sebagai interrogative marker**
- **K29-CAND — recognition `يَا` sebagai nida' marker**

Keduanya pada dependency graph sebenarnya paralel; numbering hanya linearization pedagogis.

## 5. Evidence Rules

### K28
- token harus `هل` pada fungsi interrogative;
- clause scope tidak otomatis menjadi bagian target;
- contoh penuh yang mengandung K30+ tetap boleh disimpan sebagai PREMATURE/CONTEXT-ONLY, bukan core evidence.

### K29
- token harus `يا` pada fungsi nida';
- jenis munada dan i'rab tetap locked;
- `يا + phrase` hanya core jika seluruh phrase <= K29, jika tidak token-only evidence dipakai.

## 6. Gate Assessment

- K28: **READY FOR DRAFT-FREEZE**
- K29: **READY FOR DRAFT-FREEZE**

Syarat bersama: metadata wajib membedakan `recognition_target` dari `construction_unlocked`.

## 7. Next Frontier

Setelah K28–K29, kandidat terdekat:
- K30-CAND — recognition hamzah istifham `أَ` dengan clitic segmentation;
- K31-CAND — recognition future marker `سوف`, lalu `سـ` sebagai segmented prefix bila evidence memadai;
- fa'il mustatir tetap ditunda;
- nida' construction dan interrogative clause analysis menjadi relation nodes terpisah di tahap lebih tinggi.
