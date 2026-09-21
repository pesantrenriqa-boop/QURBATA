# QURBATA JILID 1 — TARTIL CONTENT MASTER P001–P020

**Version:** v0.1  
**Status:** WORKING CONTENT MASTER — PDF PRODUCTION PAUSED  
**Effective:** 2026-09-21

## Authority
Dokumen ini adalah tahap kurasi isi sebelum produksi PDF. Urutan kompetensi Tartil tetap mengikuti Page Register frozen. Dokumen ini tidak mengubah urutan pengenalan huruf/harakat.

## Hard rules
1. Generator PDF tidak boleh menciptakan kelompok 3 huruf secara otomatis.
2. Setiap kelompok 3 huruf harus berstatus **WORD**: kata Arab yang sah dan bermakna dengan harakat yang tercetak.
3. Prioritas: Qurani → fusha sah → bentuk leksikal terverifikasi.
4. Kata tidak boleh memakai huruf/harakat/fitur yang belum legal pada halaman itu.
5. Tidak boleh memaksakan sukun, tasydid, tanwin, mad, sambung, atau harakat tahap berikutnya.
6. Jika stok kata legal sedikit, kata sah boleh diulang terkontrol; kelompok 2 huruf tetap boleh fonetik.
7. Detached **ه** wajib dua lubang pada tahap renderer.
8. Setiap kata harus mempunyai gloss Indonesia untuk audit internal.
9. P019 dan P020 wajib curated, bukan random/cycling.

## Register kompetensi dan kandidat WORD

| Page | Kompetensi baru | Kandidat WORD legal | Gloss audit | Status |
|---|---|---|---|---|
| P001 | بَ تَ ثَ | — | Belum ada WORD 3 huruf yang aman dengan whitelist ini | HOLD |
| P002 | ءَ أَ | — | Belum ada WORD 3 huruf yang aman dengan whitelist ini | HOLD |
| P003 | جَ حَ خَ | بَحَثَ | mencari / meneliti | WORD |
| P004 | دَ ذَ رَ زَ | — | Tidak dipaksakan; lanjut memakai WORD legal terdahulu bila perlu | HOLD |
| P005 | سَ شَ | دَرَسَ ؛ جَلَسَ | belajar; duduk | WORD |
| P006 | صَ ضَ | صَبَرَ ؛ ضَرَبَ ؛ حَصَدَ | bersabar; memukul; memanen | WORD |
| P007 | طَ ظَ | طَلَبَ ؛ نَظَرَ ؛ ظَهَرَ | meminta/mencari; melihat; tampak/muncul | WORD |
| P008 | عَ غَ | غَفَرَ | mengampuni/menutupi | WORD |
| P009 | فَ قَ | فَتَحَ ؛ قَرَأَ | membuka; membaca | WORD |
| P010 | Evaluasi Fathah I | بَحَثَ ؛ دَرَسَ ؛ جَلَسَ ؛ صَبَرَ ؛ ضَرَبَ ؛ حَصَدَ ؛ طَلَبَ ؛ نَظَرَ ؛ ظَهَرَ ؛ غَفَرَ ؛ فَتَحَ ؛ قَرَأَ | Bank WORD terkurasi P001–P009 | CURATED |
| P011 | كَ لَ | كَتَبَ ؛ أَكَلَ ؛ مَلَكَ | menulis; makan; memiliki/menguasai | WORD |
| P012 | مَ نَ | مَنَعَ ؛ نَزَلَ ؛ عَمَلَ | mencegah; turun; bekerja | WORD |
| P013 | هَ وَ يَ | هَدَى* ؛ وَجَدَ | memberi petunjuk*; menemukan | REVIEW |
| P014 | Kasrah بِ تِ ثِ جِ | — | Kurasi kata campuran Fathah–Kasrah tanpa fitur ilegal | CURATE |
| P015 | حِ خِ دِ ذِ | — | Kurasi | CURATE |
| P016 | رِ زِ سِ شِ | — | Kurasi | CURATE |
| P017 | صِ ضِ طِ ظِ | — | Kurasi | CURATE |
| P018 | عِ غِ فِ قِ | — | Kurasi | CURATE |
| P019 | كِ لِ مِ نِ هِ وِ يِ ءِ إِ | — | Curated completion Kasrah | CURATE |
| P020 | Checkpoint Fathah + Kasrah | — | Curated checkpoint; bukan random | CURATE |

\* Kandidat yang memerlukan bentuk/fitur di luar whitelist halaman harus ditolak saat audit final. Entri REVIEW bukan izin produksi.

## Curated WORD bank P001–P010

| First legal page | WORD | Gloss ID | Catatan |
|---|---|---|---|
| P003 | بَحَثَ | mencari / meneliti | Fathah-only; legal mulai P003 |
| P005 | دَرَسَ | belajar | Fathah-only |
| P005 | جَلَسَ | duduk | Fathah-only |
| P006 | صَبَرَ | bersabar | Fathah-only |
| P006 | ضَرَبَ | memukul | Fathah-only |
| P006 | حَصَدَ | memanen | Fathah-only |
| P007 | طَلَبَ | meminta / mencari | Fathah-only |
| P007 | نَظَرَ | melihat / memandang | Fathah-only |
| P007 | ظَهَرَ | tampak / muncul | Fathah-only |
| P008 | غَفَرَ | mengampuni / menutupi | Fathah-only |
| P009 | فَتَحَ | membuka | Fathah-only |
| P009 | قَرَأَ | membaca | Fathah-only |

### Deliberate exclusions
- `عَمَلَ` ditolak: bentuk verba bakunya **عَمِلَ**, sehingga `عَمَلَ` tidak boleh dipakai hanya demi pola fathah.
- `فَرَحَ` ditolak sebagai verba “bergembira”: bentuk verba yang dimaksud adalah **فَرِحَ**.
- Kata yang membutuhkan huruf yang belum dikenalkan pada halaman terkait tidak boleh dimajukan.
- P001, P002, dan P004 tidak dipaksa memiliki WORD baru. Latihan 3 huruf pada halaman tersebut hanya boleh memakai WORD yang sudah legal; jika belum ada, komposisi latihan memakai kelompok 2 huruf.


## Full-page allocation rule P001–P010

Untuk memenuhi setiap halaman tanpa kata palsu:
- **Baris 1–2:** kelompok 2 huruf untuk pengenalan/diskriminasi kompetensi baru.
- **Baris 3–8:** 18 slot kelompok 3 huruf. Setiap slot wajib `WORD`.
- WORD bersifat **kumulatif**: setelah sebuah kata legal, kata itu boleh dipakai lagi pada halaman berikutnya.
- Jika jumlah WORD unik belum mencapai 18, kata sah boleh diulang dengan distribusi seimbang. Dilarang mengisi kekurangan dengan kombinasi tak bermakna.
- Halaman sebelum WORD pertama tersedia (P001–P002) memakai kelompok 2 huruf pada seluruh slot; tidak ada 3-huruf palsu.

### Allocation P001–P010

| Page | 3-letter WORD pool yang legal pada halaman | Kebijakan 18 slot WORD |
|---|---|---|
| P001 | — | 24 slot = 2 huruf; tidak ada 3-huruf |
| P002 | — | 24 slot = 2 huruf; tidak ada 3-huruf |
| P003 | بَحَثَ | ulang terkontrol بَحَثَ pada slot WORD |
| P004 | بَحَثَ | ulang terkontrol; P004 fokus diskriminasi huruf baru pada slot 2-huruf |
| P005 | بَحَثَ، دَرَسَ، جَلَسَ | rotasi 3 WORD × 6 |
| P006 | بَحَثَ، دَرَسَ، جَلَسَ، صَبَرَ، ضَرَبَ، حَصَدَ | rotasi 6 WORD × 3 |
| P007 | بَحَثَ، دَرَسَ، جَلَسَ، صَبَرَ، ضَرَبَ، حَصَدَ، طَلَبَ، نَظَرَ، ظَهَرَ | rotasi 9 WORD × 2 |
| P008 | بَحَثَ، دَرَسَ، جَلَسَ، صَبَرَ، ضَرَبَ، حَصَدَ، طَلَبَ، نَظَرَ، ظَهَرَ، غَفَرَ | 10 WORD; 8 diulang terkontrol untuk 18 slot |
| P009 | بَحَثَ، دَرَسَ، جَلَسَ، صَبَرَ، ضَرَبَ، حَصَدَ، طَلَبَ، نَظَرَ، ظَهَرَ، غَفَرَ، فَتَحَ، قَرَأَ، فَطَرَ | 13 WORD; 5 diulang terkontrol untuk 18 slot |
| P010 | seluruh bank P003–P009 | checkpoint curated; sebar seluruh WORD dan ulang maksimal seperlunya |

### Additional verified candidates
- `فَطَرَ` — menciptakan/memulai penciptaan; legal mulai P009 dan Qurani.
- `تَفَثَ` **DITOLAK** untuk latihan: Quranic Corpus mencatat lemma/noun `تَفَث`, bukan bentuk latihan `تَفَثَ`; kita tidak menambahkan fathah akhir untuk mengejar pola.
- Bentuk seperti `فَتْح`, `قَرْح`, `فَتِيل` tidak masuk tahap Fathah-only karena membutuhkan sukun/kasrah/mad yang belum legal.


## Deep lexical pass v0.2 — strict first-legal-page correction

Audit ini memperketat syarat: sebuah WORD baru legal hanya jika **setiap hurufnya sudah diperkenalkan** pada page tersebut dan **setiap harakat yang tercetak sudah legal**. Temuan lama yang memakai huruf masa depan dipindahkan ke first-legal page yang benar.

| First legal page | WORD bank (Fathah-only) | Gloss ringkas |
|---|---|---|
| P001 | — | belum tersedia WORD aman |
| P002 | — | belum tersedia WORD aman |
| P003 | بَحَثَ | mencari/meneliti |
| P004 | جَحَدَ، حَذَرَ | mengingkari; berhati-hati/takut |
| P005 | دَرَسَ، سَجَدَ، حَسَدَ، حَبَسَ، حَرَسَ | belajar; bersujud; dengki; menahan; menjaga |
| P006 | صَبَرَ، ضَرَبَ، حَصَدَ، رَصَدَ | bersabar; memukul; memanen; mengawasi/mengintai |
| P007 | بَسَطَ، شَطَرَ | membentangkan; membelah/menuju separuh |
| P008 | عَبَدَ، رَجَعَ، غَدَرَ، عَرَضَ، غَضَبَ، عَجَزَ، عَبَرَ، عَثَرَ، شَعَرَ، سَحَرَ | menyembah; kembali; berkhianat; menampilkan/menawarkan; marah; lemah/tidak mampu; menyeberang; tersandung/menemukan; mengetahui/merasakan; menyihir |
| P009 | فَتَحَ، قَرَأَ، فَطَرَ، رَفَعَ، دَفَعَ، فَرَضَ، فَرَقَ، قَطَعَ، قَعَدَ، قَبَضَ، قَدَرَ، قَرَعَ | membuka; membaca; menciptakan; mengangkat; menolak/mendorong; menetapkan; memisahkan; memotong; duduk; menggenggam; menentukan/mengukur; mengetuk |

### Corrections from earlier pass
- `طَلَبَ` dipindahkan: **ل** baru legal P011.
- `نَظَرَ` dipindahkan: **ن** baru legal P012.
- `ظَهَرَ` dipindahkan: **ه** baru legal P013.
- `جَلَسَ` dipindahkan: **ل** baru legal P011.
- Dengan demikian allocation lama yang menaruh bentuk-bentuk tersebut di P005/P007 **SUPERSEDED** oleh tabel strict-first-legal-page ini.

### Cumulative fill policy
Mulai P003, semua WORD pada page sebelumnya tetap tersedia secara kumulatif. Target 18 slot WORD dipenuhi dari bank legal kumulatif; pengulangan hanya digunakan setelah seluruh WORD unik legal pada page itu terpakai. P001–P002 tetap tanpa 3-huruf palsu.

### Verification notes
- Bentuk Qurani `فَتَحَ` terkonfirmasi sebagai Form I pada Quranic Arabic Corpus.
- Bentuk Qurani `فَطَرَ` terkonfirmasi sebagai Form I pada Quranic Arabic Corpus.
- `نَظَرَ` memang Qurani, tetapi secara urutan buku baru legal setelah ن diperkenalkan, sehingga tidak boleh dimajukan ke P007.
- Kandidat yang masih membutuhkan pemeriksaan kamus lebih dalam tetap tidak boleh otomatis masuk generator sampai `VERIFIED=YES`.


## Deep lexical pass v0.3 — expanded cumulative Fathah bank

Tujuan pass ini adalah memenuhi slot latihan dengan WORD sah sebanyak mungkin sambil mempertahankan **first-legal-page**. Daftar berikut menambah kandidat yang tidak membutuhkan fitur selain fathah.

| First legal page | Additional WORD | Gloss ID |
|---|---|---|
| P004 | بَدَأَ، أَخَذَ، خَبَرَ، بَرَزَ، حَرَثَ | memulai; mengambil; mengetahui/memberitakan; tampil/keluar; mengolah/menanam |
| P005 | سَأَلَ، سَبَحَ، سَرَدَ، شَرَحَ، شَرَدَ، شَرَبَ، سَحَبَ، سَخَرَ، سَرَحَ، سَرَقَ | bertanya/meminta; berenang/bertasbih menurut konteks; menuturkan berurutan; menjelaskan/membelah; lari/menyimpang; minum; menarik; mengejek/menundukkan menurut konteks; melepas/pergi; mencuri |
| P006 | صَرَخَ، صَدَرَ، ضَحَكَ، ضَجَرَ | berteriak; keluar/terbit; tertawa; jemu/gelisah |
| P007 | طَرَحَ، طَرَدَ، طَبَخَ، طَبَعَ، ظَلَمَ* | melempar/mengajukan; mengusir; memasak; mencetak/menutup; menzalimi* |
| P008 | عَرَفَ*، عَزَمَ*، عَصَرَ، عَطَفَ*، غَرَسَ، غَرَفَ، غَرَقَ، غَلَبَ*، غَلَقَ*، غَسَلَ* | mengenal*; bertekad*; memeras; membelok/menaruh kasih*; menanam; menciduk; tenggelam; mengalahkan*; menutup*; mencuci* |
| P009 | سَأَلَ، خَلَقَ*، رَزَقَ*، سَفَرَ، شَفَعَ، صَرَفَ، عَقَرَ، عَقَدَ*، فَصَلَ*، فَقَدَ، قَذَفَ، قَسَمَ، قَصَدَ، قَصَرَ، قَتَلَ* | bertanya; menciptakan*; memberi rezeki*; bepergian/tersingkap; memberi syafaat/menggenapkan; memalingkan; melukai/menyembelih; mengikat*; memisahkan*; kehilangan; melempar; membagi/bersumpah; menuju; memendekkan/membatasi; membunuh* |

\* Kandidat bertanda bintang hanya legal jika semua hurufnya memang sudah masuk whitelist kumulatif pada page tersebut; validator first-legal-page wajib memindahkan kandidat bila ada huruf masa depan. Daftar ini adalah lexical discovery pool, bukan izin otomatis generator.

### Mandatory validator before allocation
Sebelum WORD masuk slot:
1. pecah WORD menjadi huruf dasar;
2. cocokkan semua huruf dengan cumulative introduced letters pada page;
3. pastikan seluruh vokal yang tercetak hanya harakat legal;
4. tolak bentuk yang memerlukan sukun/tasydid/mad/tanwin;
5. simpan gloss dan lemma;
6. hanya `VERIFIED=YES` yang boleh masuk allocation final.

### Fill target
- P003–P009: terus perluas WORD unik sampai sebanyak mungkin; setelah seluruh WORD legal unik digunakan, pengulangan terkontrol diperbolehkan untuk mencapai 18 slot WORD.
- P010: gunakan keseluruhan bank Fathah yang telah VERIFIED, dengan distribusi huruf seluas mungkin.
- Tidak ada kombinasi 3 huruf non-kata.


## Curated allocation v0.4 — P003–P010 full 18 WORD slots

**Rule:** 6 slot awal halaman tetap dapat dipakai untuk pasangan 2 huruf; 18 slot berikut wajib WORD. Semua WORD di bawah hanya memakai huruf yang telah legal secara kumulatif dan fathah. Daftar ini menggantikan allocation algoritmik lama.

### P003
`بَحَثَ` diulang terkontrol 18×. Tidak dibuat kata palsu.

### P004
`بَحَثَ · جَحَدَ · حَذَرَ · بَدَأَ · أَخَذَ · خَبَرَ · بَرَزَ · حَرَثَ`
Distribusi 18 slot: 8 WORD unik terlebih dahulu, kemudian pengulangan terkontrol.

### P005
`بَحَثَ · جَحَدَ · حَذَرَ · بَدَأَ · أَخَذَ · خَبَرَ · بَرَزَ · حَرَثَ · دَرَسَ · سَجَدَ · حَسَدَ · حَبَسَ · حَرَسَ · سَبَحَ · شَرَحَ · شَرَدَ · شَرَبَ · سَحَبَ`

### P006
18 slot dipilih tanpa kombinasi palsu dari:
`بَحَثَ · جَحَدَ · حَذَرَ · بَدَأَ · أَخَذَ · دَرَسَ · سَجَدَ · حَسَدَ · حَبَسَ · حَرَسَ · صَبَرَ · ضَرَبَ · حَصَدَ · رَصَدَ · صَرَخَ · صَدَرَ · ضَحَكَ · ضَجَرَ`

### P007
18 slot dipilih dari bank legal kumulatif, dengan prioritas WORD yang memakai kompetensi baru:
`بَسَطَ · شَطَرَ · طَرَحَ · طَرَدَ · طَبَخَ · طَبَعَ`
ditambah WORD legal P003–P006 sampai 18 slot.

### P008
18 slot:
`عَبَدَ · رَجَعَ · غَدَرَ · عَرَضَ · غَضَبَ · عَجَزَ · عَبَرَ · عَثَرَ · شَعَرَ · سَحَرَ · عَصَرَ · غَرَسَ · غَرَفَ · غَرَقَ`
+ 4 WORD legal kumulatif dari halaman sebelumnya.

### P009
18 slot:
`فَتَحَ · قَرَأَ · فَطَرَ · رَفَعَ · دَفَعَ · فَرَضَ · فَرَقَ · قَطَعَ · قَعَدَ · قَبَضَ · قَدَرَ · قَرَعَ · سَفَرَ · شَفَعَ · صَرَفَ · فَقَدَ · قَذَفَ · قَصَدَ`

### P010 — Fathah checkpoint
18 slot checkpoint dipilih dari seluruh bank P003–P009 dengan syarat:
- minimal satu representasi setiap kompetensi huruf P001–P009;
- tidak ada kata non-meaningful;
- tidak ada kasrah/dhammah/sukun/tasydid/mad/tanwin;
- tidak ada huruf P011 ke atas;
- prioritas kata Qurani/fusha yang paling jelas.

### Quranic morphology confirmations used as hard evidence
- `فَتَحَ` = Form I, “to open / give victory”.
- `فَطَرَ` = Form I.
- `صَبَرَ` = Form I, “to be patient”.
- `ضَرَبَ` = Form I, “to strike / set forth”.
- Pola `فَعَلَ` sendiri adalah pola dasar Form I yang digunakan Quranic Arabic Corpus; tetapi kecocokan pola **tidak cukup** — lemma/kata tetap harus sah.

### Exclusion principle
Bentuk yang hanya “terlihat seperti فَعَلَ” tetapi lemma/harakatnya tidak terverifikasi tetap dilarang. Kata dengan huruf masa depan dipindah ke halaman first-legal yang benar.


## Kasrah lexical pass v0.5 — P011–P020

### Important sequencing
- P011–P013 masih **Fathah-only**. Kasrah baru legal mulai P014.
- WORD tiga huruf harus tepat 3 huruf dasar. Bentuk yang membutuhkan alif mad, ta marbuta, sukun, tasydid, tanwin, atau huruf keempat tidak masuk.
- Untuk P014–P019, bentuk campuran Fathah+Kasrah boleh dipakai hanya jika semua harakatnya telah legal.

### P011 — new كَ لَ
Kandidat prioritas:
`كَتَبَ · أَكَلَ · مَلَكَ · سَلَكَ · تَرَكَ · هَلَكَ*`
Gloss: menulis; makan; memiliki/menguasai; menempuh; meninggalkan; binasa*.
`هَلَكَ` ditahan sampai ه legal P013.

### P012 — new مَ نَ
Kandidat:
`مَنَعَ · نَزَلَ · نَصَرَ · نَفَعَ · نَفَرَ · نَشَرَ · نَقَلَ · نَكَحَ · مَسَحَ · مَسَكَ · مَكَرَ · مَلَأَ · مَرَضَ · مَرَجَ`
Gloss: mencegah; turun; menolong; memberi manfaat; berangkat/menjauh; menyebarkan; memindahkan; menikah; mengusap; memegang; membuat makar; memenuhi; sakit; bercampur/membiarkan mengalir.

### P013 — new هَ وَ يَ
Kandidat:
`هَلَكَ · هَجَرَ · هَدَمَ · هَرَبَ · وَجَدَ · وَرَدَ · وَزَنَ · وَهَبَ · يَبَسَ`
Gloss: binasa; meninggalkan; merobohkan; melarikan diri; menemukan; mendatangi; menimbang; memberi/anugerah; menjadi kering.
Kandidat yang secara bentuk memerlukan alif maqsurah/mad atau fitur lain tidak dimasukkan.

### P014 — Kasrah بِ تِ ثِ جِ
Target bukan sekadar menambah kasrah, tetapi mencari WORD yang benar-benar memiliki kasrah pada salah satu huruf legal. Kandidat awal:
`عَمِلَ · فَرِحَ · شَرِبَ · حَسِبَ · سَمِعَ · رَكِبَ · لَعِبَ · تَبِعَ · وَرِثَ · نَدِمَ`
Semua kandidat wajib dicek first-legal huruf; hanya bentuk dengan kasrah pada huruf yang sudah diperkenalkan sebagai kasrah boleh masuk page terkait.

### P015 — new حِ خِ دِ ذِ
Tambahan kandidat:
`حَفِظَ · حَمِدَ · خَسِرَ · خَشِيَ* · ذَكِرَ`
`خَشِيَ` ditahan bila bentuk akhirnya menuntut perlakuan ya/struktur yang belum sesuai gate.

### P016 — new رِ زِ سِ شِ
Tambahan:
`رَحِمَ · رَضِيَ* · سَلِمَ · شَهِدَ · عَلِمَ`
Bentuk berakhir ya seperti `رَضِيَ` diaudit khusus sebelum produksi.

### P017 — new صِ ضِ طِ ظِ
Tambahan:
`ظَلِمَ · طَمِعَ · ضَحِكَ`
Catatan: tidak semua akar dengan ص/ض/ط/ظ memiliki Form-I kasrah yang cocok; jangan memaksakan.

### P018 — new عِ غِ فِ قِ
Tambahan:
`غَضِبَ · فَهِمَ · قَدِمَ · قَبِلَ · قَدِرَ · عَرِفَ`
Gloss: marah; memahami; datang; menerima; mampu/berkuasa; mengetahui/mengenal.

### P019 — completion Kasrah
P019 memakai **curated cumulative mixed-vowel bank**, bukan random. Prioritas 18 WORD:
`عَمِلَ · فَرِحَ · شَرِبَ · حَسِبَ · سَمِعَ · رَكِبَ · لَعِبَ · تَبِعَ · وَرِثَ · نَدِمَ · حَفِظَ · حَمِدَ · خَسِرَ · رَحِمَ · سَلِمَ · شَهِدَ · عَلِمَ · فَهِمَ`

### P020 — checkpoint Fathah + Kasrah
18 WORD checkpoint curated:
`بَحَثَ · دَرَسَ · صَبَرَ · ضَرَبَ · عَبَدَ · غَفَرَ · فَتَحَ · قَرَأَ · كَتَبَ · نَزَلَ · وَجَدَ · عَمِلَ · فَرِحَ · شَرِبَ · سَمِعَ · رَكِبَ · عَلِمَ · فَهِمَ`

### Kasrah hard gate
Sebelum freeze:
`FIRST-LEGAL-LETTER PASS → FIRST-LEGAL-KASRAH PASS → LEMMA PASS → GLOSS PASS → 3-LETTER PASS → P019 CURATION PASS → P020 CURATION PASS`.


## Strict Kasrah audit v0.6 — first-legal harakat

Audit ini membedakan **huruf sudah dikenal** dari **kasrah pada huruf tersebut sudah dikenal**. Sebuah WORD campuran baru boleh tampil ketika setiap kasrah di dalam WORD sudah termasuk kompetensi page.

| Page | Kasrah baru | WORD yang lolos untuk diprioritaskan |
|---|---|---|
| P014 | بِ تِ ثِ جِ | تَبِعَ |
| P015 | حِ خِ دِ ذِ | حَسِبَ، حَمِدَ، نَدِمَ |
| P016 | رِ زِ سِ شِ | عَمِلَ، فَرِحَ، شَرِبَ، سَمِعَ، رَكِبَ، لَعِبَ، وَرِثَ، خَسِرَ، رَحِمَ، سَلِمَ، شَهِدَ، عَلِمَ |
| P017 | صِ ضِ طِ ظِ | مَرِضَ، غَضِبَ، نَشِطَ، عَطِشَ |
| P018 | عِ غِ فِ قِ | فَهِمَ، قَبِلَ، عَرِفَ، عَجِبَ، خَطِفَ، وَسِعَ |
| P019 | كِ لِ مِ نِ هِ وِ يِ ءِ إِ | أَمِنَ، بَخِلَ، كَرِهَ + seluruh WORD legal kumulatif P014–P018 |

### Corrections
- `عَمِلَ` **tidak legal di P014** karena kasrah pada م baru diperkenalkan P019; dipindahkan ke P019 jika aturan kasrah-letter literal diterapkan.
- `فَرِحَ` tidak legal sebelum رِ diperkenalkan P016.
- `شَرِبَ` tidak legal sebelum رِ P016.
- `سَمِعَ` tidak legal sebelum مِ P019.
- `رَكِبَ` tidak legal sebelum كِ P019.
- `لَعِبَ` memakai عِ, baru legal P018.
- Karena itu tabel “WORD yang lolos” di atas masih harus dibaca dengan validator posisi kasrah; daftar contoh sumber tidak otomatis sama dengan first-legal page QURBATA.

### Literal validator result — safe anchors
Untuk menghindari kesalahan urutan, anchor yang benar-benar aman:
- P014: `تَبِعَ` (kasrah pada ب).
- P015: `حَسِبَ` (kasrah pada س — **belum legal sampai P016**, maka pindah P016); `حَمِدَ` (kasrah pada م — P019), `نَدِمَ` (kasrah pada د — legal P015).
- P016: `فَرِحَ` (رِ legal), `شَرِبَ` (رِ legal), `خَسِرَ` (سِ legal), `رَحِمَ` (حِ sudah legal P015), `سَلِمَ` (لِ belum legal P019), `شَهِدَ` (هِ belum legal P019).
- P017: `مَرِضَ` (رِ legal), `غَضِبَ` (ضِ legal), `نَشِطَ` (شِ legal), `عَطِشَ` (طِ legal).
- P018: `فَهِمَ` (هِ belum legal P019), `قَبِلَ` (بِ legal P014), `عَرِفَ` (رِ legal P016), `عَجِبَ` (جِ legal P014), `خَطِفَ` (طِ legal P017), `وَسِعَ` (سِ legal P016).
- P019: seluruh bentuk di atas menjadi legal dari sisi inventori fathah+kasrah.

### Consequence for page design
P014–P018 **tidak boleh dipaksa mempunyai 18 WORD unik yang semuanya mengandung kasrah baru**. Halaman tetap dapat penuh dengan:
1. 6 slot pasangan/pola untuk penanaman kompetensi baru;
2. WORD legal yang sudah lolos sampai page tersebut;
3. pengulangan WORD sah secara terkontrol.
P019/P020 memiliki inventori cukup besar untuk 18 WORD bermakna tanpa kombinasi palsu.


## Page-material blueprint v0.7 — 24 groups before PDF

**Frozen composition target:** 8 rows × 3 groups = 24 groups. For normal pages, groups 01–06 are controlled 2-letter drills; groups 07–24 are meaningful 3-letter WORD slots. No random 3-letter generation.

### P001–P002
Because no safe meaningful 3-letter inventory exists yet under the strict whitelist, all 24 groups remain controlled 2-letter drills. This is an explicit exception, not a license for fake words.

### P003
01–06: controlled 2-letter drills emphasizing جَ حَ خَ and review بَ تَ ثَ.  
07–24: `بَحَثَ` repeated with spacing/distribution control. No fake alternatives.

### P004
01–06: drills emphasizing دَ ذَ رَ زَ.  
07–24 rotate legal WORD bank:
`بَحَثَ، جَحَدَ، حَذَرَ، بَدَأَ، أَخَذَ، خَبَرَ، بَرَزَ، حَرَثَ`, then controlled repeats.

### P005
01–06 emphasize سَ شَ.  
07–24 exactly:
`بَحَثَ، جَحَدَ، حَذَرَ، بَدَأَ، أَخَذَ، خَبَرَ، بَرَزَ، حَرَثَ، دَرَسَ، سَجَدَ، حَسَدَ، حَبَسَ، حَرَسَ، سَبَحَ، شَرَحَ، شَرَدَ، شَرَبَ، سَحَبَ`.

### P006
01–06 emphasize صَ ضَ.  
07–24 exactly:
`بَحَثَ، جَحَدَ، حَذَرَ، دَرَسَ، سَجَدَ، حَسَدَ، حَبَسَ، حَرَسَ، صَبَرَ، ضَرَبَ، حَصَدَ، رَصَدَ، صَرَخَ، صَدَرَ، ضَحَكَ، ضَجَرَ، شَرَحَ، شَرَبَ`.

### P007
01–06 emphasize طَ ظَ.  
07–24:
`بَسَطَ، شَطَرَ، طَرَحَ، طَرَدَ، طَبَخَ، طَبَعَ`
+ 12 verified cumulative WORD from P003–P006.

### P008
01–06 emphasize عَ غَ.  
07–24:
`عَبَدَ، رَجَعَ، غَدَرَ، عَرَضَ، غَضَبَ، عَجَزَ، عَبَرَ، عَثَرَ، شَعَرَ، سَحَرَ، عَصَرَ، غَرَسَ، غَرَفَ، غَرَقَ`
+ 4 verified cumulative WORD.

### P009
01–06 emphasize فَ قَ.  
07–24 exactly:
`فَتَحَ، قَرَأَ، فَطَرَ، رَفَعَ، دَفَعَ، فَرَضَ، فَرَقَ، قَطَعَ، قَعَدَ، قَبَضَ، قَدَرَ، قَرَعَ، سَفَرَ، شَفَعَ، صَرَفَ، فَقَدَ، قَذَفَ، قَصَدَ`.

### P010
Checkpoint Fathah. 24 groups curated from verified P003–P009 inventory, maximizing letter coverage; no new letter/harakat.

### P011
01–06 emphasize كَ لَ.  
07–24 use `كَتَبَ، أَكَلَ، مَلَكَ، سَلَكَ، تَرَكَ` plus verified cumulative Fathah WORD. Quranic concordance independently confirms `كَتَبَ` and `أَكَلَ`.

### P012
01–06 emphasize مَ نَ.  
07–24 prioritize:
`مَنَعَ، نَزَلَ، نَصَرَ، نَفَعَ، نَفَرَ، نَشَرَ، نَقَلَ، نَكَحَ، مَسَحَ، مَسَكَ، مَكَرَ، مَلَأَ، مَرَضَ، مَرَجَ`
+ 4 cumulative Fathah WORD.

### P013
01–06 emphasize هَ وَ يَ. Detached ه must pass two-hole renderer gate.  
07–24 prioritize:
`هَلَكَ، هَجَرَ، هَدَمَ، هَرَبَ، وَجَدَ، وَرَدَ، وَزَنَ، وَهَبَ، يَبَسَ`
+ cumulative Fathah WORD.

### P014
Two initial rows are the mandated transition planting: `بَ←بِ، تَ←تِ، ثَ←ثِ، جَ←جِ` distributed as six large groups.  
Remaining 18 slots: only WORD whose kasrah occurs on ب/ت/ث/ج. Anchor `تَبِعَ`; expand only after strict lexical verification. Repetition is preferable to an illegal kasrah.

### P015
01–06 emphasize حِ خِ دِ ذِ with Fathah comparison.  
07–24 use P014-safe WORD plus P015-safe additions such as `نَدِمَ` where kasrah is on د. Do not use `حَسِبَ` yet because سِ is P016.

### P016
01–06 emphasize رِ زِ سِ شِ.  
07–24 may add `فَرِحَ، شَرِبَ، خَسِرَ، رَحِمَ، حَسِبَ` where all kasrah positions are now legal. Quranic concordance confirms common Form-I lemmas such as `سَمِعَ` and `عَلِمَ`, but those wait until مِ/لِ become legal at P019.

### P017
01–06 emphasize صِ ضِ طِ ظِ.  
07–24 may add `مَرِضَ، غَضِبَ، نَشِطَ، عَطِشَ` plus cumulative legal WORD.

### P018
01–06 emphasize عِ غِ فِ قِ.  
07–24 may add `قَبِلَ، عَرِفَ، عَجِبَ، خَطِفَ، وَسِعَ` plus cumulative legal WORD. `فَهِمَ` waits for هِ P019.

### P019
01–06 emphasize `كِ لِ مِ نِ هِ وِ يِ ءِ إِ`; detached `هِ` is mandatory two-hole.  
07–24 curated 18 WORD:
`عَمِلَ، فَرِحَ، شَرِبَ، حَسِبَ، سَمِعَ، رَكِبَ، لَعِبَ، تَبِعَ، وَرِثَ، نَدِمَ، حَفِظَ، حَمِدَ، خَسِرَ، رَحِمَ، سَلِمَ، شَهِدَ، عَلِمَ، فَهِمَ`.

### P020
Checkpoint Fathah + Kasrah. 24 groups are curated, not cycled. Core 18 WORD:
`بَحَثَ، دَرَسَ، صَبَرَ، ضَرَبَ، عَبَدَ، غَفَرَ، فَتَحَ، قَرَأَ، كَتَبَ، نَزَلَ، وَجَدَ، عَمِلَ، فَرِحَ، شَرِبَ، سَمِعَ، رَكِبَ، عَلِمَ، فَهِمَ`.
The remaining checkpoint groups are reserved for 29-letter-name/harakat-name recognition required by the P020 register, rather than meaningless 3-letter filler.

### Evidence policy
Quranic Arabic Corpus is used as a high-priority verification source for Quranic lemmas and morphology. Its verb concordance explicitly lists, among others, `عَلِمَ`, `عَمِلَ`, `أَخَذَ`, `عَبَدَ`, `سَأَلَ`, `وَجَدَ`, `أَكَلَ`, `غَفَرَ`, `صَبَرَ`, `ضَرَبَ`, `كَتَبَ`, `نَصَرَ`, `رَزَقَ`, and `سَمِعَ` as verbs with glosses. Corpus evidence confirms lexical/morphological existence; QURBATA first-legal-page rules remain a separate curriculum gate.

## Audit fields per final word
Setiap entri final wajib dicatat sebagai:
`PAGE | ARABIC | ROOT/LEMMA | GLOSS_ID | QURAN/FUSHA | LEGAL_FEATURES | VERIFIED`

## Production gate
`REGISTER PASS → WORD-BANK PASS → HARAKAT PASS → MEANING PASS → HA-TWO-HOLE PASS → CURATED PAGE PASS → PDF GENERATION`

**PDF P001–P020 tidak boleh dibangun ulang sebagai FINAL sebelum CONTENT MASTER ini berstatus FROZEN.**
