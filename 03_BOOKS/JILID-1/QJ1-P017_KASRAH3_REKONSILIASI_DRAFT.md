# QURBATA Jilid 1 — P017 Kasrah 3 (DRAF REKONSILIASI)

**Status:** DRAF PRODUKSI DI REPO RESMI; BELUM FROZEN, BELUM SIAP CETAK.  
**Dasar urutan baru:** P014 pengayaan Fathah → P015 Kasrah 1 → P016 Kasrah 2 → **P017 Kasrah 3**. Register FROZEN v1.0 masih menetapkan P017 Kasrah 4; perubahan urutan ini belum disahkan dalam register tersebut.

## Tartil — Kasrah 3

**Kompetensi baru:** `رِ زِ سِ شِ`. **Review:** Kasrah P015–P016 (`بِ تِ ثِ جِ حِ خِ دِ ذِ`) dan Fathah kumulatif. Huruf lepas, tanpa Dhammah, mad, sukun, tasydid, tanwin, atau bentuk sambung. **Latihan tiga huruf didahulukan** sesuai keputusan produksi pengguna.

**Asal 24 slot:** keluaran deterministik spesifikasi P016 dari generator `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` (blob SHA `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`), disusun ulang tanpa mengarang latihan baru.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | شَ رِ بَ | رَ كِ بَ | فَ رِ حَ |
| 2 | كَ رِ هَ | وَ رِ ثَ | سَ مِ عَ |
| 3 | شِ رِ فَ | زِ سِ قَ | شِ رِ كَ |
| 4 | زِ سِ لَ | شِ رِ مَ | زِ نَ هَ |
| 5 | سِ وَ يَ | شِ بِ تِ | رِ ثِ جِ |
| 6 | زِ حِ خِ | رِ زِ | سِ ضَ |
| 7 | شِ طَ | رِ زِ | سِ ظَ |
| 8 | شِ عَ | رِ زِ | سِ غَ |

### Audit Tartil — wajib sebelum cetak

- 24 slot sumber, 22 unik; `رِ زِ` muncul 3 kali.
- **BLOCKED `رَ كِ بَ`:** `كِ` belum diajarkan (Kasrah akhir).
- **BLOCKED `سَ مِ عَ`:** `مِ` belum diajarkan (Kasrah akhir).
- 22 slot lain tidak mengandung Kasrah prematur menurut whitelist tahap ini; seluruh baris tetap berstatus kandidat sampai audit visual dan kurikulum tuntas.
- Dua slot BLOCKED **tidak boleh dicetak atau dipakai untuk RIQA OS**. Pengganti harus berasal dari materi terverifikasi atau disahkan melalui proses editorial.

## Bahasa Arab (Bi'ah) — penguatan bermakna, bukan materi baru berulang

- **`اِفْتَحِ الْكِتَابَ`** — Bukalah buku.
- **Status draf P017:** REPEAT-1 dari materi yang **dipercepat dan diperkenalkan pada P016**; latihan konteks lisan membuka buku, bukan mengklaim materi baru.
- Sumber asli: register integrasi FROZEN v1.3, P017 INTRODUCE. Pergeseran P016–P017 masih menunggu rekonsiliasi.

## Akhlak — penguatan pembiasaan

- **`وَقُولُوا لِلنَّاسِ حُسْنًا`** — Berkatalah yang baik kepada manusia.
- **Status draf P017:** REPEAT-1 dari pengenalan P016, bukan pengulangan yang diklaim sebagai kompetensi baru.
- Sumber asli: register integrasi FROZEN v1.3, P017–P019.

## Tahfidz — QS. Al-Ikhlas ayat 4 (usulan kesinambungan)

**Arab:** `وَلَمْ يَكُنْ لَهُ كُفُوًا أَحَدٌ`  
**Arti:** Dan tidak ada sesuatu yang setara dengan Dia.  
**Status:** **USULAN P017**, berdasarkan keputusan pengguna P016 = QS. Al-Ikhlas:3 (`03_BOOKS/JILID-1/AMENDMENT_TAHFIDZ_P016_2026-11-22.md`) dan teks Al-Ikhlas:4 yang sudah tercatat dalam generator lama P015. Belum ada keputusan eksplisit pengguna untuk mengesahkan P017; jangan menimpa baseline FROZEN sebelum rekonsiliasi.

## Gate dan jejak perubahan

1. P017 **draf** berisi 24 slot sumber, 2 BLOCKED dan 2 pengulangan tambahan; belum final cetak.
2. Bahasa Arab dan Akhlak adalah **penguatan pertama** materi P016, tidak memperkenalkan nash lain secara prematur.
3. Tahfidz mengikuti ayat sesudah P016 dan **tidak melompat ke Al-Masad**.
4. Dokumen ini tidak mengubah `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`, `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`, master Tahfidz, maupun generator PDF.
