# QURBATA

**QURBATA** adalah proyek pengembangan literasi dan pendidikan Al-Qur’an yang disusun secara bertahap, terukur, dan dapat ditelusuri oleh Rumah Ilmu Al-Qur’an (RIQA).

Repository ini menjadi sumber resmi terkendali untuk konstitusi, tata kelola, terminologi, kurikulum, buku, asesmen, penelitian, standar, dan aset pendukung QURBATA.

> **Pintu masuk operasional terbaru:** baca [`QURBATA-BASELINE.md`](QURBATA-BASELINE.md) sebelum membuat, memindahkan, atau merevisi materi. Dokumen itu mengikat kembali kode halaman, registry, master jilid, contoh, Source-ID, dan urutan kerja sejak awal menjadi satu rangkaian.

## Status Repository

QURBATA telah memiliki fondasi Governance v1.0 dan kini memasuki fase konsolidasi sumber tunggal serta produksi Buku QURBATA. Fondasi governance menetapkan:

1. `QC-000` sebagai satu-satunya Konstitusi QURBATA;
2. `QC-001–QC-012` sebagai keluarga dokumen turunan;
3. Bahasa Indonesia sebagai bahasa induk dan satu-satunya teks normatif pengendali;
4. terjemahan Inggris dan Arab sebagai produk lanjutan setelah harmonisasi;
5. register, matriks keterlacakan, RACI, bukti, risiko, CAPA, dan mekanisme audit sebagai toolkit governance.

Arsitektur lama `F-001–F-005` tidak lagi menjadi sumber kewenangan konstitusional.

## Struktur Repository

```text
docs/id/        Master Bahasa Indonesia dan toolkit governance
curriculum/     Arsitektur, lingkup, urutan, registry, dan capaian kurikulum
books/          Naskah sumber tunggal dan berkas pengembangan buku
data/           Data item terstruktur yang mengikuti master halaman
assessment/     Kerangka asesmen, instrumen, dan rubrik
research/       Rekaman penelitian, validasi, dan bukti
standards/      Standar editorial, pedagogis, bahasa, dan mutu
references/     Bibliografi dan sumber yang disetujui
assets/         Aset visual dan pendukung milik proyek
templates/      Template terkendali
archive/        Materi lama/superseded untuk keterlacakan; bukan sumber produksi
```

## Kebijakan Sumber Kebenaran

Branch `main` menjadi rekaman otoritatif. Perubahan material wajib mempunyai riwayat yang dapat ditelusuri. Draf, revisi, dan dokumen yang digantikan tidak boleh mengganti sumber resmi secara diam-diam.

Hierarki operasional dan keputusan konsolidasi berada dalam `QURBATA-BASELINE.md`. Bila ditemukan beberapa generasi materi, versi aktif harus dinormalisasi ke jalur resmi; versi yang digantikan dipindahkan ke `archive/` atau dihapus dari area aktif.

## Bahasa Kerja

Bahasa Indonesia adalah teks induk normatif dan pengendali. Bahasa Inggris dan Arab tidak mempunyai kedudukan pengendali sebelum diterjemahkan, diharmonisasikan, ditelaah, dan disahkan sesuai kewenangan.

## Aturan Pengembangan

Kurikulum, buku, asesmen, aplikasi, dan produk turunan tidak boleh dinyatakan final sebelum fondasi governance yang relevan tersedia. Ketentuan ini tidak melarang pekerjaan pengembangan paralel, tetapi setiap keluaran harus tetap berstatus draf dan dapat ditelusuri sampai memperoleh persetujuan.

Fokus produk utama adalah penyelesaian **Buku QURBATA**, dimulai dari konsolidasi Jilid 1–3. Produk turunan seperti flashcard, presentasi, audio, dan aplikasi wajib diturunkan dari master buku serta registry yang sama dan tidak boleh membentuk sumber data baru yang terpisah.

## Institusi

**Rumah Ilmu Al-Qur’an (RIQA)**  
Malang, Indonesia

---

Hak cipta © RIQA. Penggunaan dan distribusi tunduk pada keputusan lisensi resmi QURBATA.