# QURBATA Jilid 1 — P022 مُرَاجَعَةٌ وَتَقْيِيمٌ (DRAF REKONSILIASI)

**Judul Indonesia:** Pengulangan dan Evaluasi. **Prinsip:** seluruh empat bidang hanya mengulang dan mengevaluasi materi sebelumnya; tidak ada target materi baru. Cakupan kumulatif P001–P021 berdasarkan register dan alur draf, bukan bukti pelaksanaan kelas.

**Tanggal:** 22 November 2026. **Revisi:** audit cakupan Kasrah 29/29, keseimbangan 32:32, serta BA/Akhlak aplikatif checkpoint. **Status:** DRAF; BELUM FROZEN; BELUM SIAP CETAK.

## Keputusan usulan dan konflik FROZEN

- Berdasarkan keputusan pengguna: P020 Kasrah 6A `كِ لِ مِ نِ هِ`, P021 Kasrah 6B `وِ يِ ءِ إِ`, sehingga **checkpoint diusulkan P022**. Ini **bukan perubahan register resmi**.
- **FROZEN:** `PAGE_REGISTER_P011-P020_FROZEN-v1.0.md` menetapkan checkpoint pada P020; `PAGE_REGISTER_P021-P030_FROZEN-v1.0.md` menetapkan P021 Dhammah 1 `بُ تُ ثُ جُ` dan P022 Dhammah 2 `حُ خُ دُ ذُ`. Dhammah resmi P021–P030 tidak boleh dihapus; seluruh jadwal perlu pemetaan ulang terkontrol.
- **Sumber latihan:** `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`, `pageSpecs[n=14..19].triples` dan keluaran deterministik `makeRows` (16 kelompok tiga huruf) dan keluaran deterministik `makeRows` checkpoint (8 pasangan Fathah pertama). **Tidak ada rangkaian latihan baru.** Urutan disusun 16 tiga huruf dahulu, 8 pasangan kemudian sesuai arahan produksi terbaru.

## 1. Tartil — evaluasi Fathah–Kasrah

**Tidak ada kompetensi harakat baru.** Semua huruf tetap lepas; tidak ada Dhammah, mad, tanwin, sukun, tasydid, atau huruf sambung sebagai kompetensi Tartil.

| Baris | Kolom 1 | Kolom 2 | Kolom 3 |
|---:|---|---|---|
| 1 | ذَ كِ رَ | خَ دِ مَ | قِ حِ خِ |
| 2 | يِ ءِ ثِ | إِ جِ حِ | نِ شِ صِ |
| 3 | هِ وِ تِ | ضِ طِ هَ | وَ رِ ثَ |
| 4 | شَ عِ رَ | ظِ دِ ذِ | حَ فِ ظَ |
| 5 | مِ نِ بِ | صَ غِ رَ | جَ لِ سَ |
| 6 | زِ سِ قَ | بَ تَ | ثَ ءَ |
| 7 | أَ جَ | حَ خَ | دَ ذَ |
| 8 | رَ زَ | سَ شَ | صَ ضَ |

### Audit otomatis karakter, cakupan, dan keunikan (REVISI)

- **24/24 slot terisi dan unik**; 16 kelompok tiga huruf di depan, 8 pasangan di belakang; **0 duplikasi** dan **0 token di luar whitelist** Fathah–Kasrah.
- **32 token Fathah : 32 token Kasrah**, tepat **50% : 50%**.
- **29/29 bentuk Kasrah tercakup**, tanpa satu bentuk yang hilang. Bentuk Fathah unik yang muncul dalam grid: **21/29**. Karena itu **tidak diklaim semua bentuk Fathah telah tercakup di grid**; 29 identitas huruf diuji pada panel tersendiri, dan evaluasi Fathah individual penuh tetap perlu pemeriksaan.
- **Sumber per slot:** semua 16 kelompok tiga huruf disalin persis dari `pageSpecs[n=14..19].triples` atau keluaran deterministik `makeRows` generator resmi `production/vivliostyle/scripts/build-p011-p020-from-frozen.mjs` blob `f3cc15a5b696231b57ded8e3bd173d0ec4b83b6e`; 8 pasangan Fathah diambil dari keluaran `makeRows` checkpoint P020, yaitu 16 token pertama `FATHA_ALL`. Tidak mengarang rangkaian latihan.
- **Audit grafem khusus:** `ءِ`, `إِ` ada dalam cakupan tetapi belum diverifikasi secara visual dengan font KFGQPC Uthman Taha.
- **Status gate:** **cakupan Kasrah dan keseimbangan harakat LULUS audit karakter**; **cetak tetap BLOCKED** karena FROZEN berbeda, audit grafem, kecukupan evaluasi Fathah individual, dan render A5 belum selesai.

### Evaluasi identitas 29 huruf tanpa harakat

**Urutan identitas huruf persis dari `letters29` pada generator:**

`ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي ء`

- **29/29 identitas tercantum**, unik sebagai simbol menurut daftar sumber. Guru menunjuk secara acak dan meminta santri **menyebutkan nama huruf**, membedakan bentuk, dan membaca contoh harakat yang sudah dipelajari.
- **Batas audit:** sumber hanya menyimpan bentuk identitas, **tidak menyimpan 29 nama huruf lengkap**; daftar nama tertulis perlu disahkan dari master khusus sebelum diproduksi sebagai tabel nama.

### Pelengkap evaluasi Fathah lisan

Delapan bentuk yang belum tampil di grid, disalin dari `FATHA_ALL` generator: `طَ عَ غَ فَ كَ لَ نَ يَ`. Guru menguji satu per satu secara lisan sebagai review, bukan slot cetak tambahan atau materi baru. Cakupan rancangan asesmen menjadi 29/29 Fathah (21 grid + 8 lisan); 29/29 Kasrah di grid. Hasil belajar aktual belum diukur.

### Pengenalan nama harakat

- Fathah: `فَتْحَة`.
- Kasrah: `كَسْرَة`.
- Tidak menguji Dhammah karena belum diperkenalkan pada alur draf.

## 2. Bahasa Arab — murajaah dan taqyim kumulatif

Sumber: overlay integrasi FROZEN v1.3 P001–P019 dan draf P019–P021 untuk penutupan buku. Tujuh ungkapan lama; tidak ada mufradat baru. Materi lengkap menjadi panduan guru, panel cetak dapat ringkas.

| Ungkapan | Asal | Praktik |
|---|---|---|
| السَّلَامُ عَلَيْكُمْ | P001–P003 FROZEN | Mengucapkan salam |
| اُنْظُرْ | P004–P006 FROZEN | Memperhatikan |
| اِسْتَمِعْ | P007–P010 FROZEN | Menyimak |
| اِقْرَأْ | P011–P013 FROZEN | Membaca |
| أَعِدْ | P014–P016 FROZEN | Mengulangi |
| اِفْتَحِ الْكِتَابَ | P017–P019 FROZEN; P019 draf berbeda | Membuka buku |
| أَغْلِقِ الْكِتَابَ | P019–P021 draf; P021–P023 FROZEN | Menutup buku |

Guru mengacak instruksi, santri merespons tanpa terjemahan awal; catat Mandiri / Dengan bantuan / Belum. Untuk materi dengan konflik P019, cek keterpaparan aktual sebelum menguji. Jangan mencampur skor BA dan Tartil.

## 3. Akhlak — murajaah dan taqyim kumulatif

Sumber: overlay integrasi FROZEN v1.3 P001–P019 dan draf P019–P021. Semua nash berikut merupakan materi terdahulu dalam sumber; bukan nash baru P022.

| Nash | Asal | Evaluasi |
|---|---|---|
| أَفْشُوا السَّلَامَ بَيْنَكُمْ | P001–P003, P010 FROZEN | Membiasakan salam |
| وَقُلْ رَبِّ زِدْنِي عِلْمًا | P004–P006 FROZEN | Berdoa sebelum belajar |
| فَاسْتَمِعُوا لَهُ وَأَنْصِتُوا | P007–P009 FROZEN | Menyimak dengan tenang |
| إِنَّ اللَّهَ مَعَ الصَّابِرِينَ | P011–P013 FROZEN | Menunggu giliran |
| وَلَكَ الْجَنَّةُ | P014–P016 FROZEN | Mengingat makna motivasi surga; bukan skor perilaku yang tidak teramati |
| وَقُولُوا لِلنَّاسِ حُسْنًا | P017–P019 FROZEN; P019 draf berbeda | Berbicara sopan |
| أَدِّ الْأَمَانَةَ إِلَى مَنِ ائْتَمَنَكَ | P019–P021 draf; P021–P023 FROZEN | Menjaga titipan, mengembalikan barang, melaporkan keadaan dengan jujur |

Rubrik Mandiri / Dengan bantuan / Belum tampak; catat hanya tindakan yang teramati. Materi doa P020 FROZEN tercakup sebagai review dari P004–P006, tetapi pemetaan resmi tetap tidak diubah. Cek keterpaparan aktual terutama bila alur draf berbeda. Tidak ada penambahan nash.

## 4. Tahfidz — murajaah kumulatif tanpa ayat baru

| Target review | Sumber |
|---|---|
| An-Nas 1–6 | P001–P006 FROZEN |
| Al-Falaq 1–4 | P007–P010 FROZEN |
| Al-Falaq 5 | Generator lama P011 (cek terhadap master Tahfidz sebelum asesmen) |
| Al-Ikhlas 1–2 | Generator lama P012–P013 (cek terhadap master Tahfidz sebelum asesmen) |
| Al-Ikhlas 3–4 | Alur draf P016–P017 sebagaimana dicatat pada draf P019 |
| Al-Masad 1–4 | Alur draf P018–P021; draf P019, P020, P021 |

**Al-Masad ayat 5 dikeluarkan dari target P022** karena belum tercatat sebagai materi sebelumnya pada alur draf. Tidak dihapus dari kurikulum; perlu penempatan berikutnya melalui rekonsiliasi Tahfidz. Guru meminta santri menyambung hafalan dari target yang benar-benar sudah dipelajari, mencatat kelancaran dan ketepatan secara terpisah. Daftar di atas adalah cakupan rencana review, bukan klaim hafalan santri atau validasi master Tahfidz lengkap. Panel cetak ringkas; daftar lengkap untuk panduan guru. Arti Indonesia dan teks Utsmani setiap ayat yang akhirnya dicetak wajib diverifikasi.

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

**Konflik lintas domain:** FROZEN P021 menetapkan Tahfidz An-Nasr:1, BA `صَحِيحٌ`, Akhlak amanah; P022 Tahfidz An-Nasr:2 dan BA `حَاوِلْ مَرَّةً أُخْرَى`. Materi tersebut **tidak dihapus**, tetapi membutuhkan pemetaan ulang setelah checkpoint. BA dan Akhlak P022 menjadi review kumulatif; `اِقْرَأْ`, praktik amanah, dan doa menuntut ilmu tetap tercakup. Pemetaan FROZEN tetap wajib direkonsiliasi, bukan dihapus.

## Gate sebelum FINAL

1. **AUDIT KASRAH LULUS:** seluruh 29 bentuk Kasrah terwakili; komposisi 32 Kasrah dan 32 Fathah. **PELENGKAP:** 21/29 bentuk Fathah unik di grid + 8 bentuk dalam panduan lisan; rancangan cakupan 29/29, belum diuji pada santri.
2. Audit pengenalan 29 nama huruf (sumber generator hanya identitas grafem), khusus `ءِ` dan `إِ` dengan master tipografi.
3. Rekonsiliasi konflik FROZEN P020–P040, khususnya urutan Dhammah dan domain Tahfidz–BA–Akhlak.
4. Verifikasi ayat Tahfidz terhadap mushaf dan render A5 sebelum cetak.
5. **Tidak mengubah FROZEN**, generator, atau master kurikulum; dokumen ini hanya draf produksi.
