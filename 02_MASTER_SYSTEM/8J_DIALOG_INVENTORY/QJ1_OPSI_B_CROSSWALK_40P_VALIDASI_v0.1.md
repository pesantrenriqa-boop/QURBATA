# QURBATA J1 — CROSSWALK OPERASIONAL OPSI B P001–P040 v0.1

**Status: OWNER-APPROVED-FOR-VALIDATION / NOT FROZEN / NOT PRINT READY.**

**Sumber baris:** `02_MASTER_SYSTEM/TAHFIDZ/QURBATA-TAHFIDZ-J1-P001-P040-MAP-v0.2.md` (salinan target, mode, murojaah dan alignment apa adanya). Keputusan arah: `DEC_TAHFIDZ_J1_ALIGNMENT_001_OWNER_DIRECTION_OPSI_B.md`. Ini matriks validasi, bukan revisi dokumen FROZEN.

## Data 40 halaman

| Halaman | TAHFIDZ_NEW_TARGET | TAHFIDZ_MODE | MUROJAAH_SCOPE / VALIDATION_FOCUS | TARTIL_ALIGNMENT | IS_REVIEW_GATE |
|---|---|---|---|---|---|
| P001 | An-Nas 1 | TQ | target baru | PREVIEW | FALSE |
| P002 | An-Nas 2 | TQ | An-Nas 1 | PREVIEW | FALSE |
| P003 | An-Nas 3 | TQ | An-Nas 1–2 | PREVIEW | FALSE |
| P004 | An-Nas 4 | TQ | An-Nas 1–3 | PREVIEW | FALSE |
| P005 | An-Nas 5 | TQ | An-Nas 1–4 | PREVIEW | FALSE |
| P006 | An-Nas 6 | TQ | An-Nas 1–5; tutup surah | PREVIEW | FALSE |
| P007 | Al-Falaq 1 | TQ | An-Nas lengkap | PREVIEW | FALSE |
| P008 | Al-Falaq 2 | TQ | Al-Falaq 1 + An-Nas | PREVIEW | FALSE |
| P009 | Al-Falaq 3 | TQ | Al-Falaq 1–2 + An-Nas | PREVIEW | FALSE |
| P010 | NONE | RG | validasi An-Nas lengkap + Al-Falaq 1–3 | PREVIEW | TRUE |
| P011 | Al-Falaq 4 | TV | Al-Falaq 1–3 | PREVIEW | FALSE |
| P012 | Al-Falaq 5 | TV | Al-Falaq 1–4; tutup surah | PREVIEW | FALSE |
| P013 | Al-Ikhlas 1 | TV | An-Nas + Al-Falaq | PREVIEW | FALSE |
| P014 | Al-Ikhlas 2 | TV | Al-Ikhlas 1 | PREVIEW | FALSE |
| P015 | Al-Ikhlas 3–4 | TV | Al-Ikhlas 1–2; tutup surah | PREVIEW | FALSE |
| P016 | Al-Fatihah 1 | TV | 3 surah pendek | PREVIEW | FALSE |
| P017 | Al-Fatihah 2 | TV | Al-Fatihah 1 | PREVIEW | FALSE |
| P018 | Al-Fatihah 3 | TV | Al-Fatihah 1–2 | PREVIEW | FALSE |
| P019 | Al-Fatihah 4 | TV | Al-Fatihah 1–3 | PREVIEW | FALSE |
| P020 | NONE | RG | validasi Al-Fatihah 1–4 + 3 surah pendek | PREVIEW | TRUE |
| P021 | Al-Fatihah 5 | TV | Al-Fatihah 1–4 | PREVIEW | FALSE |
| P022 | Al-Fatihah 6 | TV | Al-Fatihah 1–5 | PREVIEW | FALSE |
| P023 | Al-Fatihah 7 | TV | Al-Fatihah lengkap | PREVIEW | FALSE |
| P024 | Al-Kawthar 1 | TV | Al-Fatihah lengkap | PREVIEW | FALSE |
| P025 | Al-Kawthar 2–3 | TV | Al-Kawthar 1; tutup surah | PREVIEW | FALSE |
| P026 | An-Nasr 1 | T3 | Al-Kawthar + Al-Fatihah | PARTIAL | FALSE |
| P027 | An-Nasr 2 | T3 | An-Nasr 1 | PARTIAL | FALSE |
| P028 | An-Nasr 3 | T3 | An-Nasr 1–2; tutup surah | PARTIAL | FALSE |
| P029 | Al-Kafirun 1–2 | T3 | An-Nasr lengkap | PARTIAL | FALSE |
| P030 | NONE | RG | cumulative gate: Al-Fatihah + An-Nas s.d. An-Nasr + Al-Kafirun 1–2 | PARTIAL | TRUE |
| P031 | Al-Kafirun 3–4 | T3 | Al-Kafirun 1–2 | PARTIAL | FALSE |
| P032 | Al-Kafirun 5–6 | T3 | Al-Kafirun 1–4; tutup surah | PARTIAL | FALSE |
| P033 | Al-Masad 1 | T3 | Al-Kafirun lengkap | PARTIAL | FALSE |
| P034 | Al-Masad 2 | T3 | Al-Masad 1 | PARTIAL | FALSE |
| P035 | Al-Masad 3 | T3 | Al-Masad 1–2 | PARTIAL | FALSE |
| P036 | Al-Masad 4 | T3 | Al-Masad 1–3 | PARTIAL | FALSE |
| P037 | Al-Masad 5 | T3 | Al-Masad 1–4; tutup surah | PARTIAL | FALSE |
| P038 | Al-Ma'un 1–2 | T3 | Al-Masad lengkap | PARTIAL | FALSE |
| P039 | Al-Ma'un 3–7 | T3 | Al-Ma'un 1–2; tutup surah melalui talqin bertahap | PARTIAL | FALSE |
| P040 | NONE | TC | terminal validation seluruh corpus J1 | PARTIAL | TRUE |

## Kontrol validasi

- P010, P020, P030: RG, **tidak ada hafalan baru**; P040: TC, **tidak ada hafalan baru**.
- P039: Al-Ma'un 3–7 adalah **CANDIDATE LOAD STRESS POINT**, bukan target siap cetak; jangan pecah/geser ayat tanpa keputusan revisi berikutnya.
- TQ = TALQIN dominant; TV = TALQIN + visual familiarity; T3 = TALQIN + three-harakat awareness. PREVIEW/PARTIAL tidak berarti santri mampu membaca mushaf mandiri.
- Seluruh teks ayat, terjemah, qiraah, waqaf, tajwid dan kelayakan beban memerlukan pemeriksaan ahli.
- Keputusan DEC-CUR-004 mengenai objek Al-Fatihah tetap **INACTIVE**, tidak otomatis diganti oleh matriks ini.
- Bila P039 tidak layak, evaluasi redistribusi ke J2. J2 P001 baseline saat ini Quraisy 1–2; perubahan harus dianalisis untuk mencegah beban ganda.

## Gate

- [ ] Ahli menilai beban P039, talqin, retensi dan safeguarding.
- [ ] Tashih nash dan verifikasi seluruh 40 target.
- [ ] Keputusan tertulis hubungan dengan DEC-CUR-004.
- [ ] Audit kesinambungan J2 dan dampak RIQA OS.
- [ ] Persetujuan freeze baru dan izin publikasi terpisah.
