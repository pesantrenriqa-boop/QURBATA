# DEC-CUR-009 — Transisi Tangga Empat Huruf pada Tahap Tanwin

**Decision-ID:** DEC-CUR-009  
**Tanggal:** 29 Juli 2026  
**Status:** BERLAKU UNTUK PRODUKSI DRAF JILID 2–8  
**Pemilik Akademik:** Aris Liswanto  
**Melanjutkan:** DEC-CUR-007 dan DEC-CUR-008

## 1. Keputusan

Mulai halaman pengenalan tanwin, tangga latihan meningkat dari rangkaian tiga huruf menjadi **kata tiga huruf sebagai jembatan, kemudian kata empat huruf dasar**. Tanwin adalah tanda bunyi akhir dan tidak dihitung sebagai huruf kelima.

## 2. Titik Transisi

- QJ2-P001–P015: 24 tangga × 3 huruf.
- Mulai QJ2-P016 dan setiap halaman tahap empat huruf: Tangga 1–8 tetap kata tiga huruf; Tangga 9–24 meningkat menjadi kata empat huruf.
- Pola jembatan 3→4 ini diulang pada setiap halaman terkait, bukan hanya halaman pertama tanwin.
- Pola tersebut diteruskan pada Jilid 3–8 sampai Decision-ID tahap berikutnya menetapkan struktur yang lebih panjang.

## 3. Distribusi 50:50

Pada halaman akuisisi:

- Tangga 1–8: 4 fokus + 4 review, masing-masing tiga huruf = 12 token fokus + 12 token review;
- Tangga 9–24: 8 fokus + 8 review, masing-masing empat huruf = 32 token fokus + 32 token review;
- total 44 token fokus + 44 token review = 88 token per halaman.

Pada halaman evaluasi, integrasi, dan penguatan: struktur tetap 8 tangga tiga huruf + 16 tangga empat huruf = 88 token review/transfer tanpa materi baru.

## 4. Syarat Kata Tanwin

1. Tanwin hanya ditempatkan pada huruf akhir kata.
2. Setiap tangga diutamakan berupa kata Arab bermakna.
3. Kata Qur’ani atau hadis wajib mempunyai Source-ID dan verifikasi teks.
4. Fathatain harus mengikuti aturan alif penyangga dan seluruh pengecualiannya.
5. Kasratain dan dhammatain harus menggunakan bentuk akhir dan shaping yang benar.
6. Sukun, tasydid, mad, atau kaidah lain tidak boleh muncul sebelum whitelist tahapnya sah.
7. Pseudo-kata bertanwin dilarang.

## 5. Murojaah

Porsi review tetap mencampurkan huruf penyambung dengan huruf pemutus sambungan serta merotasi ء، أ/إ، د، ذ، ر، ز، و. Pemilihan kata empat huruf tidak boleh mengurangi cakupan kumulatif.

## 6. Gate Audit

Halaman tahap tanwin gagal apabila:

- Tangga 1–8 tidak tepat tiga huruf atau Tangga 9–24 tidak tepat empat huruf dasar;
- tanwin tidak berada pada huruf akhir kata;
- jumlah token bukan 88;
- halaman akuisisi tidak mencapai 44:44;
- bentuk tanwin tidak mempunyai entri whitelist;
- kata dinisbatkan kepada Al-Qur’an/hadis tanpa Source-ID;
- ditemukan pseudo-kata tanwin.

## 7. Status Produksi

Keputusan struktur ini sah, tetapi produksi QJ2-P016 dan seterusnya tetap mengikuti BLK-QJ2-ORTHO-001. Isi nyata baru boleh dibuat setelah whitelist empat-huruf bertanwin dan verifikasi ahli tersedia.

## 8. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.2.0-id | 29 Juli 2026 | Mengoreksi transisi: setiap halaman empat-huruf selalu diawali delapan tangga tiga-huruf; total 44:44 |
| 0.1.0-id | 29 Juli 2026 | Menetapkan transisi awal ke kata empat huruf pada tahap tanwin |
