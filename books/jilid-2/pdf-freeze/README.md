# QURBATA Jilid 2 — PDF Freeze Control

Folder ini adalah **source of truth khusus produksi PDF Jilid 2**.

Tujuan utamanya: keputusan visual yang sudah disetujui tidak boleh hilang hanya karena file di `dist/` terhapus, renderer diganti, atau eksperimen font dilakukan.

## Aturan wajib

1. `dist/` hanyalah artefak render sementara, **bukan sumber kebenaran**.
2. Setiap halaman yang dinyatakan `FROZEN` wajib memiliki rekam pada `QJ2-PDF-ARTIFACT-REGISTER.csv`.
3. Rekam freeze halaman minimal berisi: halaman, sumber materi, renderer, commit renderer, nama PDF, SHA-256 PDF, tanggal persetujuan, dan catatan.
4. Properti visual global yang sudah freeze berada di `QJ2-PDF-VISUAL-BASELINE.json`.
5. Renderer baru **tidak boleh** mengubah visual grammar frozen secara diam-diam. Perubahan harus menaikkan versi baseline dan mendapat persetujuan eksplisit.
6. Amiri/Amiri Quran tidak boleh kembali menjadi base font produksi Jilid 2. Base font frozen adalah KFGQPC Uthman Taha Naskh.
7. Sukun memakai baseline V7.6 frozen: codepoint U+0652, outline visual Amiri U+06E1, shift -1700 unit, dengan positioning KFGQPC dipertahankan.
8. Format materi baru/presentasi panah serta grid adaptif 4 kotak/3 kotak merupakan visual grammar yang harus dipertahankan saat recovery.
9. Halaman dengan status `RECOVERY_AUDIT_REQUIRED` **tidak boleh dianggap baru atau kosong**. Status itu berarti riwayat visual lama harus dipulihkan lebih dulu sebelum membuat ulang.
10. Setelah halaman disetujui lagi, isi register diubah ke `FROZEN` dan SHA-256 PDF wajib dicatat.

## Prosedur freeze satu halaman

1. Recovery sumber materi dan visual terakhir yang sah.
2. Render dengan baseline KFGQPC saat ini.
3. Review visual oleh pemilik akademik.
4. Setelah dinyatakan `freeze`, hitung SHA-256 PDF.
5. Isi register halaman dengan source path, renderer path, commit, filename, SHA-256, tanggal persetujuan.
6. Setelah itu halaman tersebut menjadi immutable kecuali ada keputusan versi baru.

## Referensi historis penting

- QJ2 final master freeze checklist: commit `7e72f9e8b43aeb5432d63ec5e89c39c76e6061d4`.
- Riwayat repository menunjukkan QJ2 pernah memiliki struktur halaman per halaman dan beberapa siklus recovery/freeze; karena itu recovery harus dilakukan dari history sebelum membuat ulang.

## Prinsip recovery sekarang

**Jangan menciptakan ulang sebelum mencari versi lama yang sudah dibangun.**

Urutan kerja:

`Git history → halaman/sumber/renderer terakhir → visual grammar frozen → KFGQPC wrapper → render → review → SHA-256 → FROZEN register`.
