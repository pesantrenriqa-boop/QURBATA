# QURBATA Jilid 1 — P022 Checkpoint Fathah–Kasrah (DRAF REKONSILIASI)

**Tanggal:** 22 November 2026. **Status:** DRAF; BELUM FROZEN; BELUM SIAP CETAK.

## Keputusan usulan dan konflik FROZEN

- Berdasarkan keputusan pengguna: P020 Kasrah 6A `كِ لِ مِ نِ هِ`, P021 Kasrah 6B `وِ يِ ءِ إِ`, sehingga **checkpoint diusulkan P022**. Ini **bukan perubahan register resmi**.
- **FROZEN:** `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md` menetapkan checkpoint pada P020; `PAGE_REGISTER_P021-P030_FROZEN-v1.0.md` menetapkan P021 Dhammah 1 `بُ تُ ثُ جُ` dan P022 Dhammah 2 `حُ خُ دُ ذُ`. Dhammah resmi P021–P030 tidak boleh dihapus; seluruh jadwal perlu pemetaan ulang terkontrol.
- **Sumber latihan:** `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`, `pageSpecs[n=20].triples` (16 contoh persis) dan keluaran deterministik `makeRows` checkpoint (8 pasangan Fathah pertama). **Tidak ada rangkaian latihan baru.** Urutan disusun 16 tiga huruf dahulu, 8 pasangan kemudian sesuai arahan produksi terbaru.

## 1. Tartil — evaluasi Fathah–Kasrah

**Tidak ada kompetensi harakat baru.** Semua huruf tetap lepas; tidak ada Dhammah, mad, tanwin, sukun, tasydid, atau huruf sambung sebagai kompetensi Tartil.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | كَ تَ بَ | حَ مَ دَ | رَ حِ مَ |
| 2 | عَ مِ لَ | وَ جَ دَ | شَ كَ رَ |
| 3 | خَ لَ قَ | حَ فِ ظَ | فَ هِ مَ |
| 4 | سَ مِ عَ | شَ رِ بَ | بَ صِ رَ |
| 5 | فَ قِ هَ | بَ قِ يَ | مَ لِ كَ |
| 6 | جَ لِ سَ | بَ تَ | ثَ ءَ |
| 7 | أَ جَ | حَ خَ | دَ ذَ |
| 8 | رَ زَ | سَ شَ | صَ ضَ |

### Audit otomatis karakter dan keunikan

- **24/24 slot terisi**, **24/24 unik**, 16 tiga-huruf + 8 dua-huruf, total 64 token; **0 duplikasi**.
- **0 token di luar whitelist** Fathah kumulatif dan Kasrah 1–6.
- Komposisi latihan generator checkpoint: **53 token Fathah**, **11 token Kasrah**, **8 bentuk Kasrah berbeda**. **PERINGATAN:** komposisi tidak seimbang dan **tidak mencakup semua 29 bentuk Kasrah**; checkpoint ini **belum lulus audit coverage**. Tidak boleh mengklaim seluruh Kasrah diuji hanya karena whitelist lulus. Perlu perluasan/pertukaran slot menggunakan sumber sah sebelum cetak.
- Pasangan Fathah di bagian akhir bersumber langsung dari urutan awal pool generator checkpoint; bukan latihan karangan.

### Evaluasi identitas 29 huruf tanpa harakat

**Urutan identitas huruf persis dari `letters29` pada generator:**

`ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ء`

- **29/29 identitas tercantum**, unik sebagai simbol menurut daftar sumber. Guru menunjuk secara acak dan meminta santri **menyebutkan nama huruf**, membedakan bentuk, dan membaca contoh harakat yang sudah dipelajari.
- **Batas audit:** sumber hanya menyimpan bentuk identitas, **tidak menyimpan 29 nama huruf lengkap**; daftar nama tertulis perlu disahkan dari master khusus sebelum diproduksi sebagai tabel nama.

### Pengenalan nama harakat

- Fathah: `فَتْحَة`.
- Kasrah: `كَسْرَة`.
- Tidak menguji Dhammah karena belum diperkenalkan pada alur draf.

## 2. Bahasa Arab — review checkpoint

**`اِقْرَأْ`** — **Bacalah.** Sumber: `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`, **P020 REINFORCE**. Materi resmi tertunda akibat pergeseran halaman dan diusulkan dipulihkan pada P022. Guru menunjuk bacaan yang sudah sah, santri merespons perintah. Ini bukan materi baru atau perubahan FROZEN.

## 3. Akhlak — review checkpoint

**`وَقُلْ رَبِّ زِدْنِي عِلْمًا`** — **Dan katakanlah: Ya Tuhanku, tambahkanlah ilmuku.** Sumber: `PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`, **P020 REINFORCE**. Dipulihkan sebagai usulan P022; praktik doa sebelum belajar dan adab menuntut ilmu. Tidak mengubah register.

## 4. Tahfidz — QS. Al-Masad ayat 5 (usulan)

**`فِي جِيدِهَا حَبْلٌ مِنْ مَسَدٍ`** — **Di lehernya ada tali dari sabut yang dipintal.** Teks berasal dari generator checkpoint lama `pageSpecs[n=20].tahfidz` sebagai Al-Masad:5 review. Setelah draf P021 Al-Masad:4, diusulkan P022 Al-Masad:5, **bukan penetapan master Tahfidz**. Perlu audit mushaf/font KFGQPC Uthman Taha sebelum cetak.

## Dampak pergeseran Dhammah — daftar konflik yang harus diselesaikan

| Halaman FROZEN | Kompetensi resmi | Dampak usulan P020–P022 |
|---|---|---|
| P020 | Checkpoint Fathah–Kasrah | Diusulkan pindah ke P022 |
| P021 | Dhammah 1: `بُ تُ ثُ جُ` | Bertabrakan dengan draf Kasrah 6B |
| P022 | Dhammah 2: `حُ خُ دُ ذُ` | Bertabrakan dengan checkpoint usulan |
| P023 | Dhammah 3: `رُ زُ سُ شُ` | Kandidat penempatan Dhammah 1, **belum disahkan** |
| P024–P027 | Dhammah 4–7 | Perlu pemetaan ulang bertahap, bukan penghapusan |
| P028–P030 | Penguatan dan latihan kumulatif Dhammah | Perlu kajian apakah bergeser ke P030–P032; konsekuensi halaman berikutnya harus diaudit |

**Pemetaan tentatif:** P023 Dhammah 1 → P024 Dhammah 2 → P025 Dhammah 3 → P026 Dhammah 4 → P027 Dhammah 5 → P028 Dhammah 6 → P029 Dhammah 7 → P030 penguatan → P031–P032 kumulatif. Ini hanya **usulan hitungan pergeseran +2**, belum dicek konflik dengan register FROZEN P031–P040 dan belum sah.

**Konflik lintas domain:** FROZEN P021 menetapkan Tahfidz An-Nasr:1, BA `صَحِيحٌ`, Akhlak amanah; P022 Tahfidz An-Nasr:2 dan BA `حَاوِلْ مَرَّةً أُخْرَى`. Materi tersebut **tidak dihapus**, tetapi membutuhkan pemetaan ulang setelah checkpoint. BA/Akhlak P020 `اِقْرَأْ` / `وَقُلْ رَبِّ زِدْنِي عِلْمًا` ditempatkan dalam draf checkpoint untuk pemulihan.

## Gate sebelum FINAL

1. **BLOCKED COVERAGE:** revisi slot dari sumber terverifikasi supaya evaluasi Fathah–Kasrah benar-benar representatif; saat ini hanya 8 bentuk Kasrah muncul dari 29 bentuk.
2. Audit pengenalan 29 nama huruf (sumber generator hanya identitas grafem), khusus `ءِ` dan `إِ` dengan master tipografi.
3. Rekonsiliasi konflik FROZEN P020–P040, khususnya urutan Dhammah dan domain Tahfidz–BA–Akhlak.
4. Verifikasi ayat Tahfidz terhadap mushaf dan render A5 sebelum cetak.
5. **Tidak mengubah FROZEN**, generator, atau master kurikulum; dokumen ini hanya draf produksi.
