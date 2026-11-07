# Evidence Bank K01–K10 v0.1

**Status:** WORKING EVIDENCE — RESEARCH LAYER ONLY  
**Tujuan:** menempelkan bukti Qurani awal ke kandidat K1–K10 dan menandai `PASS / REVIEW / PREMATURE` sesuai cumulative-only rule.  
**Catatan:** bank ini belum lengkap dan tidak dibatasi jumlah contoh; semua kandidat valid akan terus ditambahkan.

## Aturan Evidence

- unit boleh berupa token, frasa, atau klausa contiguous;
- target relation harus tetap utuh setelah ekstraksi;
- contoh `Kn` hanya boleh membutuhkan kompetensi pada `K1..Kn`;
- unsur morfologis tambahan yang belum dipelajari membuat kandidat `PREMATURE`;
- contoh yang analisisnya belum diverifikasi penuh diberi `REVIEW`;
- ayat penuh tetap disimpan sebagai provenance walaupun unit pembelajaran hanya potongan.

---

## K1 — Mengenali Isim Sederhana

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 112:2 | `اللَّهُ` | PASS | proper noun / nominal token |
| 112:2 | `الصَّمَدُ` | PASS | noun token |
| 2:11 | `الْأَرْضِ` | PASS | noun token; fungsi sintaksis belum dibahas di K1 |
| 10:77 | `مُوسَىٰ` | PASS | proper noun |
| 10:79 | `فِرْعَوْنُ` | PASS | proper noun |

**Gate:** STRONG.

---

## K2 — Mengenali `الـ` pada Isim

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 112:2 | `الصَّمَدُ` | PASS | `الـ` + noun |
| 2:11 | `الْأَرْضِ` | PASS | `الـ` + noun |
| 3:196 | `الْبِلَادِ` | PASS | `الـ` + noun |
| 17:67 | `الْبَرِّ` | PASS | `الـ` + noun |
| 18:94 | `الْأَرْضِ` | PASS | pengulangan diperbolehkan di corpus bank; bukan item baru secara leksikal |

**Gate:** STRONG.

---

## K3 — Mengenali Nakirah/Tanwin Sederhana

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 2:263 | `قَوْلٌ` | PASS | noun bertanwin |
| 2:263 | `مَغْفِرَةٌ` | PASS | noun bertanwin |
| 3:39 | `بِكَلِمَةٍ` | REVIEW | token membawa preposisi `بِـ`; untuk K3 murni perlu segment-level display `كَلِمَةٍ` |
| 3:64 | `كَلِمَةٍ` | PASS | noun bertanwin dalam unit nominal |
| 35:40 | `شِرْكٌ` | PASS | noun bertanwin |

**Gate:** STRONG, dengan aturan segment extraction.

---

## K4 — Mengenali Huruf Jar Frekuen

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 2:11 | `فِي` | PASS | preposition recognition |
| 5:33 | `مِنْ` | PASS | preposition recognition |
| 17:67 | `إِلَى` | PASS | preposition recognition |
| 28:39 | `فِي` | PASS | recognition only |
| 35:40 | `عَلَىٰ` | PASS | recognition only |

**Gate:** STRONG.

---

## K5 — Mengenali Dhamir Munfashil Dasar

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 2:29 | `هُوَ` | PASS | independent pronoun |
| 10:68 | `هُوَ` | PASS | independent pronoun |
| 28:39 | `هُوَ` | PASS | independent pronoun |
| 35:15 | `أَنْتُمُ` | PASS | independent pronoun; paradigma plural belum dianalisis penuh |
| 23:29 | `أَنْتَ` | PASS | independent pronoun |

**Gate:** COMPETENCY STRONG; **sequence position remains REVIEW**.

---

## K6 — Mengenali Fi‘il Madhi Sederhana

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 10:77 | `قَالَ` | PASS | perfect verb, 3ms, tanpa suffix objek |
| 10:81 | `قَالَ` | PASS | bentuk sama, konteks berbeda |
| 10:89 | `قَالَ` | PASS | clean recognition token |
| 10:82 | `كَرِهَ` | PASS | perfect verb, 3ms |
| 10:83 | `آمَنَ` | PASS | perfect verb, 3ms |

**Gate:** STRONG.

---

## K7 — Mengenali Fi‘il Mudhari‘ Sederhana

Tipe: `REC`

| Ref | Unit | Status | Catatan |
|---|---|---|---|
| 10:81 | `يُصْلِحُ` | PASS | imperfect verb, 3ms |
| 10:82 | `يُحِقُّ` | PASS | imperfect verb, 3ms |
| 10:68 | `تَعْلَمُونَ` | PREMATURE | membawa wawu jama‘ah; ditahan sampai suffix/person-number competence |
| 22:46 | `يَعْقِلُونَ` | PREMATURE | wawu jama‘ah |
| 27:48 | `يُفْسِدُونَ` | PREMATURE | wawu jama‘ah |

**Temuan:** K7 valid, tetapi clean bank harus memprioritaskan bentuk mudhari‘ 3ms/3fs tanpa suffix kompleks.

**Gate:** STRONG WITH EVIDENCE-EXPANSION FLAG.

---

## K8 — Jumlah Ismiyyah Core: Mubtada’ + Khabar Isim Zhahir

Tipe: `REL`

| Ref | Unit | Status | Required-K | Catatan |
|---|---|---|---|---|
| 112:2 | `اللَّهُ الصَّمَدُ` | PASS-ANCHOR | K1,K2,K8 | Quranic Arabic Corpus menganalisis eksplisit sebagai `مبتدأ وخبر` |
| 4:128 | `الصُّلْحُ خَيْرٌ` | PASS | K1,K2,K3,K8 | predikasi nominal sederhana |
| 64:6 | `اللَّهُ غَنِيٌّ` | REVIEW-PASS | K1,K3,K8 | diekstrak dari klausa lebih panjang; aturan minimal-unit harus dipertahankan |
| 47:38 | `اللَّهُ الْغَنِيُّ` | REVIEW | K1,K2,K8 | perlu verifikasi dependency final |
| 35:15 | `أَنْتُمُ الْفُقَرَاءُ` | PREMATURE-K8-CORE | K5 + K8 | ditahan dari core karena memakai dhamir sebagai mubtada’ |

**Gate:** VERY STRONG.

---

## K9 — Fi‘il + Fa‘il Isim Zhahir Sederhana

Tipe: `REL`

| Ref | Unit | Status | Required-K | Catatan |
|---|---|---|---|---|
| 10:77 | `قَالَ مُوسَىٰ` | PASS-ANCHOR | K1,K6,K9 | perfect verb + explicit proper-noun subject |
| 10:79 | `قَالَ ... فِرْعَوْنُ` | REVIEW | K1,K6,K9 | surface order/intervening structure perlu dicek untuk unit extraction; jangan dipakai sebagai teaching core sebelum verifikasi |
| 10:80 | `جَاءَ السَّحَرَةُ` | PASS | K1,K2,K6,K9 | perfect verb + explicit plural noun subject; plural morphology belum dianalisis sebagai target |
| 10:82 | `يُحِقُّ اللَّهُ` | PASS | K1,K7,K9 | imperfect verb + explicit subject |
| 10:83 | `آمَنَ ... ذُرِّيَّةٌ` | REVIEW | K1,K3,K6,K9 | terdapat unsur intervening; perlu standar unit extraction |

**Gate:** STRUCTURALLY STRONG; evidence bank masih perlu diperbesar dengan pasangan contiguous yang benar-benar clean.

---

## K10 — Huruf Jar + Isim Zhahir sebagai Jar–Majrur

Tipe: `REL`

| Ref | Unit | Status | Required-K | Catatan |
|---|---|---|---|---|
| 2:11 | `فِي الْأَرْضِ` | PASS-ANCHOR | K1,K2,K4,K10 | preposition + explicit noun |
| 3:196 | `فِي الْبِلَادِ` | PASS | K1,K2,K4,K10 | clean local phrase |
| 5:33 | `مِنَ الْأَرْضِ` | PASS | K1,K2,K4,K10 | clean local phrase |
| 17:67 | `إِلَى الْبَرِّ` | PASS | K1,K2,K4,K10 | clean local phrase |
| 18:94 | `فِي الْأَرْضِ` | PASS | K1,K2,K4,K10 | repeated pattern, separate Qur'anic occurrence |
| 35:40 | `فِي السَّمَاوَاتِ` | PASS | K1,K2,K4,K10 | plural noun as object of preposition; plural morphology not target |
| 35:40 | `مِنَ الْأَرْضِ` | PASS | K1,K2,K4,K10 | second clean occurrence |
| 14:13 | `مِنْ أَرْضِنَا` | PREMATURE | K4 + dhamir muttashil | possessive suffix not yet allowed |
| 20:63 | `مِنْ أَرْضِكُمْ` | PREMATURE | K4 + dhamir muttashil | suffix pronoun blocks K10-core |

**Gate:** VERY STRONG.

---

## Cross-K Findings v0.1

1. **K8 dan K10 mempunyai anchor clean yang sangat kuat.**
2. **K9 valid secara dependency**, tetapi memerlukan pencarian lebih ketat untuk pasangan fi‘il–fa‘il yang contiguous dan bebas unsur intervening.
3. **K7 mudhari‘** perlu diperluas dengan bentuk 3ms/3fs sederhana karena banyak kemunculan Qurani membawa suffix plural.
4. **K5** valid sebagai recognition competence, tetapi posisinya dalam sequence belum sepenuhnya ditentukan oleh hard dependency.
5. Segment-level filtering wajib: bentuk seperti `بِكَلِمَةٍ`, `وَلِلَّهِ`, atau preposisi + pronominal suffix tidak boleh otomatis diperlakukan sebagai contoh murni untuk K yang lebih rendah.

## Freeze Gate Status

| K | Status |
|---|---|
| K1 | PASS-STRUCTURAL |
| K2 | PASS-STRUCTURAL |
| K3 | PASS-STRUCTURAL |
| K4 | PASS-STRUCTURAL |
| K5 | PASS-COMPETENCY / POSITION-REVIEW |
| K6 | PASS-STRUCTURAL |
| K7 | PASS-STRUCTURAL / EXPAND-EVIDENCE |
| K8 | PASS-STRONG |
| K9 | PASS-DEPENDENCY / EXPAND-CLEAN-EVIDENCE |
| K10 | PASS-STRONG |

## Next Evidence Batch

1. perluas K7 dengan mudhari‘ sederhana tanpa suffix kompleks;
2. perluas K9 dengan minimal 20 kandidat fi‘il + fa‘il zhahir yang contiguous;
3. perluas K8 dan K10 ke puluhan PASS untuk membuktikan yield tinggi;
4. audit K5 sequence position menggunakan jumlah clean examples yang dibuka pada K8;
5. setelah evidence gate memadai, terbitkan `DRAFT-FROZEN-K01-K10-v1.0` di research layer.

## Sumber Verifikasi Linguistik

- Quranic Arabic Corpus: morphology, Quran search, syntactic treebank, dependency graphs, dan grammar pages.
- QS 112:2 grammar page digunakan sebagai anchor eksplisit untuk `مبتدأ وخبر`.
