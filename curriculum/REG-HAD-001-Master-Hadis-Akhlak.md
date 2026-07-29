# REG-HAD-001 — Master Hadis Akhlak QURBATA

**Register-ID:** REG-HAD-001  
**Status:** DRAF TERKENDALI — 40 KANDIDAT SOURCE-CHECK; 0 APPROVED  
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

Empat puluh kandidat awal telah dimasukkan melalui BAT-HAD-001 sampai BAT-HAD-005 dan dipetakan melalui MAP-HAD-QJ1-001. Tidak ada Hadith-ID yang diaktifkan; semua masih memerlukan takhrij, review penggalan, terjemah, pedagogi, safeguarding, dan keputusan ahli.

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
| HAD-000009 | FHD-000009 | niat | J1/P009 usulan | Bukhari 1; Muslim 1907 | SOURCE-CHECK / EXCERPT |
| HAD-000010 | FHD-000010 | konsistensi | J1/P010 usulan | Muslim 783; Bukhari 6465 | SOURCE-CHECK / VARIANT |
| HAD-000011 | FHD-000011 | tidak mengganggu | J1/P011 usulan | Bukhari 10; Muslim 40/41 | SOURCE-CHECK / VARIANT |
| HAD-000012 | FHD-000012 | kendali marah | J1/P012 usulan | Bukhari 6116 | SOURCE-CHECK / CONTEXT |
| HAD-000013 | FHD-000013 | kebaikan bagi sesama | J1/P013 usulan | Bukhari 13; Muslim 45 | SOURCE-CHECK / WORDING |
| HAD-000014 | FHD-000014 | membantu sesama | J1/P014 usulan | Muslim 2699 | SOURCE-CHECK / EXCERPT |
| HAD-000015 | FHD-000015 | belajar Al-Qur’an | J1/P015 usulan | Bukhari 5027 | SOURCE-CHECK / VARIANT |
| HAD-000016 | FHD-000016 | berkata baik | J1/P016 usulan | Muslim 47; Bukhari 6018/6138 | SOURCE-CHECK / EXCERPT |
| HAD-000017 | FHD-000017 | kekuatan bermanfaat | J1/P017 usulan | Muslim 2664 | SOURCE-CHECK / INCLUSION |
| HAD-000018 | FHD-000018 | berterima kasih | J1/P018 usulan | Tirmidzi 1954; Abu Dawud 4811 | SOURCE-CHECK / VARIANT |
| HAD-000019 | FHD-000019 | menguasai diri | J1/P019 usulan | Bukhari 6114; Muslim 2609 | SOURCE-CHECK / PROGRESSION |
| HAD-000020 | FHD-000020 | akhlak baik | J1/P020 usulan | Muslim 2553 | SOURCE-CHECK / EXCERPT |
| HAD-000021 | FHD-000021 | saling menguatkan | J1/P021 usulan | Bukhari 6026; Muslim 2585 | SOURCE-CHECK / LOCATOR |
| HAD-000022 | FHD-000022 | tidak menipu | J1/P022 usulan | Muslim 101/102 | SOURCE-CHECK / WORDING |
| HAD-000023 | FHD-000023 | menyingkirkan gangguan | J1/P023 usulan | Muslim 35 | SOURCE-CHECK / SAFETY |
| HAD-000024 | FHD-000024 | ihsan | J1/P024 usulan | Muslim 1955 | SOURCE-CHECK / HIGH-CONTEXT |
| HAD-000025 | FHD-000025 | kejujuran | J1/P025 usulan | Bukhari 6094; Muslim 2607 | SOURCE-CHECK / EXCERPT |
| HAD-000026 | FHD-000026 | setiap kebaikan | J1/P026 usulan | Bukhari 6021 | SOURCE-CHECK / OVERLAP |
| HAD-000027 | FHD-000027 | persaudaraan aman | J1/P027 usulan | Bukhari 2442; Muslim 2580 | SOURCE-CHECK / SAFE |
| HAD-000028 | FHD-000028 | anti-kezaliman | J1/P028 usulan | Muslim 2578 | SOURCE-CHECK / AGE |
| HAD-000029 | FHD-000029 | kasih sayang luas | J1/P029 usulan | Abu Dawud 4941; Tirmidzi 1924 | SOURCE-CHECK / VARIANT |
| HAD-000030 | FHD-000030 | tawaduk | J1/P030 usulan | Muslim 2588 | SOURCE-CHECK / CONCEPT |
| HAD-000031 | FHD-000031 | persaudaraan tanpa iri | J1/P031 usulan | Muslim 2563 | SOURCE-CHECK / VARIANT |
| HAD-000032 | FHD-000032 | nasihat tulus | J1/P032 usulan | Muslim 55 | SOURCE-CHECK / HIGH-CONCEPT |
| HAD-000033 | FHD-000033 | kelembutan memperindah | J1/P033 usulan | Muslim 2594 | SOURCE-CHECK / SEMANTIC-OVERLAP |
| HAD-000034 | FHD-000034 | memudahkan dan menggembirakan | J1/P034 usulan | Bukhari 69; Muslim 1734 | SOURCE-CHECK / CONTEXT |
| HAD-000035 | FHD-000035 | menunjukkan kebaikan | J1/P035 usulan | Muslim 1893 | SOURCE-CHECK / ATTRIBUTION |
| HAD-000036 | FHD-000036 | kasih muda dan hormat tua | J1/P036 usulan | Abu Dawud 4943; Tirmidzi 1920 | SOURCE-CHECK / THEOLOGICAL-WORDING / SAFE |
| HAD-000037 | FHD-000037 | kelapangan bermuamalah | J1/P037 usulan | Bukhari 2076 | SOURCE-CHECK / AGE-LOAD |
| HAD-000038 | FHD-000038 | menjaga anak yatim | J1/P038 usulan | Bukhari 6005 | SOURCE-CHECK / PRIVACY |
| HAD-000039 | FHD-000039 | membantu keluarga rentan | J1/P039 usulan | Bukhari 5353; Muslim 2982 | SOURCE-CHECK / EXCERPT / PRIVACY |
| HAD-000040 | FHD-000040 | kebaikan kecil yang ikhlas | J1/P040 usulan | Bukhari 1417; Muslim 1016 | SOURCE-CHECK / EXCERPT / AGE-SAFETY |

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
- 40 kandidat Jilid 1 telah tersedia dari kapasitas desain maksimal 320 slot; 280 slot lintas Jilid 2–8 belum memiliki kandidat;
- SRC-HAD-QJ1-001 mengonsolidasikan perawi dan sumber awal 40/40 kandidat; 40/40 memiliki locator daring eksplisit dan 0/40 masih mengandalkan locator batch, sementara standar edisi/locator final belum diputuskan;
- takhrij, terjemah, whitelist literasi, dan safeguarding belum dijalankan;
- MAP-HAD-QJ1-001 v0.2 memetakan P001–P040, interval 1/3/7/14, checkpoint maksimum delapan prompt, dan carryover; AUD-HAD-QJ1-001 selesai internal, tetapi frekuensi aktual serta mapping Jilid 2–8 belum tersedia;
- PROP-HAD-QJ1-001 menyediakan resolusi enam klaster semantik dan prioritas pemindahan/penggantian; REV/RUB/FRM/PRO/DEC-HAD-QJ1-001 menyiapkan review hingga otorisasi. Seluruh keputusan panel, prasyarat pilot, data, Reviewer-ID, Evidence-ID, dan Decision-ID masih kosong.

Karena itu register ini meningkatkan kesiapan arsitektur dan inventaris awal, bukan kesiapan terbit.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.20.0-id | 29 Juli 2026 | Menambahkan WRK-HAD-QJ1-003; instrumen terperinci kumulatif 24/40, hasil ahli tetap 0/24 |
| 0.19.0-id | 29 Juli 2026 | Menambahkan WRK-HAD-QJ1-002 untuk delapan objek Gelombang 2; instrumen kumulatif siap 16/40, hasil ahli tetap 0/16 |
| 0.18.0-id | 29 Juli 2026 | Menambahkan WRK-HAD-QJ1-001 untuk delapan objek Gelombang 1; instrumen siap, hasil ahli tetap 0/8 |
| 0.17.0-id | 29 Juli 2026 | Menambahkan QPR-HAD-QJ1-001: antrean pra-takhrij lima gelombang untuk 40 objek; pekerjaan ahli tetap 0/40 |
| 0.16.0-id | 29 Juli 2026 | Menambahkan locator daring HAD-000025–HAD-000032; cakupan locator daring awal lengkap 40/40 |
| 0.15.0-id | 29 Juli 2026 | Menambahkan locator daring HAD-000017–HAD-000024; cakupan locator daring menjadi 32/40 |
| 0.14.0-id | 29 Juli 2026 | Menambahkan locator daring HAD-000009–HAD-000016; cakupan locator daring menjadi 24/40 |
| 0.13.0-id | 29 Juli 2026 | Menambahkan locator daring HAD-000001–HAD-000008; cakupan locator daring menjadi 16/40 |
| 0.12.0-id | 29 Juli 2026 | Menambahkan SRC-HAD-QJ1-001; perawi dan sumber awal 40/40 terkonsolidasi, 0 Evidence-ID ahli |
| 0.11.0-id | 29 Juli 2026 | Menambahkan PROP-HAD-QJ1-001 untuk membedakan enam klaster tema dan memprioritaskan objek yang mungkin dipindah/diganti |
| 0.10.0-id | 29 Juli 2026 | Menambahkan protokol pilot bertahap dan record otorisasi; status efektif NO-GO sampai prasyarat dibuktikan |
| 0.9.0-id | 29 Juli 2026 | Menambahkan rubrik perkembangan aman dan form bukti pilot 40 halaman; belum ada data atau aktivasi |
| 0.8.0-id | 29 Juli 2026 | Mengoreksi beban checkpoint menjadi maksimum delapan prompt dan menambahkan AUD-HAD-QJ1-001; validasi ahli tetap OPEN |
| 0.7.0-id | 29 Juli 2026 | Menambahkan MAP-HAD-QJ1-001 dan REV-HAD-QJ1-001; intro P001–P040 serta jadwal recall tersedia, keputusan ahli tetap 0 APPROVED |
| 0.6.0-id | 29 Juli 2026 | Menambahkan HAD-000033–000040 melalui BAT-HAD-005; kandidat P001–P040 lengkap, akumulasi 40 SOURCE-CHECK dan 0 APPROVED |
| 0.5.0-id | 29 Juli 2026 | Menambahkan HAD-000025–000032 melalui BAT-HAD-004; akumulasi 32 SOURCE-CHECK, 0 APPROVED |
| 0.4.0-id | 29 Juli 2026 | Menambahkan HAD-000017–000024 melalui BAT-HAD-003; akumulasi 24 SOURCE-CHECK, 0 APPROVED |
| 0.3.0-id | 29 Juli 2026 | Menambahkan HAD-000009–000016 melalui BAT-HAD-002; akumulasi 16 SOURCE-CHECK, 0 APPROVED |
| 0.2.0-id | 29 Juli 2026 | Menambahkan HAD-000001–000008 melalui BAT-HAD-001; seluruhnya SOURCE-CHECK dan HOLD-PARTICIPANT |
| 0.1.0-id | 29 Juli 2026 | Membentuk register kosong terstruktur |
