# QURBATA Content Pipeline v1.0 — audit aman, tanpa mengubah naskah

## Tujuan
Memeriksa kelengkapan 320 halaman (8 jilid × 40 halaman) dalam sekali jalan, menghasilkan daftar halaman hilang dan masalah integrasi. **Script tidak mengubah file, tidak mengesahkan hadis, tidak membandingkan mushaf primer, dan tidak pernah menaikkan status CONTENT-FINAL.**

## Cara menjalankan
Dari akar repository:
```bash
python 02_MASTER_SYSTEM/8J_DIALOG_INVENTORY/QURBATA_CONTENT_PIPELINE_v1.0.py --root 02_MASTER_SYSTEM --out audit-qurbata
```
Hasil: `audit-qurbata/audit.csv` dan `audit-qurbata/summary.json`.

## Validasi otomatis vs manual
- Otomatis: file ada, penanda empat inventaris, penanda FROZEN, indikator integrasi kandidat hadis J2.
- Manual wajib: G1 token mushaf Utsmani + kunci; G2 dialog Arab; G3 takhrij dan konteks hadis; G4 setoran dan urutan ayat FROZEN; G5 integrasi dan layout.
- Semua hasil otomatis adalah indikator **REVIEW** saja. **Tidak boleh memberi label final dari regex atau AI semata.**
- Format filename J1/J3–J8 belum tentu sama dengan J2; angka file hilang dari script adalah *missing dalam format ini*, bukan bukti tidak ada inventaris di repo.
- Script memeriksa **keberadaan penanda**, bukan kebenaran isi. Audit mendalam perlu validator berbasis data terstruktur, Quran corpus terverifikasi, dan penashih.
- Perbaiki 10–20 halaman per batch; gunakan SHA commit, catat error; jangan menulis ulang Tahfidz FROZEN.
