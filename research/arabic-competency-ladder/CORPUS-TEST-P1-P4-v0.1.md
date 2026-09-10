# Corpus Test P1–P4 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Tujuan:** menguji frontier awal kompetensi dengan bukti Qurani dan cumulative clean-example rule.  
**Sumber linguistik utama:** Quranic Arabic Corpus (morphology, syntax, dependency graph, grammar pages).

## 1. Dasar Corpus

Quranic Arabic Corpus mendefinisikan jumlah ismiyyah secara fungsional sebagai struktur yang memiliki peran `mubtada'` dan `khabar`. Corpus juga memberi tag `NS` untuk `jumlah ismiyyah` dan relasi dependency `pred` untuk hubungan `mubtada'–khabar`.

Anchor paling sederhana yang diberikan corpus adalah QS 112:2:

> اللَّهُ الصَّمَدُ

Corpus menganalisisnya sebagai `مبتدأ وخبر`.

## 2. P1 — Isim sebagai kategori kata

### Hipotesis

Peserta mengenali satu token Qurani sebagai isim tanpa terlebih dahulu menuntut analisis fungsi sintaksisnya.

### Dependency

Tidak ada dependency sintaksis wajib. Unit evidence dapat berupa satu token Qurani.

### Status awal

`VIABLE AS EARLY FRONTIER`, tetapi **belum difreeze sebagai K1**.

### Catatan

P1 berfungsi sebagai kompetensi identifikasi. Ia tidak boleh dicampur dengan marfu'/manshub/majrur, mubtada', mudhaf, na'at, atau fungsi isim lainnya.

## 3. P2 — `الـ` ta'rif pada isim

### Hipotesis

Peserta mengenali `الـ` sebagai penanda definiteness pada isim yang sudah dikenali.

### Dependency

- P1 isim.

### Status awal

`VIABLE`, tetapi urutan terhadap fitur nominal lain masih perlu diuji.

### Catatan

P2 hanya pengenalan bentuk permukaan `الـ`; sistem `ma'rifah` secara lengkap **tidak** ditempatkan di sini karena ma'rifah juga mencakup dhamir, isim isyarah, isim maushul, nama diri, dan idhafah tertentu.

## 4. P3 — Nakirah/tanwin nominal sederhana

### Hipotesis

Peserta mengenali isim nakirah sederhana yang bertanwin tanpa menganalisis seluruh sistem i'rab.

### Dependency

- P1 isim.

### Status awal

`VIABLE`, namun **P2 dan P3 belum dipastikan harus berurutan linear**. Keduanya mungkin merupakan sibling dependencies setelah P1.

## 5. P4 — Jumlah Ismiyyah Dasar: Mubtada' + Khabar Isim

### Hipotesis

Peserta memahami relasi predikatif paling dasar antara dua unsur nominal tanpa fi'il dan tanpa ekspansi sintaksis lain.

### Dependency minimum yang sedang diuji

- P1 isim;
- fitur definiteness/nakirah hanya sejauh benar-benar diperlukan oleh contoh;
- belum boleh membutuhkan dhamir, jar–majrur, idhafah, na'at, maushul, inna, kana, syarth, atau jumlah bersarang.

## 6. Evidence Awal P4

| Ref | Quranic unit | Analisis target | Status | Alasan |
|---|---|---|---|---|
| 112:2 | `اللَّهُ الصَّمَدُ` | mubtada' + khabar | PASS-ANCHOR | Corpus secara eksplisit menganalisis `الله الصمد` sebagai مبتدأ وخبر; hanya dua unsur nominal inti |
| 4:128 | `الصُّلْحُ خَيْرٌ` | mubtada' + khabar | PASS | Grammar corpus menyebut `والصلح خير` sebagai jumlah mu'taridhah; unit inti `الصلح خير` mempertahankan predikasi nominal sederhana |
| 64:6 | `اللَّهُ غَنِيٌّ` dari `وَاللَّهُ غَنِيٌّ حَمِيدٌ` | mubtada' + khabar | REVIEW-PASS | Unit dua kata secara internal membentuk predikasi sederhana; keseluruhan klausa memiliki unsur tambahan `حميد` sehingga perlu standardisasi aturan pemotongan unit |
| 47:38 | `اللَّهُ الْغَنِيُّ` dari `وَاللَّهُ الْغَنِيُّ` | mubtada' + khabar | REVIEW | Secara permukaan sangat sederhana, tetapi analisis dependency harus diverifikasi sebelum promosi ke PASS |
| 87:17 | `الْآخِرَةُ خَيْرٌ وَأَبْقَى` | jumlah ismiyyah | PREMATURE untuk P4 | mengandung coordination `و` dan bentuk tafdhil tambahan; bukan clean-example P4 jika kompetensi itu belum ditempatkan sebelumnya |
| 35:15 | `أَنْتُمُ الْفُقَرَاءُ` | mubtada' dhamir + khabar | PREMATURE untuk P4 | membutuhkan dhamir munfashil sebelum jumlah ismiyyah ini dapat dipakai sebagai clean-example |
| 35:15 | `اللَّهُ هُوَ الْغَنِيُّ الْحَمِيدُ` | struktur nominal kompleks | PREMATURE | membutuhkan dhamir pemisah/struktur pronominal dan ekspansi nominal |
| 39:7 | `اللَّهَ غَنِيٌّ عَنْكُمْ` | predikasi setelah inna | PREMATURE | bukan jumlah ismiyyah dasar bebas; membutuhkan `inna` dan jar–majrur |

## 7. Temuan Metodologis Penting

### 7.1 P4 nyata dan memiliki clean anchor

QS 112:2 membuktikan bahwa struktur `mubtada' + khabar` murni benar-benar tersedia di dalam Al-Qur'an dan dapat menjadi model pengajaran awal.

### 7.2 Tidak semua jumlah ismiyyah layak menjadi contoh pada tahap yang sama

Contoh seperti `أنتم الفقراء`, `الله هو الغني الحميد`, atau `الآخرة خير وأبقى` tetap merupakan struktur nominal, tetapi membawa dependency tambahan. Karena itu corpus bank harus menyimpan **status tahap**, bukan hanya label `jumlah ismiyyah`.

### 7.3 Minimal-unit extraction wajib distandardisasi

Ada ayat yang memiliki inti sederhana di dalam klausa yang lebih panjang. Contoh `والله غني حميد` mengandung inti `الله غني`. Kita membutuhkan aturan tegas:

1. unit harus contiguous;
2. target relation tetap utuh;
3. penghilangan unsur kiri/kanan tidak boleh mengubah analisis target;
4. unit tidak boleh menghasilkan makna gramatikal palsu;
5. setiap pemotongan harus tetap menyimpan referensi ayat penuh.

Sebelum aturan ini divalidasi, kandidat hasil pemotongan diberi `REVIEW-PASS`, bukan `PASS` final.

## 8. Implikasi terhadap Urutan P1–P4

Hasil awal mendukung struktur dependency berikut:

```text
P1 isim
 ├─ P2 al-ta'rif
 └─ P3 nakirah/tanwin
       \
        \__ fitur nominal dasar
                ↓
P4 mubtada' + khabar isim sederhana
```

Tetapi grafik ini **belum membuktikan bahwa P2 harus sebelum P3 atau sebaliknya**. Kemungkinan terbaik sementara adalah memperlakukan P2 dan P3 sebagai dua cabang setelah P1, lalu menentukan linearization berdasarkan clean-example yield dan pedagogical simplicity.

## 9. Keputusan Sementara

- P1: `CANDIDATE-STRONG`
- P2: `CANDIDATE-STRONG`
- P3: `CANDIDATE-STRONG`
- P4: `CANDIDATE-STRONG`, dengan QS 112:2 sebagai anchor evidence
- belum ada `K1–K4` yang difreeze;
- corpus bank harus terus diperbesar sebelum linearization final.

## 10. Batch Berikutnya

1. perluas evidence P4 sampai puluhan kandidat dari seluruh Al-Qur'an;
2. klasifikasikan menjadi `PURE`, `MINIMAL-EXTRACTABLE`, dan `PREMATURE`;
3. hitung dependency apa yang paling sering menghalangi kandidat P4;
4. gunakan hasil itu untuk menentukan apakah dhamir, na'at, idhafah, atau jar–majrur harus masuk sebelum/ sesudah P4;
5. baru mulai menguji kandidat frontier P5.

## 11. Referensi Corpus

- Quranic Arabic Corpus — Phrase Tags (`NS = جملة اسمية`)
- Quranic Arabic Corpus — Syntactic Relations (`pred = مبتدأ وخبر`)
- Quranic Arabic Corpus — Dependency Graph documentation (QS 112:2 sebagai contoh hubungan mubtada'–khabar)
- Quranic Arabic Corpus — Grammar QS 112:2
- Quranic Arabic Corpus — Grammar QS 4:128
- Quranic Arabic Corpus — search/dictionary evidence untuk QS 64:6, 47:38, 35:15, 39:7, 87:17
