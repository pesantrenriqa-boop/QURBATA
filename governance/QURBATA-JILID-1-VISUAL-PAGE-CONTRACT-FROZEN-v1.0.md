# QURBATA JILID 1 — VISUAL PAGE CONTRACT — FROZEN v1.0

**Status:** FROZEN / CONTROLLING VISUAL BASELINE  
**Tanggal:** 2026-09-10  
**Pemilik akademik:** Aris Liswanto  
**Scope:** Artwork/halaman QURBATA Jilid 1 P001–P040  
**Parent curriculum:** governance/QURBATA-JILID-1-MASTER-40-PAGE-CURRICULUM-FROZEN-v1.0.md  
**Parent workflow:** governance/QURBATA-BOOK-CONTENT-WORKFLOW-FROZEN-v1.0.md

## 1. Prinsip

P001–P040 bukan 40 desain independen. Seluruh halaman adalah instansiasi dari **satu master visual contract**.

P001 akan menjadi calon **MASTER VISUAL REFERENCE**. Setelah disetujui pemilik akademik, seluruh P002–P040 wajib mempertahankan geometri, hierarki, tipografi, panel, dan bahasa visual yang sama.

Perubahan visual yang disetujui setelah freeze **wajib langsung memperbarui dokumen ini di repository** dan menaikkan versi/changelog bila material. Tidak boleh ada keputusan visual penting yang hanya hidup di percakapan.

## 2. Format Tetap

| Elemen | Kontrak |
|---|---|
| Ukuran | A5 portrait |
| Margin | Seragam P001–P040 |
| Grid | Satu master grid/koordinat |
| Header | Logo QURBATA + identitas Jilid + nomor halaman + kompetensi |
| Judul | “Mari Membaca” + judul Arab/Utsmani sesuai kebutuhan |
| Font Arab produksi | KFGQPC Uthman Taha; Amiri dilarang sebagai font produksi QURBATA |
| Penanaman | Posisi tetap; huruf sebesar huruf latihan; lama → baru jika ada prerequisite |
| Area Tartil | Area terbesar/dominan |
| Grid latihan | Ukuran huruf, jarak, alignment dan ritme visual konsisten |
| Panel integrasi | Tahfidz – Bahasa Arab – Akhlak selalu di area/urutan yang sama |
| Tahfidz | Ayat aktual ditampilkan |
| Bahasa Arab | Kata/ungkapan/kalimat aktual sesuai master kurikulum |
| Akhlak | Matan/penggalan hadis aktual ditampilkan |
| Footer | Aktivitas Bi'ah QURBATA + tanggal + nilai + TTD |
| RIQA OS | Area QR/identitas digital konsisten |
| Slogan | Quran • Bahasa Arab • Tahfidz • Akhlak |
| Warna | Satu palet buku, konsisten |
| Ornamen | Satu keluarga visual, tidak diganti-ganti antarhalaman |

## 3. Hierarki Ruang

Urutan dominasi visual:
1. **Latihan Tartil**
2. **Penanaman kompetensi baru**
3. **Panel Tahfidz / Bahasa Arab / Akhlak**
4. **Aktivitas Bi'ah / RIQA OS / administrasi**

Panel integrasi dan footer harus ringkas agar tidak mengurangi area latihan Tartil secara berlebihan.

## 4. Penanaman Kompetensi Baru

- Wajib pada halaman akuisisi.
- Huruf contoh sebesar huruf latihan.
- Arah Arab RTL.
- Menunjukkan kompetensi lama → baru pada huruf sama.
- P001 tidak membuat transformasi palsu; cukup بَ تَ ثَ.
- Blok ini menggantikan satu baris latihan pada render halaman akuisisi.
- Halaman akuisisi: 1 blok penanaman + 7 baris × 3 contoh.
- Tidak boleh ada kompetensi masa depan.

## 5. Tipografi Arab

- Seluruh Arab produksi: **KFGQPC Uthman Taha**.
- Harakat harus jelas dan tidak bertabrakan dengan garis/kotak.
- Huruf latihan dibuat sebesar mungkin dengan ruang napas yang cukup.
- Judul Arab juga mengikuti sistem tipografi Utsmani.
- Bentuk huruf tidak boleh diganti font lain karena alasan estetika.
- Audit bentuk ه dan bentuk sensitif lain mengikuti keputusan kurikulum/ortografi yang berlaku.

## 6. Konten yang Boleh Berubah per Halaman

Hanya:
- Page-ID/nomor halaman;
- judul kompetensi;
- materi Penanaman;
- contoh latihan;
- ayat Tahfidz;
- ungkapan Bahasa Arab;
- matan Akhlak;
- QR/ID kompetensi bila berbeda;
- status/evaluasi yang memang ditetapkan master kurikulum.

## 7. Elemen yang Tidak Boleh Drift

Tanpa keputusan revisi eksplisit, jangan mengubah:
- ukuran halaman;
- margin;
- posisi logo;
- geometri header/footer;
- posisi dan ukuran panel integrasi;
- ukuran dasar huruf latihan;
- grid latihan;
- hierarchy spacing;
- radius/garis/bentuk panel;
- palet;
- gaya ikon/ornamen;
- posisi area QR;
- gaya nomor halaman.

## 8. Kontrak Gambar ChatGPT

Gambar yang dibuat melalui ChatGPT adalah **visual artwork/reference per halaman**, bukan alasan untuk mengubah kurikulum.

Workflow:
1. ambil SPEC/FROZEN konten halaman;
2. render artwork di chat;
3. pemilik akademik mengoreksi;
4. revisi halaman yang sama;
5. setelah dinyatakan FIX/FREEZE, simpan artwork final dengan Page-ID;
6. gunakan artwork final sebagai referensi visual dan arsip;
7. produksi buku/PDF deterministik tetap harus tunduk pada master kurikulum dan kontrak visual ini.

AI tidak boleh mengimprovisasi:
- teks Arab;
- ayat;
- hadis;
- contoh latihan;
- kompetensi;
- jumlah/urutan panel.

Semua teks harus berasal dari data halaman yang telah disetujui.

## 9. Struktur Repository Artwork

Target:
```
books/jilid-1/
  pages/
    QJ1-P001.md
    ...
    QJ1-P040.md
  artwork/
    QJ1-P001.png
    ...
    QJ1-P040.png
  production/
```

Draft yang ditolak tidak menjadi baseline final. Artwork final menggunakan Page-ID yang sama dengan SPEC halaman.

## 10. Gate Konsistensi Sebelum Freeze Artwork

Sebelum artwork halaman dinyatakan final, cek:
- [ ] ukuran/rasio sama;
- [ ] header sama;
- [ ] font Arab benar;
- [ ] Tartil dominan;
- [ ] Penanaman sesuai kompetensi;
- [ ] tidak ada competency leakage;
- [ ] jumlah latihan sesuai kontrak;
- [ ] ayat Tahfidz tampil;
- [ ] BA tampil;
- [ ] matan Akhlak tampil;
- [ ] footer/aktivitas tampil;
- [ ] QR/RIQA OS konsisten;
- [ ] tidak ada typo Arab;
- [ ] tidak ada drift desain.

## 11. Change-Control

**Perintah pemilik akademik:** jika ada perubahan aturan halaman yang disetujui, perubahan tersebut harus langsung dicatat pada file FROZEN ini di GitHub.

Prosedur:
1. identifikasi aturan yang berubah;
2. update dokumen ini pada commit yang sama/segera setelah keputusan;
3. tulis alasan pada commit message/changelog;
4. jika perubahan material, naikkan versi;
5. audit halaman yang sudah dibuat terhadap aturan baru;
6. jangan membiarkan repo dan keputusan chat berbeda.

## 12. Status

**QJ1_VISUAL_PAGE_CONTRACT = FROZEN_v1.0**

P001 selanjutnya digunakan untuk menguji dan mengunci master visual aktual. Setelah P001 disetujui, referensi P001 menjadi baseline visual P002–P040.
