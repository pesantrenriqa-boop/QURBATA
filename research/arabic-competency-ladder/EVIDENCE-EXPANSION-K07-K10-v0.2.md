# Evidence Expansion K07–K10 v0.2

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Scope:** memperbesar evidence bank untuk K7–K10 dan menilai kesiapan draft-freeze.  
**Sumber verifikasi utama:** Quranic Arabic Corpus morphology, syntax, dependency relations, and search results.

## 1. Prinsip Verifikasi

- `K7` adalah recognition fi'il mudhari' sederhana; unit satu token diperbolehkan selama token tidak membawa suffix/pronoun kompleks yang belum diajarkan.
- `K8` adalah jumlah ismiyyah core dengan mubtada' + khabar isim zhahir sederhana.
- `K9` adalah fi'il + fa'il isim zhahir; fa'il harus tampak eksplisit, bukan hanya dhamir mustatir atau suffix.
- `K10` adalah huruf jar + isim zhahir sebagai jar–majrur; bentuk preposition + pronoun ditahan.
- Semua candidate yang membawa kompetensi sesudah target tetap disimpan sebagai `PREMATURE` atau `REVIEW`, bukan dihapus.

## 2. Dasar Linguistik Corpus

Quranic Arabic Corpus menggunakan relasi:

- `pred` untuk mubtada'–khabar;
- `subj` untuk fa'il pada verba;
- `gen` untuk jar–majrur;
- `adj` untuk na'at;
- `poss` untuk idhafah.

Corpus juga menyatakan bahwa setiap verba aktif memiliki fa'il, eksplisit atau tersembunyi. Karena itu evidence K9 hanya memilih kasus dengan fa'il isim zhahir yang benar-benar muncul pada teks.

## 3. K7 — Fi'il Mudhari' Sederhana (Recognition)

### PASS / STRONG CANDIDATES

| Ref | Unit | Catatan | Status |
|---|---|---|---|
| 2:185 | `يُرِيدُ` | imperfect verb; tanpa suffix object pada token target | PASS |
| 5:49 | `يُرِيدُ` | imperfect verb; target token bersih | PASS |
| 8:70 | `يَعْلَمِ` | imperfect verb; bentuk surface dipengaruhi konteks tetapi tetap mudhari' | REVIEW-PASS |
| 29:45 | `يَعْلَمُ` | imperfect verb sederhana | PASS |
| 29:52 | `يَعْلَمُ` | imperfect verb sederhana | PASS |
| 29:60 | `يَرْزُقُ` | imperfect verb sederhana | PASS |
| 33:33 | `يُرِيدُ` | imperfect verb sederhana | PASS |
| 3:176 | `يُرِيدُ` | imperfect verb sederhana | PASS |

### PREMATURE / HOLD

| Ref | Unit | Konflik | Status |
|---|---|---|---|
| 7:181 | `يَهْدُونَ` | wawu jama'ah / subject pronoun suffix | PREMATURE |
| 9:6 | `يَعْلَمُونَ` | wawu jama'ah | PREMATURE |
| 8:60 | `يَعْلَمُهُمْ` | object pronoun suffix | PREMATURE |
| 78:1 | `يَتَسَاءَلُونَ` | wawu jama'ah + form VI | PREMATURE |

### K7 assessment

`CLEAN YIELD = HIGH` karena unit recognition dapat berupa satu token. K7 tidak lagi dianggap bottleneck utama untuk freeze.

## 4. K8 — Jumlah Ismiyyah Core

### PASS / ANCHOR

| Ref | Unit | Analisis | Status |
|---|---|---|---|
| 112:2 | `اللَّهُ الصَّمَدُ` | mubtada' + khabar isim zhahir | PASS-ANCHOR |
| 4:128 | `الصُّلْحُ خَيْرٌ` | nominal predication core | PASS |

### REVIEW / EXTRACTABLE

| Ref | Unit | Catatan | Status |
|---|---|---|---|
| 47:38 | `اللَّهُ الْغَنِيُّ` | sangat sederhana secara permukaan; dependency perlu final verification | REVIEW |
| 64:6 | `اللَّهُ غَنِيٌّ` | inti nominal sederhana di dalam klausa lebih panjang | REVIEW-PASS |

### PREMATURE

| Ref | Unit | Konflik | Status |
|---|---|---|---|
| 35:15 | `أَنْتُمُ الْفُقَرَاءُ` | mubtada' berupa dhamir | PREMATURE untuk K8 core |
| 35:15 | `اللَّهُ هُوَ الْغَنِيُّ الْحَمِيدُ` | dhamir + ekspansi nominal | PREMATURE |
| 87:17 | `الْآخِرَةُ خَيْرٌ وَأَبْقَى` | coordination + tafdhil tambahan | PREMATURE |

### K8 assessment

K8 tetap **VERY STRONG structurally**, tetapi teaching-set 20–30+ belum dibuktikan. Corpus bank harus terus diperbesar dengan pola mubtada' isim zhahir + khabar isim zhahir tanpa ekspansi lain.

## 5. K9 — Fi'il + Fa'il Isim Zhahir

### PASS / STRONG CANDIDATES

| Ref | Unit | Analisis | Status |
|---|---|---|---|
| 17:81 | `جَاءَ الْحَقُّ` | fi'il madhi + fa'il isim zhahir | PASS |
| 17:81 | `زَهَقَ الْبَاطِلُ` | fi'il madhi + fa'il isim zhahir | PASS |
| 2:185 | `يُرِيدُ اللَّهُ` | fi'il mudhari' + fa'il isim zhahir | PASS |
| 5:49 | `يُرِيدُ اللَّهُ` | fi'il mudhari' + fa'il isim zhahir | PASS |
| 3:176 | `يُرِيدُ اللَّهُ` | fi'il mudhari' + fa'il isim zhahir | PASS |
| 33:33 | `يُرِيدُ اللَّهُ` | fi'il mudhari' + fa'il isim zhahir | PASS |
| 29:60 | `يَرْزُقُهَا` + `اللَّهُ` | object suffix pada verba membuat unit tidak bersih untuk K9 core | PREMATURE |
| 3:142 | `يَعْلَمِ اللَّهُ` | mudhari' + fa'il zhahir; konteks jussive/subordinate membuatnya bukan contoh core awal | REVIEW |
| 8:70 | `يَعْلَمِ اللَّهُ` | conditional context; target relation valid tetapi clause environment lebih tinggi | REVIEW |

### HOLD / PREMATURE

| Ref | Unit | Konflik | Status |
|---|---|---|---|
| 95:4 | `خَلَقْنَا` | fa'il berupa suffix pronoun `نا`, bukan isim zhahir | PREMATURE |
| 5:117 | `قُلْتُ` | fa'il suffix `ت` | PREMATURE |
| 8:66 | `عَلِمَ` | subject implicit / context not clean two-unit target | HOLD |
| 7:181 | `يَهْدُونَ` | fa'il encoded in wawu jama'ah | PREMATURE |

### K9 assessment

K9 dependency valid dan memiliki clean anchors yang nyata. Namun strict policy `fa'il isim zhahir` mengurangi yield. **Status: DRAFT-FREEZE POSSIBLE WITH EVIDENCE-EXPANSION FLAG.**

## 6. K10 — Jar–Majrur dengan Isim Zhahir

### PASS / STRONG CANDIDATES

| Ref | Unit | Analisis | Status |
|---|---|---|---|
| 59:1 | `فِي السَّمَاوَاتِ` | preposition + genitive noun | PASS |
| 59:1 | `فِي الْأَرْضِ` | preposition + genitive noun | PASS |
| 78:2 | `عَنِ النَّبَإِ` | preposition + genitive noun | PASS |
| 1:1 | `بِاسْمِ` | prefixed preposition + genitive noun; morphological segmentation required | REVIEW-PASS |
| 95:4 | `فِي أَحْسَنِ` | target PP contains genitive nominal but immediately enters idhafah `أحسن تقويم`; not core-clean if whole unit needed | PREMATURE |
| 7:181 | `بِالْحَقِّ` | prefixed preposition + genitive noun | PASS |

### PREMATURE / HOLD

| Ref | Unit | Konflik | Status |
|---|---|---|---|
| 5:117 | `لَهُمْ` | preposition + pronoun suffix | PREMATURE |
| 5:117 | `بِهِ` | preposition + pronoun suffix | PREMATURE |
| 100:5 | `بِهِ` | preposition + pronoun suffix | PREMATURE |
| 78:1 | `عَمَّ` | preposition + interrogative noun / fused structure | PREMATURE |

### K10 assessment

K10 tetap frontier relasional paling kuat. Quranic Arabic Corpus mendefinisikan PP sebagai preposition + genitive nominal dan menandai relasi ini secara eksplisit. `CLEAN YIELD = VERY HIGH` setelah filter pronoun/clitic diterapkan.

## 7. Updated Freeze Readiness

| K | Readiness | Catatan |
|---|---|---|
| K7 | READY-STRUCTURAL | clean recognition yield tinggi |
| K8 | READY-STRUCTURAL / EVIDENCE EXPAND | anchor sangat kuat, bank masih perlu diperbesar |
| K9 | READY-WITH-FLAG | strict explicit-fa'il filter menurunkan yield |
| K10 | READY-STRUCTURAL | dependency dan clean yield sangat kuat |

## 8. Temuan Baru

### 8.1 Recognition dan relation harus tetap dipisah

K7 dapat mempunyai sangat banyak evidence karena satu token cukup. K9 jauh lebih ketat karena harus mempertahankan relasi verba–fa'il sekaligus bebas dari object suffix dan struktur tinggi. Ini membenarkan pemisahan `REC` dan `REL` sebagai kelas kompetensi.

### 8.2 K9 tidak boleh disederhanakan menjadi “semua jumlah fi'liyyah”

Jika K9 diberi nama terlalu luas, banyak contoh otomatis membawa:

- fa'il dhamir mustatir;
- suffix subject;
- maf'ul bih;
- particle environment;
- subordinate clause;
- coordination.

Karena itu K9 core tetap dibatasi ke **fi'il + fa'il isim zhahir sederhana**.

### 8.3 K10 lebih stabil daripada K9 sebagai construction-K awal

Secara clean-example yield, `حرف جر + اسم ظاهر` lebih mudah dikontrol daripada `فعل + فاعل ظاهر`. Ini menjadi alasan kuat mempertimbangkan apakah K10 seharusnya dipindah sebelum K9 pada linearization final.

## 9. Candidate Reordering Question

Dua opsi kini perlu diuji:

### Option A — current

`K8 jumlah ismiyyah → K9 fi'il+fa'il → K10 jar–majrur`

### Option B — yield-first

`K8 jumlah ismiyyah → K9 jar–majrur → K10 fi'il+fa'il`

Karena jar–majrur mempunyai dependency lebih ringan dan clean yield lebih tinggi, **Option B kini menjadi challenger serius**.

## 10. Next Batch

1. lakukan head-to-head test `REL-VS` vs `REL-PP`;
2. ukur hard dependency, clean-yield, prematurity rate, dan reuse potential;
3. jika PP menang jelas, revisi K9/K10 sebelum freeze;
4. perluas evidence K8 sampai pola nominal core cukup representatif;
5. setelah itu terbitkan `DRAFT-FROZEN-K01-K10-v1.0` bila tidak ada counterexample besar baru.
