# QURBATA J1 P001–P040 — Master QA Gate Register v0.1

**Status: WORKING QA, NOT FROZEN, NOT PRINT READY.** Daftar ini menyatukan audit yang telah ada tanpa mengubah sumber kurikulum FROZEN. PASS terbatas hanya berarti dimensi yang tertulis telah diuji.

| Rentang | Status struktur Tartil | Sumber kandidat/QA | Tindakan terbuka |
|---|---|---|---|
| P001–P009 | PERLU AUDIT ULANG terhadap hard gate FROZEN | `QJ1_P001-P020_TOKEN_AUDIT_v0.1.md`; `QJ1_P001-P010_OVERLAY_4_INVENTARIS_AUTHORITY_v0.2.md` | Audit sel-per-sel 8×3, TARGET-only, EXACT-3, unik, legalitas review; P001 foundation pengecualian awal |
| P010 | CHECKPOINT / QA parsial | `QJ1_P010_P020_EVALUASI_AUTHORITY_CORRECTED_v0.2.md` | Audit cakupan dan glyph, tashih panel |
| P011 | BLOCKED — exception pending | `QJ1_P011-P012_KANDIDAT_GRID_EXCEPTION_PENDING_v0.1.md` | Dua target tidak dapat membentuk enam pasangan unik; minta persetujuan formal |
| P012 | BLOCKED — exception pending | `QJ1_P012_GRID_EXCEPTION_PENDING_v0.2.md` | Kandidat baru menghapus duplikasi latihan tak disengaja; persetujuan pengecualian tetap wajib |
| P013–P018 | PASS TERBATAS struktur/token | `QJ1_P013-P018_GRID_CURATED_HARD_GATE_v0.3.md` | Tashih dan kurasi pedagogis, proof A5 |
| P019 | PASS TERBATAS struktur/token | `QJ1_P019_GRID_KASRAH_HARD_GATE_v0.2.md` | Proof identitas ءِ / إِ / هِ dan layout |
| P020 | PASS TERBATAS checkpoint | `QJ1_P020_CHECKPOINT_AUDIT_STRUKTUR_v0.2.md` | Cakupan identitas lengkap, tashih panel, proof A5 |
| P021–P027 | PASS TERBATAS hard gate | `QJ1_P021-P027_AUDIT_HARD_GATE_DHAMMAH_v0.2.md` | Tashih harakat, glyph, pedagogi, layout |
| P028–P039 | PASS TERBATAS struktur/token (audit dalam sesi, laporan repo belum terkonfirmasi) | Tiga file `GRID_REVIEW_8x3_v0.1.md` untuk P028–030, P031–033, P034–039 | Kurasi pemerataan 29 identitas, proof visual, laporan QA perlu disimpan |
| P040 | PASS TERBATAS checkpoint final | `QJ1_P040_AUDIT_CAKUPAN_IDENTITAS_v0.2.md` | Tashih dan uji cetak; 29/29 identitas dan 24 token per harakat |

## Gerbang lintas halaman sebelum siap cetak
1. Sahkan atau tolak pengecualian penanaman P011–P012 melalui change control; jangan ubah FROZEN diam-diam.
2. Audit ulang P001–P010 memakai aturan yang sama dan putuskan khusus checkpoint.
3. Rekonsiliasi empat inventaris (Tartil, Bi'ah, Akhlak, Tahfidz) per halaman ke sumber otoritatif.
4. Tashih teks Arab, harakat, sumber nash Akhlak, dan arti ayat Tahfidz oleh pemeriksa kompeten.
5. Uji render A5 RTL, font KFGQPC Uthman Taha, ha dua lubang, alif/hamzah, QR RIQA OS, nilai–tanggal–paraf, dan proof cetak.

**Catatan versi:** `QJ1_P001-P020_TOKEN_AUDIT_v0.1.md` menghitung kandidat historis; jangan gunakan angkanya untuk menggantikan hasil kandidat baru P011–P019. `QJ1_P011-P020_AUDIT_TERPADU_KANDIDAT_v0.1.md` masih merekam P012 v0.1; status terbaru P012 ada di v0.2.
