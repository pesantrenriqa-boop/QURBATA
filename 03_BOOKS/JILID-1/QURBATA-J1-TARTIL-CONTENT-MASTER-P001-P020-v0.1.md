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

## Audit fields per final word
Setiap entri final wajib dicatat sebagai:
`PAGE | ARABIC | ROOT/LEMMA | GLOSS_ID | QURAN/FUSHA | LEGAL_FEATURES | VERIFIED`

## Production gate
`REGISTER PASS → WORD-BANK PASS → HARAKAT PASS → MEANING PASS → HA-TWO-HOLE PASS → CURATED PAGE PASS → PDF GENERATION`

**PDF P001–P020 tidak boleh dibangun ulang sebagai FINAL sebelum CONTENT MASTER ini berstatus FROZEN.**
