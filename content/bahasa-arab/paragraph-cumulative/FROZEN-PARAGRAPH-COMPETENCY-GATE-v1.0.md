# QURBATA Bahasa Arab — FROZEN Paragraph Competency Gate v1.0

Status: **FROZEN**
Tanggal freeze: 2026-08-16
Cakupan: Bahasa Arab QURBATA Jilid 1–8, P001–P040 per jilid (320 halaman)

## 1. Prinsip inti
Setiap halaman/materi QURBATA Bahasa Arab memiliki micro-text/paragraf kumulatif.

Paragraf pada suatu halaman **hanya boleh menggunakan kompetensi yang telah diajarkan sebelum atau pada halaman tersebut**.

Tidak boleh ada struktur, pola komunikatif, fungsi bahasa, atau kompetensi gramatikal yang baru akan diajarkan pada halaman berikutnya.

Rumus:

`LEGAL(Pn) = UNION(KOMPETENSI P001 ... Pn)`

Lintas jilid:

`LEGAL(Jx-Pn) = seluruh kompetensi J1 ... J(x-1) + kompetensi Jx P001 ... Pn`

Target audit wajib:

`NEW_COMPETENCY_LEAKAGE = 0`

## 2. Yang dimaksud kompetensi
Gate berlaku bukan hanya pada kosakata. Yang diaudit sekurang-kurangnya:
- pola/struktur kalimat;
- fungsi komunikatif;
- bentuk pertanyaan dan jawaban;
- bentuk fi'il/waktu yang telah diajarkan;
- dhamir dan rujukan;
- penghubung/relasi antarkalimat;
- negasi;
- alasan/sebab;
- perbandingan;
- urutan/sekuens;
- pola instruksi/respons;
- pola evaluasi, koreksi, refleksi, dan rencana belajar.

Kosakata baru tidak boleh diam-diam menjadi kendaraan bagi kompetensi struktur yang belum legal.

## 3. Bentuk teks bertahap
Panjang teks tidak dipaksakan sama pada seluruh halaman.

- Tahap kompetensi sangat awal: micro-text 2–3 kalimat.
- Setelah corpus legal membesar: 3–5 kalimat.
- Tahap menengah: 4–6 kalimat yang saling terhubung.
- Tahap lanjut: paragraf/wacana utuh sesuai kompetensi legal.

Prinsip: **lebih pendek tetapi 100% legal lebih baik daripada panjang dengan leakage.**

## 4. Sifat kumulatif
Paragraf bukan tempat mengajarkan materi baru. Fungsinya adalah:
1. retrieval kompetensi lama;
2. integrasi kompetensi lama + kompetensi halaman berjalan;
3. produksi Bahasa Arab;
4. penguatan konteks belajar Al-Qur'an dan komunikasi sehari-hari yang relevan;
5. bahan latihan dikte Indonesia → Arab.

## 5. Aturan dikte Indonesia → Arab
Untuk setiap micro-text/paragraf disiapkan pasangan makna Bahasa Indonesia yang dapat dibacakan guru.

Peserta mendengar teks Indonesia lalu menuliskan Bahasa Arab berdasarkan kompetensi yang sudah legal.

Versi Indonesia tidak boleh memaksa penggunaan struktur Arab yang belum diajarkan.

## 6. Hubungan dengan TARTIL QURBATA
Kemampuan menulis Arab tetap mengikuti ceiling kemampuan TARTIL pada jilid/halaman terkait. Kompetensi Bahasa Arab tidak boleh memaksa bentuk tulisan yang melampaui kemampuan baca-tulis QURBATA TARTIL pada tahap tersebut.

## 7. Gate per halaman
Setiap halaman harus memiliki data minimal:

- `page_id`
- `new_competency`
- `legal_competencies`
- `forbidden_future_competencies`
- `micro_text_id`
- `indonesian_dictation_text`
- `arabic_target_text`
- `competency_trace`
- `leakage_count`
- `audit_status`

Status PASS hanya jika:

`leakage_count = 0`

## 8. Gate lintas jilid
- Jilid 1: hanya kompetensi J1 sampai halaman berjalan.
- Jilid 2: seluruh kompetensi legal J1 + J2 sampai halaman berjalan.
- Jilid 3: seluruh kompetensi legal J1–J2 + J3 sampai halaman berjalan.
- Jilid 4: seluruh kompetensi legal J1–J3 + J4 sampai halaman berjalan.
- Jilid 5: seluruh kompetensi legal J1–J4 + J5 sampai halaman berjalan.
- Jilid 6: seluruh kompetensi legal J1–J5 + J6 sampai halaman berjalan.
- Jilid 7: seluruh kompetensi legal J1–J6 + J7 sampai halaman berjalan.
- Jilid 8: seluruh kompetensi legal J1–J7 + J8 sampai halaman berjalan.

## 9. Quality gate
Sebelum paragraf dianggap final, wajib lulus:

1. `COMPETENCY_LEAKAGE = 0`
2. tidak ada grammar feature masa depan;
3. tidak ada communicative function masa depan;
4. sesuai ceiling TARTIL;
5. teks alami dan dapat digunakan guru;
6. versi Indonesia dan Arab ekuivalen pada kompetensi yang sedang diuji;
7. kompetensi lama muncul secara kumulatif dan proporsional, tidak sekadar mengulang satu pola.

## 10. Perubahan setelah freeze
Dokumen ini adalah baseline v1.0. Perubahan substantif tidak dilakukan diam-diam. Setiap perubahan aturan wajib membuat versi baru dan mencatat alasan perubahan.

---

**FROZEN DECISION:** QURBATA Bahasa Arab 1–8 menggunakan cumulative paragraph competency gate dengan target absolut `NEW_COMPETENCY_LEAKAGE = 0`.