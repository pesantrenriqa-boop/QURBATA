# QJ2 — Register Sumber Recovery

**Status:** ACTIVE  
**Induk:** `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`

## Baseline Sumber

Commit `67a42c40d796cbdcead4e98f5d03da370ac22406` mencatat cakupan sumber Jilid 2 mencapai 40/40 halaman:

- P001–P020: `COMPLETE-DRAFT`;
- P021–P040: `STAGED-BLOCKED`.

Master pengendali: `books/jilid-2/QJ2-MASTER-Struktur-40-Halaman.md` versi 0.22.0-id atau penerus sahnya.

## Register

| Rentang | Status | Audit/Keputusan | Ketentuan recovery |
|---|---|---|---|
| P001–P015 | FOUND-COMPLETE-DRAFT | DEC-CUR-010 | Pilih hasil regenerasi sah. Versi lama dinyatakan `SUPERSEDED` dan tidak boleh digunakan. |
| P016–P020 | FOUND-COMPLETE-DRAFT | AUD-QJ2-CONTENT-011 | Ekstrak sebagai baseline fondasi bentuk lanjutan. |
| P021–P024 | FOUND-STAGED-BLOCKED | AUD-QJ2-TAN-003; BLK-QJ2-ORTHO-001 | Simpan isi tanwin sebagai sumber terblokir; jangan otorisasi cetak. |
| P025 | FOUND-STAGED-BLOCKED | Objek hafalan khusus | Isi dan metadata khusus harus dipisahkan dari pola halaman latihan biasa. |
| P026–P027 | FOUND-STAGED-BLOCKED | AUD-QJ2-MAD-001 | Kandidat mad alif dan mad ya; verifikasi urutan tangga terbaru. |
| P028 | FOUND-STAGED-BLOCKED | Objek Bahasa Arab khusus | Materi lisan dan materi baca peserta wajib dipisahkan. |
| P029–P030 | FOUND-STAGED-BLOCKED | AUD-QJ2-MAD-001 | Kandidat mad waw dan evaluasi mad. |
| P031–P040 | FOUND-STAGED-BLOCKED | AUD-QJ2-FINAL-001 | Ekstrak sebagai sumber akhir, lalu audit kata, frasa, evaluasi, dan halaman khusus. |

## Larangan

- Jangan mengambil QJ2-P001–P015 dari draf warisan yang telah superseded.
- Jangan mengubah status `STAGED-BLOCKED` menjadi siap cetak hanya karena file ditemukan.
- Jangan mencampur contoh peserta, naskah guru, audit, dan blocker dalam dataset latihan yang sama.
