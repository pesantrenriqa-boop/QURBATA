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
| Register/audit sumber Jilid 1 | 40 halaman | 20 | 50% | IN PROGRESS |
| Penemuan sumber Jilid 2 | 40 halaman | 40 | 100% | SOURCE COMPLETE |
| Integrasi kanonik Jilid 2 | 40 halaman | 20 | 50% | 20 COMPLETE-DRAFT; 20 STAGED-BLOCKED |
| Penemuan sumber Jilid 3 | 40 halaman | 40 | 100% | SOURCE FOUND |
| Pengembalian batch Jilid 3 ke jalur resmi | 4 batch | 4 | 100% | RECOVERED-SOURCE-COMPLETE |
| Migrasi Jilid 3 ke file per halaman | 40 halaman | 0 | 0% | NEXT PRIORITY |
| Freeze sumber recovery Jilid 1–3 | 1 baseline | 1 | 100% | FROZEN |
| Snapshot branch pengaman | 1 branch | 1 | 100% | ACTIVE |

## 2. Ringkasan Persentase

- **Keamanan sumber data Jilid 1–3:** 100%
- **Pengembalian data ke jalur resmi proyek:** 83%
- **Konsolidasi menjadi satu file kanonik per halaman:** 50%
- **Audit akademik dan progression:** 17%
- **Kesiapan pilot/cetak:** belum dinilai sebagai progres recovery

Persentase keamanan sumber berarti commit dan file sumber utama telah ditemukan serta dicatat. Persentase tersebut tidak berarti seluruh halaman sudah disahkan secara akademik atau siap cetak.

## 3. Status per Jilid

### Jilid 1

- Struktur 40 halaman tersedia pada `books/jilid-1/`.
- Halaman kanonik tersedia pada `books/jilid-1/pages/`.
- Recovery register telah memetakan P001–P020.
- Konflik pemerataan mutlak, 50:50, dan 60:40 dipertahankan sampai keputusan final.
- Prioritas berikutnya: audit dan register P021–P040.

**Progres recovery terkendali Jilid 1: 50%.**

### Jilid 2

- Sumber 40/40 ditemukan.
- P001–P020 berstatus `COMPLETE-DRAFT`.
- P021–P040 berstatus `STAGED-BLOCKED` dan tetap diamankan.
- Contoh kanonik sudah ditemukan pada `books/jilid-2/pages/`.
- Prioritas berikutnya: menyalin sumber terblokir ke jalur recovery resmi tanpa mengaktifkannya sebagai materi cetak.

**Progres keamanan sumber Jilid 2: 100%.**  
**Progres konsolidasi kanonik Jilid 2: 50%.**

### Jilid 3

Empat batch telah dikembalikan ke:

- `books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P001-P010.md`
- `books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P011-P020.md`
- `books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P021-P030.md`
- `books/jilid-3/recovery/QJ3-RECOVERED-SOURCE-P031-P040.md`

Prioritas berikutnya adalah migrasi tanpa kehilangan isi menjadi:

- `books/jilid-3/pages/QJ3-P001.md`
- hingga `books/jilid-3/pages/QJ3-P040.md`

**Progres keamanan sumber Jilid 3: 100%.**  
**Progres migrasi per halaman Jilid 3: 0%.**

## 4. Gate Definisi Recovery 100%

Recovery Jilid 1–3 hanya dinyatakan 100% apabila:

- [x] seluruh sumber utama ditemukan;
- [x] commit asal dicatat;
- [x] baseline freeze dibuat;
- [x] snapshot branch pengaman dibuat;
- [ ] P001–P040 Jilid 1 memiliki status recovery per halaman;
- [ ] P001–P040 Jilid 2 berada pada jalur kanonik/recovery resmi;
- [ ] P001–P040 Jilid 3 memiliki file kanonik per halaman;
- [ ] tidak ada sumber staging/batch sebagai satu-satunya salinan;
- [ ] manifest akhir dan freeze final diperbarui;
- [ ] checksum/commit baseline final dicatat.

## 5. Urutan Eksekusi Aktif

1. Menyelesaikan register Jilid 1 P021–P040.
2. Mengintegrasikan Jilid 2 P021–P040 sebagai sumber `STAGED-BLOCKED` yang aman.
3. Memecah recovery Jilid 3 menjadi QJ3-P001–P040 tanpa mengubah isi sumber.
4. Menjalankan audit duplikasi dan progression lintas Jilid 1–3.
5. Memperbarui freeze final dan snapshot branch.
6. Setelah recovery 100%, melanjutkan penyusunan halaman dan jilid berikutnya.

## 6. Dokumen Kendali

- `books/QURBATA-JILID-1-3-RECOVERY-FREEZE.md`
- `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`
- `books/jilid-1/RECOVERY-SOURCES.md`
- `books/jilid-2/RECOVERY-SOURCES.md`
- `books/jilid-3/RECOVERY-SOURCES.md`
- `books/jilid-3/recovery/README.md`

Dashboard ini harus diperbarui setelah setiap batch recovery atau perubahan status halaman.