# Placement Pilot L19 — Batch 02 v1.0

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Scope:** L19 P13–P24 expansion  
**Competency band:** K40–K57  
**Parent:** `PLACEMENT-PILOT-L19-BATCH-01-v1.0.md`

## 1. Tujuan

Melanjutkan L19 dari 12/36 menjadi 24/36 dengan independent coverage K51–K57, condition-result environment tambahan, nested relations, dan prerequisite-routing L14–L18. Seluruh item tetap dibatasi sampai K57; reasoning K58+ tidak boleh menjadi syarat jawaban benar.

## 2. Items P13–P24

### L19-P13 — K51 independent interclausal dependency
- Target: K51
- Prerequisite: K39/K41
- Reference: QS 2:286
- Target span: `إِن نَّسِينَا أَوْ أَخْطَأْنَا`
- Response class: interclausal boundary
- Prompt: identifikasi marker syarat dan dua unit verbal terkoordinasi di dalam domain syarat tanpa menebak jawab yang tidak ada pada span.
- Expected: `إن` membuka domain syarat; `نسينا` dan `أخطأنا` berada dalam domain tersebut dan terhubung dengan `أو`.
- Critical misconception: menganggap koordinasi internal sama dengan jawab syarat.
- Error: E05/E07/E08
- Ambiguity: MEDIUM
- Status: PILOT WITH CEILING NOTE

### L19-P14 — K52 explicit condition-result transfer
- Target: K52
- Prerequisite: K40/K41
- Reference: QS 3:160
- Target span: `إِن يَنصُرْكُمُ اللَّهُ فَلَا غَالِبَ لَكُمْ`
- Response class: relation/transfer
- Prompt: petakan protasis dan result clause yang ditandai eksplisit.
- Expected: `إن ينصركم الله` = protasis; `فلا غالب لكم` = result/jawab dengan `فـ` sebagai marker penghubung.
- Critical misconception: mengenali `إن` dan `فـ` terpisah tanpa relation mapping.
- Error: E05/E06/E08
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L19-P15 — K53 nested relative inside larger clause
- Target: K53
- Prerequisite: K36/K42
- Reference: QS 2:3
- Target span: `الَّذِينَ يُؤْمِنُونَ بِالْغَيْبِ وَيُقِيمُونَ الصَّلَاةَ`
- Response class: embedded integration
- Prompt: petakan relative head dan dua predikasi verbal di dalam silah tanpa keluar ke discourse relation.
- Expected: `الذين` membuka relative unit; dua predikasi verbal berada di dalam silah dan terkoordinasi.
- Critical misconception: salah satu predikasi dianggap berada di luar relative unit.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT INTEGRATIVE

### L19-P16 — K54 scope retention under fronting
- Target: K54
- Prerequisite: K33/K44
- Reference: QS 1:5
- Target span: `إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ`
- Response class: scope/integration
- Prompt: tunjukkan bahwa setiap objek depan tetap berelasi dengan verba lokalnya dan tidak mengambil scope atas kedua verba sekaligus.
- Expected: pasangan lokal `إياك↔نعبد` dan `إياك↔نستعين` dipertahankan; `و` hanya mengoordinasikan unit.
- Critical misconception: objek pertama dianggap shared-object untuk dua verba.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT

### L19-P17 — K55 negative control: apparent complexity without target dependency
- Target: K55
- Prerequisite: K49
- Reference: QS 112:1–4
- Target span: four short verses
- Response class: negative/contrast
- Prompt: apakah banyaknya ayat otomatis membentuk satu nested dependency K55?
- Expected: tidak; jumlah ayat/token bukan bukti nested dependency tertentu.
- Critical misconception: complexity-by-length.
- Error: E07/E08
- Ambiguity: LOW
- Status: PILOT NEGATIVE CONTROL

### L19-P18 — K56 prerequisite-routing probe
- Target: K56
- Prerequisite: K32/K33/K36/K43
- Reference: QS 107:1–3
- Target span: `الَّذِي يُكَذِّبُ بِالدِّينِ ... الَّذِي يَدُعُّ الْيَتِيمَ وَلَا يَحُضُّ عَلَىٰ طَعَامِ الْمِسْكِينِ`
- Response class: prerequisite/integration
- Prompt: petakan dua relative units, satu verb–object relation, dan satu koordinasi/negation unit tanpa memberi tafsir moral.
- Expected: relative units tetap lokal; `يدع`–`اليتيم` dipetakan; `ولا يحض` merupakan unit verbal terkoordinasi/terhubung pada frame lokal.
- Critical misconception: recognition benar tetapi dependency map runtuh saat unit bertambah.
- Error: E05/E08
- Ambiguity: HIGH
- Status: PILOT REVIEW

### L19-P19 — K57 cap of Stage 4 integration
- Target: K57
- Prerequisite: K40–K56 sampled
- Reference: QS 110:1–3
- Target span: full local structure
- Response class: integration/discrimination
- Prompt: bangun relation map lengkap terbatas pada syntax/domain: pembuka conditional, coordinated material, visual/perception clause, dan response unit.
- Expected: domain dan local relations konsisten; tidak perlu semantic/discourse interpretation K58+.
- Critical misconception: mengganti relation map dengan parafrasa makna.
- Error: E01/E05/E08
- Ambiguity: HIGH
- Status: PILOT INTEGRATIVE REVIEW

### L19-P20 — Alternative condition-result environment
- Target: K52/K57
- Prerequisite: K40/K41
- Reference: QS 4:59
- Target span: `فَإِن تَنَازَعْتُمْ فِي شَيْءٍ فَرُدُّوهُ إِلَى اللَّهِ`
- Response class: transfer/integration
- Prompt: identifikasi conditional unit dan response yang ditandai `فـ` tanpa menilai isi normatif ayat.
- Expected: `إن تنازعتم ...` = conditional unit; `فردوه ...` = response/result.
- Critical misconception: gagal mempertahankan relation karena ada prepositional material di dalam protasis.
- Error: E05/E06/E08
- Ambiguity: LOW
- Status: PILOT TRANSFER

### L19-P21 — Nested domain with coordination internal to protasis
- Target: K51/K53
- Prerequisite: K34/K40
- Reference: QS 3:160
- Target span: `وَإِن يَخْذُلْكُمْ فَمَن ذَا الَّذِي يَنصُرُكُم مِّن بَعْدِهِ`
- Response class: embedded/contrast
- Prompt: petakan conditional frame dan relative unit di dalam response tanpa masuk ke rhetorical interrogation.
- Expected: `إن يخذلكم` = conditional domain; response contains a demonstrative/interrogative frame with `الذي ينصركم` as relative unit.
- Critical misconception: relative unit dianggap keluar dari response domain.
- Error: E05/E08
- Ambiguity: HIGH
- Status: PILOT REVIEW

### L19-P22 — Negative control for K58+ leakage
- Target: K57 boundary
- Reference: QS 103:1–3
- Target span: full surah
- Response class: boundary/negative
- Prompt: apakah untuk lulus L19 peserta harus menjelaskan relasi semantik waktu, pengecualian, dan discourse purpose seluruh surah?
- Expected: tidak; L19 menilai structural integration sampai K57, bukan S5 semantic/discourse capstone.
- Critical misconception: mengira placement L19 identik dengan tafsir wacana.
- Error: E07/E08
- Ambiguity: LOW
- Status: PILOT BOUNDARY CONTROL

### L19-P23 — L14–L16 routing probe
- Target: K43/K44
- Prerequisite: K32/K33/K34
- Reference: QS 17:81
- Target span: `جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ`
- Response class: prerequisite routing
- Prompt: sebelum analisis integrasi, petakan dua subject relations dan marker koordinasi. Jika gagal di relasi lokal, jangan kredit integrasi.
- Expected: `الحق`↔`جاء`; `الباطل`↔`زهق`; `و` mengoordinasi unit.
- Critical misconception: relation map kompleks ditebak tanpa fondasi lokal.
- Error: E05/E08
- Ambiguity: LOW
- Status: PILOT ROUTING PROBE

### L19-P24 — L17–L18 routing probe
- Target: K46/K50
- Prerequisite: K35/K36/K37/K42
- Reference: QS 2:5
- Target span: `أُولَٰئِكَ عَلَىٰ هُدًى مِّن رَّبِّهِمْ وَأُولَٰئِكَ هُمُ الْمُفْلِحُونَ`
- Response class: prerequisite/integration
- Prompt: petakan dua frame demonstratif dan predikasi lokal masing-masing; jangan memberi discourse interpretation pengulangan.
- Expected: dua frame `أولئك ...` dibedakan; predikasi lokal masing-masing dipetakan; koordinasi antardua frame dikenali.
- Critical misconception: pengulangan `أولئك` diperlakukan sebagai satu frame saja.
- Error: E05/E08
- Ambiguity: MEDIUM
- Status: PILOT ROUTING INTEGRATION

## 3. Distribution audit after P24

Pool L19 cumulative: **24/36 = 66.67%**.

Coverage sekarang:
- K40–K50: tersedia dari Batch 01;
- K51–K57: seluruhnya sudah mendapat explicit independent or boundary coverage pada Batch 02;
- condition-result tidak lagi bergantung hanya pada QS 110; sudah ditambah QS 3:160 dan QS 4:59;
- nested/embedded coverage bertambah pada QS 2:3 dan QS 3:160;
- routing probes sekarang mulai membedakan gap L14–L16 versus L17–L18.

Functional balance:
- direct/integration: adequate;
- negative/boundary: P17/P22 plus Batch-01 P10;
- prerequisite-routing: P18/P23/P24;
- transfer: P14/P20/P21;
- high-ambiguity items explicitly flagged for Arabic-content review.

## 4. Remaining work P25–P36

1. add 3–4 final integrative discriminators with lower ambiguity where possible;
2. add more independent examples for K45–K50;
3. run full PREMATURE/K58+ leakage audit across all 36;
4. create six-item assembly simulation with >=4 primary K, >=1 prerequisite, >=1 negative, >=1 transfer, >=2 integration items;
5. mark any item that cannot be answered without K58+ as HOLD/PREMATURE.

## 5. Governance

Research layer only. No production freeze. This batch extends the parent L19 pool and does not alter canonical competency definitions.