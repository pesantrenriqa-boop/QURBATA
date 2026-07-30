# AUD-QJ3-001 — Audit Tahap I QURBATA Jilid 3

**Kode:** AUD-QJ3-001  
**Versi:** 1.0.0-id  
**Status:** COMPLETE-MECHANICAL / LEXICAL-SOURCE OPEN  
**Tanggal:** 30 Juli 2026  
**Cakupan:** QJ3-P001–P040  
**Cabang:** feature/qj1-master-structure

## 1. Ringkasan hasil

| Pemeriksaan | Hasil |
|---|---|
| Batch materi tersedia | 8/8 |
| Halaman terdeteksi | 40 |
| Kode unik | 40 |
| Rentang | P001–P040 |
| Halaman hilang | 0 |
| Klaim per batch | 120 kotak |
| Total struktural | 960 kotak |
| Tanda tasydid pada delapan dokumen materi | 0 |
| Istilah idzhar/ikhfa/idgham/iqlab | 0 |
| Regresi eksplisit tangga dua huruf | 0 |
| Status cetak | BELUM LULUS |

Total 960 adalah kelulusan struktur dokumen. Normalisasi token per kotak, tashih bahasa Arab, rasm, qira’at, audio, dan sumber belum selesai.

## 2. Kelulusan mekanis

1. P001–P040 lengkap dan tidak duplikat.
2. Setiap batch B01B, B01C, B02A, B02B, B03A, B03B, B04A, B04B berisi lima halaman.
3. Tangga tidak kembali ke huruf tunggal atau dua huruf.
4. Kompleksitas meningkat dari kata 3 huruf menuju 8+ huruf dan frasa.
5. P020/P030 memakai checkpoint awā’il berbeda; P040 tidak mengulang awā’il.
6. Frasa akhir mempunyai locator ayat dan registry; tidak ada frasa yang dinyatakan hasil rangkaian kata berjauhan.
7. Materi menyatakan larangan tasydid, syamsiyah, sukun qalqalah, dan hubungan tajwid antarkata prematur.

## 3. Antrean tashih leksikal prioritas A

Kandidat berikut tidak boleh masuk whitelist sebelum tashih. Bila makna, ضبط, frekuensi, atau kelayakan anak lemah, langsung ganti.

| Halaman | Kandidat |
|---|---|
| P013 | بَغْيٌ، شَغْبٌ، دَغْلٌ |
| P014 | جُؤْرٌ |
| P016 | خُضْرٌ، نَضْرٌ، حَضْرٌ، عَضْلٌ، رَضْعٌ |
| P017 | كَظْمٌ، يَظْعَنُ، مَظْرُوفٌ، مَظْفُورٌ |
| P023 | مِلْحَفٌ، مِلْقَطٌ، مُلْتَقًى، مُلْتَحِفٌ |
| P024–P025 | مُسْتَلْهِمٌ، مُسْتَلْحَقٌ، مُسْتَلْطَفٌ |
| P026–P030 | seluruh variasi kasus pedagogis اَلْفَمُ/اَلْفَمَ/اَلْفَمِ dan اَلْأَبُ/اَلْأَبَ/اَلْأَبِ |
| P031–P040 | seluruh bentuk panjang/maṣdar/partisipel yang belum memiliki lema dan makna terdaftar |

## 4. Antrean ortografi dan rasm prioritas A

1. Tetapkan satu kebijakan tampilan: pedagogis `اَلْ` atau rasm `ٱلْ`; jangan bercampur tanpa fungsi.
2. Audit kursi hamzah pada P014 dan P029.
3. Audit alif maqṣūrah, tanwin fatḥah, tā’ marbūṭah, dan tanda mad.
4. Audit apakah berhenti pada akhir kotak mengubah tanwin atau bentuk waqaf yang belum diajarkan.
5. P037–P040 wajib memakai teks mushaf acuan yang sama, bukan vokalisasi umum yang diketik ulang.

## 5. Audit klasifikasi fokus–transfer

- يَعْلَمُونَ = transfer عْ + mad wāw; bukan fokus لْ.
- Bentuk ـُونَ lain harus dilabeli menurut huruf yang benar-benar menyandang sukun.
- Kata ber-ال pada P026–P032 adalah fokus qamariyah; kata ber-ال pada P033–P040 menjadi transfer.
- Tanwin pada P034/P038 hanya dinilai di dalam kata; hubungan antarkata tetap ditahan.
- Frasa yang diulang pada P038–P040 adalah retensi/evaluasi, bukan materi baru.

## 6. Audit frasa Qurani

### Kandidat lanjut tashih
- ٱلْكِتَابُ لَا رَيْبَ
- ٱلْكِتَابُ لَا رَيْبَ فِيهِ
- ٱلْيَوْمَ يَئِسَ
- ٱلْيَوْمَ أَكْمَلْتُ
- ٱلْعَفْوَ وَأْمُرْ
- ٱلْيَوْمَ نَخْتِمُ
- ٱلْيَوْمَ نَخْتِمُ عَلَىٰ
- عَلَىٰ أَفْوَاهِهِمْ
- بِمَا كَانُوا يَكْسِبُونَ

### Gate
- cocokkan huruf per huruf dengan mushaf;
- tetapkan titik mulai dan akhir;
- periksa dependency sambungan;
- sediakan Source-ID, audio ahli, dan keputusan reviewer;
- bila satu dependency gagal, seluruh frasa tetap HOLD.

## 7. Audit pemerataan yang masih terbuka

- frekuensi setiap huruf pembawa sukun P001–P040;
- distribusi tiga harakat sebelum sukun;
- distribusi tiga mad;
- distribusi tiga tanwin;
- bentuk awal–tengah–akhir dan huruf pemutus;
- pengulangan N+1/N+2/N+4/N+8;
- rasio fokus–murojaah setiap halaman;
- jumlah lema unik versus pengulangan;
- keterwakilan pola Qurani ـُونَ dan pola eligible lain.

## 8. Gate menuju Tahap II

1. Normalisasi 960 kotak menjadi data per item.
2. Beri Item-ID, Page-ID, target, panjang kata, pola, status fokus/review, dan Source-ID.
3. Jalankan audit otomatis larangan dan pemerataan.
4. Tashih daftar prioritas A.
5. Regenerasi item yang gagal.
6. Baru lakukan audit Tahfidz, Bahasa Arab, hadis/akhlak, NIDOM, dan layout.

## 9. Keputusan

Jilid 3 tetap **COMPLETE-DRAFT**, bukan SIAP UJI/CETAK. Struktur 40 halaman lulus audit tahap I; isi leksikal, rasm, sumber, audio, pemerataan, dan review ahli masih OPEN.
