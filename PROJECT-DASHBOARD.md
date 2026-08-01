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
| Salinan isi penuh Jilid 2 ke jalur kanonik/recovery | 40 halaman | 20 | 50% | P021–P040 NEXT EXTRACTION |
| Penemuan sumber Jilid 3 | 40 halaman | 40 | 100% | SOURCE FOUND |
| Pengembalian batch Jilid 3 ke jalur resmi | 4 batch | 4 | 100% | RECOVERED-SOURCE-COMPLETE |
| Migrasi Jilid 3 ke file per halaman | 40 halaman | 40 | 100% | P001–P040 CREATED |
| Freeze sumber recovery Jilid 1–3 | 1 baseline | 1 | 100% | FROZEN |
| Snapshot branch pengaman | 1 branch | 1 | 100% | ACTIVE |

## 2. Ringkasan Persentase

- **Keamanan sumber data Jilid 1–3:** 100%
- **Register/status recovery 120 halaman:** 100%
- **Konsolidasi isi penuh ke jalur kanonik/recovery:** 83%
- **Audit akademik dan progression:** 33%
- **Kesiapan pilot/cetak:** belum dinilai sebagai progres recovery

Persentase keamanan sumber berarti commit dan file sumber utama telah ditemukan serta dicatat. Persentase tersebut tidak berarti seluruh halaman sudah disahkan secara akademik atau siap cetak.

## 3. Status per Jilid

### Jilid 1

- Struktur 40 halaman tersedia pada `books/jilid-1/`.
- Halaman kanonik tersedia pada `books/jilid-1/pages/`.
- Recovery register telah memetakan P001–P040.
- Konflik pemerataan mutlak, 50:50, dan 60:40 dipertahankan sampai keputusan final.
- Unit Bahasa Arab, hafalan, akhlak, evaluasi, simulasi, dan checkpoint nama huruf telah dipisahkan statusnya dari halaman latihan baca.

**Progres register recovery Jilid 1: 100%.**  
**Status akademik:** masih memiliki konflik kebijakan dan gate ahli; belum siap cetak.

### Jilid 2

- Sumber 40/40 ditemukan.
- P001–P020 berstatus `COMPLETE-DRAFT`.
- P021–P040 berstatus `STAGED-BLOCKED`.
- Register terintegrasi P021–P040 tersedia pada `books/jilid-2/recovery/QJ2-RECOVERED-SOURCE-P021-P040.md`.
- Jalur sumber lama yang terkunci: `books/jilid-2/regenerated/`.
- Tahap berikutnya adalah menyalin isi penuh setiap sumber staged ke file recovery/kanonik per halaman tanpa mengubah statusnya.

**Progres keamanan dan register sumber Jilid 2: 100%.**  
**Progres salinan isi penuh per halaman Jilid 2: 50%.**

### Jilid 3

Empat batch sumber telah dikembalikan ke jalur recovery resmi, dan file kanonik per halaman telah dibuat lengkap:

- `books/jilid-3/pages/QJ3-P001.md`
- hingga `books/jilid-3/pages/QJ3-P040.md`

P001–P036 memuat contoh yang ditemukan atau hasil pemetaan terkendali dari batch sumber. P006–P010, P027, P029, dan P037–P039 tetap diberi status `RECOVERED-SOURCE-INCOMPLETE` apabila sumber batch tidak memberi contoh khusus. Tidak ada materi baru yang direkayasa untuk menutup kekosongan.

**Progres keamanan sumber Jilid 3: 100%.**  
**Progres migrasi per halaman Jilid 3: 100%.**

## 4. Gate Definisi Recovery 100%

Recovery Jilid 1–3 hanya dinyatakan 100% apabila:

- [x] seluruh sumber utama ditemukan;
- [x] commit asal dicatat;
- [x] baseline freeze dibuat;
- [x] snapshot branch pengaman dibuat;
- [x] P001–P040 Jilid 1 memiliki status recovery per halaman;
- [x] P001–P040 Jilid 2 memiliki register recovery resmi;
- [x] P001–P040 Jilid 3 memiliki file kanonik per halaman;
- [ ] P021–P040 Jilid 2 mempunyai salinan isi penuh di jalur recovery/kanonik;
- [ ] tidak ada sumber staging/batch sebagai satu-satunya salinan;
- [ ] manifest akhir dan freeze final diperbarui;
- [ ] checksum/commit baseline final dicatat.

## 5. Urutan Eksekusi Aktif

1. Mengekstrak isi penuh Jilid 2 P021–P040 dari `books/jilid-2/regenerated/` ke jalur recovery resmi.
2. Membandingkan P006–P010 Jilid 3 dengan versi lanjutan commit `f9f9677a6a5388afa740158b969520dc61fbb7a0`.
3. Menjalankan audit duplikasi dan progression lintas Jilid 1–3.
4. Memperbarui freeze final dan snapshot branch.
5. Setelah recovery 100%, melanjutkan penyusunan halaman dan jilid berikutnya.

## 6. Dokumen Kendali

- `books/QURBATA-JILID-1-3-RECOVERY-FREEZE.md`
- `books/RECOVERY-CONSOLIDATION-INDEX-JILID-1-3.md`
- `books/jilid-1/RECOVERY-SOURCES.md`
- `books/jilid-2/RECOVERY-SOURCES.md`
- `books/jilid-2/recovery/QJ2-RECOVERED-SOURCE-P021-P040.md`
- `books/jilid-3/RECOVERY-SOURCES.md`
- `books/jilid-3/recovery/README.md`

Dashboard ini harus diperbarui setelah setiap batch recovery atau perubahan status halaman.
