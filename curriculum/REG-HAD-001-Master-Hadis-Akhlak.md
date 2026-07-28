# REG-HAD-001 — Master Hadis Akhlak QURBATA

**Register-ID:** REG-HAD-001  
**Status:** DRAF TERKENDALI — REGISTER KOSONG TERSTRUKTUR  
**Tanggal:** 29 Juli 2026  
**Pengendali:** HCP-QUR-001  
**Cakupan:** Jilid 1–8

## 1. Fungsi

Register ini adalah sumber tunggal untuk memastikan hadis akhlak QURBATA bertahap, tidak berulang, terlacak sumbernya, dan tidak diaktifkan sebelum takhrij serta validasi ahli.

## 2. Aturan Identitas

- Format objek: HAD-000001, HAD-000002, dan seterusnya.
- Full-Hadith-ID menyatukan seluruh kutipan yang berasal dari hadis yang sama.
- Dua redaksi/riwayat tidak dianggap berbeda secara otomatis; ahli menentukan apakah keduanya satu objek, varian, syahid, atau objek terpisah.
- Pengulangan tema boleh; pengulangan Full-Hadith-ID sebagai materi baru dilarang.
- Nomor hadis dari platform atau edisi berbeda tidak boleh menjadi satu-satunya kunci deduplikasi.

## 3. Kolom Wajib

| Field | Isi |
|---|---|
| Hadith-ID | identitas unik QURBATA |
| Full-Hadith-ID | identitas hadis induk |
| Theme-ID | tema akhlak |
| Arabic-Text | teks tervokalisasi yang disajikan |
| Full-Text-Locator | lokasi teks lengkap |
| Indonesian-Meaning | terjemah terkendali |
| Companion | perawi sahabat |
| Primary-Collection | kitab sumber |
| Book/Chapter | kitab/bab |
| Hadith-Locator | nomor/edisi/locator |
| Grading | status penerimaan |
| Grading-Authority | ulama/lembaga/edisi penilai |
| Excerpt-Rationale | alasan dan keamanan penggalan |
| Jilid/Page-Intro | lokasi pengenalan |
| Review-Pages | lokasi murojaah |
| Literacy-Prerequisite | batas teks peserta/guru |
| Observable-Action | tindakan akhlak |
| Assessment-ID | asesmen |
| Reviewer-ID | ahli penelaah |
| Evidence-ID | bukti |
| Decision-ID | keputusan |
| Status | status workflow |

## 4. Register Objek

Belum ada Hadith-ID yang diaktifkan. Kandidat pertama hanya boleh dimasukkan setelah sumber dan mekanisme takhrij disepakati.

| Hadith-ID | Full-Hadith-ID | Tema | Jilid/Halaman | Sumber | Status |
|---|---|---|---|---|---|
| — | — | — | — | — | REGISTER READY; NO CANDIDATE ENTERED |

## 5. Register Tema Awal

Tema di bawah adalah ruang pencarian, bukan daftar hadis sah:

| Theme-ID | Tema | Tahap awal |
|---|---|---:|
| AKH-THM-001 | niat dan ikhlas | 1–8 bertingkat |
| AKH-THM-002 | kasih sayang | 1–8 bertingkat |
| AKH-THM-003 | salam dan adab perjumpaan | 1–4 |
| AKH-THM-004 | kebersihan dan kerapian | 1–4 |
| AKH-THM-005 | adab belajar dan ilmu | 1–8 |
| AKH-THM-006 | jujur dan amanah | 2–8 |
| AKH-THM-007 | sabar dan syukur | 2–8 |
| AKH-THM-008 | menjaga lisan | 3–8 |
| AKH-THM-009 | tolong-menolong dan kepedulian | 2–8 |
| AKH-THM-010 | maaf dan penyelesaian konflik | 4–8 |
| AKH-THM-011 | adil dan bertanggung jawab | 4–8 |
| AKH-THM-012 | kepemimpinan dan pelayanan | 6–8 |

## 6. Audit Deduplikasi

Sebelum aktivasi, pemeriksa wajib membandingkan matan lengkap dan kutipan, perawi, koleksi/jalur, kesamaan Full-Hadith-ID, seluruh Jilid 1–8, serta register retired/superseded. Hasil dicatat sebagai UNIQUE, VARIANT-REVIEW, atau DUPLICATE.

## 7. Blocker Awal

- pemilik akademik belum menetapkan panel ahli hadis/syar‘i;
- daftar kandidat 320 slot belum disusun;
- sumber teks/edisi dan standar locator belum diputuskan;
- takhrij, terjemah, whitelist literasi, dan safeguarding belum dijalankan;
- mapping Hadith-ID ke halaman Jilid 1–8 belum tersedia;
- Evidence-ID dan Decision-ID belum tersedia.

Karena itu register ini meningkatkan kesiapan arsitektur, bukan kesiapan terbit.
