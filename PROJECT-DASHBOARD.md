# QURBATA — Dashboard Progres Proyek

**Status:** ACTIVE PROJECT CONTROL  
**Tanggal pembaruan:** 1 Agustus 2026  
**Pemilik Akademik:** Aris Liswanto  
**Repositori:** `pesantrenriqa-boop/QURBATA`  
**Cabang resmi:** `main`

## 1. Progres Utama

| Area | Target | Selesai | Progres | Status |
|---|---:|---:|---:|---|
| Penemuan sumber Jilid 1 | 40 | 40 | 100% | SOURCE FOUND |
| Register/audit sumber Jilid 1 | 40 | 40 | 100% | RECOVERY STATUS COMPLETE |
| Penemuan sumber Jilid 2 | 40 | 40 | 100% | SOURCE COMPLETE |
| Register recovery terintegrasi Jilid 2 | 40 | 40 | 100% | COMPLETE |
| Salinan isi Jilid 2 ke jalur recovery | 40 | 30 | 75% | P021–P030 RECOVERED |
| Penemuan sumber Jilid 3 | 40 | 40 | 100% | SOURCE FOUND |
| Migrasi Jilid 3 per halaman | 40 | 40 | 100% | CREATED |
| Freeze dan snapshot pengaman | 1 | 1 | 100% | ACTIVE |

## 2. Ringkasan

- **Keamanan sumber Jilid 1–3:** 100%
- **Register/status recovery 120 halaman:** 100%
- **Konsolidasi isi ke jalur kanonik/recovery:** 92%
- **Audit akademik dan progression:** 33%
- **Kesiapan pilot/cetak:** belum dinyatakan.

## 3. Status per Jilid

### Jilid 1
Register P001–P040 lengkap. Konflik kebijakan dan gate ahli masih terbuka.

### Jilid 2
- P001–P020: `COMPLETE-DRAFT`.
- P021–P024: salinan recovery penuh unit tanwin.
- P025–P029: salinan recovery tangga mad alif dan transfer.
- P030: versi revisi mad waw; baru 16 contoh terkonfirmasi dan tetap memerlukan pelengkapan 24 kotak final.
- Seluruh P021–P030 berada di `books/jilid-2/recovery/pages/`.

**Progres salinan isi Jilid 2: 30/40 — 75%.**

### Jilid 3
Empat batch sumber dan file per halaman P001–P040 telah diamankan. Kekosongan sumber tetap ditandai, tidak diisi dengan materi rekaan.

## 4. Gate Recovery 100%

- [x] seluruh sumber utama ditemukan;
- [x] commit asal dicatat;
- [x] baseline freeze dan snapshot dibuat;
- [x] seluruh 120 halaman memiliki status recovery;
- [x] Jilid 3 P001–P040 memiliki file per halaman;
- [ ] Jilid 2 P031–P040 memiliki salinan isi pada jalur recovery;
- [ ] tidak ada sumber staging/batch sebagai satu-satunya salinan;
- [ ] manifest akhir, freeze final, dan commit baseline final dicatat.

## 5. Urutan Eksekusi Aktif

1. Ekstraksi Jilid 2 P031–P040.
2. Bandingkan Jilid 3 P006–P010 dengan commit lanjutan.
3. Audit duplikasi dan progression lintas Jilid 1–3.
4. Freeze final, snapshot, dan baseline commit.
5. Lanjut penyusunan halaman dan jilid berikutnya.

## 6. Dokumen Kendali

- `books/QURBATA-JILID-1-3-RECOVERY-FREEZE.md`
- `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`
- `books/jilid-1/RECOVERY-SOURCES.md`
- `books/jilid-2/RECOVERY-SOURCES.md`
- `books/jilid-2/recovery/QJ2-RECOVERED-SOURCE-P021-P040.md`
- `books/jilid-2/recovery/pages/QJ2-P021.md` sampai `QJ2-P030.md`
- `books/jilid-3/RECOVERY-SOURCES.md`
