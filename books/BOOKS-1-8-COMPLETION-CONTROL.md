# QURBATA Buku 1–8 — Completion Control

**Kode:** CTL-BOOK-QUR-001  
**Status:** ACTIVE CONTROL  
**Tanggal:** 30 Juli 2026  
**Branch resmi:** `main`

## Tujuan

Dokumen ini mengendalikan penyelesaian Buku QURBATA Jilid 1–8 sebagai satu rangkaian. Tidak boleh ada versi paralel di luar jalur resmi berikut:

`books/jilid-N/QJN-MASTER-Struktur-40-Halaman.md` → `books/jilid-N/pages/QJN-P001.md` s.d. `QJN-P040.md` → data item → audit → review → pilot → otorisasi.

## Aturan Mutlak

1. Setiap jilid berisi 40 halaman materi baca.
2. Kode halaman final hanya `QJ1-P001` s.d. `QJ8-P040`.
3. Nama batch, regenerated, rebased, draft, dan staging bukan kode produk final.
4. Setiap halaman wajib memuat target baca, 24 kotak/objek latihan, murojaah kumulatif, integrasi Tahfidz, Bahasa Arab, hadis/akhlak, evaluasi, remedial, dan metadata keterlacakan.
5. Contoh diprioritaskan dari Al-Qur'an, lalu hadis, mufradat Arab bermakna, lalu drill terkendali.
6. Contoh Qurani wajib mempunyai Source-ID dan tashih.
7. Materi baru dan murojaah mengikuti keputusan kurikulum aktif; keputusan terbaru mengesampingkan versi lama.
8. Materi superseded dipindahkan ke `archive/` dan tidak boleh dipakai untuk cetak atau aplikasi.

## Status Nyata

| Jilid | Master 40 halaman | Halaman individual | Isi contoh | Audit | Status kontrol |
|---|---|---:|---|---|---|
| 1 | tersedia | 40/40 | draft lengkap | audit tersedia | konsolidasi dan validasi akhir |
| 2 | tersedia | 15 aktif awal + versi regenerated/rebased | perlu normalisasi ke 40 kode final | audit tersedia | konsolidasi prioritas |
| 3 | tersedia | masih berbentuk batch | 40 halaman draft batch | audit tersedia | pecah ke QJ3-P001–P040 dan tashih |
| 4 | tersedia | 0/40 | belum diproduksi | belum | produksi setelah gate Jilid 3 |
| 5 | tersedia | 0/40 | belum diproduksi | belum | produksi setelah gate Jilid 4 |
| 6 | tersedia | 0/40 | belum diproduksi | belum | produksi setelah gate Jilid 5 |
| 7 | tersedia | 0/40 | belum diproduksi | belum | produksi setelah gate Jilid 6 |
| 8 | tersedia | 0/40 | belum diproduksi | belum | produksi setelah gate Jilid 7 |

## Urutan Penyelesaian Terkunci

1. Normalisasi Jilid 2 menjadi satu folder `pages/` berisi 40 kode final.
2. Pecah materi batch Jilid 3 menjadi 40 halaman individual.
3. Audit lintas Jilid 1–3 agar tidak ada lompatan, pengulangan tidak perlu, atau materi prematur.
4. Produksi Jilid 4 halaman 1–40.
5. Produksi Jilid 5 halaman 1–40.
6. Produksi Jilid 6 halaman 1–40.
7. Produksi Jilid 7 halaman 1–40.
8. Produksi Jilid 8 halaman 1–40.
9. Audit vertikal Jilid 1–8.
10. Review ahli, pilot, revisi, dan otorisasi final.

## Definisi Selesai

Sebuah jilid tidak boleh disebut selesai hanya karena memiliki 40 file. Status `COMPLETE` mensyaratkan:

- 40 halaman individual;
- seluruh contoh terisi dan ditashih;
- distribusi materi baru dan murojaah lulus audit;
- tidak ada materi di luar prasyarat;
- Source-ID, Evidence-ID, dan Decision-ID lengkap;
- asesmen serta remedial tersedia;
- review ahli dan pilot tercatat;
- keputusan otorisasi diterbitkan.

## Larangan

- Tidak membuat “master content engine” terpisah dari registry resmi.
- Tidak membuat ulang kode huruf, pola, kata, atau contoh tanpa memeriksa registry.
- Tidak mempertahankan dua versi aktif untuk halaman yang sama.
- Tidak mengklaim Jilid 1–8 selesai sebelum gate di atas terpenuhi.
