# MATRIKS PENGUMPULAN EMPAT DOMAIN QURBATA 8 JILID — v0.1

**Status:** staging pra-produksi. Belum berarti 320 halaman siap cetak.

## Dokumen yang sudah tersedia

1. `02_MASTER_SYSTEM/QURBATA_8J_INVENTARIS_TARTIL_PRA_PRODUKSI_v0.1.md` — peta materi Tartil 8 × 40 halaman dari master historis, dengan peringatan konflik J1.
2. `02_MASTER_SYSTEM/QURBATA_J1_KOMPILASI_4_DOMAIN_P001-P040_v0.1.md` — empat register Tartil J1 serta overlay integrasi J1 yang sudah ada.

## Matriks status per jilid

| Jilid | Tartil | Percakapan guru–santri | Akhlak/Hadis | Tahfidz |
|---|---|---|---|---|
| 1 | Empat register FROZEN 40 halaman; konflik historis ditandai | Bi'ah overlay 40 halaman; dialog integratif baru P001 contoh, sisanya belum disahkan | Overlay tema/nash P001–P040 tersedia; audit jenis sumber diperlukan | Urutan sebagian ada dalam register; P011–P020 perlu master Tahfidz |
| 2 | Master 40 halaman draf; bentuk sambung, tanwin, mad asli | Belum ditemukan bank dialog terintegrasi lengkap | Panel akhlak/hadis diwajibkan master, rincian 40 halaman belum diverifikasi | Panel diwajibkan, pilihan ayat 40 halaman belum diverifikasi |
| 3 | Master 40 halaman draf; sukun dan qamariyah | Belum ditemukan bank dialog terintegrasi lengkap | Tema/teks per halaman perlu ditelusuri | Pilihan ayat per halaman perlu ditelusuri |
| 4 | Master 40 halaman draf; nun/mim sakinah, alif-lam | Belum ditemukan bank dialog terintegrasi lengkap | Tema J4: lisan, prasangka, tolong-menolong, tetangga; nash perlu diverifikasi | Unit hafalan masih generik dalam master |
| 5 | Master 40 halaman draf; mad lanjutan | Belum ditemukan bank dialog terintegrasi lengkap | Tema J5: niat, tanggung jawab, disiplin, adil; nash perlu diverifikasi | Unit hafalan masih generik dalam master |
| 6 | Master 40 halaman draf; tafkhim–tarqiq, waqaf–ibtida' | Belum ditemukan bank dialog terintegrasi lengkap | Tema J6: persaudaraan, konflik, maaf, sosial; nash perlu diverifikasi | Unit hafalan masih generik dalam master |
| 7 | Master 40 halaman draf; tartil terpadu dan mutasyabihat | Belum ditemukan bank dialog terintegrasi lengkap | Tema J7: kepemimpinan, khidmah, musyawarah; nash perlu diverifikasi | Unit hafalan masih generik dalam master |
| 8 | Master 40 halaman draf; tashih internal dan transfer | Belum ditemukan bank dialog terintegrasi lengkap | Tema J8: istiqamah, hikmah, kematangan moral; nash perlu diverifikasi | Unit hafalan masih generik dalam master |

## Skema yang harus diisi sebelum produksi setiap halaman

```yaml
unit_id: QJx-Pxxx
tartil:
  source_register: REQUIRED
  active_competence: REQUIRED
  review_competence: REQUIRED
  approved: false
quranic_examples:
  - text_exact: REQUIRED
    surah: REQUIRED
    ayah: REQUIRED
    source_id: REQUIRED
    verified_against_mushaf: false
    within_tartil_prerequisites: false
arabic_interaction:
  teacher_prompt: REQUIRED
  student_response: REQUIRED
  interaction_level: REQUIRED
  derived_from: REQUIRED
  is_quran_quotation: false
tahfidz:
  source_surah: REQUIRED
  ayah_range: REQUIRED
  verified: false
akhlaq:
  theme: REQUIRED
  source_type: QURAN_OR_HADITH_OR_TEACHER_GUIDANCE
  source_reference: REQUIRED
  verified: false
assessment:
  tartil: REQUIRED
  arabic_interaction: REQUIRED
production_gate: BLOCKED_UNTIL_VERIFIED
```

## Ketentuan isi
- Kompetensi Tartil tidak berubah karena kebutuhan percakapan.
- Teks Qurani wajib persis, berlokasi jelas, dan diverifikasi; huruf lepas pedagogis tidak diberi label kutipan mushaf.
- Hadis harus memiliki rujukan hadis dan status verifikasi; ungkapan guru bukan hadis.
- Pilihan Tahfidz memperhatikan progresi hafalan yang telah ditetapkan dan tidak harus sama dengan tingkat kemampuan membaca mandiri pada halaman itu.
- Bahasa Arab J1 lebih banyak menunjuk, mendengar, mengulang, menjawab satu kata; tingkat percakapan dan diskusi meningkat bertahap sesuai perkembangan kompetensi.
- Materi J2–J8 yang belum terisi tidak boleh diisi dengan karangan lalu disebut sebagai materi lama.

## Langkah lanjutan
Telusuri berkas materi halaman J2–J3 pada branch `content/qurbata-jilid-1-8-production`, sumber Tahfidz terpisah, dan kurikulum hadits/akhlak. Setelah ditemukan, susun bank terverifikasi, matriks per halaman, audit ahli, kemudian produksi buku.
