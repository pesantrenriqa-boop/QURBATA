# QURBATA J1 — Temuan QA P011–P018 terhadap Register Tartil FROZEN

Status: **BLOCKED — HARD GATE FAIL** pada file kandidat grid `QJ1_P011-P018_GRID_PATCH_APPLIED_v0.2.md`; bukan perubahan register FROZEN.

## Bukti
Register Tartil `02_MASTER_SYSTEM/QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md` menetapkan:
- REGULAR/TRANSITION: sel 1–6 harus EXACT-2 dan TARGET-only; sel 7–24 EXACT-3, memuat minimal satu TARGET dan sisanya hanya review legal.
- Kelompok duplikat dilarang; grup 1 huruf dilarang.

Grid kandidat P011 dan P012 masing-masing mengulang pasangan TARGET pada dua baris awal (misalnya `كَ لَ` berulang pada P011). P011–P012 hanya memiliki dua TARGET, sehingga enam pasangan TARGET-only unik tidak mungkin tercapai: maksimum kombinasi berurutan dengan pengulangan huruf hanya empat (`AA`, `AB`, `BA`, `BB`). Ini adalah konflik struktural antara register dan himpunan TARGET; **tidak boleh diselesaikan dengan mengarang kompetensi baru**.

Grid kandidat P011–P018 juga memuat kelompok latihan tanpa TARGET pada baris 5–8 (contoh P011 `بَ تَ ثَ`; P014 `وَ ءَ دَ`), melanggar HARD GATE relevansi TARGET. P011 dan P012 bahkan memiliki beberapa kelompok dua token di bagian latihan, bukan EXACT-3.

Dokumen verifikasi rasio `QJ1_P011-P018_VERIFIKASI_GRID_TOKEN_v0.1.md` menyatakan PASS TERBATAS untuk hitungan 60/40 dan whitelist, tetapi itu **tidak sama dengan PASS seluruh hard gates**.

## Keputusan
- Jangan mempromosikan kandidat P011–P018 sebagai final atau print-ready.
- Untuk P011–P012, minta keputusan kurikulum tentang konflik 6 pasangan unik TARGET-only pada halaman dengan 2 TARGET; tanpa izin jangan mengubah FROZEN.
- Untuk P013–P018, perlu kurasi ulang grid mengikuti target, jumlah token per sel dan keunikan kelompok.
- Audit P019/P020 terpisah; tiga panel pendukung P011–P020 telah dipetakan dari register integrasi v1.3 dan distribusi Tahfidz.
