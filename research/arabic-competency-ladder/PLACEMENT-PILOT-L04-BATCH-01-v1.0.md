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

## 4. Distribution audit after P18

Current pool size: **18 items / target 36 = 50%**.

Working distribution:
- direct/recognition-heavy: P01, P02, P07, P08, P09, P10, P11, P12, P13 = 9
- contrast/negative-control: P03, P15 = 2
- prerequisite-integrity/relation: P04, P14, P16, P17 = 4
- transfer: P05, P18 = 2
- integrative: P06, P17 = 2 (P17 double-tags integration + prerequisite)

Gap before 36-item completion:
- add more negative/contrast controls;
- add more transfer items from different surahs;
- reduce duplicate reliance on very short surahs;
- expand independent examples for K08–K12;
- perform content validation for any item carrying surface structure above ceiling.

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

## 7. Expansion target

Pool L04 minimum sebelum pilot operasional:
- 12 direct items
- 6 negative/contrast controls
- 6 prerequisite-integrity items
- 6 transfer items
- 6 integrative items

Total target: **36 items**.

Batch berikutnya: L04-P19–P30 dengan prioritas negative controls, transfer diversity, dan independent K08–K12 evidence; kemudian P31–P36 untuk balancing + final PREMATURE audit.

## 8. Governance note

Dokumen ini berada di research layer PR #4 dan tidak mengubah registry produksi QURBATA. Promotion ke assessment production membutuhkan freeze terpisah setelah content review, psychometric/pilot review, dan mapping RIQA OS.