# QURBATA Book Blueprint v1.0

**Status:** FROZEN  
**Effective date:** 2026-09-06  
**Authority:** QURBATA / Rumah Ilmu Al-Qur’an  
**Reference implementation:** Vivliostyle production template on PR #11.

## Freeze Decision

Bismillah. Desain halaman pilot QURBATA yang telah disetujui ditetapkan sebagai **QURBATA Book Blueprint v1.0** dan menjadi baseline resmi produksi buku.

## Struktur halaman yang dibekukan

1. Identitas buku dan nomor halaman.
2. Judul pembelajaran.
3. Blok integrasi Tahfidz, Bahasa Arab, dan NIDHOM.
4. Latihan Tartil sebagai area visual dominan.
5. Grid latihan Tartil 8 baris × 3 kolom.
6. Aktivitas Bi’ah QURBATA.
7. Catatan tanggal, nilai, dan TTD guru.
8. QR resolver menuju RIQA OS.
9. Page/competency identifier dan footer QURBATA.

## Tipografi Arab

Seluruh teks Arab pada baseline produksi menggunakan **KFGQPC Uthman Taha Naskh**. Penggantian font wajib melalui uji regresi harakat, ligatur, tanda Qurani, embedding PDF, dan persetujuan editorial/akademik.

## Aturan perubahan

Blueprint v1.0 tidak diubah diam-diam. Perubahan struktur, grid, tipografi produksi, proporsi utama, sistem QR, atau kontrak integrasi RIQA OS harus:
- memiliki alasan perubahan;
- memperoleh version bump (mis. v1.1/v2.0);
- diuji terhadap PDF;
- dicatat dalam governance QURBATA.

Konten per halaman boleh berubah mengikuti tangga kompetensi tanpa mengubah kontrak layout blueprint.

## Baseline teknis

- Format halaman: 176 × 250 mm.
- Mesin layout: Vivliostyle.
- Grid Tartil: 8 × 3.
- Font Tartil baseline: 41 pt.
- Font Arab: KFGQPC Uthman Taha Naskh.
- QR: resolver RIQA OS per halaman.
- Build resmi: GitHub Actions QURBATA Book PDF.

## Keputusan

Mulai versi ini, pengembangan Jilid 1 dan jilid berikutnya harus menggunakan blueprint ini sebagai template dasar sampai ada keputusan governance yang menetapkan versi pengganti.
