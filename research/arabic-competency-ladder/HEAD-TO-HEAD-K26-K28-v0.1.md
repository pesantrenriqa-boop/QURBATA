# Head-to-Head K26–K28 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent:** `RECOGNITION-RESCAN-PRE-K26-v0.1.md`

## Candidates

- A — recognition fi'il amr sederhana
- B — recognition partikel nafi dasar
- C — recognition penanda istifham atomik

## A. Fi'il Amr Recognition

Target hanya mengenali imperative pada occurrence Qurani yang tervalidasi.

Dependencies:
- verbal recognition sudah ada K6/K7;
- tidak perlu relation baru bila fungsi subject tetap locked.

Strengths:
- kategori verbal baru yang penting;
- banyak occurrence pendek dan jelas;
- membuka command clauses berikutnya.

Burden:
- bentuk imperative sering membawa person/number morphology;
- jangan mengajarkan fa'il mustatir atau attached subject sekaligus;
- imperative irregular/weak forms dapat ditunda.

**Judgement:** VERY HIGH.

## B. Basic Negation Recognition

Tidak dibuat sebagai satu competence besar “nafi”. Kandidat harus function-tagged.

Core recognition candidates:
- `لا` pada occurrence nafi yang jelas;
- `ما` pada occurrence nafi yang jelas;
- `لم` sebagai negative/jussive particle recognition;
- `لن` sebagai negative/subjunctive particle recognition.

Pada tahap recognition, governing effect belum dibuka.

Strengths:
- token-level;
- frequency tinggi;
- sangat produktif untuk struktur berikutnya.

Burden:
- polyfunctionality `لا` dan `ما`;
- `لم`/`لن` terkait governing effect yang harus dikunci;
- occurrence tagging wajib.

**Judgement:** VERY HIGH, tetapi membutuhkan metadata ambiguity/function lebih ketat daripada imperative.

## C. Interrogative Recognition — Atomicity Audit

Satu kompetensi “istifham” terlalu luas. Frontier dipecah:

### C1 — `هَلْ` recognition

- particle recognition sederhana;
- dependency sangat rendah;
- fungsi cukup spesifik.

### C2 — hamzah istifham recognition

- sering terikat sebagai prefiks pada token berikutnya;
- segmentation burden lebih tinggi daripada `هل`.

### C3 — interrogative nominals/adverbials

`مَنْ`, `مَا`, `أَيْنَ`, `كَيْفَ`, `مَتَى` dll. tidak disatukan karena POS dan fungsi sintaksis berbeda.

**Judgement:** `هل` sangat ringan, tetapi terlalu sempit jika berdiri sendiri tanpa justification pedagogis. Hamzah lebih rumit secara segmentation.

## Head-to-Head Result

### First position
**Fi'il amr recognition** menang tipis untuk K26 karena:
- memperluas paradigma verbal yang sudah dimulai K6/K7;
- target masih satu kategori jelas;
- tidak bergantung pada ambiguity resolution sebanyak nafi.

### Second position
**Basic negation recognition** layak K27 dengan syarat occurrence/function tagging.

### Third position
Istifham perlu dipecah. Untuk sementara jangan freeze satu K28 bernama “istifham”. Kandidat paling layak adalah `هل` recognition, tetapi harus dibandingkan dengan recognition node lain agar tidak membuat K terlalu sempit.

## Revised hypothesis

- **K26-CAND — recognition fi'il amr sederhana**
- **K27-CAND — recognition partikel nafi dasar, function-tagged**
- **K28-CAND — belum final; `هل` recognition sebagai kandidat utama**
- **K29+ — hamzah istifham, fa'il mustatir, silah maushul, governing effects**

## Freeze conditions

K26:
- imperative occurrence verified;
- subject analysis locked;
- weak/irregular complexity flagged.

K27:
- surface token and actual function stored;
- governing effect locked;
- non-negative occurrence of same surface token rejected.

K28:
- no freeze until atomicity/yield comparison with other lightweight recognition nodes.

## Next

1. build evidence bank K26–K27;
2. freeze if integrity passes;
3. rescan candidate lightweight nodes for K28 before allowing fa'il mustatir to rise.