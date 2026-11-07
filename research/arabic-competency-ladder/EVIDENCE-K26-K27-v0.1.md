# Evidence Bank K26–K27 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE
**Parent:** `HEAD-TO-HEAD-K26-K28-v0.1.md`

## K26-CAND — Recognition Fi'il Amr Sederhana

Target: mengenali bentuk fi'il amr Qurani yang occurrence-nya tervalidasi sebagai imperative, tanpa membuka analisis fa'il mustatir, i'rab, atau paradigma tashrif lengkap.

### Evidence policy

PASS bila:
- token benar-benar imperative;
- recognition cukup pada surface morphology + corpus tag;
- tidak perlu menjelaskan subject recovery;
- suffix/object tambahan yang membawa kompetensi sesudah K26 tidak menjadi bagian target core.

REVIEW/PREMATURE bila:
- imperative melekat dengan object suffix yang belum ingin dianalisis;
- bentuk membutuhkan analysis of weak verb/complex derivation untuk sekadar dikenali;
- target bercampur dengan particle/government yang belum tersedia.

### Candidate forms for corpus expansion

Contoh jenis bentuk yang akan dicari dan divalidasi occurrence-specific:
- قُلْ
- خُذْ
- كُلْ
- اذْهَبْ
- اعْبُدُوا
- اذْكُرُوا

Catatan: bentuk plural seperti `اعبدوا` membawa subject morphology; boleh masuk recognition bank, tetapi fungsi subject/person tidak menjadi target K26.

### Integrity judgement

**STRONG.** K26 dapat dipertahankan sebagai recognition node selama metadata memisahkan `verb_form=imperative` dari `subject_analysis=locked`.

---

## K27-CAND — Recognition Partikel Nafi Dasar

Target bukan “menguasai nafi” secara penuh, tetapi mengenali occurrence yang berfungsi negatif dengan function tagging.

### Atomicity rule

Tidak semua bentuk disatukan sebagai satu efek gramatikal:
- `لا`
- `ما`
- `لم`
- `لن`

mempunyai governance dan potensi fungsi lain yang berbeda.

K27 hanya membuka **recognition of negative function**.

### Evidence record wajib

- surface_token
- corpus_tag
- negative_function=yes/no
- governing_effect
- governing_effect_unlocked=no
- ambiguity_flag

### PASS

Occurrence dapat masuk bila fungsi negatifnya jelas dan efek lanjutan pada mudhari'/nominal belum diperlukan untuk target recognition.

### PREMATURE

- `لا` النافية للجنس jika pembelajaran menuntut isim/khabar la;
- `لم` jika target dipaksa sekaligus menjelaskan jazm;
- `لن` jika target dipaksa sekaligus menjelaskan nasb;
- `ما` pada occurrence non-negatif.

### Integrity judgement

**STRONG WITH FUNCTION TAGGING.** Recognition dapat ditempatkan awal, tetapi governance harus dikunci.

---

## Head-to-head result

K26 tetap sedikit lebih awal daripada K27 karena:
- memperluas kategori verbal yang sudah dikenal;
- target recognition dapat dipahami tanpa menambah operator sintaksis baru;
- K27 mempunyai ambiguity/polyfunctionality lebih tinggi.

Urutan dipertahankan:

- K26 — recognition fi'il amr
- K27 — recognition partikel nafi dasar

## Freeze readiness

- K26: READY-FOR-DRAFT-FREEZE
- K27: READY-FOR-DRAFT-FREEZE WITH FUNCTION-TAGGING CONSTRAINT

## K28 Rescan

Kandidat K28 belum otomatis `هل`. Sebelum freeze berikutnya, audit lightweight recognition berikut:
- `هل` sebagai interrogative marker;
- hamzah istifham sebagai clitic/particle;
- vocative particle `يا`;
- future marker `سـ / سوف`;
- emphatic/attention particles jika corpus dependency sangat rendah.

Prinsip: jangan memajukan satu token hanya karena bentuknya singkat; nilai dependency, ambiguity, productivity, dan clean-example yield.