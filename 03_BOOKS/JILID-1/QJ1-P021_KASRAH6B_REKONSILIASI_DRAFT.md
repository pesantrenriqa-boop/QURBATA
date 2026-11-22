# QURBATA Jilid 1 — P021 Kasrah 6B (DRAF BARU)

**Tanggal:** 22 November 2026. **Status:** DRAF; BELUM FROZEN; BELUM SIAP CETAK. **Dasar:** persetujuan pengguna membagi Kasrah 6 ke P020–P021; checkpoint diusulkan P022.

## Sumber primer dan batas kewenangan

- `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md`: Kasrah 6 resmi masih P019, checkpoint resmi P020.
- `PAGE_REGISTER_P021-P030_FROZEN-v1.0.md`: Dhammah 1 resmi P021 dan Dhammah 2 resmi P022. **Usulan checkpoint P022 bertabrakan dengan kedua halaman tersebut; belum disahkan.**
- `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`: BA P020 `اِقْرَأْ`, Akhlak P020 `وَقُلْ رَبِّ زِدْنِي عِلْمًا`; BA P021–P023 `أَغْلِقِ الْكِتَابَ`, Akhlak P021–P023 `أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ`. Dua materi P020 resmi harus tetap dipertahankan dalam rencana rekonsiliasi, bukan dihapus.
- `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`: sumber latihan P019 Kasrah 6, P020 checkpoint, dan P018 Kasrah 5. Latihan diambil **verbatim** dari `triples` atau keluaran deterministik `makeRows`, bukan rangkaian baru.
- Seluruh ini adalah **draf penyimpangan terkontrol dari FROZEN** atas persetujuan pengguna untuk pembagian Kasrah 6. FROZEN, generator, dan master tidak diubah.

## 1. Tartil — Kasrah 6B

**Kompetensi baru:** `وِ يِ ءِ إِ`. **Review:** Kasrah 6A `كِ لِ مِ نِ هِ`, Kasrah 1–5, seluruh Fathah. Bentuk Hamzah/Alif **wajib audit master grafem KFGQPC Uthman Taha**. Semua latihan huruf lepas; tanpa Dhammah, mad, sukun, tanwin, tasydid.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |\n|---:|---|---|---|\n| 1 | هِ وِ تِ | يِ ءِ ثِ | إِ جِ حِ |
| 2 | مَ لِ كَ | كَ بِ رَ | عَ مِ لَ |
| 3 | فَ هِ مَ | لَ بِ سَ | جَ لِ سَ |
| 4 | وَ رِ ثَ | بَ قِ يَ | مِ نِ بِ |
| 5 | كِ خِ دِ | لِ ذِ رِ | مِ زِ سِ |
| 6 | نِ شِ صِ | هِ وِ | يِ هَ |
| 7 | ءِ وَ | إِ كِ | كِ لِ |
| 8 | مِ مَ | نِ نَ | لِ يَ |

### Audit per slot

- **24/24 slot terisi dan unik**; 16 tiga-huruf di depan, 8 dua-huruf di belakang; **0 duplikasi**.
- **0 token di luar whitelist P021**; tidak ada Dhammah.
- Cakupan bentuk baru: `وِ` 2×; `يِ` 2×; `ءِ` 2×; `إِ` 2×.
- **Asal sumber:** 16 kelompok tiga huruf dan delapan pasangan berasal dari keluaran deterministik generator P019 Kasrah 6; sebagian merupakan review sah dari Kasrah 6A. Tidak ada latihan yang dibuat sendiri.
- **Audit karakter saja**; `ءِ`, `إِ` dan tampilan grafem perlu verifikasi khusus, belum final cetak.

## 2. Bahasa Arab — REPEAT-2

**`أَغْلِقِ الْكِتَابَ`** — **Tutuplah buku.** P019 INTRODUCE, P020 REPEAT-1, P021 REPEAT-2 dalam **alur draf**. Kegiatan: guru memberi instruksi, santri melaksanakannya dan memberi instruksi kepada teman. Sumber nash register integrasi P021–P023.

## 3. Akhlak — REPEAT-2

**`أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ`** — **Tunaikanlah amanah kepada orang yang mempercayaimu.** P019 INTRODUCE, P020 REPEAT-1, P021 REPEAT-2 dalam **alur draf**. Praktik: menjaga dan mengembalikan barang amanah. Sumber register integrasi P021–P023.

## 4. Tahfidz — QS. Al-Masad:4 (USULAN)

**`وَامْرَأَتُهُ حَمَّالَةَ الْحَطَبِ`** — **Dan (begitu pula) istrinya, pembawa kayu bakar.** Teks diambil dari generator lama P019; diusulkan sesudah P020 Al-Masad:3. Belum mengubah master Tahfidz FROZEN.

## Gate dan keputusan terbuka

- **BLOCKED CETAK:** P021 FROZEN adalah Dhammah 1 `بُ تُ ثُ جُ` dengan Tahfidz An-Nasr:1, BA `صَحِيحٌ`, Akhlak amanah; pergeseran ini memerlukan revisi terkontrol seluruh rangkaian P021–P030 sebelum disahkan.
- Checkpoint Fathah–Kasrah **diusulkan P022** (bertentangan dengan Dhammah 2 resmi); perlu evaluasi 29 identitas huruf, Fathah–Kasrah, BA `اِقْرَأْ`, Akhlak `وَقُلْ رَبِّ زِدْنِي عِلْمًا` yang tertunda, tanpa menghapus materi.
- Audit glyph `ءِ`/`إِ`, ayat Tahfidz, dan render A5 belum tuntas.
