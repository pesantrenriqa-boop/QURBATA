# DEC-TAHFIDZ-J1-ALIGNMENT-001 — Persetujuan Arah Opsi B

**Status:** OWNER-APPROVED-FOR-VALIDATION / NOT FROZEN / NOT ACTIVE
**Tanggal pencatatan:** 14 Oktober 2026
**Rujukan keputusan:** persetujuan eksplisit pemilik akademik dalam percakapan: "opsi b".
**Scope:** QURBATA Jilid 1 P001–P040, hanya arah penyelarasan Tahfidz.
**Tidak mengubah:** register Tartil FROZEN v1.0, integrasi Bi'ah/Akhlak FROZEN v1.3, DEC-CUR-004, atau dokumen distribusi Tahfidz FROZEN.

## Keputusan yang disetujui

Pemilik akademik memilih **Opsi B** dari `DEC_TAHFIDZ_J1_ALIGNMENT_001_DRAFT.md` sebagai **dasar revisi untuk diuji**, yaitu `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.2.md` (REVISED CANDIDATE / NOT FROZEN).

- P010: review gate, tanpa hafalan baru.
- P020: review gate, tanpa hafalan baru.
- P030: review gate, tanpa hafalan baru.
- P040: terminal consolidation, tanpa hafalan baru.
- P039: target kandidat Al-Ma'un 3–7; **FIELD TEST REQUIRED** karena beban lima ayat dalam satu halaman.
- Tahfidz J1 tetap jalur **talqin**; target hafalan tidak dianggap kompetensi Tartil membaca mandiri.

## Hubungan dengan DEC-CUR-004

`curriculum/DEC-CUR-004-Aktivasi-Objek-Tahfidz-Jilid-1.md` tetap berstatus **OWNER-APPROVED-FOR-VALIDATION — BELUM ACTIVE**. Objek Al-Fatihah HAF-000001–000003 tidak otomatis dibatalkan atau diaktifkan oleh persetujuan Opsi B. Hubungan operasional antara objek tersebut dan pemetaan 40 halaman masih harus ditetapkan melalui audit ahli dan keputusan lanjutan.

## Konsekuensi dan pekerjaan yang diizinkan

1. Menyusun crosswalk kandidat Opsi B untuk 40 halaman dengan field `TAHFIDZ_NEW_TARGET`, `TAHFIDZ_MODE`, `MUROJAAH_SCOPE`, dan `IS_REVIEW_GATE`.
2. Menyusun rancangan uji beban P039 dan retensi checkpoint.
3. Mengkaji dampak perubahan distribusi terhadap awal Jilid 2, integrasi RIQA OS dan objek DEC-CUR-004.
4. Meminta validasi ahli Tahfidz/Qiraat, tashih ayat, terjemah, rasm, tajwid, waqaf/ibtida, dan bukti dengan Evidence-ID.
5. Setelah validasi lulus, **mengajukan** register baru berversi untuk persetujuan freeze terpisah.

## Larangan dan batas status

- Jangan mengedit dokumen FROZEN lama secara diam-diam.
- Jangan menyatakan map v0.2 sudah FROZEN, tashih selesai, atau buku siap cetak.
- Jangan mengaktifkan target otomatis Tahfidz di Supabase/RIQA OS sebelum gate dan keputusan aktivasi tersendiri.
- Jika uji beban P039 tidak lulus, evaluasi pemindahan sebagian target ke Jilid 2; ini **usulan bersyarat**, bukan perubahan yang telah disetujui.

## Gate validasi

- [ ] Review ahli dengan Evidence-ID dan keputusan qiraah/tahfidz
- [ ] Tashih teks ayat, rasm, harakat, terjemah, tajwid, waqaf/ibtida
- [ ] Uji beban P039 dan keputusan jika gagal
- [ ] Audit retensi P010/P020/P030/P040
- [ ] Audit hubungan dengan DEC-CUR-004
- [ ] Audit kesinambungan J2 dan RIQA OS
- [ ] Register revisi disahkan secara terpisah
- [ ] Audit render A5 dan otorisasi publikasi

**Kesimpulan:** Opsi B **disetujui untuk dikembangkan dan divalidasi**, bukan disahkan sebagai pemetaan final.
