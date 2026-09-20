# Head-to-Head K21–K23 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent:** `FRONTIER-K21-PLUS-v0.1.md`

## 1. K21 — Dhamir Muttashil sebagai Maf'ul Bih

### Formula

`فعل + ضمير متصل` dengan fungsi suffix sebagai objek langsung.

### Dependency

- K6/K7: recognition fi'il;
- K14: maf'ul bih sebagai fungsi;
- K15: recognition dhamir muttashil.

### Evidence pattern

Target evidence harus membuktikan tiga hal sekaligus:

1. host memang fi'il;
2. suffix memang dhamir muttashil;
3. fungsi suffix adalah maf'ul bih, bukan fa'il, bukan mudhaf ilaih, dan bukan objek preposisi.

### Clean candidates — pola kerja

- `خَلَقَهُ`
- `هَدَاهُ`
- `آتَاهُ`
- `رَزَقَهُ`
- `عَلَّمَهُ`

Setiap kandidat tetap wajib diverifikasi berdasarkan occurrence Qurani spesifik, karena bentuk surface yang sama dapat berada dalam konteks berbeda.

### Premature blockers

- suffix fa'il;
- dua objek;
- object clause;
- passive;
- clitic tambahan yang belum diizinkan;
- embedded coordination/subordination yang diperlukan untuk memahami target.

### Judgement

**VERY HIGH INTEGRATION VALUE.** K21 adalah integrasi langsung K14 + K15 dan tidak memerlukan kategori baru.

---

## 2. K22 Candidate A — Jar–Majrur sebagai Pelengkap Fi'il

### Formula

`فعل ... جار ومجرور` dengan attachment ke verba sederhana.

### Dependency

- K10: verbal relation dasar;
- K9/K20: jar–majrur;
- attachment relation baru antara verba dan PP.

### Strength

- sangat produktif di Al-Qur'an;
- mengintegrasikan dua struktur yang sudah dikenal;
- membuka adverbial/complement expansion pada jumlah fi'liyyah.

### Burden

- PP bisa attach ke verb, noun, adjective, atau clause level;
- surface adjacency tidak cukup untuk memastikan attachment;
- dapat muncul bersama maf'ul, dhamir, atau clause material lain.

### Judgement

**HIGH**, tetapi memerlukan dependency parsing lebih kuat daripada token-recognition.

---

## 3. K23 Candidate B — Recognition Isim Isyarah

### Formula

Mengenali token demonstratif seperti `هَذَا`, `هَذِهِ`, `هَؤُلَاءِ`, `ذَلِكَ`, `تِلْكَ` pada occurrence Qurani.

### Dependency

Recognition-level dependency sangat rendah. Tidak perlu mengajarkan fungsi mubtada', na'at, badal, atau demonstrative phrase sekaligus.

### Strength

- target satu token;
- locality maksimal;
- tidak memerlukan attachment inference;
- sangat mudah dipisahkan dari construction-level competence berikutnya.

### Burden

- paradigma gender/number/distance;
- sebagian bentuk terintegrasi dengan `ل`/`ك` historis atau deictic elements, tetapi untuk tahap recognition cukup diperlakukan sebagai lexicalized demonstrative form;
- penggunaan sintaksis ditahan untuk K sesudahnya.

### Judgement

**VERY HIGH AS REC.** Secara dependency dan clean-yield potensial, lebih ringan daripada verbal PP attachment.

---

## 4. Head-to-Head Result: K22 vs K23

| Criterion | Verb + PP attachment | Isim Isyarah recognition |
|---|---|---|
| Dependency depth | lebih tinggi | sangat rendah |
| Unit locality | sedang | sangat tinggi |
| Hidden relation | ada | hampir tidak ada |
| Parsing burden | tinggi | rendah |
| Clean filtering | lebih sulit | lebih mudah |
| Expansion value | sangat tinggi | tinggi |

**Winner for earlier sequence: Isim Isyarah recognition.**

## 5. Revised Candidate Order

- **K21-CAND** — dhamir muttashil sebagai maf'ul bih
- **K22-CAND** — recognition isim isyarah
- **K23-CAND** — jar–majrur sebagai pelengkap fi'il sederhana
- **K24-CAND** — recognition isim maushul
- **K25-CAND** — fa'il mustatir dasar

## 6. Why K22 Moves Up

Tangga pembelajaran tidak hanya mengikuti expansion dari struktur sebelumnya; recognition competence yang dependency-nya lebih rendah boleh menyela relation competence yang lebih berat.

Ini konsisten dengan pola sebelumnya:
- K15 recognition attached pronoun muncul sebelum fungsi-fungsi suffix tertentu;
- K16 recognition conjunction muncul sebelum 'athaf construction.

Maka recognition isim isyarah wajar berada sebelum verbal PP attachment bila clean evidence mendukung.

## 7. K21 Evidence Expansion Rule

Evidence bank K21 harus dipisahkan berdasarkan host tense:

- past verb + object suffix;
- imperfect verb + object suffix;
- imperative + object suffix hanya setelah imperative sendiri menjadi kompetensi yang diizinkan; sampai saat itu PREMATURE.

Metadata minimal:

- surah:ayah;
- token location;
- surface form;
- verb lemma;
- tense/aspect;
- pronoun form;
- syntactic function = object;
- other dependencies;
- status PASS/PREMATURE/REVIEW.

## 8. Freeze Assessment

- K21: **READY FOR EVIDENCE-GATED FREEZE**, belum final sebelum evidence integrity check occurrence-specific.
- K22: **STRONG CANDIDATE**.
- K23: **STRONG BUT HIGHER PARSING BURDEN**.

## 9. Next

1. build occurrence-specific evidence bank K21;
2. build recognition evidence bank K22;
3. compare K23 vs K24 (relative pronoun recognition) karena K24 juga recognition-level;
4. jangan freeze K23 sebelum dibandingkan dengan K24;
5. pertahankan fa'il mustatir di belakang sampai seluruh recognition frontier ringan selesai diaudit.