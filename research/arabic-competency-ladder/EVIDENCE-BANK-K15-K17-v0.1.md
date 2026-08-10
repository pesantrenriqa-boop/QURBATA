# Evidence Bank K15–K17 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent:** `FINAL-GATE-K11-K14-v1.0.md`  
**Scope:** K15 recognition dhamir muttashil, K16 na'at–man'ut core, K17 recognition huruf 'athaf.

## K15-CAND — Mengenali Dhamir Muttashil sebagai Segmen Morfologis

### Target
Peserta dapat memecah bentuk Qurani menjadi host + attached pronoun tanpa terlebih dahulu dituntut menganalisis seluruh fungsi sintaksis suffix.

### Evidence classes

#### Host = noun
- `رَبُّهُ` → `رَبّ + هُ`
- `كِتَابُهُ` → `كِتَاب + هُ`
- `رَبُّكُمْ` → `رَبّ + كُمْ`

#### Host = verb
- `خَلَقَهُ` → `خَلَقَ + هُ`
- `آتَاهُ` → `آتَى + هُ`
- `نَصَرَهُ` → `نَصَرَ + هُ`

#### Host = preposition
- `لَهُ` → `لِ + هُ`
- `بِهِ` → `بِ + هِ`
- `مِنْهُ` → `مِنْ + هُ`

### Policy
Pada K15, `syntactic_function` boleh dicatat di metadata tetapi **tidak dijadikan target pembelajaran**. Fungsi possessive, maf'ul bih, atau object of preposition akan menjadi kompetensi berikutnya.

### Status
`VERY STRONG REC CANDIDATE`.

---

## K16-CAND — Na'at–Man'ut Sederhana

### Target
Memahami relasi sifat pada dua unsur nominal sederhana yang agreement-nya terlihat jelas dan tidak membawa struktur lebih tinggi.

### Candidate evidence
- `قَوْلًا سَدِيدًا`
- `أَجْرًا عَظِيمًا`
- `عَذَابٌ أَلِيمٌ`
- `رِزْقٌ كَرِيمٌ`
- `فَوْزًا عَظِيمًا`
- `قُرْآنًا عَرَبِيًّا`

### Required checks
Setiap contoh harus diverifikasi terhadap:
- definiteness agreement;
- case agreement;
- gender agreement;
- number agreement;
- tidak ada idhafah/coordination/nested relation yang diperlukan untuk target.

### Status
`STRONG BUT AGREEMENT-SENSITIVE`.

---

## K17-CAND — Mengenali Huruf 'Athaf Frekuen

### Target
Recognition dulu, construction nanti.

### Core forms
- `وَ`
- `فَ`
- `ثُمَّ`
- `أَوْ`

### Boundary
K17 belum mengajarkan semua fungsi discourse setiap partikel. Hanya mengenali partikel sebagai connector candidate pada konteks yang teranotasi jelas.

### Why separate from K18
Jika recognition dan relation digabung, contoh K18 akan membawa dua kompetensi baru sekaligus: bentuk connector + struktur coordination. Karena itu dipisah.

### Status
`VERY STRONG REC CANDIDATE`.

## Head-to-Head Preliminary

| Candidate | Dependency depth | Hidden burden | Clean unit potential | Preliminary rank |
|---|---:|---:|---:|---:|
| K15 attached-pronoun recognition | rendah | sedang (polyfunction) | sangat tinggi | 1 |
| K17 conjunction recognition | sangat rendah | rendah–sedang (polysemy) | sangat tinggi | 2 |
| K16 na'at–man'ut | sedang | tinggi (agreement) | tinggi | 3 |

## Preliminary Reordering Hypothesis

Evidence awal membuka kemungkinan bahwa recognition huruf 'athaf lebih baik ditempatkan **sebelum** na'at relation:

- K15-CAND — dhamir muttashil recognition
- K16-CAND — huruf 'athaf recognition
- K17-CAND — na'at–man'ut
- K18-CAND — 'athaf construction
- K19-CAND — fa'il mustatir

Belum freeze. Head-to-head formal berikutnya wajib menguji K16/K17 sebelum perubahan urutan diterima.

## Next

1. head-to-head attached pronoun vs conjunction recognition vs na'at;
2. perluas evidence na'at sampai puluhan clean candidates;
3. setelah recognition conjunction stabil, bangun evidence K18 coordination;
4. pertahankan cumulative-only rule pada seluruh unit Qurani.
