# QURBATA Jilid 1 — P018 Kasrah 4 (DRAF REKONSILIASI)

**Status:** DRAF PRODUKSI, BELUM FROZEN / BELUM SIAP CETAK. **Tanggal:** 22 November 2026.

## Dasar dan otoritas

- Urutan produksi usulan: P014 Fathah pengayaan; P015 Kasrah 1; P016 Kasrah 2; P017 Kasrah 3; **P018 Kasrah 4**.
- **Register FROZEN v1.0 masih menyatakan P018 Kasrah 5 (`عِ غِ فِ قِ`)**; dokumen ini tidak mengubahnya.
- Semua 24 slot Tartil di bawah berasal dari **keluaran deterministik spesifikasi P017 Kasrah 4** pada `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs`, blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`. Diurutkan ulang dengan **16 kelompok tiga huruf dahulu, lalu 8 kelompok dua huruf**. Tidak menciptakan latihan baru.

## Tartil — Kasrah 4

**Kompetensi baru:** `صِ ضِ طِ ظِ`. **Murojaah:** Kasrah 1–3 (`بِ تِ ثِ جِ حِ خِ دِ ذِ رِ زِ سِ شِ`) dan seluruh Fathah sebelumnya. Huruf tetap lepas; tanpa Dhammah, mad, tanwin, sukun, tasydid, atau sambung.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | بَ صِ رَ | رَ ضِ يَ | فَ طِ نَ |
| 2 | عَ ظِ مَ | حَ صِ رَ | فَ ضِ لَ |
| 3 | عَ طِ شَ | ظِ صِ لَ | ضِ طِ مَ |
| 4 | ظِ صِ نَ | ضِ طِ هَ | ظِ وَ يَ |
| 5 | صِ بِ تِ | ضِ ثِ جِ | طِ حِ خِ |
| 6 | ظِ دِ ذِ | صِ ضِ | طِ عَ |
| 7 | ظِ غَ | صِ ضِ | طِ فَ |
| 8 | ظِ قَ | صِ ضِ | طِ كَ |

### Audit 24 slot

- **24/24 slot terisi** dari sumber generator, terdiri atas **16 tiga-huruf + 8 dua-huruf** (total 64 token).
- **22/24 slot unik**: `صِ ضِ` muncul **3 kali**. Dua duplikasi harus diperbaiki dari sumber terverifikasi atau melalui persetujuan editorial sebelum cetak.
- **Whitelist harakat:** 24/24 slot hanya memakai Kasrah yang telah diperkenalkan sampai Kasrah 4 atau Fathah kumulatif; **0 Kasrah prematur** pada tahap ini. Ini audit karakter, **bukan** persetujuan final semua aspek pedagogis.
- **Format:** 3-huruf dahulu adalah keputusan produksi terbaru; berbeda dari urutan 8 pasangan dahulu dalam generator FROZEN.
- **Gate cetak:** **BLOCKED** karena duplikasi dan ketidaksesuaian urutan kurikulum terhadap register FROZEN. Tidak boleh diimpor ke RIQA OS sebagai halaman final.

## Bahasa Arab (Bi'ah) — REPEAT-2 / penguatan terakhir

- `اِفْتَحِ الْكِتَابَ` — **Bukalah buku.**
- Diperkenalkan dalam **draf P016**, REPEAT-1 pada P017, dan **REPEAT-2 pada P018**. Bukan pengenalan materi baru lagi. Fokus kegiatan: murid merespons perintah dengan membuka buku, kemudian mengucapkannya dengan benar.
- Sumber nash: register integrasi FROZEN v1.3, asal P017–P019. Urutan draf dimajukan satu halaman dan belum disahkan dalam FROZEN.

## Akhlak — REPEAT-2 / penguatan terakhir

- `وَقُولُوا لِلنَّاسِ حُسْنًا` — **Berkatalah yang baik kepada manusia.**
- Diperkenalkan dalam **draf P016**, REPEAT-1 pada P017, **REPEAT-2 pada P018**. Fokus pembiasaan: mengucapkan kalimat yang baik kepada teman.
- Sumber nash: register integrasi FROZEN v1.3, asal P017–P019.

## Tahfidz — usulan QS. Al-Masad ayat 1

- **Target usulan P018:** **QS. Al-Masad:1** — `تَبَّتْ يَدَا أَبِي لَهَبٍ وَتَبَّ`.
- **Arti:** Binasalah kedua tangan Abu Lahab dan benar-benar binasa dia.
- **Alur:** P016 Al-Ikhlas:3 (**ditetapkan pengguna**), P017 Al-Ikhlas:4 (**usulan**), P018 Al-Masad:1 (**usulan**).
- **Asal ayat:** generator lama memuat Al-Masad:1 pada P016; ayat digeser ke P018 sebagai konsekuensi urutan Tahfidz yang diminta, **belum menjadi revisi resmi master Tahfidz FROZEN**.

## Catatan sebelum finalisasi

1. Ganti dua duplikasi `صِ ضِ` dengan materi yang sah dan bersumber, lalu audit ulang 24 slot.
2. Verifikasi kesinambungan Tahfidz P015–P019 terhadap baseline master; P017 dan P018 belum mendapat ketetapan eksplisit pengguna.
3. Rekonsiliasi register FROZEN dan generator produksi secara terkendali sebelum membuat PDF final.
4. Jangan melanjutkan pengulangan panel Bahasa Arab dan Akhlak yang sama ke P019 sebagai pengenalan baru tanpa peninjauan progres.

## Sumber

- `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`.
- `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`.
- `03_BOOKS/JILID-1/QJ1-P017_KASRAH3_REKONSILIASI_DRAFT.md`.
- `03_BOOKS/JILID-1/AMENDMENT_TAHFIDZ_P016_2026-11-22.md`.
- `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs`.
