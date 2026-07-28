# REG-HAD-001 — Master Hadis Akhlak QURBATA

**Register-ID:** REG-HAD-001  
**Status:** DRAF TERKENDALI — 8 KANDIDAT SOURCE-CHECK; 0 APPROVED  
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

Delapan kandidat awal telah dimasukkan melalui BAT-HAD-001. Tidak ada Hadith-ID yang diaktifkan; semua masih memerlukan takhrij, review penggalan, terjemah, pedagogi, safeguarding, dan keputusan ahli.

| Hadith-ID | Full-Hadith-ID | Tema | Jilid/Halaman | Sumber | Status |
|---|---|---|---|---|---|
| HAD-000001 | FHD-000001 | kasih sayang | J1/P001 usulan | Bukhari 6013; Muslim 2319 | SOURCE-CHECK |
| HAD-000002 | FHD-000002 | ucapan baik | J1/P002 usulan | Bukhari 2989; Muslim 1009 | SOURCE-CHECK / EXCERPT |
| HAD-000003 | FHD-000003 | bersuci dan kebersihan | J1/P003 usulan | Muslim 223 | SOURCE-CHECK / EXCERPT |
| HAD-000004 | FHD-000004 | wajah ramah | J1/P004 usulan | Tirmidzi 1956; Ibn Hibban 529 | SOURCE-CHECK / VARIANT |
| HAD-000005 | FHD-000005 | haya’ terpuji | J1/P005 usulan | Bukhari 6117; Muslim 37 | SOURCE-CHECK |
| HAD-000006 | FHD-000006 | kelembutan | J1/P006 usulan | Muslim 2593; Bukhari 6927 | SOURCE-CHECK / EXCERPT |
| HAD-000007 | FHD-000007 | salam | J1/P007 usulan | Muslim 54 | SOURCE-CHECK / EXCERPT |
| HAD-000008 | FHD-000008 | kebaikan kecil | J1/P008 usulan | Muslim 2626 | SOURCE-CHECK / OVERLAP-REVIEW |

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
- baru 8 kandidat dari kapasitas desain maksimal 320 slot yang tersedia; 312 slot belum memiliki kandidat;
- sumber dan locator awal tersedia untuk 8 kandidat, tetapi standar edisi/locator lintas register belum diputuskan;
- takhrij, terjemah, whitelist literasi, dan safeguarding belum dijalankan;
- mapping Hadith-ID ke halaman Jilid 1–8 belum tersedia;
- Evidence-ID dan Decision-ID belum tersedia.

Karena itu register ini meningkatkan kesiapan arsitektur dan inventaris awal, bukan kesiapan terbit.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.2.0-id | 29 Juli 2026 | Menambahkan HAD-000001–000008 melalui BAT-HAD-001; seluruhnya SOURCE-CHECK dan HOLD-PARTICIPANT |
| 0.1.0-id | 29 Juli 2026 | Membentuk register kosong terstruktur |
