# REG-ASM-QJ1-001 — Master Asesmen QURBATA Level 1

**Register-ID:** REG-ASM-QJ1-001  
**Versi:** 0.1.0-id  
**Status:** DRAFT TERKENDALI  
**Tanggal:** 29 Juli 2026  
**Pengendali:** QCF-QUR-003 dan QCF-QUR-L1-001  
**Cakupan:** Assessment-ID kandidat untuk Level 1 / Jilid 1  
**Cabang kerja:** `feature/qj1-master-structure`

## 1. Fungsi

Register ini menjadi sumber tunggal Assessment-ID Level 1. Instrumen, rubrik, formulir, aplikasi, dan laporan tidak boleh menggunakan Assessment-ID yang belum tercatat di sini.

Seluruh entri masih **CANDIDATE** atau **BLOCKED**. Tidak ada instrumen yang dinyatakan tervalidasi pada versi ini.

## 2. Struktur Data Minimum

| Field | Ketentuan |
|---|---|
| Assessment-ID | unik dan permanen |
| Domain | TIL, HIF, FAH, AMT, KHT |
| Competency-ID | kompetensi yang diukur |
| Mode | lisan, performa, observasi, atau portofolio |
| Sampel | unit/sampel yang diberikan |
| Dimensi | aspek mutu yang dinilai |
| Critical Error | kesalahan yang menggagalkan atau mewajibkan remedial |
| Evidence | bukti yang wajib disimpan |
| Retest | aturan uji ulang |
| Status | CANDIDATE, REVIEW, BLOCKED, ACTIVE, RETIRED |

## 3. Register Asesmen Tilawah

| Assessment-ID | Competency-ID | Mode | Fokus minimum | Evidence | Status |
|---|---|---|---|---|---|
| ASM-QJ1-TIL-001 | QCF-TIL-L1-001A | lisan/identifikasi | bentuk, titik, identitas | lembar skor atau rekaman | CANDIDATE |
| ASM-QJ1-TIL-002 | QCF-TIL-L1-001B | lisan | ketepatan bunyi dan harakat | lembar skor atau rekaman | CANDIDATE |
| ASM-QJ1-TIL-003 | QCF-TIL-L1-001C | lisan/kontras | pembedaan keluarga huruf | lembar analitik | CANDIDATE |
| ASM-QJ1-TIL-004 | QCF-TIL-L1-001D | performa baca | rangkaian dua unsur | lembar skor dan daftar kesalahan | CANDIDATE |
| ASM-QJ1-TIL-005 | QCF-TIL-L1-001E | performa baca | rangkaian tiga unsur | lembar skor dan daftar kesalahan | CANDIDATE |
| ASM-QJ1-TIL-006 | QCF-TIL-L1-001F | performa retensi | campuran lama, baru, dan transfer | rekaman/lembar retensi | CANDIDATE |

### Kesalahan kritis kandidat Tilawah

- menukar identitas huruf secara berulang;
- mengabaikan titik;
- menukar harakat;
- menghilangkan atau menambah unsur;
- menebak tanpa membaca urutan;
- ketergantungan penuh pada prompt guru.

Batas final belum ditetapkan dan wajib direview ahli Tilawah/asesmen.

## 4. Register Asesmen Hifzh

| Assessment-ID | Competency-ID | Mode | Fokus minimum | Evidence | Status |
|---|---|---|---|---|---|
| ASM-QJ1-HIF-001 | QCF-HIF-L1-001A | talqin-performa | ketepatan tiruan dan urutan | rekaman/lembar setoran | BLOCKED-VALIDATION |
| ASM-QJ1-HIF-002 | QCF-HIF-L1-001B | setoran lisan | urutan, ketepatan, kemandirian | rekaman/lembar setoran | BLOCKED-VALIDATION |
| ASM-QJ1-HIF-003 | QCF-HIF-L1-001C | murojaah dekat | mulai, sambung, selesai setelah jeda | rekaman/lembar retensi | BLOCKED-VALIDATION |

Materi, unit hafalan, batas kesalahan, dan interval murojaah belum boleh ditetapkan final sebelum blocker Tahfidz ditutup.

## 5. Register Asesmen Fahm

| Assessment-ID | Competency-ID | Mode | Fokus minimum | Evidence | Status |
|---|---|---|---|---|---|
| ASM-QJ1-FAH-001 | QCF-FAH-L1-001A | lisan/visual | hubungan lafaz dan makna dasar | lembar respons | CANDIDATE |
| ASM-QJ1-FAH-002 | QCF-FAH-L1-001B | lisan/kontekstual | penggunaan ulang kosakata | lembar respons | CANDIDATE |

Aktivasi mengikuti validasi register Bahasa Arab, gate siklus, dan keputusan P028.

## 6. Register Observasi Amal dan Tazkiyah

| Assessment-ID | Competency-ID | Mode | Fokus minimum | Evidence | Status |
|---|---|---|---|---|---|
| OBS-QJ1-AMT-001 | QCF-AMT-L1-001A | observasi berulang | adab menyimak dan giliran | catatan observasi | CANDIDATE |
| OBS-QJ1-AMT-002 | QCF-AMT-L1-001B | observasi berulang | respons terhadap koreksi | catatan observasi | CANDIDATE |
| OBS-QJ1-AMT-003 | QCF-AMT-L1-001C | observasi berulang | menjaga bahan belajar | catatan observasi | CANDIDATE |

Satu kejadian tunggal tidak cukup untuk menetapkan penguasaan atau kegagalan kecuali termasuk insiden safeguarding yang wajib ditangani melalui prosedur khusus.

## 7. Register Observasi Khidmah dan Tamkin

| Assessment-ID | Competency-ID | Mode | Fokus minimum | Evidence | Status |
|---|---|---|---|---|---|
| OBS-QJ1-KHT-001 | QCF-KHT-L1-001A | observasi performa | menyiapkan kegiatan sesuai arahan | catatan observasi | CANDIDATE |
| OBS-QJ1-KHT-002 | QCF-KHT-L1-001B | observasi performa | merapikan kegiatan secara aman | catatan observasi | CANDIDATE |

## 8. Rekapitulasi

| Domain | Jumlah Assessment-ID |
|---|---:|
| Tilawah | 6 |
| Hifzh | 3 |
| Fahm | 2 |
| Amal/Tazkiyah | 3 |
| Khidmah/Tamkin | 2 |
| **Total** | **16** |

## 9. Aturan Penguasaan Kandidat

Sebelum kriteria final tervalidasi, sistem hanya boleh menggunakan status:

- NOT-ASSESSED;
- EMERGING;
- DEVELOPING;
- PROVISIONAL-MASTERY;
- RETEST-REQUIRED;
- BLOCKED.

Status MASTERED, RETAINED, atau TRANSFERRED tidak boleh diaktifkan sebelum rubrik, batas kesalahan, interval retensi, dan Evidence-ID validasi tersedia.

## 10. Gate Aktivasi

1. blueprint tiap instrumen selesai;
2. sampel dan tingkat kesulitan diaudit;
3. rubrik analitik tersedia;
4. critical error dan remedial direview ahli;
5. safeguarding asesmen lulus review;
6. pilot instrumen dilakukan;
7. hasil pilot dianalisis;
8. Evidence-ID dan Decision-ID aktivasi tersedia.

## 11. Batas Klaim

- Register ini tidak menyatakan validitas atau reliabilitas instrumen.
- Tidak ada hasil peserta yang dicatat.
- Tidak ada Assessment-ID berstatus ACTIVE.
- Progres keluar-Draft tidak otomatis naik karena register dibuat.

## 12. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 29 Juli 2026 | Membentuk 16 Assessment-ID kandidat untuk seluruh objek kompetensi Level 1 |
