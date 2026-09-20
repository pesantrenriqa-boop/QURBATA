# Evidence K32–K33 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Baseline:** K1–K31 DRAFT-FROZEN.  
**Candidates:** K32 `قَدْ` recognition, K33 `إِنَّ` recognition.

## 1. K32 — Recognition `قَدْ`

Target hanya mengenali `قَدْ` sebagai partikel pada occurrence Qurani yang tervalidasi. Efek semantik/aspektual pada fi'il madhi atau mudhari' tidak otomatis dibuka.

### Dependency
- K6/K7 verbal recognition sudah tersedia;
- target token-level sangat lokal;
- tidak memerlukan i'rab baru.

### Clean-context policy
PASS bila:
- `قد` tervalidasi sebagai particle;
- fi'il sesudahnya berada dalam kelas yang sudah dikenali;
- analisis aspek/taqrib/tahqiq tetap dikunci.

PREMATURE bila contoh hanya bisa dipahami dengan struktur verbal kompleks yang belum tersedia.

### Judgement
**VERY STRONG recognition node.**

## 2. K33 — Recognition `إِنَّ`

Target hanya mengenali `إِنَّ` sebagai particle/token. Efek nasb pada isim dan raf' pada khabar tidak dibuka pada K33.

### Dependency
- jumlah ismiyyah sudah tersedia K8;
- recognition token sangat lokal;
- tetapi occurrence `إنّ` secara struktur hampir selalu membuka nominal clause yang governed.

### Clean-context policy
PASS bila:
- token `إنّ` tervalidasi;
- siswa hanya diminta mengenali particle;
- isim/khabar sesudahnya berada dalam vocabulary/structure yang sudah dikenal atau tidak dijadikan target analisis.

PREMATURE bila pengajaran contoh secara implisit menuntut `اسم إنّ`/`خبر إنّ` dan perubahan case.

### Judgement
**STRONG recognition node, but higher latent grammar burden than `قد`.**

## 3. Head-to-head result

| Criterion | `قد` | `إنّ` |
|---|---|---|
| Token locality | very high | very high |
| Hard dependency | low | low–moderate |
| Latent government burden | low | high |
| Risk of premature i'rab | low | high |
| Clean recognition isolation | easier | slightly harder |

**Result: keep K32 = `قد`, K33 = `إنّ`.**

No evidence-based reason to swap them.

## 4. Gate readiness

- K32: READY FOR DRAFT-FREEZE.
- K33: READY FOR DRAFT-FREEZE WITH LOCKED-GOVERNMENT TAG.

Required metadata for K33:
- `governing_effect_locked = true`
- `ism_inna_analysis_unlocked_at = later`
- `khabar_inna_analysis_unlocked_at = later`

## 5. Next

After final gate K32–K33:
- compare K34 `كان` recognition vs K35 `ليس` recognition;
- rescan whether another lighter particle should precede either;
- keep full nawasikh construction separate from recognition nodes.