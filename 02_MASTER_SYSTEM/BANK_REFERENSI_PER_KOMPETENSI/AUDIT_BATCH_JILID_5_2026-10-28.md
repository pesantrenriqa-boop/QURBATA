# Audit massal register QURBATA Jilid 5 — 28 Oktober 2026

**Sumber:** `REGISTER_24_KELOMPOK_JILID_5.md` pada branch `audit/j4-tashih-20261024`.

## Hasil pemeriksaan struktur (40 halaman)

- Kapasitas: **480 slot** (P001–P020 masing-masing 16; P021–P040 masing-masing 8).
- Terisi: **417 slot (86,875%)**.
- Kosong: **63 slot (13,125%)**.
- Pemeriksaan pola rujukan QS: **0 slot tanpa pola rujukan** pada halaman selain P028 (Bahasa Arab) dan P038 (Akhlak/Hadis).
- Redaksi identik setelah penghilangan harakat pada halaman sama: **1 pasangan**, yaitu P013 K02 dan K07; kedua rujukan **QS 6:143 dan QS 6:144**. Keduanya memiliki konteks ayat berbeda, sehingga **tidak boleh otomatis dihapus**.

## Halaman dengan kekosongan terbesar

| Halaman | Terisi | Kosong | Fokus |
|---|---:|---:|---|
| P013 | 4 | 12 | Mad farq: korpus terbatas, tidak perlu memaksakan 16 contoh berbeda |
| P009 | 6 | 10 | Mad silah thawilah: verifikasi ha dhamir dan hamzah sesudahnya |
| P011 | 10 | 6 | Mad lazim kalimi |
| P010 | 11 | 5 | Evaluasi Mad I |
| P012 | 12 | 4 | Mad lazim harfi |
| P014 | 12 | 4 | Kontras mad lazim |
| P006 | 13 | 3 | Kontras wajib–jaiz |
| P024 | 5 | 3 | Mad dan waqaf awal |

## Batas pemeriksaan

Audit ini hanya memeriksa **struktur, keterisian, keberadaan pola rujukan, dan redaksi identik**. Keberadaan label QS **tidak membuktikan** potongan ayat benar. Tashih mushaf Utsmani, ketepatan nomor ayat, dan kesesuaian tajwid **belum otomatis tervalidasi**. Contoh yang berstatus KANDIDAT tetap kandidat.

## Prosedur cepat dan aman

1. Jalankan `python tools/audit_qurbata_register.py 02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_5.md`.
2. Kelompokkan temuan per halaman, lakukan verifikasi teks terhadap mushaf otoritatif.
3. Jangan menggandakan ayat hanya untuk mengisi kuota. Biarkan slot kosong bila tidak ada contoh sah yang berbeda.
4. Simpan perubahan dalam batch dengan satu commit setelah pengecekan.
5. Jalankan audit ulang dan catat selisih keterisian sebelum–sesudah.

**Status:** pemeriksaan struktur telah dilakukan; validasi tajwid dan rasm belum dinyatakan selesai.
