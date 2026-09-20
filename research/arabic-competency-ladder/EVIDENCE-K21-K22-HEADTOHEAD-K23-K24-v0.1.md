# Evidence K21–K22 + Head-to-Head K23–K24 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE

## K21 — Dhamir muttashil sebagai maf'ul bih

### Dependency
- K14 maf'ul bih zhahir
- K15 recognition dhamir muttashil
- K6/K7 recognition verba sesuai contoh

### Core rule
Target hanya suffix pronoun yang occurrence-specific berfungsi sebagai direct object. Jangan memasukkan possessive suffix atau object of preposition.

### Evidence pattern
Core forms yang dicari:
- `خَلَقَهُ`
- `آتَاهُ`
- `هَدَاهُ`
- `نَصَرَهُ`
- `رَزَقَهُ`

Setiap occurrence wajib diverifikasi fungsi sintaksisnya.

### Premature filters
- dua objek;
- object clause;
- passive;
- suffix subject;
- quoted speech bila diperlukan untuk memahami target;
- additional clause dependency.

**Assessment:** READY FOR STRESS TEST.

## K22 — Recognition isim isyarah

### Dependency
Recognition sangat ringan dan tidak membutuhkan penggunaan sintaksis.

### Core forms
- `هَذَا`
- `هَذِهِ`
- `هَؤُلَاءِ`
- `ذَلِكَ`
- `تِلْكَ`
- `أُولَئِكَ`

### Scope
Hanya recognition token dan fitur dasar deiksis; fungsi sebagai mubtada', na'at-like apposition, atau objek ditunda.

### Premature filters
Jangan menjadikan seluruh frasa setelah isim isyarah sebagai bagian kompetensi jika membawa K lebih tinggi.

**Assessment:** VERY STRONG.

## Head-to-Head K23 vs K24

Candidates:
- A — jar–majrur sebagai pelengkap fi'il sederhana
- B — recognition isim maushul

### A. Verbal + PP
Dependencies:
- K10 fi'il+fa'il
- K9/K20 jar–majrur sesuai surface form
- attachment relation ke verba

Beban:
- attachment ambiguity;
- PP dapat melekat pada verba, nomina, atau keseluruhan clause;
- contoh clean perlu parser-level verification.

**Strength:** HIGH, but relationally heavier.

### B. Recognition isim maushul
Core forms:
- `الَّذِي`
- `الَّتِي`
- `الَّذِينَ`
- `اللَّاتِي` / variants yang relevan

Dependency recognition rendah. Shilah maushul belum diajarkan.

Risiko:
- token hampir selalu diikuti clause, tetapi unit pembelajaran dapat dibatasi ke token recognition selama fungsi shilah ditahan.

**Strength:** VERY HIGH AS REC.

## Result

Recognition isim maushul lebih ringan daripada verbal PP attachment.

### Revised candidate order
- K21-CAND — dhamir muttashil sebagai maf'ul bih
- K22-CAND — recognition isim isyarah
- **K23-CAND — recognition isim maushul**
- **K24-CAND — jar–majrur sebagai pelengkap fi'il sederhana**
- K25-CAND — fa'il mustatir dasar

## Freeze readiness

- K21: conditional-ready, evidence occurrence tagging wajib
- K22: ready
- K23: ready as recognition only
- K24: not yet freeze; needs attachment evidence bank

## Next

1. stress-test K21–K23;
2. bila lolos, draft-freeze batch K21–K23;
3. bangun evidence K24;
4. compare K24 vs fa'il mustatir dan kandidat lain seperti penggunaan isim isyarah dalam jumlah ismiyyah atau isim maushul + shilah sederhana.