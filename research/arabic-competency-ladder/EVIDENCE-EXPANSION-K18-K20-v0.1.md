# Evidence Expansion K18–K20 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent:** `HEAD-TO-HEAD-K18-K20-v0.1.md`  
**Rule:** cumulative-only; unit Qurani terkecil yang utuh; semua segmen morfologis diperiksa.

## 1. K18 — Dhamir Muttashil sebagai Mudhaf Ilaih

Formula minimum:

`اسم + ضمير متصل`

Interpretasi kompetensi:
- host berupa isim;
- suffix berupa dhamir muttashil yang sudah dikenali pada K15;
- relasi possessive/genitive dibaca dengan landasan idhafah K13;
- fungsi object dan prep-object tetap ditahan.

Contoh kerja yang cocok untuk bank awal:

- `رَبُّهُ`
- `رَبِّهِ`
- `كِتَابَهُ`
- `قَوْمِهِ`
- `أَهْلِهِ`
- `رَسُولِهِ`
- `عِبَادِهِ`
- `آيَاتِهِ`
- `سَبِيلِهِ`
- `دِينِهِ`

Catatan evidence:
- bentuk akhir host dapat berubah sesuai posisi i'rab; ini tidak mengubah target utama K18;
- contoh dengan chain idhafah atau na'at tambahan ditandai REVIEW/PREMATURE bila struktur tambahannya belum tersedia;
- bentuk seperti `لَهُ` bukan K18 karena host-nya preposition, bukan noun.

**Yield judgement:** VERY HIGH.

## 2. K19 — 'Athaf Dua Unsur Nominal Sederhana

Formula minimum:

`اسم / عبارة اسمية بسيطة + حرف عطف + اسم / عبارة اسمية بسيطة`

Dependencies:
- K16 recognition conjunction;
- kedua conjunct harus berasal dari kompetensi <= K19.

Contoh kerja:

- `السَّمَاوَاتِ وَالْأَرْضَ`
- `اللَّيْلِ وَالنَّهَارِ`
- `الشَّمْسَ وَالْقَمَرَ`
- `الْجِنَّ وَالْإِنسَ`
- `الْبَرِّ وَالْبَحْرِ`
- `الْمَشْرِقِ وَالْمَغْرِبِ`

Filter:
- clause coordination ditahan;
- conjunct dengan embedded relative clause/complex idhafah ditahan;
- `ف` yang berfungsi sababiyyah/fashihah bukan core K19.

**Yield judgement:** HIGH.

## 3. K20 Candidate A — Fa'il Mustatir Dasar

Target:
- memahami bahwa subject/fa'il dapat tidak muncul sebagai token isim terpisah;
- memulihkan subject dasar dari fitur verba dan konteks lokal.

Dependencies:
- K6/K7 verb recognition;
- K10 verbal relation;
- pengalaman dhamir K5/K15 membantu interpretasi persona.

Beban:
- unsur target tidak tampak sebagai token independen;
- membutuhkan inferensi person/number/gender;
- banyak verba Qurani membawa object/PP/particle tambahan;
- raw clean-example yield diperkirakan tinggi, tetapi **pedagogical purity lebih rendah** daripada relasi surface-visible.

**Judgement:** IMPORTANT, BUT ABSTRACT.

## 4. Search for Lighter K20 Competitors

Setelah K18–K19, beberapa kandidat lebih ringan daripada fa'il mustatir muncul dari dependency graph:

### Candidate B — Dhamir Muttashil sebagai Object of Preposition

Formula:

`حرف جر + ضمير متصل`

Dependencies:
- K9 jar–majrur;
- K15 attached-pronoun recognition.

Contoh surface sangat lokal:
- `لَهُ`
- `بِهِ`
- `فِيهِ`
- `عَلَيْهِ`
- `مِنْهُ`
- `إِلَيْهِ`

Kelebihan:
- integrasi dua kompetensi yang sudah ada;
- target surface-visible;
- clean unit sangat pendek;
- tidak perlu inferensi subject tersembunyi.

**Strength:** VERY HIGH.

### Candidate C — Dhamir Muttashil sebagai Maf'ul Bih

Formula:

`فعل + ضمير متصل`

Dependencies:
- K14 maf'ul bih;
- K15 attached-pronoun recognition;
- verb recognition K6/K7.

Contoh surface:
- bentuk seperti `خَلَقَهُ`, `هَدَاهُ`, `رَزَقَهُ` pada occurrence yang clean.

Beban:
- host verbal dapat sekaligus membawa subject suffix atau struktur tambahan;
- perlu memastikan suffix target benar object, bukan subject morphology.

**Strength:** HIGH.

### Candidate D — Idhafah Chain Tiga Unsur Sederhana

Dependencies:
- K13 idhafah;
- K18 attached-pronoun mudhaf-ilaih dapat memperluas variasi.

Tetapi ini expansion depth, bukan kategori baru. Lebih baik ditahan sebagai reinforcement sebelum diberi K baru.

**Strength:** NOT PRIORITIZED AS NEW K.

## 5. Head-to-Head Result for K20

Perbandingan:

| Candidate | Surface visible | Dependency depth | Hidden inference | Clean locality | Priority |
|---|---:|---:|---:|---:|---:|
| Fa'il mustatir | tidak | sedang | tinggi | sedang | medium |
| Prep + attached pronoun | ya | rendah | rendah | sangat tinggi | **highest** |
| Verb + object pronoun | ya | sedang | sedang | tinggi | high |

**Temuan:** fa'il mustatir sebaiknya tidak menjadi K20.

## 6. Revised Candidate Order

- **K18-CAND** — dhamir muttashil sebagai mudhaf ilaih
- **K19-CAND** — 'athaf dua unsur nominal sederhana
- **K20-CAND** — dhamir muttashil sebagai object of preposition / `حرف جر + ضمير متصل`
- **K21-CAND** — dhamir muttashil sebagai maf'ul bih
- **K22-CAND** — fa'il mustatir dasar

Ini memperpanjang ladder secara natural; tidak ada alasan memaksa semua kandidat masuk 20 level.

## 7. Why This Matters

Perubahan K20 menegaskan prinsip utama proyek:

> Struktur yang secara tradisional dianggap penting belum tentu harus diajarkan lebih awal bila ada integrasi Qurani yang lebih lokal, surface-visible, dan cumulative-clean.

K20 baru hanya membutuhkan K9 + K15 dan memberi banyak contoh Qurani sangat pendek. Ini lebih konsisten dengan controlled-example rule dibanding fa'il mustatir.

## 8. Status Recommendation

- K18: READY-FOR-DRAFT-FREEZE
- K19: READY-FOR-DRAFT-FREEZE WITH FUNCTIONAL-TAGGING
- K20(new): READY-FOR-DRAFT-FREEZE AFTER QUICK COUNTEREXAMPLE CHECK
- K21: strong candidate
- K22: defer until later

## 9. Next Batch

1. quick counterexample test K18–K20 revised;
2. bila lolos, freeze K18–K20 di research layer;
3. lanjut head-to-head K21 object-pronoun vs kandidat lain (mis. jumlah ismiyyah dengan khabar sifat/idhafah yang lebih kompleks, atau fi'il-fa'il dengan attached subject forms);
4. tetap simpan `sequence_order` terpisah dari `hard_dependencies[]`.