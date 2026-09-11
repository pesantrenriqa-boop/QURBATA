# QURBATA JILID 1 - ORGANIC ARABESQUE MASTER - FROZEN v1.0

**Status:** FROZEN / APPROVED VISUAL ORNAMENT BASELINE  
**Tanggal:** 2026-09-11  
**Pemilik akademik:** Aris Liswanto  
**Scope:** QURBATA Jilid 1 P001-P040  
**Parent visual contract:** governance/QURBATA-JILID-1-VISUAL-PAGE-CONTRACT-FROZEN-v1.0.md

## Keputusan

Gaya ornamen P001 dengan sistem **organic arabesque** dinyatakan disimpan sebagai baseline visual untuk kelanjutan halaman QURBATA Jilid 1.

Aturan yang dikunci:

1. Ornamen tidak memakai pola repetitif kaku sebagai elemen dominan.
2. Ornamen menggunakan garis kurva arabesque organik, aksen sudut, medallion kecil, serta hiasan tengah atas-bawah.
3. Palet utama tetap hijau tua, emas, dan krem/putih hangat.
4. Ornamen harus ringan dan menyisakan ruang putih; latihan Tartil tetap dominan secara visual.
5. Ornamen berada sebagai layer dekoratif dan tidak boleh mengubah data kurikulum, teks Arab, urutan panel, grid latihan, QR, atau administrasi footer.
6. Seluruh huruf Arab produksi tetap memakai KFGQPC Uthman Taha.
7. Geometri dan keluarga ornamen yang sama diteruskan ke P002-P040 agar tidak terjadi visual drift.
8. Bila kemudian dipakai aset ornamen eksternal, aset tersebut harus tetap tunduk pada baseline ini dan tidak boleh mengganggu keterbacaan latihan.

## Implementasi produksi

Baseline saat ini diimplementasikan melalui:

- `production/vivliostyle/scripts/inject-p001-mushaf-ornament.mjs`
- Build P001 pada pipeline Vivliostyle branch `codex/qurbata-uthmani-font`

P002 dan halaman berikutnya wajib mewarisi sistem ornamen yang sama sampai ada keputusan revisi eksplisit dari pemilik akademik.

**Status akhir:** `QJ1_ORNAMENT_MASTER = ORGANIC_ARABESQUE_FROZEN_v1.0`
