# BLK-QJ2-ORTHO-001 — Gate Ortografi Tanwin Jilid 2

**Blocker-ID:** BLK-QJ2-ORTHO-001  
**Tanggal:** 29 Juli 2026  
**Status:** OPEN — AUTOMATED AUDIT PASS / EXPERT GATE OPEN  
**Cakupan:** QJ2-P021–P024  

## 1. Alasan

Tanwin hanya sah pada posisi akhir. Fathatain mempunyai aturan alif penyangga dan pengecualian ortografis; contoh rangkaian buatan yang tidak dikendalikan dapat menghasilkan tulisan Arab yang salah. Kasratain dan dhammatain juga memerlukan bentuk akhir, konteks kata, shaping, serta model pelafalan yang tepat.

## 2. Keputusan Sementara

1. P021–P024 tidak diisi dengan pseudo-kata tanwin.
2. Materi tanwin harus berasal dari whitelist kata nyata: delapan tangga tiga huruf sebagai jembatan dan enam belas tangga empat huruf, semuanya mempunyai Source-ID.
3. Setiap entri memuat bentuk dasar, bentuk bertanwin, posisi akhir, aturan alif, arti, sumber, dan status review.
4. Sukun, tasydid, dan mad yang belum diajarkan tidak boleh bocor melalui kata pilihan.
5. Bila tidak tersedia cukup kata sesuai prasyarat, urutan tanwin dipindahkan melalui Decision-ID.

## 2A. Kemajuan Whitelist

WLT-QJ2-TAN-001 menyediakan 8 kandidat kata tiga huruf dan 16 kandidat kata empat huruf beserta 72 bentuk tanwin. AUD-QJ2-TAN-001 lulus audit struktur otomatis; MAP-QJ2-TAN-001 telah superseded oleh DEC-CUR-010; MAP-QJ2-TAN-002 wajib memetakan P021–P024; REV-QJ2-TAN-001 siap dikirim. Verifikasi ahli, teks Utsmani, dan render masih terbuka.

## 3. Bukti untuk Menutup Gate

- standar ortografi fathatain, kasratain, dan dhammatain;
- daftar alif penyangga dan pengecualian;
- whitelist minimal 8 kata nyata tiga huruf dan 16 kata nyata empat huruf per halaman;
- review ahli Bahasa Arab/Al-Qur'an;
- audit shaping Amiri Quran;
- Reviewer-ID, Evidence-ID, dan Decision-ID.

## 4. Dampak

P001–P020 telah diproduksi sebagai fondasi bentuk. P021–P024 boleh dibuat sebagai staging, tetapi tetap **BLOCKED-CONTENT** sampai review ahli, Evidence-ID, dan audit render menutup gate. Blocker ini menjaga ketepatan ilmiah dan tidak membatalkan struktur 40 halaman.
