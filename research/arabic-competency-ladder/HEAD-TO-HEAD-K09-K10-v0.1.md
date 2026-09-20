# Head-to-Head Test: Jar–Majrur vs Fi'il–Fa'il v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Scope:** menentukan urutan dua construction-K awal setelah jumlah ismiyyah core.  
**Candidates:**
- A: K8 jumlah ismiyyah → K9 fi'il+fa'il → K10 jar–majrur
- B: K8 jumlah ismiyyah → K9 jar–majrur → K10 fi'il+fa'il

## 1. Kriteria

1. hard dependency minimum;
2. clean-unit locality;
3. hidden-analysis burden;
4. morphological/clitic burden;
5. risk kompetensi prematur;
6. availability of clean Qur'anic examples;
7. value sebagai pembuka struktur berikutnya.

## 2. Jar–Majrur

Target minimum: `حرف جر + اسم ظاهر`.

Hard dependency:
- isim sudah dikenali;
- huruf jar sudah dikenali.

Kelebihan:
- relasi bersifat lokal dan contiguous;
- tidak ada subjek tersembunyi yang harus dipulihkan;
- contoh dapat difilter ketat ke isim zhahir;
- preposisi+dhamir dapat ditunda;
- clitic tambahan dapat ditandai PREMATURE bila belum tersedia.

Contoh kerja yang relatif bersih:
- `فِي الْأَرْضِ`
- `فِي السَّمَاوَاتِ`
- `عَنِ النَّبَإِ`
- `بِالْحَقِّ`
- `مِنَ الْأَرْضِ`

Risiko:
- sebagian token Qurani memiliki prefiks koordinasi/partikel tambahan;
- teori i'rab majrur jangan dipaksa menjadi prerequisite abstrak; dapat digeneralisasi sesudah exposure.

**Judgement:** VERY STRONG EARLY RELATION.

## 3. Fi'il + Fa'il Isim Zhahir

Target minimum: `فعل + فاعل ظاهر`.

Hard dependency:
- mengenali fi'il madhi/mudhari' sesuai contoh;
- mengenali isim;
- memahami relasi subject/fa'il.

Kelebihan:
- predikasi verbal merupakan struktur inti bahasa Arab Qurani;
- membuka maf'ul bih, adverbial attachment, coordination, dan clause expansion.

Contoh kerja:
- `جَاءَ الْحَقُّ`
- `زَهَقَ الْبَاطِلُ`
- `قَالَ مُوسَىٰ`
- `يُرِيدُ اللَّهُ`

Beban tersembunyi:
- verba aktif selalu mempunyai subject/fa'il secara sintaksis, tetapi surface subject dapat tidak langsung mengikuti verba;
- fa'il dapat berupa dhamir mustatir atau suffix;
- banyak contoh Qurani cepat membawa maf'ul, quoted speech, prepositional attachment, coordination, atau subordinate material;
- karena itu clean extraction memerlukan dependency parsing lebih ketat daripada jar–majrur.

**Judgement:** ESSENTIAL BUT HIGHER FILTERING BURDEN.

## 4. Hasil Head-to-Head

| Criterion | Jar–majrur | Fi'il+fa'il |
|---|---|---|
| Hard dependency | lebih pendek | lebih panjang |
| Locality | sangat lokal | dapat non-lokal |
| Hidden element | tidak | sering mungkin |
| Clean filtering | lebih mudah | lebih ketat |
| Prematurity risk | rendah–sedang | sedang–tinggi |
| Qur'anic productivity | sangat tinggi | sangat tinggi |
| Expansion value | tinggi | sangat tinggi |

**Winner untuk urutan lebih awal: JAR–MAJRUR.**

## 5. Revised Candidate Order

Dengan hasil ini, candidate linearization direvisi:

1. K1-CAND — isim sederhana
2. K2-CAND — `الـ` pada isim
3. K3-CAND — nakirah/tanwin sederhana
4. K4-CAND — huruf jar frekuen
5. K5-CAND — dhamir munfashil dasar (recognition)
6. K6-CAND — fi'il madhi sederhana
7. K7-CAND — fi'il mudhari' sederhana
8. K8-CAND — jumlah ismiyyah core: mubtada' + khabar isim zhahir
9. **K9-CAND — jar–majrur dengan isim zhahir**
10. **K10-CAND — fi'il + fa'il isim zhahir sederhana**

Perubahan hanya swap K9/K10 dari proposal sebelumnya. Tidak ada perubahan registry produksi.

## 6. Freeze Gate Assessment

### K8
`READY-FOR-DRAFT-FREEZE`

Alasan: anchor pure tersedia dan dependency stabil.

### K9 (jar–majrur)
`READY-FOR-DRAFT-FREEZE`

Alasan: dependency pendek, clean unit stabil, evidence dapat diperluas secara luas.

### K10 (fi'il+fa'il)
`CONDITIONALLY READY`

Syarat:
- evidence bank harus menandai hanya fa'il zhahir yang benar-benar menjadi subject target;
- contoh dengan fa'il mustatir/suffix tidak digunakan untuk core teaching set K10;
- quoted speech atau material sesudah unit target tidak otomatis menjadi bagian unit pembelajaran.

## 7. Pedagogical Extraction Rule

Untuk semua K relasional:

> Gunakan unit Qurani terkecil yang utuh untuk target, bukan otomatis seluruh ayat.

Contoh:
- ayat dapat panjang, tetapi `جَاءَ الْحَقُّ` dapat menjadi unit K10 bila unit itu syntactically valid dan struktur di luar unit tidak diperlukan untuk memahami target;
- referensi surah:ayat tetap disimpan penuh di metadata.

## 8. Decision of This Batch

**Candidate B accepted for research-layer ordering:**

`K8 jumlah ismiyyah → K9 jar–majrur → K10 fi'il+fa'il`.

Status ini belum authoritative. Ia menjadi input langsung untuk dokumen `DRAFT-FROZEN-K01-K10-v1.0` setelah audit akhir K5 dan evidence integrity check.

## 9. Next

1. audit posisi K5 dhamir munfashil;
2. audit integrity seluruh K1–K10 terhadap rule cumulative-only;
3. terbitkan draft-frozen v1.0 bila tidak ada dependency reversal;
4. sesudah itu baru lanjut K11+ (kemungkinan ekspansi dhamir dalam jumlah, idhafah, na'at, maf'ul bih, dan struktur berikutnya) tanpa menyentuh registry resmi sampai keputusan formal.
