# QURBATA Whole-Quran Source Policy

**Status:** ACTIVE AND BINDING  
**Scope:** seluruh produksi konten QURBATA Jilid 1–8.

## Keputusan

Seluruh Al-Qur'an 30 juz menjadi korpus sumber QURBATA. Pemilihan contoh tidak mengikuti urutan juz, surah, atau ayat, tetapi mengikuti kompetensi pembelajaran.

## Tujuan akhir

Lulusan QURBATA Jilid 1–8 harus siap membaca seluruh Al-Qur'an 30 juz. Karena itu bank data wajib mewakili:

- kata mudah, sedang, dan sulit;
- seluruh keluarga bentuk huruf;
- harakat pendek;
- mad;
- sukun;
- tanwin;
- tasydid;
- hamzah;
- alif-lam;
- tanda waqaf;
- frasa pendek dan panjang;
- potongan ayat;
- ayat utuh;
- variasi ortografi dan bentuk Utsmani yang relevan.

## Aturan pemilihan

1. Mesin mencari kandidat dari seluruh 30 juz.
2. Kandidat diberi tag kompetensi dan prasyarat.
3. Kandidat yang memiliki unsur belum aktif masuk `HOLD`.
4. Kandidat yang lolos diberi `DifficultyScore` dan `PedagogicalScore`.
5. Generator memilih contoh terbaik untuk kompetensi baru dan review kompetensi lama.
6. Review selalu menggunakan contoh berbeda selama bank data masih menyediakan alternatif yang layak.
7. Contoh dari satu juz tidak boleh mendominasi hanya karena lebih mudah ditemukan.

## Distribusi sumber

Setiap jilid harus secara bertahap memperluas representasi 30 juz. Distribusi tidak harus sama rata per halaman, tetapi pada akhir Jilid 8 bank aktif dan halaman buku harus memperlihatkan cakupan seluruh mushaf.

## Hubungan objek

```text
QWO satu kata
→ QPO frasa 2–5 kata
→ QAO potongan ayat/ayat utuh
→ QSO surah utuh
→ kesiapan membaca mushaf 30 juz
```

## Kedudukan Iqro'

Iqro' digunakan sebagai referensi pedagogis untuk:

- progression;
- kepadatan latihan;
- pengulangan kompetensi;
- transisi materi;
- pola peningkatan kesulitan.

Iqro' bukan batas sumber contoh. Contoh QURBATA dipilih dari seluruh Al-Qur'an dan disusun menurut struktur kompetensi QURBATA.

## Gate produksi

Sebuah objek baru belum boleh masuk buku apabila belum memiliki:

- rujukan surah dan ayat;
- teks tervokalisasi;
- kompetensi target;
- seluruh prasyarat;
- kompetensi kumulatif;
- skor kesulitan;
- skor pedagogis;
- jilid/halaman minimum;
- status verifikasi sumber.
