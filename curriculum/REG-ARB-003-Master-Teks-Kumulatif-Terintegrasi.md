# REG-ARB-003 — Master Teks Kumulatif Terintegrasi

**Register-ID:** REG-ARB-003  
**Status:** DRAF TERKENDALI  
**Tanggal:** 28 Juli 2026  
**Pengendali:** STD-ARB-002  
**Cakupan:** seluruh siklus pembelajaran Bahasa Arab QURBATA Jilid 1–8

## 1. Pola ID

- microtext/paragraf: AR-TXT-xxxxxx;
- pertanyaan pemahaman: AR-TQ-xxxxxx;
- tugas produksi: AR-TP-xxxxxx.

## 2. Kendali Siklus dan Ketuntasan

Setiap entri Text-ID wajib mencatat Cycle-ID, pelajaran akuisisi prasyarat, Integration-Lesson-ID, status gerbang, dan Evidence-ID. Teks pilot belum boleh dipetakan final ke halaman sebelum bukti gerbang tersedia.

## 3. Teks Pilot Pertama

### AR-TXT-000001 — Adab Belajar di Kelas

**Status:** CANDIDATE  
**Integration-Type:** AKHLAQ  
**Stage maksimum:** AR-STG-007  
**Sumber nilai:** adab menjaga kebersihan, duduk tertib, membaca, dan menyimak; belum dikaitkan sebagai kutipan hadis/ayat.

**Teks Arab:**

> هٰذَا فَصْلٌ نَظِيفٌ. يَدْخُلُ الطَّالِبُ الْفَصْلَ. يَجْلِسُ الطَّالِبُ عَلَى الْكُرْسِيِّ. يَفْتَحُ الْمُعَلِّمُ الْمُصْحَفَ. يَقْرَأُ الطَّالِبُ الْكِتَابَ. يَسْمَعُ الطَّالِبُ الْمُعَلِّمَ.

**Arti:**

> Ini ruang kelas yang bersih. Pelajar masuk ke ruang kelas. Pelajar duduk di kursi. Guru membuka mushaf. Pelajar membaca buku. Pelajar mendengar guru.

## 4. Audit Unsur AR-TXT-000001

| Jenis | Objek |
|---|---|
| Review kosa kata | فَصْلٌ، طَالِبٌ، كُرْسِيٌّ، مُعَلِّمٌ، مُصْحَفٌ، كِتَابٌ |
| Review sifat | نَظِيفٌ |
| Review verba | دَخَلَ، جَلَسَ، فَتَحَ، قَرَأَ، سَمِعَ melalui bentuk mudhari‘ |
| Bentuk turunan | يَدْخُلُ، يَجْلِسُ، يَفْتَحُ، يَقْرَأُ، يَسْمَعُ |
| Struktur | AR-GRM-000005, AR-GRM-000010–11 |
| Pola | AR-PAT-000005, AR-PAT-000010 |
| Kosa kata baru tersembunyi | NIHIL |
| Kutipan ayat/hadis | TIDAK |

Semua lema pernah diperkenalkan pada LEX-ARB-001–003. Teks tidak menambah hitungan baseline 40.

## 5. Tugas Pilot

| ID | Tugas | Keterampilan |
|---|---|---|
| AR-TQ-000001 | Di mana pelajar duduk? | pemahaman rinci |
| AR-TQ-000002 | Siapa yang membuka mushaf? | pemahaman pelaku |
| AR-TQ-000003 | Apa yang dibaca pelajar? | pemahaman objek |
| AR-TP-000001 | Ceritakan kembali dengan bantuan gambar/objek | berbicara |
| AR-TP-000002 | Ganti satu benda atau pelaku memakai kosa kata lama | transfer |
| AR-TP-000003 | Dengarkan ulang setelah jeda dan urutkan peristiwa | retensi |

Pertanyaan dapat disampaikan dalam Bahasa Indonesia pada tahap awal. Versi Arab hanya dibuka setelah struktur pertanyaan tersedia.

## 6. Aturan Penempatan

- satu Text-ID direncanakan untuk setiap siklus yang telah mencapai status SIAP INTEGRASI;
- pelajaran pengenalan kosa kata, latihan kata, frasa, atau pola sebelum gerbang tidak wajib memuat Text-ID;
- Text-ID ditempatkan pada pelajaran integrasi/murojaah setelah kosa kata dan struktur prasyarat cukup dikuasai;
- teks tidak menunggu seluruh kosa kata satu jilid selesai; gerbang berlaku per unit kompetensi;
- teks awal dapat diajarkan secara lisan sebelum boleh dibaca;
- satu teks boleh kembali pada pelajaran lain sebagai murojaah, tetapi tidak menjadi Text-ID baru;
- versi perluasan mempunyai Version-ID atau Parent-Text-ID;
- teks tidak boleh dipetakan final ke halaman sebelum Arabic progression disahkan.

## 7. Status Produksi

| Cakupan | Target sistem | Tersedia | Status |
|---|---:|---:|---|
| Teks integrasi Jilid 1 | mengikuti jumlah siklus yang lulus gerbang | 1 | PILOT—BELUM DIPETAKAN |
| Teks Jilid 2–8 | menunggu pemetaan | 0 | UNMAPPED |

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.2.0-id | 28 Juli 2026 | Penempatan Text-ID dikunci per siklus setelah gerbang ketuntasan |
| 0.1.0-id | 28 Juli 2026 | Register dibentuk dan microtext pilot pertama ditambahkan |
