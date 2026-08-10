# Final Gate K32–K33 v1.0

**Status:** DRAFT-FROZEN — RESEARCH LAYER ONLY

## K32 — REC-QAD
Recognition `قَدْ` pada occurrence Qurani tervalidasi.

- target: recognition token;
- efek aspek/taqrib/tahqiq tidak dibuka;
- contoh wajib berada dalam cumulative competency boundary.

**Gate:** PASS.

## K33 — REC-INNA
Recognition `إِنَّ` pada occurrence Qurani tervalidasi.

- target: recognition token;
- `اسم إنّ` dan `خبر إنّ` belum diajarkan;
- governing effect dikunci dalam metadata.

Required metadata:
- `governing_effect_locked = true`
- `ism_inna_analysis_unlocked_at = later`
- `khabar_inna_analysis_unlocked_at = later`

**Gate:** PASS WITH LOCKED GOVERNMENT.

## Ordering decision

K32 remains before K33 because `قد` has lower latent grammar burden and lower premature-i'rab risk.

## Updated progress

Research-layer competency ladder is now DRAFT-FROZEN through **K33**.

No production registry or master content is changed by this gate.

## Next frontier

- compare K34 `كان` recognition vs K35 `ليس` recognition;
- rescan lighter nodes before either;
- keep full nawasikh constructions separate from recognition nodes.