# Head-to-Head Test K11–K14 v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Parent baseline:** `DRAFT-FROZEN-K01-K10-v1.0`

## 1. Pair A — K11 vs K12

### Candidate A1 — Dhamir munfashil sebagai mubtada'

Hard dependency:
- K5 recognition dhamir munfashil;
- K8 jumlah ismiyyah core.

Bentuk minimum:
`ضمير منفصل + خبر اسمي`

Kekuatan:
- hanya menggabungkan dua kompetensi yang sudah dikuasai;
- tidak menambah kategori morfologi baru;
- unit target dapat sangat pendek dan lokal.

Risiko:
- beberapa contoh Qurani memiliki dhamir fashl, predikat kompleks, atau ekspansi tambahan sehingga harus difilter.

**Judgement:** VERY STRONG.

### Candidate A2 — Khabar jar–majrur

Hard dependency:
- K8 jumlah ismiyyah core;
- K9 jar–majrur.

Bentuk minimum:
`مبتدأ + جار ومجرور` atau `جار ومجرور + مبتدأ` bila urutan inversi belum menjadi target terpisah harus ditahan.

Kekuatan:
- juga merupakan integrasi dua kompetensi frozen;
- struktur sangat produktif di Al-Qur'an.

Risiko:
- posisi khabar dapat muqaddam;
- attachment ambiguity pada sebagian ayat;
- beberapa contoh memerlukan mubtada' dhamir atau idhafah.

**Head-to-head result:** K11 tetap lebih dahulu daripada K12 karena bentuk target dapat dipertahankan lebih dekat ke pola jumlah ismiyyah yang sudah dipelajari tanpa perubahan tipe khabar menjadi شبه جملة.

**Decision:**
- K11-CAND = dhamir munfashil sebagai mubtada' sederhana
- K12-CAND = khabar jar–majrur sederhana

## 2. Pair B — K13 vs K14

### Candidate B1 — Maf'ul bih isim zhahir

Hard dependency:
- K10 fi'il + fa'il zhahir;
- K1 isim.

Bentuk minimum:
`فعل + فاعل ظاهر + مفعول به ظاهر`

Kekuatan:
- ekspansi langsung jumlah fi'liyyah yang sudah dikuasai;
- peran objek dapat dikenali dari relasi verbal tanpa memperkenalkan frasa nominal baru.

Risiko:
- word order dapat bervariasi;
- objek dapat berupa dhamir, klausa, atau lebih dari satu objek;
- banyak ayat membawa attachment tambahan.

**Judgement:** HIGH.

### Candidate B2 — Idhafah dua isim sederhana

Hard dependency:
- K1 isim;
- exposure majrur dari K9 membantu memahami mudhaf ilaih.

Bentuk minimum:
`مضاف + مضاف إليه`

Kekuatan:
- relasi lokal dua nominal;
- sangat produktif;
- tidak memerlukan verba.

Risiko:
- perlu memahami bahwa mudhaf tidak mengambil `الـ`/tanwin pada pola dasar;
- unsur kedua majrur;
- banyak contoh memakai dhamir sebagai mudhaf ilaih dan harus ditahan.

**Head-to-head result:** idhafah lebih lokal, tetapi maf'ul bih adalah ekspansi langsung dari K10 dan tidak memperkenalkan relasi nominal baru. Untuk linearization pembelajaran, K13 maf'ul bih tetap sedikit lebih kuat **jika** evidence clean cukup. Jika yield evidence rendah, K14 dapat dinaikkan.

**Decision sementara:**
- K13-CAND = maf'ul bih isim zhahir sederhana
- K14-CAND = idhafah dua isim sederhana

## 3. Candidate Order K11–K14

1. K11-CAND — dhamir munfashil sebagai mubtada'
2. K12-CAND — khabar jar–majrur sederhana
3. K13-CAND — maf'ul bih isim zhahir sederhana
4. K14-CAND — idhafah dua isim sederhana

## 4. Freeze Gate

### K11
`READY-FOR-EVIDENCE-EXPANSION`

### K12
`READY-FOR-EVIDENCE-EXPANSION`

### K13
`CONDITIONALLY READY` — wajib uji clean yield lebih besar.

### K14
`READY-FOR-EVIDENCE-EXPANSION`

## 5. Next

1. bangun evidence bank K11–K14;
2. prioritaskan K13 untuk memastikan 20–30+ clean examples realistis;
3. jika K13 gagal yield test, swap dengan K14;
4. setelah itu lanjut audit K15–K18.
