# Evidence Expansion K15–K17 v0.2 + Frontier K18–K20

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE
**Parent order under test:** K15 dhamir muttashil recognition → K16 huruf 'athaf recognition → K17 na'at–man'ut core.

## 1. K15 — Dhamir Muttashil Recognition

Target hanya segmentasi morfologis: `host + suffix pronoun`.

Contoh kerja yang sesuai prinsip recognition-only:
- `رَبُّهُ` → `رَبّ + هُ`
- `رَبُّكَ` → `رَبّ + كَ`
- `رَبُّكُمْ` → `رَبّ + كُمْ`
- `لَهُ` → `لِـ + هُ`
- `لَكُمْ` → `لِـ + كُمْ`
- `عَلَيْهِ` → host preposisional + `هِ`
- `خَلَقَهُ` → verba + `هُ`
- `خَلَقَكُمْ` → verba + `كُمْ`

Aturan penting:
- fungsi sintaksis suffix belum diajarkan di K15;
- cukup mengenali bahwa ada pronomina terikat;
- metadata menyimpan host_type dan syntactic_function tetapi function dapat berstatus WITHHELD.

**Assessment:** VERY STRONG. Recognition yield tinggi dan dependency rendah.

## 2. K16 — Huruf 'Athaf Recognition

Target: mengenali conjunction pada fungsi koordinatif, bukan sekadar bentuk huruf.

Core forms:
- `وَ`
- `فَ`
- `ثُمَّ`

Risiko:
- `وَ` dapat berfungsi sebagai waw qasam, waw hal, atau fungsi lain;
- `فَ` dapat membawa fungsi sababiyyah/ta'qib dan bukan selalu coordination sederhana.

Maka evidence K16 hanya menerima token yang pada analisis sintaksis benar-benar merupakan conjunction/coordination marker.

**Assessment:** STRONG, tetapi function-disambiguation wajib.

## 3. K17 — Na'at–Man'ut Core

Target minimum: `اسم + صفة` dengan agreement yang dapat diamati tanpa struktur tambahan besar.

Contoh kerja yang potensial:
- `عَذَابٌ أَلِيمٌ`
- `أَجْرٌ عَظِيمٌ`
- `صِرَاطٌ مُسْتَقِيمٌ`
- `قُرْآنٌ كَرِيمٌ`
- `كِتَابٌ مُبِينٌ`
- `قَوْمٌ ظَالِمُونَ`

Filter:
- kedua unsur harus membentuk relasi adjective;
- chain sifat lebih dari satu ditahan untuk reinforcement;
- idhafah kompleks, coordination, maushul, dan struktur lain yang belum tersedia membuat kandidat REVIEW/PREMATURE.

Agreement yang diamati:
- definiteness;
- gender;
- number;
- case.

Namun K17 tidak mengajarkan teori agreement abstrak penuh; peserta mulai dari pola konkret dan konsisten.

**Assessment:** STRONG / READY FOR FINAL STRESS TEST.

## 4. Head-to-Head Outcome Confirmed

Urutan tetap:

- K15-CAND — attached pronoun recognition
- K16-CAND — conjunction recognition
- K17-CAND — adjective relation

Alasan:
- K15 dan K16 = REC;
- K17 = REL dan memiliki agreement burden;
- tidak ada dependency reversal ditemukan.

## 5. Freeze Readiness

### K15
`READY-FOR-DRAFT-FREEZE`

### K16
`READY-FOR-DRAFT-FREEZE WITH FUNCTION TAGGING`

### K17
`READY-FOR-DRAFT-FREEZE WITH AGREEMENT-SCOPING`

## 6. Frontier K18–K20

### K18-CAND — 'Athaf dua unsur nominal sederhana

Formula: `اسم + حرف عطف + اسم` atau dua nominal phrase sederhana.

Dependencies:
- K1 nominal recognition;
- K16 conjunction recognition.

Core harus menahan:
- coordinated clauses;
- coordination dengan nested idhafah/na'at berat;
- conjunction dengan semantic/syntactic function non-coordinate.

**Strength:** VERY HIGH.

### K19-CAND — Fa'il Mustatir Dasar

Target: memahami bahwa subject dapat tidak hadir sebagai token isim zhahir tetapi terwakili pada verba.

Dependencies:
- K6/K7 verbal recognition;
- K10 fi'il+fa'il relation;
- K15 membantu memahami pronominal encoding.

Beban:
- lebih abstrak;
- memerlukan inference dari morphology/verb features.

**Strength:** HIGH BUT ABSTRACT.

### K20-CAND — Dhamir Muttashil sebagai Mudhaf Ilaih

Target: penggunaan attached pronoun pada host nominal sebagai relasi possessive sederhana.

Dependencies:
- K13 idhafah;
- K15 attached-pronoun recognition.

Contoh pola:
- `رَبُّهُ`
- `رَبُّكَ`
- `رَبُّكُمْ`

Ini merupakan integrasi langsung K13 + K15 dan secara dependency sangat dekat.

**Strength:** VERY HIGH.

## 7. Candidate Reordering K18–K20

Secara dependency, K20 kemungkinan lebih mudah daripada K19. Maka kandidat linearization terbaru:

- **K18-CAND** — 'athaf dua unsur nominal sederhana
- **K19-CAND** — dhamir muttashil sebagai mudhaf ilaih
- **K20-CAND** — fa'il mustatir dasar

Belum freeze. Head-to-head K18/K19/K20 diperlukan.

## 8. Next Batch

1. final stress test K15–K17;
2. jika lolos, terbitkan `DRAFT-FROZEN-K15-K17-v1.0`;
3. head-to-head K18–K20;
4. evidence expansion untuk attached possessive dan fa'il mustatir;
5. lanjutkan K21+ tanpa memaksa blok numerik jika dependency graph menunjukkan urutan lain.
