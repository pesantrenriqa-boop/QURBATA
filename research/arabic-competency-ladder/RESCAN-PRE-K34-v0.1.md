# Rescan Before K34 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K33 DRAFT-FROZEN.

## Purpose

Menguji apakah `كان` dan `ليس` memang node recognition paling ringan berikutnya, atau masih ada unsur Qurani frekuen dengan dependency lebih pendek yang seharusnya mendahului keduanya.

## Candidates audited

### A. `كَانَ` recognition

Target hanya mengenali lemma/family `كان` sebagai verba khusus yang kelak memodifikasi jumlah ismiyyah. Efek `اسم كان / خبر كان` dikunci.

Strength:
- verb recognition sudah tersedia;
- sangat frekuen dalam Al-Qur'an.

Burden:
- bentuk infleksi banyak (`كان`, `كانوا`, `كنت`, `كنا`, `يكون`, dll.);
- jika target terlalu luas, recognition berubah menjadi paradigm competence;
- semantic/copular use tidak selalu identik secara sederhana.

Judgement: **HIGH but needs family-boundary discipline.**

### B. `لَيْسَ` recognition

Target recognition `ليس` dan bentuk terinfleksi yang occurrence-specific, tanpa membuka isim/khabarnya.

Strength:
- fungsi negatif relatif khas;
- family lebih terbatas daripada `كان`.

Burden:
- tetap membawa agreement/person suffixes;
- secara pedagogis berkaitan dengan nominal predication.

Judgement: **HIGH.**

### C. `إِلَّا` recognition

Target mengenali `إلا` sebagai marker istitsna' pada occurrence yang tervalidasi, tanpa menganalisis jenis istitsna' atau i'rab mustatsna.

Strength:
- token lokal dan invariant;
- dependency recognition sangat rendah;
- frekuen dan pedagogically salient.

Burden:
- fungsi dalam struktur hasr/negation + exception dapat kompleks;
- full construction harus dikunci.

Judgement: **VERY HIGH AS RECOGNITION.**

### D. `إِنْ` conditional recognition

Target recognition marker syarth pada occurrence yang tervalidasi.

Strength: token lokal.

Burden:
- homography/function ambiguity with other `إن` uses;
- jawab syarth, jazm, and clause linkage are higher competencies.

Judgement: **HIGH but ambiguity-sensitive.**

### E. `لَوْ` recognition

Target recognition conditional/counterfactual marker on occurrence.

Strength: invariant token, local.

Burden: semantic relation between protasis/apodosis is higher.

Judgement: **HIGH.**

## Main finding

`كان` dan `ليس` **tidak seharusnya langsung menjadi K34/K35**. `إلا` memiliki dependency recognition yang lebih ringan dan lebih atomik.

Conditional particles are also light, but their clause-linking semantics and ambiguity make them less clean than `إلا`.

## Revised frontier hypothesis

- **K34-CAND — recognition `إِلَّا`**
- **K35-CAND — recognition `لَيْسَ`**
- **K36-CAND — recognition family `كَانَ` dengan scope terbatas**
- **K37-CAND — recognition `لَوْ`**
- **K38-CAND — recognition conditional `إِنْ` occurrence-specific**

This is not frozen. K35 vs K36 requires evidence; `ليس` tentatively precedes `كان` because its recognition family is narrower.

## Locked effects

- K34 does not unlock istitsna' types/i'rab/hasr analysis.
- K35 does not unlock اسم ليس / خبر ليس.
- K36 does not unlock اسم كان / خبر كان or full conjugational paradigm.
- K37/K38 do not unlock جواب الشرط or governing effects.

## Next

1. evidence + head-to-head `إلا` vs `ليس`;
2. define exact family scope for `كان` recognition;
3. compare `ليس` vs limited `كان` family;
4. keep fa'il mustatir and silah maushul later until lightweight recognition frontier is exhausted.