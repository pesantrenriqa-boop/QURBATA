# Topological Candidate Order v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Tujuan:** menggabungkan nominal track dan verbal track menjadi urutan kandidat awal yang tidak melanggar dependency dan tetap tunduk pada cumulative clean-example rule.

## 1. Prinsip Topological Ordering

Sebuah kandidat hanya boleh ditempatkan jika seluruh prasyaratnya sudah berada pada posisi sebelumnya. Urutan juga mempertimbangkan:

- recognition simplicity;
- clean-example yield;
- frequency/reuse potential;
- prematurity risk;
- pedagogical granularity;
- kemampuan membuka struktur berikutnya.

Urutan ini belum `K1–Kn` final. Nomor `T1..Tn` adalah posisi topologis sementara.

## 2. Kandidat T1–T15

| Posisi | Kandidat | Tipe | Dependency minimum | Status |
|---|---|---|---|---|
| T1 | mengenali isim sederhana | REC | — | STRONG |
| T2 | mengenali fi‘il sederhana | REC | — | STRONG |
| T3 | mengenali `الـ` pada isim | REC | T1 | STRONG |
| T4 | mengenali nakirah/tanwin sederhana | REC | T1 | STRONG |
| T5 | mengenali fi‘il madhi sederhana | REC | T2 | STRONG |
| T6 | mengenali fi‘il mudhari‘ sederhana | REC | T2 | STRONG |
| T7 | jumlah ismiyyah core: mubtada’ + khabar isim zhahir | REL | T1,T3/T4 secukupnya | STRONG |
| T8 | fi‘il + fa‘il isim zhahir | REL | T1,T2,T5/T6 | STRONG |
| T9 | mengenali huruf jar frekuen | REC | —/T1 untuk contoh | STRONG |
| T10 | jar–majrur: huruf jar + isim zhahir | REL | T1,T9 | STRONG |
| T11 | mengenali dhamir munfashil dasar | REC | — | STRONG |
| T12 | mubtada’ dhamir + khabar sederhana | REL | T7,T11 | MEDIUM-STRONG |
| T13 | fi‘il + fa‘il + maf‘ul bih isim zhahir | REL | T1,T2,T8 | MEDIUM-STRONG |
| T14 | idhafah dua isim sederhana | REL | T1 + majrur operasional minimum | MEDIUM-STRONG |
| T15 | na‘at–man‘ut sederhana | REL | T1,T3/T4 + agreement minimum | MEDIUM |

## 3. Kandidat K1–K10 v0.1 — PROMOTION CANDIDATE, BELUM FREEZE

Setelah dependency audit, clean-yield test, dan verbal-track integration, sepuluh posisi pertama yang paling stabil untuk diuji sebagai `K1–K10` adalah:

1. **K1-CAND:** mengenali isim sederhana;
2. **K2-CAND:** mengenali fi‘il sederhana;
3. **K3-CAND:** mengenali `الـ` pada isim;
4. **K4-CAND:** mengenali nakirah/tanwin sederhana;
5. **K5-CAND:** mengenali fi‘il madhi sederhana;
6. **K6-CAND:** mengenali fi‘il mudhari‘ sederhana;
7. **K7-CAND:** jumlah ismiyyah core: mubtada’ + khabar isim zhahir sederhana;
8. **K8-CAND:** fi‘il + fa‘il isim zhahir sederhana;
9. **K9-CAND:** mengenali huruf jar frekuen;
10. **K10-CAND:** jar–majrur dengan isim zhahir sederhana.

### Mengapa belum freeze?

Karena masih ada dua konflik penting:

- apakah `huruf jar recognition` seharusnya muncul sebelum K7/K8 karena sangat sederhana secara token;
- apakah `dhamir munfashil recognition` lebih layak masuk 10 besar daripada salah satu struktur REL.

Keduanya perlu counterexample testing sebelum promosi final.

## 4. Counterexample Tests yang Wajib

### Test A — K7 jumlah ismiyyah

Harus tersedia cukup contoh PURE/clean yang hanya memerlukan K1–K7. Jika sebagian besar kandidat ternyata membutuhkan dhamir, idhafah, na‘at, atau jar–majrur, posisi K7 harus digeser.

### Test B — K8 fi‘il + fa‘il

Harus tersedia contoh dengan:

- fi‘il sederhana;
- fa‘il isim zhahir;
- tanpa maf‘ul bih;
- tanpa suffix dhamir yang belum dipelajari;
- tanpa koordinasi/maushul/syarth/partikel kompleks.

Jika clean yield rendah, K8 perlu dipindah setelah morfologi persona tertentu.

### Test C — K9/K10 jar–majrur

Harus tersedia cukup contoh `preposition + noun` tanpa attached pronoun dan tanpa clitic prematur yang mengubah beban analisis.

## 5. Dua Jalur Dependency yang Kini Stabil

### Nominal track

```text
isim
├─ al-ta‘rif
├─ nakirah/tanwin
├─ jumlah ismiyyah core
├─ huruf jar → jar–majrur
├─ idhafah
└─ na‘at
```

### Verbal track

```text
fi‘il
├─ madhi
├─ mudhari‘
└─ fi‘il + fa‘il
      ↓
   fi‘il + fa‘il + maf‘ul bih
```

### Titik integrasi

Kedua track bertemu ketika satu jumlah mulai memakai ekspansi nominal, jar–majrur, dhamir, atau objek/komplemen. Titik ini kemungkinan setelah K10–K15.

## 6. Prinsip Penamaan Final

Saat freeze, nama K harus berupa kompetensi operasional, bukan label bab. Format yang disarankan:

`K001 — Mengidentifikasi Isim Qurani Sederhana`

bukan sekadar:

`K001 — Isim`.

Setiap K final wajib memiliki:

- definisi kompetensi;
- batas cakupan;
- prerequisite-K;
- allowed structures;
- forbidden structures;
- Quranic evidence bank;
- clean-example count;
- contoh inti terpilih;
- status review.

## 7. Status Saat Ini

- T1–T10: `STRONG TOPOLOGICAL CANDIDATES`;
- T11–T15: `STRONG/MEDIUM NEXT FRONTIER`;
- belum ada K yang difreeze;
- tidak ada perubahan ke `REG-ARB-001`;
- semua pekerjaan tetap research-layer.

## 8. Batch Berikutnya

1. counterexample testing untuk K1-CAND sampai K10-CAND;
2. uji khusus posisi huruf jar dan dhamir munfashil;
3. uji apakah fi‘il madhi dan mudhari‘ perlu dua K terpisah atau satu recognition-K lalu dipisah pada construction;
4. jika 10 kandidat lolos, promosi menjadi `K1–K10 DRAFT-FROZEN` di research layer saja;
5. lanjutkan T11–T20 setelah itu.
