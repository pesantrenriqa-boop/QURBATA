# MAT-CUR-QJ1-001 — Matriks Murojaah dan Distribusi Jilid 1

**Kode Dokumen:** MAT-CUR-QJ1-001  
**Status:** Draf Terkendali — Audit Korektif Berjalan  
**Versi:** 0.3.0-id  
**Tanggal:** 28 Juli 2026  
**Pemilik Akademik:** Aris Liswanto  
**Keputusan Pengendali:** DEC-CUR-001  
**Cakupan:** QJ1-P001–QJ1-P040  

## 1. Tujuan

Matriks ini mengendalikan pemerataan identitas huruf, harakat, materi fokus, murojaah kumulatif, jarak pengulangan, dan Keselarasan Leksikal Qurani. Angka baseline berikut berasal dari 30 halaman baca yang tersedia pada QJ1-P001–QJ1-P032; QJ1-P018 dan QJ1-P028 merupakan unit khusus tanpa tangga baca.

## 2. Baseline Sebelum Koreksi

| Huruf | Kemunculan | Huruf | Kemunculan | Huruf | Kemunculan |
|---|---:|---|---:|---|---:|
| ء | 55 | أ/إ | 80 | ب | 113 |
| ت | 96 | ث | 91 | ج | 64 |
| ح | 59 | خ | 52 | د | 68 |
| ذ | 58 | ر | 56 | ز | 56 |
| س | 71 | ش | 73 | ص | 80 |
| ض | 74 | ط | 78 | ظ | 74 |
| ع | 72 | غ | 69 | ف | 74 |
| ق | 68 | ك | 67 | ل | 66 |
| م | 47 | ن | 46 | ه | 46 |
| و | 32 | ي | 35 | — | — |

Rentang baseline adalah **32–113**, sehingga rasio identitas tertinggi terhadap terendah mencapai **3,53:1**. Bentuk أ/إ berjumlah 80 dan bukan yang paling sedikit, tetapi distribusinya terkonsentrasi dan hilang pada banyak halaman.

## 3. Aturan Halaman

| Jenis Halaman | Fokus/Materi Baru | Murojaah | Ketentuan |
|---|---:|---:|---|
| Akuisisi pertama QJ1-P001 | 64 | 0 | Belum ada prasyarat |
| Akuisisi berikutnya | 32 | 32 | Semua identitas prasyarat; harakat seimbang |
| Integrasi/penguatan/simulasi | 0 | 64 | Cakupan kumulatif dan transfer |
| Evaluasi | 0 | 64 | Sampel terstratifikasi dan bentuk paralel |
| Hafalan/Bahasa Arab/Akhlak | N/A | N/A | Murojaah lisan/bermakna; klaim baca dipisahkan |

## 4. Jadwal Murojaah

| Tahap | Kewajiban |
|---|---|
| N | Materi diperkenalkan |
| N+1 | Pengulangan langsung |
| N+2 | Penguatan dekat |
| N+4 | Retensi menengah |
| N+8 | Retensi lanjut |
| Rotasi | Masuk pemerataan kumulatif |
| Siklus 3 halaman | Seluruh kombinasi huruf–harakat yang sah tercakup |

## 5. Audit Per Halaman

Setiap halaman baca wajib mempunyai catatan mesin berikut:

| Field | Isi |
|---|---|
| Token total | 64 |
| Token fokus | 64 pada P001; 32 pada akuisisi lain; 0 pada integrasi/evaluasi |
| Token murojaah | 0 pada P001; 32 pada akuisisi lain; 64 pada integrasi/evaluasi |
| Identitas huruf eligible | Daftar huruf yang sudah sah |
| Identitas hadir | Daftar aktual |
| Harakat eligible | Fathah/kasrah/dhammah yang sudah sah |
| Distribusi harakat | Jumlah aktual per harakat |
| Jadwal N+1/N+2/N+4/N+8 | Lulus/gagal |
| Siklus tiga halaman | Kombinasi belum tercakup |
| Tag leksikal | QLX-Q / QLX-A / CTL |
| Pengecualian | Alasan dan Decision-ID |

## 6. Keselarasan Leksikal Qurani

Kandidat akar prioritas awal untuk diversifikasi tiga huruf:

| Pola | Arah Makna | Status |
|---|---|---|
| ك ت ب | kitab/menulis | Kandidat—verifikasi wajib |
| ع ل م | ilmu/mengetahui | Kandidat—verifikasi wajib |
| ر ح م | rahmat | Kandidat—verifikasi wajib |
| ح م د | pujian | Kandidat—verifikasi wajib |
| س ل م | keselamatan | Kandidat—verifikasi wajib |
| ع ب د | penghambaan | Kandidat—verifikasi wajib |
| غ ف ر | ampunan | Kandidat—verifikasi wajib |
| ص ب ر | kesabaran | Kandidat—verifikasi wajib |
| ذ ك ر | mengingat | Kandidat—verifikasi wajib |
| ق ر أ | membaca | Kandidat—verifikasi wajib |

Tag tersebut merupakan metadata penyusun. Huruf yang tampil terpisah tetap latihan bunyi dan tidak boleh dilabeli sebagai kata peserta.

## 7. Status Koreksi

| Cakupan | Status |
|---|---|
| Kebijakan dan aturan pengendali | Draf tersedia |
| CUR-QJ1-001 | Dalam pembaruan |
| QJ1-MASTER | Dalam pembaruan |
| QJ1-P001–QJ1-P032 | Wajib revisi |
| QJ1-P033–QJ1-P040 | Belum diproduksi; wajib aturan baru |
| Audit akhir distribusi | Belum dilakukan |
| Penelaahan akademik/Bahasa Arab/asesmen | Menunggu |

## 8. Gate

- [ ] seluruh halaman akuisisi memenuhi pembagian token yang berlaku;
- [ ] seluruh identitas huruf memenuhi jadwal;
- [ ] distribusi harakat lulus pemerataan;
- [ ] seluruh kombinasi eligible tercakup dalam siklus tiga halaman;
- [ ] seluruh tag QLX diverifikasi sumber dan maknanya;
- [ ] tidak ada bentuk sambung, mad, tanwin, sukun, atau tasydid prematur;
- [ ] audit independen dan persetujuan QC-007 selesai.


## 6C. Pemerataan Mutlak — DEC-CUR-002

1. Semua identitas huruf yang telah dipelajari hadir di setiap halaman baca berikutnya.
2. Jumlah antarahuruf berbeda maksimal satu token.
3. Harakat dibagi seimbang di dalam jatah tiap identitas; bentuk yang belum diajarkan tetap dilarang.
4. Materi baru mendapat penekanan pada posisi tangga, talqin, dan talaqqi, bukan dominasi jumlah.
5. Setelah 29 identitas selesai, setiap identitas muncul dua atau tiga kali pada halaman 64 token.
6. Kombinasi huruf–harakat penuh ditutup melalui siklus maksimal dua halaman.
7. DEC-CUR-002 menggantikan ketentuan alokasi 50:50 dalam DEC-CUR-001.
