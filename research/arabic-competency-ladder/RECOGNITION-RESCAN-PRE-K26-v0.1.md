# Recognition Rescan Before K26 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Purpose:** memastikan tangga tidak terlalu cepat masuk ke fa'il mustatir sebelum recognition nodes yang lebih ringan dipetakan.

## Baseline

K1–K23 draft-frozen. K24 demonstrative-mubtada' dan K25 verbal PP attachment sedang menuju gate. Kandidat lama K26 adalah fa'il mustatir.

## Recognition candidates audited

### A. Fi'il amr recognition

Target hanya mengenali bentuk perintah Qurani yang tervalidasi sebagai imperative, tanpa mengajarkan fa'il mustatir atau paradigma penuh.

Dependencies:
- verbal category recognition sudah ada K6/K7;
- tidak perlu relation baru bila target token-level.

Risiko:
- banyak imperative membawa subject morphology yang secara sintaksis terkait dhamir mustatir/attached subject;
- bentuk surface dapat memerlukan morfologi lebih kompleks.

Judgement: **HIGH**, tetapi jangan sekaligus mengajarkan subject analysis.

### B. Partikel nafi recognition

Kandidat bentuk seperti `لا`, `ما`, `لم`, `لن` tidak boleh disatukan sebagai satu fungsi gramatikal tunggal karena governance berbeda.

Strategi aman:
- recognition category dapat dimulai dari partikel yang occurrence-nya jelas;
- efek pada mudhari' (jazm/nasb), `لا` النافية للجنس, dan `ما` dengan fungsi non-negatif harus dikunci.

Judgement: **VERY HIGH AS FUNCTION-TAGGED REC**, tetapi polyfunctionality wajib dicatat.

### C. Partikel istifham recognition

Kandidat seperti `هل`, hamzah istifham, `مَن`, `ما`, `متى`, `أين`, `كيف` membawa campuran particle/pronominal/adverbial categories.

Jika dibuat satu K terlalu luas, atomicity rusak. `هل` sebagai recognition paling bersih, tetapi satu-token-only K mungkin terlalu sempit jika tidak ada pedagogical yield cukup.

Judgement: **MODERATE-HIGH; needs decomposition**.

## Main finding

Fa'il mustatir **belum layak menjadi K26**. Ada recognition nodes yang dependency-nya lebih ringan.

Namun jangan membuat satu kompetensi besar bernama “nafi” atau “istifham” tanpa memisahkan surface recognition dari governing effect.

## Revised frontier hypothesis

Setelah K24–K25, kandidat lebih aman:

- **K26-CAND — recognition fi'il amr sederhana**
- **K27-CAND — recognition partikel nafi dasar dengan function tagging**
- **K28-CAND — recognition `هل`/interrogative marker dasar, setelah atomicity test**
- **K29-CAND — fa'il mustatir dasar**
- **K30+ — isim maushul + silah minimal dan governing effects of particles**

Urutan K26/K27 belum freeze; perlu head-to-head evidence.

## Architectural rule added

Untuk partikel polyfunctional, evidence record wajib menyimpan:
- surface token;
- corpus POS/tag;
- function in occurrence;
- governing effect;
- effect_unlocked_at_K;
- ambiguity flag.

Dengan demikian recognition dapat diajarkan lebih awal tanpa menyelundupkan kompetensi i'rab/government yang lebih tinggi.

## Next

1. final gate K24–K25 bila evidence integrity lolos;
2. head-to-head fi'il amr vs basic negation recognition;
3. pecah interrogative frontier secara atomik;
4. tunda fa'il mustatir sampai recognition frontier cukup dipetakan.