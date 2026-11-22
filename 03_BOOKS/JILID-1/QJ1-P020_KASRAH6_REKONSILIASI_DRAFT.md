# QURBATA Jilid 1 — P020 Kasrah 6 (DRAF REKONSILIASI)

**Tanggal:** 22 November 2026. **Status:** DRAF PRODUKSI; BELUM FROZEN; BELUM FINAL CETAK.

## Keputusan usulan rekonsiliasi P020 vs checkpoint

- **Alur draf terbaru:** P014 pengayaan Fathah → P015 Kasrah 1 → P016 Kasrah 2 → P017 Kasrah 3 → P018 Kasrah 4 → P019 Kasrah 5 → **P020 Kasrah 6**.
- **Alasan pedagogis:** Kasrah 6 belum diajarkan pada alur draf P019; checkpoint Fathah–Kasrah tidak semestinya dilaksanakan sebelum seluruh Kasrah selesai.
- **USULAN:** pindahkan checkpoint P020 lama ke **P021**, **bukan keputusan FROZEN**. Ini menimbulkan benturan dengan register resmi P021 (materi berikutnya) dan harus direkonsiliasi sebelum pengesahan.
- **FROZEN TIDAK DIUBAH:** `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md` masih menetapkan P019 Kasrah 6 dan P020 CHECKPOINT 20; `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md` masih menetapkan P020 BA `اِقْرَأْ` dan Akhlak `وَقُلْ رَبِّ زِدْنِي عِلْمًا`. Materi tersebut tidak boleh hilang dari kurikulum akibat usulan pergeseran.

## 1. Tartil — Kasrah 6

**Kompetensi baru:** `كِ لِ مِ نِ هِ وِ يِ ءِ إِ` (bentuk hamzah memerlukan audit master tipografi). **Review:** semua Fathah dan Kasrah 1–5. Latihan huruf lepas, tanpa Dhammah, mad, tanwin, sukun, tasydid, atau sambung.

**Sumber semua slot:** keluaran deterministik spesifikasi **P019 Kasrah 6** dari `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`; **16 latihan tiga huruf dahulu**, diikuti 8 latihan dua huruf. Tidak mengarang latihan.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | مَ لِ كَ | كَ بِ رَ | عَ مِ لَ |
| 2 | فَ هِ مَ | لَ بِ سَ | جَ لِ سَ |
| 3 | وَ رِ ثَ | بَ قِ يَ | مِ نِ بِ |
| 4 | هِ وِ تِ | يِ ءِ ثِ | إِ جِ حِ |
| 5 | كِ خِ دِ | لِ ذِ رِ | مِ زِ سِ |
| 6 | نِ شِ صِ | كِ لِ | مِ مَ |
| 7 | نِ نَ | هِ وِ | يِ هَ |
| 8 | ءِ وَ | إِ كِ | لِ يَ |

### Audit slot

- **24/24 slot terisi**, 16 kelompok tiga huruf + 8 kelompok dua huruf, total 64 token.
- **24/24 slot unik**, **0 duplikasi**.
- **0 token Kasrah prematur** berdasarkan whitelist Fathah kumulatif + Kasrah 1–6.
- **Catatan wajib:** `ءِ` dan `إِ` harus diaudit dengan KFGQPC Uthman Taha dan master grafem; bentuk cetak belum diverifikasi. Audit karakter bukan verifikasi pedagogis, fonologis, atau visual final.
- **Gate cetak: BLOCKED** hingga rekonsiliasi FROZEN, audit glyph dan render, serta persetujuan urutan checkpoint.

## 2. Bahasa Arab — REPEAT-1

**`أَغْلِقِ الْكِتَابَ`** — **Tutuplah buku.**

- Diperkenalkan pada draf P019, P020 adalah penguatan pertama. Guru memerintah, santri menutup buku dan mengulang instruksi.
- Nash berasal dari `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md` P021–P023; pemetaan maju ke P019–P021 **belum disahkan**.
- **Kewajiban rekonsiliasi:** `اِقْرَأْ` (Bacalah) yang tercatat untuk P020 FROZEN harus tetap ditempatkan pada checkpoint/usulan halaman lain, bukan dihapus.

## 3. Akhlak — REPEAT-1

**`أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ`** — **Tunaikanlah amanah kepada orang yang mempercayaimu.**

- Diperkenalkan pada draf P019, P020 penguatan pertama. Pembiasaan: mengembalikan pinjaman dan menjaga titipan.
- Nash berasal dari register integrasi FROZEN v1.3 P021–P023, belum diubah.
- **Kewajiban rekonsiliasi:** `وَقُلْ رَبِّ زِدْنِي عِلْمًا` yang tercatat untuk P020 FROZEN tidak boleh hilang dari progres Akhlak.

## 4. Tahfidz — QS. Al-Masad ayat 3 (USULAN)

**`سَيَصْلَىٰ نَارًا ذَاتَ لَهَبٍ`** — **Kelak dia akan masuk ke dalam api yang bergejolak.**

- Alur usulan: P016 Al-Ikhlas:3 (**keputusan pengguna**) → P017 Al-Ikhlas:4 → P018 Al-Masad:1 → P019 Al-Masad:2 → **P020 Al-Masad:3**.
- Generator lama mencantumkan Al-Masad:3 untuk P018 (`سَيَصْلَى نَارًا ذَاتَ لَهَبٍ`); versi dengan alif kecil `سَيَصْلَىٰ` memerlukan verifikasi glyph Utsmani.
- **Belum disahkan** sebagai perubahan master Tahfidz FROZEN.

## Gate produksi lanjutan

1. Rekonsiliasi benturan checkpoint P021 dengan materi P021–P030 yang masih FROZEN, termasuk BA/Akhlak P020.
2. Audit khusus bentuk `ءِ`, `إِ` dan ayat Tahfidz terhadap font Utsmani.
3. Audit 24 slot secara visual dan kesesuaian tahap, lalu render buku A5.
4. Jangan mengubah register FROZEN, generator PDF, atau page object final tanpa persetujuan.

## Bukti sumber

- `03_BOOKS/JILID-1/QJ1-P019_KASRAH5_REKONSILIASI_DRAFT.md`
- `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`
- `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`
- `03_BOOKS/JILID-1/AMENDMENT_TAHFIDZ_P016_2026-11-22.md`
- `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs`
