# QJ5 — Audit otomatis awal register (28 Oktober 2026)

Sumber: `REGISTER_24_KELOMPOK_JILID_5.md` pada branch `audit/j4-tashih-20261024`.

- Kapasitas aktif: **480** (20 halaman ×16 + 20 halaman ×8).
- Kandidat terisi: **468**; kosong: **12**, seluruhnya P013 Mad Farq dan disengaja.
- Kolom Sah seluruh halaman: **0**; belum ada tashih final yang tercatat.
- Pemeriksaan **teks contoh identik persis** (Unicode NFC, mengabaikan catatan dalam kurung siku): **272** kemunculan ulang setelah kemunculan pertama. Ini indikator audit, bukan otomatis kesalahan: kompetensi yang berbeda mungkin memerlukan pengulangan terkendali.
- Kandidat tanpa pola rujukan `QS nomor:ayat`: **8** (P028 K01, P028 K02, P028 K03, P028 K04, P028 K05, P028 K06, P028 K07, P028 K08); sebagian dapat berupa notasi ayat lain, sehingga perlu audit manual.
- **Jangan menyamakan kelengkapan kandidat dengan kelulusan tashih.**
- Audit lanjutan: cek rasm Utsmani, sumber ayat, kompetensi target, hukum prasyarat, variasi antarhalaman dan lintas jilid, serta contoh berulang.

## Sampel duplikasi identik untuk diperiksa
- P002 K08 = P003 K01
- P002 K16 = P003 K02
- P002 K07 = P003 K03
- P002 K10 = P003 K04
- P002 K04 = P003 K06
- P002 K11 = P003 K07
- P002 K03 = P003 K08
- P002 K15 = P003 K10
- P002 K02 = P003 K11
- P001 K04 = P004 K02
- P004 K15 = P005 K01
- P004 K04 = P005 K02
- P001 K04 = P005 K04
- P004 K01 = P005 K05
- P004 K07 = P005 K06
- P004 K12 = P005 K07
- P004 K13 = P005 K08
- P004 K08 = P005 K10
- P004 K05 = P005 K11
- P002 K01 = P006 K01
- P004 K01 = P006 K02
- P002 K04 = P006 K03
- P004 K03 = P006 K04
- P002 K16 = P006 K05
- P002 K02 = P006 K07
- P001 K04 = P006 K08
- P002 K06 = P006 K09
- P002 K03 = P006 K11
- P004 K12 = P006 K12
- P002 K05 = P006 K14

Catatan: audit ini bersifat deteksi awal berbasis teks; **tidak mengesahkan maupun menghapus contoh**.
