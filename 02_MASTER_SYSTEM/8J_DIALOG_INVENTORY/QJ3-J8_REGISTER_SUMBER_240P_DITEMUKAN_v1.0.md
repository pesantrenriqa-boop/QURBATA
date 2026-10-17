# Register penemuan sumber J3–J8 — 17 Oktober 2026

**Temuan penting:** enam jilid **tidak kosong**. Inventarisnya sudah tersedia sebagai dokumen agregat 40 halaman per jilid, bukan file individual bernama `QJx_P001_...`.

| Jilid | Matriks 4 inventaris (40 halaman) | Dialog 40 halaman | Pengayaan 40 halaman | Status |
|---|---|---|---|---|
| J3 | `QJ3_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md` | `QJ3_P001-P040_DIALOG_TERINTEGRASI_v0.1.md` | `QJ3_P001-P010_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ3_P011-P020_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ3_P021-P040_PENGAYAAN_4_INVENTARIS_v0.1.md` | STAGING, bukan final |
| J4 | `QJ4_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md` | `QJ4_P001-P040_DIALOG_TERINTEGRASI_v0.1.md` | `QJ4_P001-P010_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ4_P011-P020_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ4_P021-P040_PENGAYAAN_4_INVENTARIS_v0.1.md` | STAGING, bukan final |
| J5 | `QJ5_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md` | `QJ5_P001-P040_DIALOG_TERINTEGRASI_v0.1.md` | `QJ5_P001-P010_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ5_P011-P020_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ5_P021-P040_PENGAYAAN_4_INVENTARIS_v0.1.md` | STAGING, bukan final |
| J6 | `QJ6_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md` | `QJ6_P001-P040_DIALOG_TERINTEGRASI_v0.1.md` | `QJ6_P001-P010_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ6_P011-P020_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ6_P021-P040_PENGAYAAN_4_INVENTARIS_v0.1.md` | STAGING, bukan final |
| J7 | `QJ7_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md` | `QJ7_P001-P040_DIALOG_TERINTEGRASI_v0.1.md` | `QJ7_P001-P010_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ7_P011-P020_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ7_P021-P040_PENGAYAAN_4_INVENTARIS_v0.1.md` | STAGING, bukan final |
| J8 | `QJ8_MATRIKS_4_INVENTARIS_40P_STAGING_v0.1.md` | `QJ8_P001-P040_DIALOG_TERINTEGRASI_v0.1.md` | `QJ8_P001-P010_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ8_P011-P020_PENGAYAAN_4_INVENTARIS_v0.1.md`; `QJ8_P021-P040_PENGAYAAN_4_INVENTARIS_v0.1.md` | STAGING, bukan final |

## Pemeriksaan sampel isi
- J5 matriks P001: fokus Tartil `Orientasi mad lanjutan`; Tahfidz `An-Naba 1–8`; nash Akhlak masih ditandai belum teridentifikasi/tertakh­rij.
- J6 dialog P001: dialog guru–santri tersedia, tetapi contoh Qurani dan ayat Tahfidz belum diisi pada dokumen dialog tersebut; crosswalk Tahfidz harus dibaca dari sumber berwenang.
- J8 pengayaan P021–P023: latihan praktik, dialog, tema adab dan target Tahfidz ada, namun nash hadis dan grid latihan belum terverifikasi.

## Implikasi ke pipeline
1. **Jangan menciptakan ulang 240 halaman dari nol.** Ekstrak 6 matriks + 6 dialog + 18 dokumen pengayaan ke data per halaman; simpan lokasi sumber dan kutipan field.
2. `source_present` tidak sama dengan `ready_to_print`. Bedakan `FOCUS_MAPPED`, `DIALOG_DRAFT`, `HADITH_PENDING`, `TAHFIDZ_MAPPED`, `EXERCISE_PENDING`.
3. Cek referensi Tahfidz setiap jilid dengan crosswalk FROZEN, bukan dengan placeholder dialog.
4. Jangan mengganti tema adab dengan hadis yang belum ditakhrij; bank hadis 12 kandidat hanya sumber kurasi.
5. J1: gunakan jalur Opsi B untuk validasi saja, karena masih NOT FROZEN. J2: 40 paket siap review, belum CONTENT-FINAL.

## Prioritas produksi berikutnya
- Bangun extractor deterministik untuk baris matriks Markdown 40×6, ekspor CSV/JSON dengan source path, status dan blocker.
- Gabungkan dialog dan pengayaan per nomor halaman secara eksplisit; tandai ambiguitas untuk reviewer.
- Jalankan uji sampel P001, P020, P038, P040 setiap jilid sebelum ekspor seluruh halaman.
- Review nash/hadis dan token Qurani terpisah dari kelengkapan struktur.

**CONTENT-FINAL belum disahkan.**
