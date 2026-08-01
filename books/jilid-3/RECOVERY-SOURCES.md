# QJ3 — Register Sumber Recovery

**Status:** ACTIVE  
**Induk:** `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`

## Keputusan Kurikulum Pengendali

Jilid 3 harus diperlakukan sebagai tahap **sukun per huruf target dan integrasi bertahap**, tanpa memasukkan tasydid atau hukum tajwid lanjutan sebelum waktunya. Versi yang mendahului realignment ini hanya menjadi sumber pembanding.

## Batch yang Ditemukan

| Rentang | File/commit | Status | Tindakan |
|---|---|---|---|
| P001–P010 | `books/JILID-3/PAGE-001-010.md`; `3c47a20fb8bb2f9688f4f1521c1068db53274a7c` | FOUND-DRAFT-BATCH | P001–P005 mengandung contoh. P006–P010 harus diambil dari versi produksi/koreksi yang lebih baru. |
| P006–P010 | commit `f9f9677a6a5388afa740158b969520dc61fbb7a0` | FOUND-LATER-VERSION | Bandingkan dengan urutan sukun per huruf target serta hasil QA P001–P010. |
| P011–P020 | `books/JILID-3/PAGE-011-020.md`; `aadd8918ba865a2a4338fdfdf736ceb154b95173` | FOUND-DRAFT-BATCH | Audit semua contoh terhadap prasyarat. Sejumlah frasa memuat tasydid/struktur lanjut sehingga tidak otomatis lolos. |
| P021–P030 | commit `05dfd094584c39e1ef09cee181d75516f52c63a8` | FOUND-DRAFT-BATCH | Ekstrak per halaman, lalu audit progression dan materi baru. |
| P031–P040 | commit `fb0a15ddf60239d99aa299dc40ce85a4a531c997` | FOUND-DRAFT-BATCH | Ekstrak per halaman, lalu audit progression, evaluasi, dan integrasi akhir. |
| Master | commit `e2df1c7aeca82285b23df704697c48178445f98d` | FOUND-MASTER | Sejajarkan dengan keputusan kurikulum sukun tanpa tasydid. |

## Sumber yang Dikecualikan

- Commit `4c61a3dcb9390225308b031fe9944fac99f6db2d` dan batch yang dinyatakan invalid/frozen.
- Versi sebelum realignment Jilid 3 menjadi tahap sukun.
- Contoh yang memasukkan tasydid, hukum tajwid, atau unsur lain yang belum lulus whitelist halaman.
- Klaim rasio 60:40 yang bertentangan dengan keputusan distribusi terbaru.

## Lokasi Tujuan

Setelah diekstrak dan diverifikasi, setiap halaman ditempatkan pada:

`books/jilid-3/pages/QJ3-P001.md` sampai `books/jilid-3/pages/QJ3-P040.md`.

File batch lama tetap disimpan sebagai bukti recovery tetapi tidak menjadi sumber produksi langsung.
