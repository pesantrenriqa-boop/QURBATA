# Dependency Audit Bahasa Arab Qurani v0.1

**Status:** WORKING RESEARCH — NON-AUTHORITATIVE  
**Branch:** `agent/quranic-arabic-competency-ladder`  
**Tujuan:** mengaudit inventaris 127 kandidat menjadi unit kompetensi yang dapat diurutkan secara kumulatif dari mudah ke kompleks tanpa mengubah registry resmi.

## 1. Prinsip Audit

Satu `K` harus merupakan **satu kemampuan belajar yang dapat diuji**, bukan sekadar label bab besar. Karena itu:

- objek identifikasi dipisahkan dari penerapan struktur;
- objek yang merupakan kedalaman dari kompetensi sama ditautkan sebagai dependency, bukan dihitung sebagai kompetensi paralel tanpa hubungan;
- kompetensi analisis lanjutan tidak boleh ditempatkan sebelum bentuk permukaan yang menjadi prasyaratnya;
- contoh Qurani untuk `Kn` hanya boleh memerlukan `K1..Kn`;
- jumlah contoh tidak dibatasi 5; semua clean examples disimpan, lalu teaching set dapat dipilih 20–30+ sesuai kebutuhan.

## 2. Hasil Audit Inventaris Awal

### 2.1 Kandidat yang terlalu luas dan harus dipecah

- `mengenali isim` → perlu dibedakan pengenalan bentuk isim dari fungsi sintaksis isim;
- `mengenali fi'il` → dipisah dari madhi/mudhari'/amr dan tashrif;
- `harf/partikel` → tidak boleh menjadi satu K final karena fungsi partikel sangat beragam;
- `ma'rifah dan nakirah` → pengenalan `الـ` dapat lebih awal, sedangkan sistem ma'rifah lengkap membutuhkan dhamir, isim isyarah, maushul, idhafah, dll.;
- `mufrad, mutsanna, jama'` → perlu dependency sebelum tanda i'rab cabangnya;
- `i'rab operasional` → harus mengikuti struktur yang menyebabkan fungsi marfu'/manshub/majrur, bukan diajarkan sebagai blok abstrak terlebih dahulu;
- `struktur ayat kompleks` → endpoint integratif, bukan satu kompetensi elementer.

### 2.2 Kandidat yang merupakan gabungan target + prasyarat

Contoh:

- `jar–majrur` bergantung pada pengenalan huruf jar dan isim;
- `mubtada' + khabar isim mufrad` bergantung pada isim dan kemampuan membedakan dua fungsi nominal;
- `fi'il + fa'il + maf'ul bih` bergantung pada fi'il + fa'il;
- `isim maushul + shilah` bergantung pada isim maushul dan struktur jumlah yang dapat menjadi shilah;
- `inna`/`kana` bergantung pada jumlah ismiyyah dasar;
- na'at bergantung pada isim dan agreement yang relevan.

## 3. Frontier Kompetensi Dasar

Audit dependency menunjukkan bahwa kita belum boleh langsung menetapkan jumlah ismiyyah sebagai K1. Ada beberapa kemampuan atomik yang menjadi prasyarat lintas banyak struktur.

### Frontier A — pengenalan unit

Kandidat paling dasar:

1. mengenali **isim sebagai kategori kata** pada bentuk Qurani sederhana;
2. mengenali **fi'il sebagai kategori kata** pada bentuk Qurani sederhana;
3. mengenali **partikel tertentu sebagai unit fungsi**, bukan seluruh kategori harf sekaligus.

Namun ketiga objek ini tidak otomatis harus menjadi K1, K2, K3. Urutan final harus diuji dengan clean-example availability.

### Frontier B — fitur nominal dasar

Kandidat:

- `الـ` ta'rif;
- nakirah bertanwin pada bentuk sederhana;
- mufrad;
- mudzakkar/muannats yang tampak secara morfologis.

### Frontier C — relasi dua unsur paling sederhana

Kandidat:

- mubtada' + khabar isim sederhana;
- na'at–man'ut sederhana;
- idhafah dua isim sederhana;
- huruf jar + isim zhahir sederhana;
- 'athaf dua isim sederhana.

Kompetensi pada Frontier C tidak boleh ditempatkan sebelum fitur yang benar-benar diperlukan oleh contoh clean-nya.

## 4. Hipotesis Urutan Awal untuk Diuji — BUKAN FREEZE

Urutan berikut hanya kandidat eksperimen corpus:

| Posisi uji | Kandidat | Alasan dependency |
|---|---|---|
| P1 | isim sederhana | menjadi bahan dasar sebagian besar struktur nominal |
| P2 | `الـ` ta'rif | fitur permukaan sederhana dan sangat produktif |
| P3 | nakirah/tanwin nominal sederhana | membuka kontras definiteness dasar |
| P4 | jumlah ismiyyah: mubtada' + khabar isim sederhana | relasi predikatif dua isim |
| P5 | na'at–man'ut sederhana | membutuhkan dua unsur nominal dan agreement dasar |
| P6 | idhafah dua isim sederhana | relasi nominal tanpa partikel |
| P7 | huruf jar frekuen + isim zhahir | membuka jar–majrur |
| P8 | jar–majrur sebagai unit relasional | membangun dari P7 |
| P9 | dhamir munfashil | membuka mubtada' pronominal |
| P10 | dhamir muttashil nominal/preposisional dasar | membuka idhafah pronominal dan objek preposisi |

**Catatan:** P1–P10 bukan K final. Jika corpus menunjukkan bahwa P4 tidak mempunyai clean-example cukup tanpa fitur P5/P6, urutan harus direvisi.

## 5. Aturan Uji Corpus untuk Menetapkan K

Untuk setiap kandidat posisi `Pn`:

1. cari seluruh contoh Qurani yang mengandung target;
2. segmentasikan unit contoh terkecil yang tetap utuh secara linguistik;
3. anotasi semua kompetensi yang diperlukan oleh unit tersebut;
4. `PASS` jika seluruh dependency berada di `P1..Pn`;
5. `PREMATURE` jika ada dependency pada posisi sesudah `Pn`;
6. simpan seluruh `PASS`, tidak dibatasi jumlah;
7. hitung jumlah `PASS`, pola variasi, distribusi surah, dan konflik prematur;
8. jika clean-example terlalu sedikit atau dependency berulang menunjukkan urutan salah, pindahkan kandidat dan uji ulang.

## 6. Skema Evidence Bank

Setiap evidence nantinya minimal memuat:

| Field | Isi |
|---|---|
| Evidence-ID | ID kerja, belum permanen |
| Candidate-K | kompetensi target |
| Surah:Ayat | referensi sumber |
| Quranic-unit | teks Qurani yang dipakai |
| Unit-type | kata/frasa/klausa/ayat |
| Required-K | seluruh kompetensi yang diperlukan |
| Forbidden-hit | kompetensi prematur bila ada |
| Status | PASS / PREMATURE / REVIEW |
| Complexity | minimal / rendah / sedang / tinggi |
| Notes | catatan analisis |

## 7. Guardrail Integrasi

Dokumen ini tidak mengganti `REG-ARB-001`. Setelah urutan K stabil dan tervalidasi:

`research finding → review → Decision-ID bila diperlukan → mapping REG-ARB-001 → stage resmi → master/halaman/data/assessment`.

Dengan demikian hasil penelitian dapat dikonsumsi QURBATA, RIQA Education System, RIQA OS, RIQA Research Center, dan RIQA Formal Competency System tanpa membuat sumber kebenaran paralel.

## 8. Keputusan Kerja Batch Berikutnya

Batch berikutnya fokus pada **uji P1–P4**. Sasaran bukan memilih lima contoh, tetapi membangun bank contoh Qurani sebanyak mungkin yang lolos cumulative filter. Khusus P4, target uji pertama adalah struktur paling sederhana seperti `اللَّهُ الصَّمَدُ`, lalu dibandingkan dengan kandidat lain untuk memastikan bahwa contoh tidak diam-diam memerlukan kompetensi yang belum ditempatkan sebelumnya.
