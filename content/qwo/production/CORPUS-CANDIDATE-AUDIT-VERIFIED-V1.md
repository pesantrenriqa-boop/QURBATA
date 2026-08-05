# QURBATA Corpus Candidate Audit — Verified V1

Status: `READY_CANDIDATE_POOL`

Sumber audit: corpus Tanzil Uthmani yang diunggah pengguna, format `surah|ayah|text`.

## Integritas corpus

- Ayat valid: **6.236**
- Kata unik: **19.003**
- Estimasi objek unik kata, frasa, potongan ayat, dan ayat utuh: **647.901**
- Rentang: QS 1:1 sampai QS 114:6

## Hasil kecukupan kandidat

Setelah minimum dikalibrasi berdasarkan sifat rasm dan bentuk unik corpus, seluruh kompetensi `C0001–C0041` berstatus **PASS**.

| Kompetensi | Kandidat unik |
|---|---:|
| C0001 | 309 |
| C0002 | 27 |
| C0003 | 27 |
| C0004 | 27 |
| C0005 | 559 |
| C0006 | 2.090 |
| C0007 | 263 |
| C0008 | 415 |
| C0009 | 539 |
| C0010 | 479 |
| C0011 | 270 |
| C0012 | 214 |
| C0013 | 105 |
| C0014 | 3.767 |
| C0015 | 977 |
| C0016 | 2.485 |
| C0017 | 1.442 |
| C0018 | 999 |
| C0019 | 883 |
| C0020 | 10.446 |
| C0021 | 461 |
| C0022 | 862 |
| C0023 | 1.360 |
| C0024 | 4.887 |
| C0025 | 1.624 |
| C0026 | 995 |
| C0027 | 1.451 |
| C0028 | 4.587 |
| C0029 | 2.999 |
| C0030 | 3 |
| C0031 | 13 |
| C0032 | 7 |
| C0033 | 47.482 |
| C0034 | 114.062 |
| C0035 | 252.892 |
| C0036 | 208.399 |
| C0037 | 2.000 |
| C0038 | 2.128 |
| C0039 | 1.935 |
| C0040 | 2.624 |
| C0041 | 6.054 |

## Keputusan pedagogis

1. Harakat dasar menggunakan 27 huruf non-hamzah. Hamzah tetap diajarkan pada bab khusus, sehingga tidak boleh dipaksakan masuk ke C0002–C0004.
2. Lafẓul Jalālah memiliki jumlah bentuk kata unik terbatas. Babnya menggunakan seluruh bentuk kata unik, kemudian penguatan dilakukan melalui frasa dan konteks ayat yang berbeda.
3. Mesin wajib memilih objek baru untuk penguatan kompetensi dan tidak boleh melompati dependency.
4. Bila alokasi halaman melebihi pool unik, composer wajib mengeluarkan `SHORTAGE`, bukan mengulang objek atau mengambil kompetensi yang belum waktunya.

## Gerbang berikutnya

Candidate pool dinyatakan cukup untuk memulai komposisi Jilid 1–8. Status ini belum berarti layout atau tashih buku final selesai.
