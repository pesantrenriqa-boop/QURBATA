# QURBATA JILID 1 — MSL + COVERAGE AUDIT P011–P013

Status: **AUDIT v0.1**

## Audit scope
Memeriksa data P011–P013 v0.2 setelah Meaningful Sequence Layer (MSL) diintegrasikan. Audit tidak mengubah aturan lama.

## Gates
1. 24 kelompok per halaman.
2. 6 EXACT-2 + 18 EXACT-3.
3. zero duplicate per halaman.
4. tidak ada future competency.
5. setiap EXACT-3 wajib mengandung minimal satu TARGET halaman.
6. source word MSL tidak boleh berulang global.
7. coverage lama tidak boleh rusak tanpa dicatat.

## P011 — target كَ لَ
MSL: `كتب`, `ترك`, `ركب`.
- Semua MSL mengandung كَ.
- Semua kelompok 07–24 tetap mengandung كَ atau لَ.
- Global source duplicate: 0.
- Review breadth tetap luas.

**P011 = PASS.**

## P012 — target مَ نَ
MSL yang dimasukkan: `منع`, `نفع`, `نزل`, `نصر`, `نظر`, `عبد`.

Temuan fatal:
- `عَ بَ دَ` / `عبد` pada C12 **tidak mengandung مَ atau نَ**.
- Ini melanggar hard rule lama: setiap kelompok EXACT-3 P012 wajib mengandung minimal satu TARGET halaman.

Karena MSL tidak boleh mengalahkan kompetensi, `عبد` harus dikeluarkan dari P012. Kata `عبد` belum boleh diberi status USED.

**P012 = FAIL sampai C12 diperbaiki.**

## P013 — target هَ وَ يَ
MSL: `وعد`, `وهب`, `وجد`, `ولد`, `وقع`, `هلك`, `هجر`.
- Semua MSL mengandung وَ atau هَ.
- Semua kelompok 07–24 mengandung minimal satu هَ/وَ/يَ.
- Global source duplicate: 0.

**P013 = PASS.**

## Global uniqueness audit
Valid USED setelah audit:
`كتب`, `ترك`, `ركب`, `منع`, `نفع`, `نزل`, `نصر`, `نظر`, `وعد`, `وهب`, `وجد`, `ولد`, `وقع`, `هلك`, `هجر`

Total valid USED = **15**.

`عبد` = **RELEASED / NOT USED** karena tidak legal di P012.

## Required repair
P012/C12 harus kembali ke kelompok EXACT-3 yang:
- memuat مَ atau نَ;
- legal sampai P011;
- unik di P012;
- membantu coverage;
- boleh fonetik curated jika tidak ada meaningful word legal yang aman.

Keputusan audit: **aturan lama menang atas MSL. Jangan memaksa kata bermakna.**
