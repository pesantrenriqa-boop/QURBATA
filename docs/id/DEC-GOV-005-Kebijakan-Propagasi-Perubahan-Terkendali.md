# DEC-GOV-005 — Kebijakan Propagasi Perubahan Terkendali QURBATA

**Status:** BERLAKU  
**Tanggal:** 30 Juli 2026  
**Branch resmi:** `main`  
**Pemilik akademik:** Aris Liswanto  
**Dasar:** QC-000, QC-001–QC-012, QURBATA-BASELINE, register, keputusan kurikulum, dan master jilid.

## 1. Keputusan

Setiap perubahan pada QURBATA wajib dimasukkan ke GitHub dan diproses sebagai perubahan terkendali. Tidak boleh ada keputusan, contoh, kode, materi, halaman, asesmen, data, aplikasi, atau produk turunan yang berjalan di luar repository resmi.

## 2. Prinsip Propagasi

Perubahan harus mengalir menurut hierarki:

`QC-000 → QC-001–QC-012 → QCF/RCP/ACP/HCP → DEC-CUR/DEC-GOV → MASTER JILID → REGISTRY/MATRIX → HALAMAN → DATA ITEM → ASESMEN → PRODUK TURUNAN`

Bila dokumen pada tingkat lebih tinggi berubah, seluruh dokumen dan produk pada tingkat di bawahnya wajib diperiksa dan disesuaikan. Penyesuaian tidak boleh dilakukan sebagian bila perubahan memengaruhi lebih dari satu objek.

## 3. Aturan Wajib

1. Setiap perubahan material wajib mempunyai Decision-ID.
2. File yang terdampak wajib dicatat dalam daftar dampak perubahan.
3. Registry, master jilid, halaman, data item, asesmen, dan produk turunan wajib menggunakan kode yang sama.
4. Tidak boleh membuat salinan sistem baru untuk menghindari penyesuaian.
5. Versi lama yang masih diperlukan untuk audit dipindahkan ke `archive/` dan diberi alasan pembekuan.
6. Versi salah, duplikat, atau superseded tidak boleh berada di area produksi aktif.
7. Perubahan pada contoh Qurani wajib menjaga Source-ID dan status tashih.
8. Perubahan pada kompetensi wajib memicu audit ulang urutan prasyarat, distribusi, murojaah, asesmen, dan halaman terkait.
9. Perubahan pada kode tidak boleh dilakukan tanpa migrasi seluruh referensi.
10. Produk turunan tidak boleh diperbarui lebih dahulu daripada sumber buku dan registry.

## 4. Klasifikasi Dampak

- **Minor:** editorial tanpa mengubah makna, kode, urutan, kompetensi, atau sumber.
- **Material:** mengubah contoh, kompetensi, halaman, urutan, Source-ID, LO/KO, asesmen, atau integrasi lintas jilid.
- **Konstitusional:** mengubah arah, kewenangan, prinsip, terminologi pengendali, atau tata kelola.

Perubahan material dan konstitusional wajib memakai Decision-ID, audit dampak, dan riwayat versi.

## 5. Daftar Dampak Minimum

Setiap perubahan material wajib memeriksa sekurang-kurangnya:

- dokumen pengendali;
- master jilid;
- registry kompetensi dan objek;
- halaman buku;
- data item;
- asesmen dan rubrik;
- audio atau media;
- aplikasi RIQA OS;
- flashcard, presentasi, dan produk turunan lain;
- audit, Evidence-ID, dan status validasi.

## 6. Gerbang Penyelesaian Perubahan

Perubahan dinyatakan selesai hanya apabila:

1. sumber pengendali telah diperbarui;
2. seluruh referensi terdampak telah disesuaikan;
3. tidak ada kode yatim, referensi rusak, atau versi aktif ganda;
4. audit dampak selesai;
5. riwayat perubahan tercatat;
6. perubahan telah masuk ke branch `main`.

## 7. Larangan

Dilarang:

- menyimpan perubahan penting hanya di chat;
- memperbarui halaman tanpa memperbarui registry atau master yang terdampak;
- memperbarui aplikasi dengan data yang tidak sama dengan buku;
- menghapus versi lama tanpa jejak ketika masih diperlukan untuk audit;
- menyatakan perubahan selesai sebelum seluruh dampaknya ditutup.

## 8. Efektivitas

Keputusan ini berlaku sejak ditulis ke branch `main` dan menjadi aturan operasional wajib untuk seluruh pengembangan Buku QURBATA Jilid 1–8 serta semua produk turunannya.
