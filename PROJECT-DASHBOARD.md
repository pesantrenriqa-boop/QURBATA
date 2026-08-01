# QURBATA — Dashboard Progres Proyek

**Status:** ACTIVE PROJECT CONTROL  
**Tanggal pembaruan:** 1 Agustus 2026  
**Pemilik Akademik:** Aris Liswanto  
**Repositori:** `pesantrenriqa-boop/QURBATA`  
**Cabang resmi:** `main`

## 1. Progres Utama

| Area | Target | Selesai | Progres | Status |
|---|---:|---:|---:|---|
| Penemuan sumber Jilid 1 | 40 halaman | 40 | 100% | SOURCE FOUND |
| Register/audit sumber Jilid 1 | 40 halaman | 40 | 100% | RECOVERY STATUS COMPLETE |
| Penemuan sumber Jilid 2 | 40 halaman | 40 | 100% | SOURCE COMPLETE |
| Register recovery terintegrasi Jilid 2 | 40 halaman | 40 | 100% | P001–P020 COMPLETE-DRAFT; P021–P040 STAGED-BLOCKED |
| Salinan isi penuh Jilid 2 ke jalur kanonik/recovery | 40 halaman | 24 | 60% | P021–P024 RECOVERED; P025–P040 NEXT |
| Penemuan sumber Jilid 3 | 40 halaman | 40 | 100% | SOURCE FOUND |
| Pengembalian batch Jilid 3 ke jalur resmi | 4 batch | 4 | 100% | RECOVERED-SOURCE-COMPLETE |
| Migrasi Jilid 3 ke file per halaman | 40 halaman | 40 | 100% | P001–P040 CREATED |
| Freeze sumber recovery Jilid 1–3 | 1 baseline | 1 | 100% | FROZEN |
| Snapshot branch pengaman | 1 branch | 1 | 100% | ACTIVE |

## 2. Ringkasan Persentase

- **Keamanan sumber data Jilid 1–3:** 100%
- **Register/status recovery 120 halaman:** 100%
- **Konsolidasi isi penuh ke jalur kanonik/recovery:** 87%
- **Audit akademik dan progression:** 33%
- **Kesiapan pilot/cetak:** belum dinilai sebagai progres recovery

## 3. Status per Jilid

### Jilid 1

- Struktur 40 halaman tersedia pada `books/jilid-1/`.
- Recovery register telah memetakan P001–P040.
- Konflik pemerataan mutlak, 50:50, dan 60:40 dipertahankan sampai keputusan final.

**Progres register recovery Jilid 1: 100%.**  
**Status akademik:** belum siap cetak.

### Jilid 2

- Sumber 40/40 ditemukan dan seluruh halaman memiliki register recovery.
- P001–P020 berstatus `COMPLETE-DRAFT`.
- P021–P040 berstatus `STAGED-BLOCKED`.
- Salinan isi penuh recovery sudah dibuat untuk `QJ2-P021.md` sampai `QJ2-P024.md` pada `books/jilid-2/recovery/pages/`.
- Isi P021–P024 tidak lagi hanya bergantung pada folder `regenerated/`.

**Progres keamanan/register Jilid 2: 100%.**  
**Progres salinan isi penuh Jilid 2: 24/40 — 60%.**

### Jilid 3

- Empat batch sumber dan file kanonik P001–P040 telah diamankan.
- Halaman yang sumbernya tidak lengkap tetap ditandai `RECOVERED-SOURCE-INCOMPLETE`; tidak ada materi rekaan.

**Progres keamanan dan migrasi Jilid 3: 100%.**

## 4. Gate Definisi Recovery 100%

- [x] seluruh sumber utama ditemukan;
- [x] commit asal dicatat;
- [x] baseline freeze dan snapshot branch dibuat;
- [x] P001–P040 Jilid 1 memiliki status recovery;
- [x] P001–P040 Jilid 2 memiliki register recovery;
- [x] P001–P040 Jilid 3 memiliki file per halaman;
- [ ] P021–P040 Jilid 2 mempunyai salinan isi penuh di jalur recovery;
- [ ] tidak ada sumber staging/batch sebagai satu-satunya salinan;
- [ ] manifest akhir dan freeze final diperbarui;
- [ ] checksum/commit baseline final dicatat.

## 5. Urutan Eksekusi Aktif

1. Mengekstrak isi penuh Jilid 2 P025–P040.
2. Membandingkan P006–P010 Jilid 3 dengan commit lanjutan `f9f9677a6a5388afa740158b969520dc61fbb7a0`.
3. Menjalankan audit duplikasi dan progression lintas Jilid 1–3.
4. Memperbarui freeze final dan snapshot branch.
5. Setelah recovery 100%, melanjutkan penyusunan halaman dan jilid berikutnya.

## 6. Dokumen Kendali

- `books/QURBATA-JILID-1-3-RECOVERY-FREEZE.md`
- `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`
- `books/jilid-1/RECOVERY-SOURCES.md`
- `books/jilid-2/RECOVERY-SOURCES.md`
- `books/jilid-2/recovery/QJ2-RECOVERED-SOURCE-P021-P040.md`
- `books/jilid-2/recovery/pages/QJ2-P021.md` sampai `QJ2-P024.md`
- `books/jilid-3/RECOVERY-SOURCES.md`
- `books/jilid-3/recovery/README.md`
