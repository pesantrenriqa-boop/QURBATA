# K01 — Mengenali Isim Dasar

**Kode:** REC-N-BASE  
**Layer:** A — Fondasi Pengenalan  
**Status materi:** CONTENT COMPLETE / QURAN EVIDENCE VERIFIED / EXPERT REVIEW PENDING  
**Prasyarat:** tidak ada  
**Standar:** COMPETENCY-AUTHORING-STANDARD-v1.0

## 1. Capaian Kompetensi
Peserta mampu mengenali kata yang berfungsi sebagai **isim** pada contoh Al-Qur'an sederhana, tanpa dituntut menentukan kedudukan i'rab atau fungsi sintaksisnya.

## 2. Pemantik Qurani — لاحظ
Amati kata-kata berikut.

- **ٱللَّهُ** — Al-Fatihah 1:2
- **رَبِّ** — Al-Fatihah 1:2
- **يَوْمِ** — Al-Fatihah 1:4
- **ٱلنَّاسِ** — An-Nas 114:1

Pertanyaan pengamatan: Apakah kata-kata tersebut menunjukkan nama, makhluk, benda, waktu, tempat, sifat/sebutan, atau sesuatu yang dapat disebut sebagai nama?

## 3. Temukan Polanya — اكتشف
Peserta mengelompokkan contoh Qurani yang menunjukkan nama khusus, manusia/makhluk, benda/konsep, waktu, tempat, dan sifat/sebutan. Fokus awal adalah mengenali kategori kata, bukan menghafal definisi panjang.

## 4. Pahami Kaidah — افهم
**Isim (الاسم)** adalah kata yang menunjukkan makna pada dirinya dan tidak terikat dengan waktu sebagai bagian dari maknanya. Pada tahap K01, peserta cukup mampu mengenali contoh isim yang jelas.

### Batas K01
- belum menentukan mubtada, khabar, fa'il, maf'ul, mudhaf, atau fungsi sintaksis lain;
- belum menjadikan tanda i'rab sebagai target;
- belum membahas ma'rifah–nakirah sebagai target;
- belum membahas alif-lam sebagai target khusus;
- belum membahas idhafah sebagai target.

### Kesalahan umum
1. Menganggap isim hanya berarti benda konkret.
2. Menganggap setiap kata berawalan ال otomatis cukup dianalisis hanya dari ال.
3. Langsung menentukan i'rab sebelum mampu mengenali kategori katanya.

## 5. Bank Contoh Qurani Bertingkat — حلّل
Bank canonical lengkap disimpan pada `quran-examples.json` dan telah melalui QA evidence Qurani. README hanya menampilkan subset pengajaran.

| No | Contoh | Rujukan | Target | Makna ringkas | Catatan K01 |
|---|---|---|---|---|---|
| 1 | ٱللَّهُ | Al-Fatihah 1:2 | ٱللَّهُ | Allah | nama khusus |
| 2 | رَبِّ | Al-Fatihah 1:2 | رَبِّ | Tuhan/Pemelihara | sebutan |
| 3 | يَوْمِ | Al-Fatihah 1:4 | يَوْمِ | hari | waktu |
| 4 | ٱلدِّينِ | Al-Fatihah 1:4 | ٱلدِّينِ | pembalasan/agama sesuai konteks | konsep |
| 5 | ٱلصِّرَاطَ | Al-Fatihah 1:6 | ٱلصِّرَاطَ | jalan | benda/konsep |
| 6 | ٱلنَّاسِ | An-Nas 114:1 | ٱلنَّاسِ | manusia | kelompok makhluk |
| 7 | مَلِكِ | An-Nas 114:2 | مَلِكِ | Raja | sebutan |
| 8 | شَرِّ | Al-Falaq 113:2 | شَرِّ | kejahatan | konsep |
| 9 | ٱلْفَلَقِ | Al-Falaq 113:1 | ٱلْفَلَقِ | fajar | konsep/waktu |
| 10 | أَحَدٌ | Al-Ikhlas 112:1 | أَحَدٌ | Esa | sifat/sebutan |
| 11 | ٱلصَّمَدُ | Al-Ikhlas 112:2 | ٱلصَّمَدُ | tempat bergantung/Yang Mahasempurna | sebutan |
| 12 | نَصْرُ | An-Nasr 110:1 | نَصْرُ | pertolongan | konsep |

## 6. Mufradat K01
Bank canonical disimpan pada `vocabulary.json`. Kosakata K01 berfungsi sebagai exposure/receptive vocabulary; productive vocabulary untuk Bi'ah dikelola pada jalur terpisah.

## 7. Latihan Terbimbing — طبّق
1. Tandai kata yang merupakan isim pada potongan Qurani.
2. Cocokkan isim dengan makna ringkasnya.
3. Kelompokkan isim: nama khusus / manusia-makhluk / waktu / konsep / sebutan.
4. Bandingkan dua kata dan tentukan mana yang dapat dikenali sebagai isim.
5. Temukan kembali isim yang pernah muncul pada contoh sebelumnya.

Bank lengkap disimpan pada `assessment.json`.

## 8. Latihan Analisis/Transfer
Potongan ayat baru digunakan agar peserta menemukan target isim tanpa menentukan i'rab atau fungsi sintaksisnya. Item transfer tidak sekadar mengulang contoh pengajaran.

## 9. Uji Kompetensi
Bank tersedia sebanyak **30 item**, mencakup recognition, comprehension, application, analysis, dan transfer. Jawaban serta pembahasan melekat pada data assessment agar dapat dipisahkan saat produksi buku siswa.

Kriteria mastery pilot: minimal 8/10 benar dengan sekurang-kurangnya 1 item transfer benar. Ambang ini belum dianggap final sebelum pilot/validasi asesmen.

## 10. Tadabbur & Transfer Makna
Peserta menyadari bahwa satu ayat dapat memuat nama Allah, manusia, waktu, konsep, dan sebutan. Struktur bahasa dipelajari untuk membantu membaca makna Al-Qur'an secara lebih sadar, bukan sekadar menghafal istilah nahwu.

## Catatan untuk jalur Bi'ah
K01 menjadi rujukan `first_allowed_competency` bagi item Bi'ah yang target produksinya hanya membutuhkan pengenalan isim. Materi Bi'ah tidak dimasukkan sebagai contoh Qurani dan disimpan pada corpus terpisah.

## Production Gate K01
- [x] capaian dan boundary ditetapkan
- [x] pola 10 komponen diterapkan
- [x] ≥10 kandidat contoh Qurani terkumpul
- [x] bank mufradat tersedia
- [x] seluruh teks/rujukan evidence Qurani diverifikasi QA
- [x] `quran-examples.json` tersedia dan menjadi bank canonical K01
- [x] `vocabulary.json` tersedia
- [x] bank 25–40 latihan/soal — **30 item tersedia**
- [x] answer key + pembahasan tersedia di `assessment.json`
- [x] `teacher-notes.md` tersedia
- [ ] review ahli Bahasa Arab/nahwu
- [ ] review ahli pembelajaran Bahasa Arab
- [ ] validasi mastery threshold melalui pilot
- [ ] K01 FROZEN v1.0

### Aturan status
Checklist hanya boleh dibiarkan kosong jika pekerjaan memang belum dilakukan. Setiap artifact yang sudah tersedia wajib segera disinkronkan pada Production Gate agar status repo mencerminkan kondisi aktual.
