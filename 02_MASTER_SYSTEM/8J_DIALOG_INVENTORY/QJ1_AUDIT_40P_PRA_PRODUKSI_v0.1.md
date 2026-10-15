# Audit lintas-domain QURBATA Jilid 1 P001–P040 — v0.1

Status: **AUDIT DRAF / NOT FROZEN / NOT PRINT READY**. Diperiksa 15 Oktober 2026 pada branch `renderer/pagedjs-p001-prototype`.

## Hasil pemeriksaan dokumen
- Lima berkas skenario Opsi B berisi tepat 40 bagian halaman, tanpa halaman hilang: P001–P005 (5), P006–P010 (5), P011–P020 (10), P021–P030 (10), P031–P040 (10).
- Pemeriksaan pencocokan teks terhadap overlay `03_BOOKS/JILID-1/PAGE_REGISTER_P001-P040_INTEGRATION_FROZEN-v1.3.md`: 40/40 ungkapan Bi'ah cocok secara tekstual dan 40/40 nash/ungkapan Akhlak cocok secara tekstual di bagian skenario halaman. **Ini bukan tashih nash, validasi makna, atau uji praktik.**
- Otoritas Tartil empat register FROZEN v1.0 tetap berlaku. Tahfidz Opsi B v0.2 **hanya untuk validasi** dan berbeda dari target Tahfidz lama di register Tartil.
- Checkpoint: P010 evaluasi fathah, P020 checkpoint fathah/kasrah + 29 identitas huruf, P030 review Tahfidz, P040 checkpoint akhir 29 huruf dan tiga harakat. Tidak boleh diberi kompetensi Tartil baru.

## Temuan dan tindakan
| Kode | Temuan | Risiko | Tindakan |
|---|---|---|---|
| A01 | Target Tahfidz Opsi B belum diselaraskan dengan otoritas Tahfidz frozen dan entri lama register Tartil | Tinggi | Keputusan tertulis sebelum freeze baru; jangan mengubah register diam-diam |
| A02 | P039 Opsi B memuat Al-Ma'un 3–7 dalam satu halaman | Tinggi | Uji beban lapangan, retensi P040 dan kesinambungan J2; jangan mengklaim telah diuji |
| A03 | Seluruh skenario masih petunjuk guru, bukan 40 halaman layout santri | Tinggi | Produksi latihan Tartil legal, panel ayat dan arti terverifikasi, render A5 |
| A04 | Nash Tahfidz dan arti Indonesia belum ditashih satu per satu untuk cetak | Tinggi | Pemeriksaan mushaf dan penerjemahan per halaman |
| A05 | Kutipan Akhlak perlu audit asal, konteks, terjemah, dan atribusi | Sedang–tinggi | Tashih ahli; motto P040 bukan hadits |
| A06 | Ketepatan glyph ha dua lubang, grafem hamzah/alif, arah RTL, serta KFGQPC belum diuji pada render | Tinggi | Uji P013/P019/P027/P040 dan audit seluruh 40 halaman |
| A07 | P010 memiliki contoh grid 8×3; blok lain belum memiliki latihan final terverifikasi | Tinggi | Bank latihan per halaman dengan kontrol huruf legal dan 60/40 jika relevan |
| A08 | Dialog lisan memuat kosakata/struktur lebih tinggi daripada bacaan Tartil J1 | Terkendali | Pertahankan pemisahan: lisan melalui guru, tidak dinilai sebagai baca mandiri |

## Gate produksi berikutnya
1. Susun bank latihan Tartil per halaman dengan review kumulatif dan audit kompetensi legal.
2. Tashih nash, arti dan atribusi panel Tahfidz/Akhlak; cek konsistensi Bi'ah.
3. Validasi Tahfidz Opsi B dan beban P039; putuskan konflik otoritas secara tertulis.
4. Susun layout A5 dari sumber otoritatif; cek font, harakat, RTL, QR dan Tanggal–Nilai–TTD.
5. Review ahli dan audit visual sebelum label **SIAP CETAK**.

**Kesimpulan:** 40/40 skenario terdokumentasi dan panel Bi'ah/Akhlak cocok secara tekstual dengan overlay; **belum ada dasar untuk menyatakan buku siap cetak**.
