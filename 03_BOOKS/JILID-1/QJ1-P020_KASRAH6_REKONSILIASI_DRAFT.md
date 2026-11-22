# QURBATA Jilid 1 — P020 Kasrah 6A (DRAF REVISI)

**Tanggal:** 22 November 2026. **Status:** DRAF; BELUM FROZEN; BELUM SIAP CETAK. **Menggantikan draf P020 Kasrah 6 penuh** berdasarkan persetujuan pengguna membagi Kasrah 6 menjadi dua halaman.

## Sumber primer dan batas kewenangan

- `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`: Kasrah 6 resmi masih P019, checkpoint resmi P020.
- `PAGE_REGISTER_P021-P030_FROZEN-v1.0.md`: Dhammah 1 resmi P021 dan Dhammah 2 resmi P022. **Usulan checkpoint P022 bertabrakan dengan kedua halaman tersebut; belum disahkan.**
- `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`: BA P020 `اِقْرَأْ`, Akhlak P020 `وَقُلْ رَبِّ زِدْنِي عِلْمًا`; BA P021–P023 `أَغْلِقِ الْكِتَابَ`, Akhlak P021–P023 `أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ`. Dua materi P020 resmi harus tetap dipertahankan dalam rencana rekonsiliasi, bukan dihapus.
- `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`: sumber latihan P019 Kasrah 6, P020 checkpoint, dan P018 Kasrah 5. Latihan diambil **verbatim** dari `triples` atau keluaran deterministik `makeRows`, bukan rangkaian baru.
- Seluruh ini adalah **draf penyimpangan terkontrol dari FROZEN** atas persetujuan pengguna untuk pembagian Kasrah 6. FROZEN, generator, dan master tidak diubah.

## 1. Tartil — Kasrah 6A

**Kompetensi baru:** `كِ لِ مِ نِ هِ`. **Belum boleh:** `وِ يِ ءِ إِ` (baru P021). Review Fathah kumulatif dan Kasrah 1–5. Semua latihan huruf lepas; tanpa Dhammah, mad, sukun, tanwin, tasydid.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |\n|---:|---|---|---|\n| 1 | مَ لِ كَ | كَ بِ رَ | عَ مِ لَ |
| 2 | فَ هِ مَ | لَ بِ سَ | جَ لِ سَ |
| 3 | وَ رِ ثَ | بَ قِ يَ | مِ نِ بِ |
| 4 | كِ خِ دِ | لِ ذِ رِ | مِ زِ سِ |
| 5 | نِ شِ صِ | كَ تَ بَ | حَ مَ دَ |
| 6 | رَ حِ مَ | كِ لِ | مِ مَ |
| 7 | نِ نَ | لِ يَ | عِ غِ |
| 8 | فِ قَ | قِ كَ | فِ لَ |

### Audit per slot

- **24/24 slot terisi dan unik**; 16 tiga-huruf di depan, 8 dua-huruf di belakang; **0 duplikasi**.
- **0 token di luar whitelist P020**; tidak ada `وِ يِ ءِ إِ`.
- Cakupan huruf baru: `كِ` 2×; `لِ` 5×; `مِ` 4×; `نِ` 3×; `هِ` 1×.
- **Asal sumber:** 13 kelompok tiga huruf dari keluaran generator P019 Kasrah 6; 3 kelompok `كَ تَ بَ`, `حَ مَ دَ`, `رَ حِ مَ` dari `triples` checkpoint P020; empat pasangan `كِ لِ`, `مِ مَ`, `نِ نَ`, `لِ يَ` dari generator P019; empat pasangan `عِ غِ`, `فِ قَ`, `قِ كَ`, `فِ لَ` dari generator P018 Kasrah 5.
- **Audit karakter saja**; kelayakan fonetik, pedagogis, dan visual belum final.

## 2. Bahasa Arab — REPEAT-1

**`أَغْلِقِ الْكِتَابَ`** — **Tutuplah buku.** Diperkenalkan draf P019 (dipinjam dari register integrasi P021); P020 penguatan pertama. Latihan lisan: guru memerintah, santri menutup buku dan mengulangi instruksi.

## 3. Akhlak — REPEAT-1

**`أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ`** — **Tunaikanlah amanah kepada orang yang mempercayaimu.** Diperkenalkan draf P019 (sumber register integrasi P021–P023); P020 penguatan pertama. Praktik: menjaga titipan dan mengembalikan barang pinjaman.

## 4. Tahfidz — QS. Al-Masad:3 (USULAN)

**`سَيَصْلَى نَارًا ذَاتَ لَهَبٍ`** — **Kelak dia akan masuk ke dalam api yang bergejolak.** Teks mengikuti generator lama P018; pergeseran target P020 adalah usulan kesinambungan P019 Al-Masad:2. Varian grafem Utsmani dan tanda alif kecil wajib audit sebelum cetak.

## Gate dan keputusan terbuka

- **BLOCKED CETAK:** persetujuan pemetaan P020–P022 terhadap FROZEN dan register Dhammah P021–P030; render A5; audit font/grafem.
- Checkpoint diusulkan P022, belum disahkan. BA `اِقْرَأْ` dan Akhlak `وَقُلْ رَبِّ زِدْنِي عِلْمًا` dari P020 FROZEN wajib masuk daftar rekonsiliasi, tidak dihapus.
