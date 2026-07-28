# QURBATA Print Automation

Pipeline ini membangkitkan layout buku peserta langsung dari sumber halaman Markdown. Tujuannya adalah satu perubahan isi menghasilkan layout baru tanpa penataan ulang 40 halaman secara manual.

## Build

```bash
python3 -m pip install -r production/print/requirements.txt
python3 production/print/generate_qurbata_pdf.py
```

Keluaran baku:

`output/pdf/QURBATA-Jilid-1-Peserta-print.pdf`

## Prinsip

- sumber Markdown tetap menjadi sumber tunggal;
- edisi peserta dan guru dipisahkan;
- 24 latihan dibentuk otomatis menjadi grid 4 × 6;
- teks Arab memakai shaping dan RTL;
- bleed, safe area, crop marks, metadata, dan preflight dihasilkan otomatis;
- hasil tidak disebut final sebelum pemeriksaan visual dan proof print.

Lihat `PRINT-SPEC-QURBATA-v1.md` untuk standar dan gate produksi.
