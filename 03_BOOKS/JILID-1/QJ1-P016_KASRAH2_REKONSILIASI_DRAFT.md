# QURBATA Jilid 1 — P016 Kasrah 2 (DRAF REKONSILIASI)

**Status:** DRAF PRODUKSI, BELUM FROZEN, BELUM FINAL CETAK.

**Dasar:** keputusan produksi pengguna P014 pengayaan Fathah, P015 Kasrah 1; halaman berikutnya P016 direncanakan Kasrah 2. Ini **berbeda** dari register FROZEN v1.0 yang masih menetapkan P016 Kasrah 3 (`رِ زِ سِ شِ`). Tidak ada perubahan pada FROZEN.

**Sumber latihan:** keluaran deterministik P015 Kasrah 2 dari `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs`, blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`. Hanya **pemindahan dan pengurutan ulang** dari sumber yang sudah ada; tidak ada latihan baru.

## Materi

- Kompetensi kandidat: `حِ خِ دِ ذِ`.
- Review: `بِ تِ ثِ جِ` dan seluruh Fathah sebelumnya.
- Format permintaan: latihan tiga huruf lebih dahulu, kemudian dua huruf.

## 24 slot sumber generator (BELUM LULUS WHITELIST)

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | حَ فِ ظَ | خَ دِ مَ | دَ خِ لَ |
| 2 | ذَ كِ رَ | حَ ذِ رَ | قَ دِ مَ |
| 3 | ذِ حِ ظَ | خِ دِ عَ | ذِ حِ غَ |
| 4 | خِ دِ فَ | ذِ حِ قَ | خِ كَ لَ |
| 5 | دِ مَ نَ | ذِ هَ وَ | حِ يَ بِ |
| 6 | خِ تِ ثِ | حِ خِ | دِ سَ |
| 7 | ذِ شَ | حِ خِ | دِ صَ |
| 8 | ذِ ضَ | حِ خِ | دِ طَ |

## Temuan wajib diperbaiki sebelum dipakai sebagai latihan peserta

- **BLOCKED:** `حَ فِ ظَ` mengandung `فِ`, kompetensi yang baru dibuka pada Kasrah 5 dalam FROZEN saat ini.
- **BLOCKED:** `ذَ كِ رَ` mengandung `كِ`, kompetensi yang baru dibuka pada Kasrah 6 dalam FROZEN saat ini.
- Duplikasi `حِ خِ` sebanyak 3 kali. Total 24 slot, 22 unik.
- Sumber generator asli menempatkan 8 pasangan dua huruf dahulu; draf ini menempatkan 16 latihan tiga huruf dahulu sesuai arah produksi terbaru, sehingga **belum lolos gate format FROZEN**.
- **DILARANG menjadikan tabel ini sebagai master cetak/RIQA OS** sebelum dua slot BLOCKED diganti melalui sumber sah dan rekonsiliasi kurikulum disahkan.

## Integrasi (register resmi)

- **Bahasa Arab P016 — USULAN MATERI BARU:** `اِفْتَحِ الْكِتَابَ` — Bukalah buku. Materi ini **berasal dari P017 INTRODUCE** pada register integrasi FROZEN v1.3; dipercepat ke P016 atas permintaan pengguna agar panel tidak berulang empat halaman. **Belum disahkan sebagai perubahan FROZEN.**
- **Akhlak P016 — USULAN MATERI BARU:** `وَقُولُوا لِلنَّاسِ حُسْنًا` — Berkatalah yang baik kepada manusia. Materi ini **berasal dari rentang P017–P019** pada register integrasi FROZEN v1.3; dipercepat ke P016 atas permintaan pengguna. **Belum disahkan sebagai perubahan FROZEN.**
- **Status sumber lama:** P016 pada FROZEN v1.3 masih `أَعِدْ` (REPEAT-2) dan `وَلَكَ الْجَنَّةُ` (REPEAT-2); keduanya tidak dipakai sebagai fokus panel pada draf produksi P016 ini, tetapi sumber asli tetap dipertahankan.
- **Catatan urutan:** perpindahan ini perlu ditinjau pada P017 dan seterusnya agar tidak memunculkan pengulangan baru atau melewati materi resmi.
- Tahfidz: belum ditetapkan; harus diperiksa terhadap master Tahfidz dan progres halaman 15 yang nyata.

## Sumber dan otoritas

- `03_BOOKS/JILID-1/PAGE_REGISTER_P011-P020_FROZEN-v1.0.md` blob `c0a464916ae9b2a84c7bc0d85e1edb29a364b794`.
- `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md` blob `9c29d3684b33882b0dfabe2b66f579dd1f90a012`.
- Tidak mengubah Page Object lama, generator produksi, atau register FROZEN.
