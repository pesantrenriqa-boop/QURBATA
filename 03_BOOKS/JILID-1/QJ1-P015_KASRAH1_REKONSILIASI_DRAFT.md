# QURBATA Jilid 1 — P015 Kasrah 1 (DRAF REKONSILIASI)

**Status:** USULAN PRODUKSI — BELUM FROZEN / BELUM FINAL CETAK  
**Dasar keputusan pengguna:** P014 telah selesai sebagai pengayaan Fathah; P015 dimulai dengan latihan Kasrah tiga huruf `بِ تِ ثِ`.  
**Sumber latihan:** keluaran deterministik generator `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` (blob SHA `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`), **asal kompetensi P014**.  
**Sumber otoritas yang belum direvisi:** `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md` (blob SHA `c0a464916ae9b2a84c7bc0d85e1edb29a364b794`).

## Kompetensi

Kasrah pertama: `بِ تِ ثِ جِ`, dengan Fathah terdahulu sebagai murojaah. Ini merupakan usulan pemindahan materi Kasrah 1 dari P014 ke P015; **belum mengubah register FROZEN**, yang saat ini masih menetapkan P014 Kasrah 1 dan P015 Kasrah 2.

## Latihan produksi — tiga huruf dahulu

Urutan baca dan slot ditata ulang sesuai instruksi pengguna: latihan pertama persis `بِ تِ ثِ` (berasal dari instruksi pengguna, **bukan** dari generator). Slot lainnya disalin dari keluaran generator P014, **bukan dibuat baru**. Untuk mempertahankan 24 slot, contoh asli `تِ وَ يَ` tidak disertakan pada versi draf ini.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | بِ تِ ثِ | كَ تِ بَ | ثَ بِ تَ |
| 2 | تَ بِ عَ | وَ جِ دَ | سَ جِ دَ |
| 3 | رَ جِ عَ | جِ بِ صَ | تِ ثِ ضَ |
| 4 | جِ بِ طَ | تِ ثِ ظَ | جِ بِ عَ |
| 5 | تِ غَ فَ | ثِ قَ كَ | جِ لَ مَ |
| 6 | بِ نَ هَ | بِ تِ | ثِ ذَ |
| 7 | جِ رَ | بِ تِ | ثِ زَ |
| 8 | جِ سَ | بِ تِ | ثِ شَ |

## Integrasi dari register v1.3

- **Bahasa Arab:** `أَعِدْ` — Ulangilah — REPEAT-1 / murojaah pertama.
- **Akhlak:** `وَلَكَ الْجَنَّةُ` — Dan bagimu surga — REPEAT-1 / murojaah pertama.
- **Tahfidz:** belum dikunci; perlu rekonsiliasi urutan P014 yang sudah selesai terhadap master Tahfidz. Tidak mengambil urutan Tahfidz dari generator sebagai keputusan baru.

## Gate audit yang masih terbuka

- Total **24 slot**, dengan **16 kelompok tiga huruf lebih dahulu**, diikuti **8 kelompok dua huruf**; ini **menyimpang dari urutan generator lama** yang menempatkan 8 kelompok dua huruf dahulu.
- Masih terdapat duplikasi `بِ تِ` sebanyak tiga kali; **belum lulus audit keunikan**.
- Rasio baru/murojaah dan whitelist harus diaudit ulang untuk urutan yang diubah; tidak mengklaim PASS.
- **Tidak mengubah FROZEN, master kurikulum, generator resmi, ataupun Page Object lama**. Dokumen ini hanya menyimpan permintaan revisi produksi secara terlacak.

## Jejak sumber

- Generator: https://github.com/pesantrenriqa-boop/QURBATA/blob/main/production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs
- Register: https://github.com/pesantrenriqa-boop/QURBATA/blob/main/03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md
- Integrasi: `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`
