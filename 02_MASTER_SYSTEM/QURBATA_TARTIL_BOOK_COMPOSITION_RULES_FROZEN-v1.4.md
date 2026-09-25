# QURBATA TARTIL — ATURAN PENYUSUNAN BUKU

Status: **FROZEN v1.6.6**
Effective: 2026-09-25
Authority: **BOOK COMPOSITION MASTER**
Scope: penyusunan isi Tartil Jilid 1, tipografi latihan, glyph Arab, proporsi halaman, dan layout.

> v1.6.6 adalah authority aktif untuk pemilihan contoh/latihan Tartil. Aturan lama yang bertentangan—terutama fallback otomatis 1/2 huruf, random cycling, dan pemaksaan jumlah kelompok tanpa kecocokan kompetensi—dinyatakan OBSOLETE.

# A. PRINSIP KURIKULUM UTAMA

1. **PAGE COMPETENCY FIRST.** Setiap halaman mempunyai `TARGET` eksplisit dari Page Register. Seluruh contoh dan latihan harus diturunkan dari TARGET halaman itu, bukan dari pool global acak.
2. **CUMULATIVE BUT CONTROLLED.** Huruf/harakat lama boleh muncul hanya sebagai review terkontrol dan tidak boleh menggeser fokus TARGET.
3. **NO RANDOM CONTENT.** Generator dilarang membuat kombinasi dengan cycling/permutasi acak hanya untuk memenuhi 24 slot.
4. **NO SILENT FALLBACK.** Kekurangan stok contoh yang sah harus membuat `BUILD FAIL`, bukan otomatis menurunkan 3 huruf menjadi 2 atau 1 huruf.
5. **DETACHED ONLY.** Seluruh huruf latihan Tartil Jilid 1 wajib tunggal/terpisah. Sambung bukan kompetensi Jilid 1.
6. **ZERO DUPLICATE.** Kelompok identik tidak boleh berulang pada halaman yang sama.

# B. STRUKTUR HALAMAN REGULER

Struktur visual latihan tetap **8 baris × 3 kelompok = 24 kelompok**.

## B1. Dua baris penanaman
- Baris 1–2 = **6 kelompok**.
- Setiap kelompok penanaman wajib **tepat 2 huruf**, tidak 1 dan tidak 3.
- Kedua huruf harus berasal dari `TARGET` halaman.
- Untuk target tiga huruf A–B–C, enam pasangan dasar adalah seluruh pasangan berarah tanpa pengulangan diri: `AB, AC, BA, BC, CA, CB`.
- Tidak boleh ada huruf review pada dua baris penanaman.
- Tidak boleh ada kelompok satu huruf.

Contoh P003 TARGET `جَ حَ خَ`:
`جَ حَ | جَ خَ | حَ جَ`
`حَ خَ | خَ جَ | خَ حَ`

## B2. Enam baris latihan lanjutan
- Baris 3–8 = **18 kelompok**.
- Setiap kelompok wajib **tepat 3 huruf**.
- Kelompok 1 huruf atau 2 huruf pada area ini = `GROUP_LENGTH_FAIL`.
- Untuk halaman pengenalan huruf baru, **setiap kelompok 3 huruf wajib memuat minimal satu huruf TARGET**.
- Review hanya menggunakan huruf/harakat yang sudah legal sebelum halaman tersebut.
- Tidak boleh memasukkan huruf/harakat yang belum diajarkan.
- Komposisi sasaran: sekitar **60% bobot/kemunculan TARGET : 40% review**, dihitung pada level huruf/kompetensi, bukan sekadar jumlah kelompok.

# C. KEC0C0KAN KOMPETENSI

Untuk setiap halaman reguler generator wajib mempunyai:
- `TARGET`: huruf + harakat baru halaman itu;
- `REVIEW_ALLOWED`: seluruh kompetensi yang telah sah sebelum halaman itu;
- `FORBIDDEN`: semua huruf/harakat/fitur yang belum diajarkan.

Gate wajib:
1. semua 6 kelompok penanaman hanya memakai TARGET;
2. semua 18 kelompok latihan memuat TARGET;
3. seluruh unsur non-target harus termasuk REVIEW_ALLOWED;
4. satu saja unsur FORBIDDEN muncul → `COMPETENCY_MISMATCH_FAIL`;
5. halaman tidak boleh mengambil contoh dari halaman masa depan.

# D. NILAI LEKSIKAL / SEMANTIK

1. Kelompok 3 huruf dipilih secara **curated**, bukan random.
2. Bila kelompok 3 huruf dimaksudkan sebagai kata, wajib merupakan kata Arab/fusha/Qurani yang sah dengan harakat yang legal pada tahap tersebut.
3. Jangan mengarang kata untuk mengejar variasi.
4. Bila stok kata bermakna tidak cukup, gunakan kombinasi fonetik 3-huruf yang tetap legal dan relevan dengan TARGET hanya jika Page Register secara eksplisit mengizinkan `PHONETIC`; jika tidak, `BUILD FAIL` dan bank contoh harus dikurasi.
5. **Dilarang mengganti kekurangan stok 3-huruf dengan kelompok 2-huruf/1-huruf di baris 3–8.**

# E. HALAMAN KHUSUS / CHECKPOINT

P010, P020, P040 dan halaman yang Page Register tandai sebagai evaluasi/review tidak otomatis mengikuti pola pengenalan 2+6 baris.
- Struktur kelompoknya harus didefinisikan eksplisit di Page Register.
- Tidak boleh menggunakan fallback global.
- P019/P020 tetap curated.
- Jika struktur khusus belum didefinisikan, build berhenti dengan `SPECIAL_PAGE_SPEC_MISSING`.

# F. GATE PANJANG KELOMPOK

Untuk halaman reguler pengenalan:
- cell 1–6: `groupLen === 2`;
- cell 7–24: `groupLen === 3`;
- `groupLen === 1` selalu FAIL;
- jumlah total harus tepat 24;
- zero duplicate wajib.

Build errors resmi:
- `PLANTING_LENGTH_FAIL`
- `PRACTICE_LENGTH_FAIL`
- `SINGLE_LETTER_GROUP_FAIL`
- `DUPLICATE_GROUP_FAIL`
- `COMPETENCY_MISMATCH_FAIL`
- `FUTURE_COMPETENCY_FAIL`
- `SPECIAL_PAGE_SPEC_MISSING`

# G. HARD-DETACHED + HA

- Setiap huruf Arab di area Tartil dirender sebagai unit detached tersendiri.
- Ligature/contextual joining tidak boleh menyambungkan unit latihan.
- Font Arab: **KFGQPC Uthman Taha**.
- `ه` detached wajib lolos audit visual bentuk Ha dua lubang; Unicode tetap U+0647.

# H. LAYOUT FROZEN

- A5 portrait.
- Master visual tetap merujuk baseline P001/Build #31 untuk proporsi halaman.
- Urutan: Header → Penanaman → Panel Integrasi → Latihan Tartil → Footer.
- Area latihan dominan.
- Internal practice boxes tetap tidak wajib terlihat; alignment 8×3 dipertahankan.
- Footer: Tanggal | Nilai | TTD | QR | RIQA OS.
- Motto: `تَعَلَّمْ — اِعْمَلْ — عَلِّمْ`.

# I. VALIDASI PER HALAMAN SEBELUM PDF

Setiap halaman harus menghasilkan audit manifest minimal:
- page number;
- TARGET;
- REVIEW_ALLOWED;
- 6 planting groups;
- 18 practice groups;
- jumlah huruf per group;
- target occurrence ratio;
- duplicate count;
- forbidden/future competency count;
- detached renderer status;
- Ha sentinel status bila relevan.

PDF hanya boleh dibuat setelah seluruh halaman PASS.

# J. PRODUCTION GATE v1.6.6

`PAGE-REGISTER PASS → TARGET-MAPPING PASS → PLANTING EXACT-2 PASS → PRACTICE EXACT-3 PASS → COMPETENCY-MATCH PASS → FUTURE-COMPETENCY PASS → ZERO-DUPLICATE PASS → TARGET/REVIEW-RATIO PASS → DETACHED-LETTER PASS → HA-GLYPH PASS → LAYOUT PASS → PDF PASS`

**Jika satu gate gagal, jangan menghasilkan kandidat PDF final.**
