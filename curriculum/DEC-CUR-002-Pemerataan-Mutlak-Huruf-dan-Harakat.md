# DEC-CUR-002 — Pemerataan Mutlak Huruf dan Harakat Jilid 1

**Decision-ID:** DEC-CUR-002  
**Status:** Draf Terkendali — Berlaku untuk penyusunan PR #2 setelah persetujuan pemilik akademik  
**Tanggal Keputusan:** 28 Juli 2026  
**Pemilik Akademik:** Aris Liswanto  
**Ruang Lingkup:** QJ1-P001–QJ1-P040  
**Menggantikan:** ketentuan alokasi 50:50 dalam DEC-CUR-001  
**Tidak Mengubah:** Konstitusi QURBATA, Governance v1.0, safeguarding, atau blocker materi khusus  

## 1. Latar Belakang

Audit QJ1-P001–QJ1-P032 menunjukkan bahwa kewajiban “semua huruf hadir” belum cukup. Materi baru masih dapat mendominasi dan huruf lama—termasuk alif/hamza—hanya muncul satu atau dua kali tanpa pola yang stabil. Kebijakan ini menetapkan pemerataan kuantitatif, bukan sekadar kehadiran.

## 2. Keputusan Utama

1. Setiap halaman baca tetap memiliki 24 tangga dan 64 token: tangga 1–8 terdiri dari dua huruf dan tangga 9–24 terdiri dari tiga huruf.
2. Seluruh identitas huruf yang telah dipelajari wajib muncul pada setiap halaman baca berikutnya.
3. Jumlah token antaridentitas huruf pada satu halaman harus berbeda paling banyak satu.
4. Kelebihan pembagian token digilir antark halaman agar tidak selalu diterima identitas yang sama.
5. Alif berhamza `أ/إ` dan hamza mandiri `ء` dihitung sebagai dua identitas visual terkendali; masing-masing menerima jatah yang sama dengan identitas lain.
6. Rasio 50% materi saat ini dan 50% murojaah dicabut. Materi baru ditekankan melalui posisi awal, talqin, talaqqi, dan urutan pengajaran—bukan melalui dominasi frekuensi.
7. Di dalam jatah setiap identitas, semua harakat yang telah sah untuk identitas tersebut dibagi seimbang dengan selisih maksimal satu.
8. Harakat yang belum diajarkan pada suatu identitas dilarang muncul hanya untuk mengejar keseimbangan global.
9. Keseimbangan global 32:32 untuk dua harakat atau 22:21:21 untuk tiga harakat wajib setelah seluruh identitas dalam cakupan telah memperoleh set harakat yang sama. Selama fase peluncuran bertahap, distribusi global mengikuti jumlah kombinasi yang sah dan harus dilaporkan.
10. Setiap kombinasi huruf–harakat yang sah harus muncul dalam siklus maksimal dua halaman setelah seluruh alfabet selesai; pengecualian harus dicatat sebagai risiko/remedial.
11. Rangkaian tiga huruf diutamakan mendekati akar Qurani atau bahasa Arab jika tidak merusak pemerataan, whitelist, urutan materi, atau keselamatan pedagogis.
12. Kedekatan akar ditandai `QLX-Q-CANDIDATE` atau `QLX-A-CANDIDATE`; tidak boleh disebut kata atau potongan ayat sebelum verifikasi ahli.

## 3. Rumus Kapasitas

Untuk `L` identitas huruf yang telah dipelajari dan 64 token:

- jatah dasar setiap identitas = `floor(64 / L)`;
- jumlah identitas penerima satu token tambahan = `64 mod L`;
- selisih maksimum antark identitas = satu token.

Setelah 29 identitas selesai, setiap identitas muncul dua atau tiga kali per halaman. Karena 29 × 3 harakat = 87 kombinasi dan satu halaman hanya memuat 64 token, cakupan seluruh kombinasi tiga harakat dilaksanakan dalam siklus dua halaman, bukan dipaksakan dalam satu halaman.

## 4. Gate Otomatis Halaman

- [ ] tepat 24 tangga dan 64 token;
- [ ] 24 tangga unik;
- [ ] seluruh identitas yang telah dipelajari hadir;
- [ ] selisih jumlah antaridentitas maksimal satu;
- [ ] alif dan hamza mandiri memenuhi jatah yang sama;
- [ ] harakat tiap identitas seimbang dalam jatah identitas tersebut;
- [ ] tidak ada harakat yang belum sah;
- [ ] siklus dua halaman menutup seluruh kombinasi yang sah;
- [ ] kandidat leksikal tidak mengubah jumlah token;
- [ ] render, akademik, editorial, asesmen, dan safeguarding tetap ditelaah.

## 5. Dampak

- QJ1-P001–QJ1-P032 harus dibangkitkan ulang dan diaudit.
- QJ1-P033–QJ1-P040 wajib menggunakan rumus ini sejak penyusunan awal.
- CUR-QJ1-001, QJ1-MASTER, dan MAT-CUR-QJ1-001 harus merujuk keputusan ini.
- P018 dan P028 tetap unit lisan khusus; pemerataan token tidak berlaku, tetapi murojaah bermakna tetap wajib.
- `BLOCKED-CUR-HAF-001` dan `BLOCKED-CUR-ARB-001` tidak berubah.

## 6. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 28 Juli 2026 | Menetapkan pemerataan mutlak identitas huruf, pemerataan harakat per identitas, dan siklus kombinasi dua halaman |
