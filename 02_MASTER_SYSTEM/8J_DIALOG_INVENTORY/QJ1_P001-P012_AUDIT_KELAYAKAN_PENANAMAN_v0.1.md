# QURBATA J1 P001–P012 — Audit Kelayakan Kombinatorial Penanaman v0.1

**Status: BLOCKER ANALYSIS / keputusan FROZEN belum diubah.** Sumber: `02_MASTER_SYSTEM/QURBATA-J1-TARTIL-PAGE-REGISTER-FROZEN-v1.0.md`, bagian aturan struktur dan HARD GATES. Enam sel penanaman wajib berisi tepat dua token TARGET dan seluruh kelompok harus unik. Dengan n token TARGET, maksimum pasangan berurutan unik jika pengulangan token di dalam pasangan diperbolehkan adalah n²; jika tidak diperbolehkan adalah n(n−1). Karena itu n=2 tidak dapat menghasilkan enam pasangan unik, bahkan bila pasangan seperti بَ بَ diperbolehkan.

| Halaman | TARGET | n | Maksimum pasangan unik (boleh token sama) | Enam pasangan unik mungkin? |
|---|---|---:|---:|---|
| P001 | بَ تَ ثَ | 3 | 9 | YA |
| P002 | ءَ أَ | 2 | 4 | TIDAK |
| P003 | جَ حَ خَ | 3 | 9 | YA |
| P004 | دَ ذَ رَ زَ | 4 | 16 | YA |
| P005 | سَ شَ | 2 | 4 | TIDAK |
| P006 | صَ ضَ | 2 | 4 | TIDAK |
| P007 | طَ ظَ | 2 | 4 | TIDAK |
| P008 | عَ غَ | 2 | 4 | TIDAK |
| P009 | فَ قَ | 2 | 4 | TIDAK |
| P010 | CHECKPOINT | — | — | Tidak berlaku |
| P011 | كَ لَ | 2 | 4 | TIDAK |
| P012 | مَ نَ | 2 | 4 | TIDAK |

**Kesimpulan:** delapan halaman (P002, P005–P009, P011, P012) memerlukan keputusan resmi terkait `DUPLICATE_GROUP_FAIL` versus kewajiban enam pasangan TARGET-only. Ini adalah kontradiksi logis pada spesifikasi, bukan otomatis kesalahan penyusun grid. Jangan memberi PASS penuh pada halaman tersebut sebelum change control disahkan.

## Usulan keputusan (belum disahkan)
- Tetap 6 sel penanaman EXACT-2 TARGET-only.
- Khusus halaman n=2, izinkan paling banyak dua pengulangan pasangan yang disengaja dan ditandai; 18 sel latihan utama tetap wajib unik.
- Tidak mengubah urutan kompetensi, jumlah halaman, TARGET, atau aturan token review.
- P001/P003/P004 tetap harus memenuhi enam pasangan unik; audit konten grid aktual diperlukan.

## Batas audit
Dokumen ini memeriksa *kelayakan aturan*, bukan validasi 24 sel dari sumber P001–P009. Sumber grid 8×3 aktual belum berhasil diidentifikasi secara pasti di branch renderer; jangan mengarang PASS atau FAIL sel aktual. Untuk audit lanjutan, temukan path sumber produksi tiap halaman dan verifikasi dengan parser per sel. Tashih Arab, glyph, dan visual A5 masih terbuka.
