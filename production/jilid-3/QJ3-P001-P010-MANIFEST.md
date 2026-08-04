# QJ3 P001–P010 — Production Manifest

**Batch:** QJ3-BATCH-001-010  
**Status:** AUDITED-WITH-CORRECTIONS  
**Source file:** `production/jilid-3/QJ3-P001-P010-PRODUCTION-BATCH.md`  
**Audit:** `production/jilid-3/QJ3-P001-P010-AUDIT-V1.md`

## Cakupan

| Halaman | Fokus | Unit utama | Jumlah kotak |
|---|---|---|---:|
| P001 | kata tiga huruf berharakat | QT-U-008, QT-U-009 | 24 |
| P002 | kontras bentuk dan pola kata | QT-U-010, QT-U-011 | 24 |
| P003 | mad fathah + alif | QT-U-012 | 24 |
| P004 | mad kasrah + ya sukun | QT-U-013 | 24 |
| P005 | mad dhammah + wawu sukun | QT-U-014 | 24 |
| P006 | campuran tiga mad | QT-U-015 | 24 |
| P007 | sukun target ringan | QT-U-016 | 24 |
| P008 | sukun tenggorokan dan tebal | QT-U-017 | 24 |
| P009 | kata empat–lima huruf | QT-U-018 | 24 |
| P010 | integrasi dan evaluasi | QT-U-012–QT-U-018 | 24 |

## Total

- Halaman: 10
- Kotak: 240
- Kotak per halaman: 24
- Materi baru/integrasi: 96
- Review langsung: 71
- Review berjarak: 53
- Review global: 20
- Rasio: 40% materi baru dan 60% murojaah

## Hasil audit V1

- Struktur dan rasio dinyatakan valid.
- Progression mad dinyatakan valid.
- Progression sukun per huruf target dinyatakan valid secara arah.
- Satu duplikasi internal ditemukan pada P009 K11 dan wajib dikoreksi dari `يَسْمَعُ` menjadi `يَفْتَحُ`.
- Semua drill buatan wajib diklasifikasikan sebagai `CONTROLLED_DRILL` atau `CONTROLLED_PATTERN`.
- Kata Arab yang belum diverifikasi dari mushaf tidak boleh diberi klaim Qur’ani.

## Klasifikasi sumber kanonik

Setiap kotak wajib memiliki salah satu SourceType:

1. `QURAN_VERIFIED`
2. `ARABIC_LEXICON`
3. `CONTROLLED_DRILL`
4. `CONTROLLED_PATTERN`
5. `RECOVERY_SOURCE`

## Gate sebelum APPROVED

1. Terapkan koreksi audit V1.
2. Tambahkan SourceType untuk seluruh 240 kotak.
3. Verifikasi mushaf untuk item berstatus `QURAN_VERIFIED`.
4. Audit duplikasi terhadap Jilid 1–2.
5. Migrasi ke file kanonik `books/jilid-3/pages/QJ3-P001.md` sampai `QJ3-P010.md`.
6. Review akademik pemilik.

## Keputusan desain

- Contoh recovery dipertahankan bila sesuai progression.
- Contoh terlalu lanjut dipindahkan ke HOLD, tidak dihapus.
- Struktur review mengikuti prinsip Iqro’: materi lama tetap hadir sejak bagian awal sampai akhir jilid.
- Susunan, pemilihan, kode, distribusi, dan progression halaman merupakan struktur asli QURBATA.
