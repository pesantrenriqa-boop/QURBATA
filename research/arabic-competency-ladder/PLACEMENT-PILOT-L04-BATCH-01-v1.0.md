# Placement Pilot L04 — Batch 01 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** adaptive placement checkpoint L04  
**Guardrail:** item hanya boleh menuntut operasi yang telah tersedia sampai checkpoint L04; struktur lebih tinggi boleh muncul hanya bila tidak diperlukan untuk menjawab target atau item harus ditandai REVIEW/PREMATURE.

## 1. Tujuan

Membuka verse-level pilot bank untuk checkpoint L04 sebagai implementasi awal dari adaptive placement architecture. Batch ini menguji format item, scoring, prerequisite integrity, transfer, dan integrative discrimination sebelum pool diperluas menjadi minimum 36 item.

## 2. Item record schema

Setiap item wajib menyimpan:

- Item ID
- Checkpoint/Level
- Target competency/competencies
- Prerequisite competencies
- Qur'anic reference
- Target span
- Response class
- Prompt
- Expected response
- Scoring key
- Critical misconception
- Error code
- Feature ceiling
- Ambiguity flag
- Review status

## 3. Pilot core set

### L04-P01 — Direct recognition
- Target: early nominal recognition
- Reference: QS 112:2
- Target span: `اللَّهُ الصَّمَدُ`
- Response class: recognition/classification
- Prompt: identifikasi unsur nominal utama pada span tanpa meminta analisis struktur di atas feature ceiling.
- Expected: peserta mengenali token nominal yang relevan dan tidak mengubah tugas menjadi terjemahan.
- Critical misconception: lexical guessing tanpa identifikasi bentuk.
- Error: E01/E02
- Ambiguity: LOW
- Status: PILOT

### L04-P02 — Marker recognition
- Target: definite nominal marker
- Reference: QS 1:2
- Target span: `الْحَمْدُ`
- Response class: recognition
- Prompt: tunjukkan penanda bentuk nominal yang menjadi target.
- Expected: pengenalan `الـ` pada isim.
- Critical misconception: menyebut arti kata tetapi gagal mengenali marker.
- Error: E01/E02
- Ambiguity: LOW
- Status: PILOT

### L04-P03 — Contrast control
- Target: nominal definiteness contrast
- Reference: QS 2:2
- Target span: `هُدًى`
- Response class: contrast/classification
- Prompt: klasifikasikan bentuk target terhadap definite/nakirah sesuai operasi yang sudah dikuasai.
- Expected: nakirah/tanwin recognition.
- Critical misconception: semua isim dianggap ma'rifah karena berasal dari ayat Al-Qur'an.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L04-P04 — Prerequisite integrity
- Target: frequent preposition recognition + nominal target
- Reference: QS 1:2
- Target span: `لِلَّهِ`
- Response class: recognition/relation-lite
- Prompt: identifikasi huruf jar dan unsur nominal sesudahnya tanpa meminta i'rab lanjutan.
- Expected: mengenali `لِـ` sebagai huruf jar dan `الله` sebagai unsur nominal target.
- Critical misconception: membaca keseluruhan token sebagai satu label leksikal tanpa segmentasi minimal.
- Error: E02/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P05 — Transfer
- Target: independent recognition on unseen Qur'anic span
- Reference: QS 103:2
- Target span: `الْإِنسَانَ`
- Response class: transfer/classification
- Prompt: terapkan operasi pengenalan marker nominal pada contoh baru.
- Expected: pengenalan isim dengan `الـ`; tidak mensyaratkan analisis fungsi sintaksis ayat.
- Critical misconception: transfer gagal ketika kata berbeda dari contoh latihan.
- Error: E06
- Ambiguity: LOW
- Status: PILOT

### L04-P06 — Integrative discriminator
- Target: combine early form recognitions without higher-stage reasoning
- Reference: QS 114:1
- Target span: `بِرَبِّ النَّاسِ`
- Response class: integration
- Prompt: identifikasi marker awal, unsur nominal, dan definite marker yang tampak; jangan meminta analisis dependency di atas checkpoint.
- Expected: mengenali `بِـ` sebagai huruf jar; `رَبِّ` sebagai isim; `النَّاسِ` sebagai isim dengan `الـ`.
- Critical misconception: peserta hanya menerjemahkan span atau memaksakan analisis struktur yang belum menjadi target.
- Error: E01/E02/E05
- Ambiguity: MEDIUM — karena konstruksi idhafah ada pada permukaan; scoring core hanya menghitung operasi yang berada di bawah ceiling dan tidak meminta analisis idhafah.
- Status: PILOT WITH CEILING NOTE

### L04-P07 — Direct nominal recognition
- Target: K01 basic noun recognition
- Reference: QS 1:1
- Target span: `اللَّهِ`
- Response class: recognition
- Prompt: klasifikasikan bentuk target sebagai isim/fi'il/huruf tanpa meminta fungsi sintaksis.
- Expected: isim.
- Critical misconception: memilih kategori berdasarkan arti semata.
- Error: E01/E02
- Ambiguity: LOW
- Status: PILOT

### L04-P08 — Definite-marker recognition
- Target: K02 `الـ` recognition
- Reference: QS 103:1
- Target span: `الْعَصْرِ`
- Response class: recognition
- Prompt: identifikasi penanda ma'rifah yang tampak pada target.
- Expected: `الـ`.
- Critical misconception: menyebut kata ma'rifah tanpa menunjukkan marker.
- Error: E02
- Ambiguity: LOW
- Status: PILOT

### L04-P09 — Nakirah/tanwin recognition
- Target: K03
- Reference: QS 104:1
- Target span: `وَيْلٌ`
- Response class: classification
- Prompt: tentukan apakah bentuk target membawa ciri nakirah/tanwin yang tampak.
- Expected: ya; tanwin tampak pada `ويلٌ`.
- Critical misconception: menganggap semua kata tanpa `الـ` otomatis sama tanpa memeriksa bentuk akhir.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L04-P10 — Preposition recognition
- Target: K04 frequent preposition
- Reference: QS 113:1
- Target span: `بِرَبِّ`
- Response class: recognition
- Prompt: tunjukkan huruf jar pada span.
- Expected: `بِـ`.
- Critical misconception: menganggap `برب` sebagai satu unit leksikal tanpa segmentasi marker.
- Error: E02/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P11 — Detached-pronoun recognition
- Target: K05
- Reference: QS 112:1
- Target span: `هُوَ`
- Response class: recognition
- Prompt: klasifikasikan target sebagai dhamir munfashil atau bukan.
- Expected: dhamir munfashil.
- Critical misconception: hanya memberi terjemahan `Dia` tanpa identifikasi bentuk pronominal.
- Error: E01/E02
- Ambiguity: LOW
- Status: PILOT

### L04-P12 — Perfect-verb recognition
- Target: K06
- Reference: QS 110:1
- Target span: `جَاءَ`
- Response class: recognition/classification
- Prompt: tentukan apakah target merupakan fi'il madhi sederhana.
- Expected: ya, fi'il madhi.
- Critical misconception: menilai waktu hanya dari terjemahan Indonesia.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L04-P13 — Imperfect-verb recognition
- Target: K07
- Reference: QS 107:1
- Target span: `يُكَذِّبُ`
- Response class: recognition/classification
- Prompt: tentukan apakah target merupakan fi'il mudhari'.
- Expected: ya, fi'il mudhari'.
- Critical misconception: salah menganggap semua fi'il berawalan ya sebagai satu kategori tanpa mengenali pola verbal.
- Error: E02/E03
- Ambiguity: LOW
- Status: PILOT

### L04-P14 — Simple nominal predication
- Target: K08
- Prerequisite: K01/K02
- Reference: QS 112:2
- Target span: `اللَّهُ الصَّمَدُ`
- Response class: relation-lite
- Prompt: identifikasi dua unsur nominal yang membentuk predikasi sederhana tanpa i'rab detail.
- Expected: `الله` sebagai unsur pertama dan `الصمد` sebagai unsur kedua/predikat nominal sederhana.
- Critical misconception: menjawab hanya arti kalimat atau meminta analisis idhafah/na'at yang tidak ada.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P15 — Jar-majrur with overt noun
- Target: K09
- Prerequisite: K01/K04
- Reference: QS 114:2
- Target span: `مَلِكِ النَّاسِ`
- Response class: negative control
- Prompt: apakah span ini merupakan contoh huruf jar + isim zhahir?
- Expected: tidak; tidak ada huruf jar pada target span.
- Critical misconception: mengira setiap kasrah berarti didahului huruf jar.
- Error: E03/E07
- Ambiguity: MEDIUM — surface genitive exists because of another relation; useful as a negative control.
- Status: PILOT NEGATIVE CONTROL

### L04-P16 — Verb + overt subject
- Target: K10
- Prerequisite: K01/K06
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ`
- Response class: relation
- Prompt: identifikasi fi'il dan fa'il zhahir pada target.
- Expected: `جاء` = fi'il; `الحق` = fa'il zhahir.
- Critical misconception: menganggap nomina setelah fi'il selalu maf'ul bih.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P17 — Detached pronoun in nominal predication
- Target: K11
- Prerequisite: K05/K08
- Reference: QS 112:1
- Target span: `هُوَ اللَّهُ`
- Response class: integration
- Prompt: identifikasi dhamir terpisah dan fungsinya sebagai unsur awal predikasi nominal sederhana.
- Expected: `هو` = dhamir munfashil dan mubtada' sederhana; `الله` = unsur predikat nominal pada ceiling L04.
- Critical misconception: hanya mengenali `هو` sebagai pronoun tetapi gagal melihat fungsi predikatif dasar.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P18 — PP-fronted predication boundary
- Target: K12
- Prerequisite: K04/K08/K09
- Reference: QS 45:36
- Target span: `لِلَّهِ الْحَمْدُ`
- Response class: transfer/relation
- Prompt: identifikasi jar-majrur yang berfungsi sebagai unsur predikatif depan dan unsur nominal sesudahnya tanpa meminta i'rab lanjutan.
- Expected: `لله` = jar-majrur/predikatif depan; `الحمد` = unsur nominal sesudahnya.
- Critical misconception: menganggap semua jar-majrur hanya keterangan yang tidak dapat menempati fungsi khabar.
- Error: E04/E06
- Ambiguity: LOW
- Status: PILOT

### L04-P19 — Negative control for nominal predication
- Target: K08
- Prerequisite: K01/K04
- Reference: QS 113:1
- Target span: `بِرَبِّ الْفَلَقِ`
- Response class: negative control
- Prompt: apakah span ini merupakan jumlah ismiyyah mubtada' + khabar sederhana?
- Expected: tidak; span dimulai huruf jar dan tidak membentuk pasangan mubtada' + khabar nominal sederhana.
- Critical misconception: menganggap setiap dua isim yang berdekatan sebagai jumlah ismiyyah.
- Error: E04/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L04-P20 — Negative control for overt subject
- Target: K10
- Prerequisite: K06
- Reference: QS 96:2
- Target span: `خَلَقَ الْإِنسَانَ`
- Response class: negative control
- Prompt: apakah target merupakan contoh fi'il + fa'il isim zhahir?
- Expected: tidak untuk core K10; `الإنسان` bukan fa'il zhahir pada span ini.
- Critical misconception: menganggap isim setelah fi'il otomatis sebagai fa'il.
- Error: E04/E07
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L04-P21 — Negative control for jar + overt noun
- Target: K09
- Prerequisite: K04
- Reference: QS 1:7
- Target span: `عَلَيْهِمْ`
- Response class: negative control
- Prompt: apakah target memenuhi pola huruf jar + isim zhahir?
- Expected: tidak; target memuat huruf jar dengan pronomina terikat, bukan isim zhahir.
- Critical misconception: menganggap semua objek setelah huruf jar sebagai isim zhahir yang tampak.
- Error: E03/E07
- Feature ceiling: peserta hanya perlu menyatakan bahwa target bukan pola K09; analisis lengkap pronoun attachment tidak diwajibkan.
- Ambiguity: MEDIUM
- Status: PILOT NEGATIVE CONTROL WITH CEILING NOTE

### L04-P22 — Transfer K11
- Target: K11
- Prerequisite: K05/K08
- Reference: QS 57:3
- Target span: `هُوَ الْأَوَّلُ`
- Response class: transfer/relation
- Prompt: terapkan pengenalan dhamir munfashil sebagai unsur awal predikasi nominal pada contoh baru.
- Expected: `هو` = dhamir munfashil/mubtada' sederhana; `الأول` = khabar nominal sederhana pada target span.
- Critical misconception: hanya mengenali pronoun tanpa memindahkan operasi predikasi ke contoh baru.
- Error: E04/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L04-P23 — Transfer K12 with overt nominal complement
- Target: K12
- Prerequisite: K04/K08/K09
- Reference: QS 39:3
- Target span: `لِلَّهِ الدِّينُ`
- Response class: transfer/relation
- Prompt: identifikasi jar-majrur predikatif depan dan unsur nominal sesudahnya pada span minimal.
- Expected: `لله` = jar-majrur predikatif depan; `الدين` = unsur nominal sesudahnya.
- Critical misconception: menolak fungsi predikatif hanya karena jar-majrur berada di depan.
- Error: E04/E06
- Feature ceiling: kelanjutan `الخالص` tidak termasuk target span.
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L04-P24 — Prerequisite integrity K10
- Target: K10
- Prerequisite: K01/K06
- Reference: QS 7:128
- Target span: `قَالَ مُوسَىٰ`
- Response class: prerequisite/relation
- Prompt: identifikasi fi'il dan fa'il zhahir.
- Expected: `قال` = fi'il madhi; `موسى` = fa'il zhahir.
- Critical misconception: mengenali fi'il tetapi gagal menautkan isim zhahir sebagai fa'il.
- Error: E04/E05
- Ambiguity: LOW
- Status: PILOT

### L04-P25 — Transfer K09
- Target: K09
- Prerequisite: K01/K04
- Reference: QS 2:11
- Target span: `فِي الْأَرْضِ`
- Response class: transfer/relation-lite
- Prompt: identifikasi huruf jar dan isim zhahir sesudahnya pada contoh baru.
- Expected: `في` = huruf jar; `الأرض` = isim zhahir.
- Critical misconception: berhasil hanya pada `بـ`/`لـ` tetapi gagal mentransfer ke preposisi lain.
- Error: E05/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L04-P26 — Tense-form contrast
- Target: K06 versus K07
- Reference: QS 96:5
- Target span: `يَعْلَمْ`
- Response class: contrast/classification
- Prompt: apakah bentuk target termasuk fi'il madhi atau fi'il mudhari'?
- Expected: fi'il mudhari'.
- Critical misconception: mengklasifikasi tense berdasarkan terjemahan, bukan bentuk.
- Error: E02/E03
- Feature ceiling: status jazm pada akhir kata tidak diuji di L04.
- Ambiguity: LOW
- Status: PILOT CONTRAST

### L04-P27 — Transfer K06
- Target: K06
- Reference: QS 96:2
- Target span: `خَلَقَ`
- Response class: transfer/classification
- Prompt: klasifikasikan bentuk verbal pada contoh baru.
- Expected: fi'il madhi.
- Critical misconception: hanya mengenali satu bentuk madhi yang pernah dihafal.
- Error: E02/E06
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L04-P28 — Transfer K07
- Target: K07
- Reference: QS 96:5
- Target span: `يَعْلَمْ`
- Response class: transfer/classification
- Prompt: klasifikasikan bentuk verbal target tanpa menjelaskan i'rab akhirnya.
- Expected: fi'il mudhari'.
- Critical misconception: gagal mentransfer recognition mudhari' ketika ending berbeda dari contoh dasar.
- Error: E02/E06
- Feature ceiling: jazm tidak dinilai.
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L04-P29 — Integrative form recognition
- Target: K01/K02/K04
- Reference: QS 2:176
- Target span: `بِالْحَقِّ`
- Response class: integration
- Prompt: segmentasikan marker awal dan identifikasi kategori nominal serta definite marker pada target.
- Expected: `بـ` = huruf jar; `الحق` = isim dengan `الـ`.
- Critical misconception: membaca keseluruhan token sebagai satu unit tanpa segmentasi minimal.
- Error: E02/E05
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE

### L04-P30 — Integrative K06 + K10 with ceiling control
- Target: K06/K10
- Prerequisite: K01
- Reference: QS 27:16
- Target span: `وَوَرِثَ سُلَيْمَانُ`
- Response class: integration/relation
- Prompt: identifikasi fi'il madhi dan fa'il zhahir pada span minimal.
- Expected: `ورث` = fi'il madhi; `سليمان` = fa'il zhahir.
- Critical misconception: gagal mempertahankan relasi fi'il–fa'il ketika ada marker koordinatif di awal.
- Error: E04/E05
- Feature ceiling: kelanjutan objek `داود` dikeluarkan dari target span; fungsi `و` tidak dinilai.
- Ambiguity: LOW
- Status: PILOT INTEGRATIVE WITH CEILING NOTE

## 4. Distribution audit after P30

Current pool size: **30 items / target 36 = 83.33%**.

Working distribution (primary tag):
- direct/recognition/classification: P01, P02, P07, P08, P09, P10, P11, P12, P13 = 9
- negative/contrast controls: P03, P15, P19, P20, P21, P26 = 6
- prerequisite-integrity/relation: P04, P14, P16, P17, P24 = 5
- transfer: P05, P18, P22, P23, P25, P27, P28 = 7
- integrative: P06, P29, P30 = 3

Coverage note:
- K01–K12 sudah seluruhnya memiliki minimal satu item.
- K08–K12 sekarang mempunyai lebih dari satu environment untuk beberapa target penting, terutama K09–K12.
- Negative/contrast quota minimum 6 sudah terpenuhi.
- Transfer quota minimum 6 sudah terpenuhi.
- Direct quota target 12 masih kurang 3 jika kategori dipertahankan secara ketat.
- Integrative quota target 6 masih kurang 3.
- Prerequisite quota target 6 masih kurang 1.

Therefore P31–P36 harus diarahkan untuk balancing, bukan sekadar menambah jumlah:
1. 3 integrative items;
2. 1 prerequisite-integrity item;
3. 2 direct items atau recoding setelah audit final agar distribusi operasional mendekati target 12/6/6/6/6 tanpa double-counting yang menyesatkan.

## 5. Provisional routing rule

Checkpoint L04 tidak dinyatakan mastered hanya dari total skor mentah.

Working gate:
- minimum 5/6 core item benar;
- prerequisite-integrity item harus benar;
- transfer item harus benar;
- tidak ada critical misconception yang menunjukkan fondasi recognition belum stabil.

Jika 4/6 atau prerequisite/transfer gagal, sistem membuka diagnostic probe lokal sebelum menentukan placement.

## 6. Quality controls

1. Translation-only answer tidak cukup bila prompt meminta linguistic recognition.
2. Item tidak boleh membutuhkan K di atas checkpoint untuk memperoleh jawaban benar.
3. Kehadiran fitur lebih tinggi pada ayat harus di-lock/ignore secara eksplisit atau item dipindah ke REVIEW.
4. Satu ayat tidak boleh menjadi satu-satunya bukti mastery.
5. Retest memakai verse/span berbeda dengan operasi target yang sama.
6. Semua item sebelum production harus melalui Arabic-content review dan item-quality review.
7. Negative control harus memiliki alasan linguistik eksplisit, bukan sekadar jawaban 'bukan'.
8. Item integratif tidak boleh menyisipkan operasi baru di atas K12 hanya karena ayat aslinya lebih kompleks.
9. Surface feature di atas ceiling boleh hadir hanya jika target span dan scoring membuatnya benar-benar tidak diperlukan.
10. Setiap item MEDIUM ambiguity harus masuk targeted content review sebelum dipakai untuk auto-scoring.

## 7. Expansion target

Pool L04 minimum sebelum pilot operasional:
- 12 direct items
- 6 negative/contrast controls
- 6 prerequisite-integrity items
- 6 transfer items
- 6 integrative items

Total target: **36 items**.

Batch berikutnya: L04-P31–P36 untuk balancing final + PREMATURE audit seluruh 36 item, lalu quality-review decision sebelum membuka pool L10.

## 8. Governance note

Dokumen ini berada di research layer PR #4 dan tidak mengubah registry produksi QURBATA. Promotion ke assessment production membutuhkan freeze terpisah setelah content review, psychometric/pilot review, dan mapping RIQA OS.