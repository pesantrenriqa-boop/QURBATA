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
| Migrasi Jilid 3 ke file per halaman | 40 halaman | 30 | 75% | P001-P030 CREATED |
| Freeze sumber recovery Jilid 1–3 | 1 baseline | 1 | 100% | FROZEN |
| Snapshot branch pengaman | 1 branch | 1 | 100% | ACTIVE |

## 2. Ringkasan Persentase

- **Keamanan sumber data Jilid 1–3:** 100%
- **Pengembalian data ke jalur resmi proyek:** 96%
- **Konsolidasi menjadi satu file kanonik per halaman:** 75%
- **Audit akademik dan progression:** 17%
- **Kesiapan pilot/cetak:** belum dinilai sebagai progres recovery

## 3. Status per Jilid

### Jilid 1
- Struktur 40 halaman tersedia.
- Recovery register telah memetakan P001–P020.
- Prioritas berikutnya: audit dan register P021–P040.

### Jilid 2
- Sumber 40/40 ditemukan.
- P001–P020 `COMPLETE-DRAFT`; P021–P040 `STAGED-BLOCKED`.

### Jilid 3
- Empat batch sumber telah dikembalikan.
- File per halaman tersedia dari `QJ3-P001.md` sampai `QJ3-P030.md`.
- P006–P010, P027, dan P029 tetap `RECOVERED-SOURCE-INCOMPLETE` karena sumber tidak memberi contoh khusus terpisah.

**Progres migrasi per halaman Jilid 3: 75%.**

## 4. Gate Recovery 100%
- [x] seluruh sumber utama ditemukan;
- [x] commit asal dicatat;
- [x] baseline freeze dan snapshot dibuat;
- [ ] Jilid 1 P001–P040 memiliki status recovery;
- [ ] Jilid 2 P001–P040 berada pada jalur resmi;
- [ ] Jilid 3 P001–P040 memiliki file per halaman;
- [ ] manifest akhir dan freeze final diperbarui.

## 5. Urutan Eksekusi Aktif
1. Migrasi Jilid 3 P031–P040.
2. Bandingkan P006–P010 dengan commit lanjutan `f9f9677a6a5388afa740158b969520dc61fbb7a0`.
3. Selesaikan register Jilid 1 P021–P040.
4. Integrasikan Jilid 2 P021–P040.
5. Audit duplikasi dan progression.
6. Freeze final.
