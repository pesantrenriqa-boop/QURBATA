# Pedagogical Engine Foundation Checklist V1

Tanggal: 5 Agustus 2026
Branch: `content/qurbata-jilid-1-8-production`
Status: IMPLEMENTATION COMPLETE — EXECUTION VERIFICATION REQUIRED

## Komponen fondasi

- [x] Competency dependency map C0001–C0041
- [x] Pedagogical policy/rule matrix
- [x] Object-level gate
- [x] Page-level gate
- [x] Dependency graph validator
- [x] Jilid-level validator
- [x] Series-level validator Jilid 1–8
- [x] Global no-repeat object policy
- [x] Quran SourceRef requirement
- [x] Object-scope enforcement: LETTER/FRAGMENT/WORD/PHRASE/AYAH
- [x] Regression test for competency leap
- [x] Regression test for missing source
- [x] Regression test for duplicate object across series
- [x] Regression test for object-scope mismatch

## Promotion gate

Tidak ada halaman yang boleh dipromosikan menjadi `REVIEWED_PAGE` atau `ACTIVE_PAGE` sebelum seluruh pemeriksaan berikut menghasilkan nol error:

1. dependency kompetensi terpenuhi;
2. kompetensi objek berada dalam whitelist halaman;
3. fitur terlarang belum muncul;
4. jenis objek sesuai tahap;
5. SourceRef Al-Qur'an tersedia;
6. ObjectID dan CanonicalKey belum pernah digunakan sebagai objek utama;
7. urutan halaman dan jilid valid;
8. validator seri menyatakan PASS.

## Status halaman lama

Semua halaman yang dihasilkan sebelum fondasi V1, termasuk Halaman 1 dan Halaman 10 lama, berstatus `LEGACY_INVALIDATED`. Halaman tersebut tidak boleh digunakan sebagai isi produksi dan harus diregenerasi.

## Batas klaim selesai

Implementasi fondasi telah lengkap di repository. Namun status runtime baru boleh dinaikkan menjadi `VERIFIED_PASS` setelah test suite dijalankan pada checkout repository atau CI dan seluruh tes lulus. Sampai saat itu status yang sah adalah `IMPLEMENTATION_COMPLETE`.

## Perintah verifikasi

```bash
python -m pytest content/qwo/pedagogy/tests -q
```

Setelah tes lulus, jalankan regenerasi terbatas Halaman 1 dan Halaman 10 sebagai acceptance test sebelum menghasilkan seluruh Jilid 1.
