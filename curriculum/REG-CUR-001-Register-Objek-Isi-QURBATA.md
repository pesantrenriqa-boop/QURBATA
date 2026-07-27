# REG-CUR-001 — Register Objek Isi Buku QURBATA

**Kode Dokumen:** REG-CUR-001  
**Judul:** Register Objek Isi Buku QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.8.0-id  
**Pemilik:** Aris Liswanto  
**Dokumen Induk:** QC-000, QC-002, QC-004, QC-005, REG-GOV-001  
**Kurikulum Terkait:** CUR-QJ1-001  
**Tanggal Berlaku:** Belum berlaku  
**Tinjauan Berikutnya:** Setiap penambahan atau perubahan objek isi  
**Klasifikasi:** Internal selama draf  

## 1. Tujuan

Register ini menjadi sumber nomor global objek isi pendidikan. Locator produk seperti QJ1-P001 dipetakan kepada Page Object yang stabil dan tidak digunakan sebagai pengganti LO atau KO.

## 2. Register Awal

| ID | Kelas | Nama | Locator/Sumber | Status | Hubungan Utama |
|---|---|---|---|---|---|
| BO-000001 | Book Object | Buku QURBATA Jilid 1 | QJ1-MASTER | ACTIVE-DRAFT | implements CUR-000001 |
| CUR-000001 | Curriculum Object | Kurikulum Buku QURBATA Jilid 1 | CUR-QJ1-001 | ACTIVE-DRAFT | derived-from QC-000 |
| CO-000001 | Chapter Object | Fase Fathah Jilid 1 | QJ1-P001–P015 | ACTIVE-DRAFT | child-of BO-000001 |
| PO-000001 | Page Object | Halaman Keluarga Ba Berfathah | QJ1-P001 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000001 | Learning Object | Membedakan dan membaca بَ تَ ثَ dalam rangkaian terpisah | QJ1-P001 | ACTIVE-DRAFT | uses KO-000001–KO-000007 |
| KO-000001 | Knowledge Object | Bentuk dasar keluarga ب ت ث | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000002 | Knowledge Object | Bunyi بَ | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000003 | Knowledge Object | Bunyi تَ | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000004 | Knowledge Object | Bunyi ثَ | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000005 | Knowledge Object | Diskriminasi jumlah dan posisi titik ب ت ث | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000006 | Knowledge Object | Rangkaian dua huruf terpisah keluarga ب ت ث | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000007 | Knowledge Object | Rangkaian tiga huruf terpisah keluarga ب ت ث | QJ1-P001 | ACTIVE-DRAFT | used-by LO-000001 |
| KO-000008 | Knowledge Object | Adab mendengar dan menirukan bacaan guru | QJ1-P001-AKH01 | ACTIVE-DRAFT | supports LO-000001 |
| PO-000002 | Page Object | Halaman Hamza–Alif dan Penguatan Keluarga Ba | QJ1-P002 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000002 | Learning Object | Membedakan dan membaca ءَ أَ dengan review بَ تَ ثَ | QJ1-P002 | ACTIVE-DRAFT | uses KO-000009–KO-000016 |
| KO-000009 | Knowledge Object | Bentuk hamza mandiri ء | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000010 | Knowledge Object | Bentuk hamza di atas alif أ | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000011 | Knowledge Object | Bunyi fathah pendek ءَ | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000012 | Knowledge Object | Bunyi fathah pendek أَ | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000013 | Knowledge Object | Diskriminasi visual ء dan أ | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000014 | Knowledge Object | Integrasi ءَ أَ dengan review بَ تَ ثَ | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000015 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P002 | QJ1-P002 | ACTIVE-DRAFT | used-by LO-000002 |
| KO-000016 | Knowledge Object | Adab sabar dalam mengulang bacaan | QJ1-P002-AKH01 | ACTIVE-DRAFT | supports LO-000002 |
| PO-000003 | Page Object | Halaman Keluarga Jim Berfathah | QJ1-P003 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000003 | Learning Object | Membedakan dan membaca جَ حَ خَ dengan review بَ تَ ثَ | QJ1-P003 | ACTIVE-DRAFT | uses KO-000017–KO-000024 |
| KO-000017 | Knowledge Object | Bentuk dasar keluarga ج ح خ | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000018 | Knowledge Object | Bunyi جَ | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000019 | Knowledge Object | Bunyi حَ | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000020 | Knowledge Object | Bunyi خَ | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000021 | Knowledge Object | Diskriminasi jumlah dan posisi titik ج ح خ | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000022 | Knowledge Object | Integrasi جَ حَ خَ dengan review بَ تَ ثَ | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000023 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P003 | QJ1-P003 | ACTIVE-DRAFT | used-by LO-000003 |
| KO-000024 | Knowledge Object | Adab teliti sebelum membaca | QJ1-P003-AKH01 | ACTIVE-DRAFT | supports LO-000003 |
| PO-000004 | Page Object | Halaman Keluarga Dal–Ra Berfathah | QJ1-P004 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000004 | Learning Object | Membedakan dan membaca دَ ذَ رَ زَ dengan review ءَ–خَ | QJ1-P004 | ACTIVE-DRAFT | uses KO-000025–KO-000033 |
| KO-000025 | Knowledge Object | Bentuk dasar pasangan د ذ dan ر ز | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000026 | Knowledge Object | Bunyi دَ | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000027 | Knowledge Object | Bunyi ذَ | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000028 | Knowledge Object | Bunyi رَ | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000029 | Knowledge Object | Bunyi زَ | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000030 | Knowledge Object | Diskriminasi titik د ذ dan ر ز | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000031 | Knowledge Object | Integrasi دَ ذَ رَ زَ dengan review ءَ–خَ | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000032 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P004 | QJ1-P004 | ACTIVE-DRAFT | used-by LO-000004 |
| KO-000033 | Knowledge Object | Adab berhati-hati dan tidak tergesa-gesa | QJ1-P004-AKH01 | ACTIVE-DRAFT | supports LO-000004 |
| PO-000005 | Page Object | Halaman Keluarga Sin Berfathah | QJ1-P005 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000005 | Learning Object | Membedakan dan membaca سَ شَ dengan review دَ ذَ رَ زَ | QJ1-P005 | ACTIVE-DRAFT | uses KO-000034–KO-000040 |
| KO-000034 | Knowledge Object | Bentuk dasar pasangan س ش | QJ1-P005 | ACTIVE-DRAFT | used-by LO-000005 |
| KO-000035 | Knowledge Object | Bunyi سَ | QJ1-P005 | ACTIVE-DRAFT | used-by LO-000005 |
| KO-000036 | Knowledge Object | Bunyi شَ | QJ1-P005 | ACTIVE-DRAFT | used-by LO-000005 |
| KO-000037 | Knowledge Object | Diskriminasi titik س ش | QJ1-P005 | ACTIVE-DRAFT | used-by LO-000005 |
| KO-000038 | Knowledge Object | Integrasi سَ شَ dengan review دَ ذَ رَ زَ | QJ1-P005 | ACTIVE-DRAFT | used-by LO-000005 |
| KO-000039 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P005 | QJ1-P005 | ACTIVE-DRAFT | used-by LO-000005 |
| KO-000040 | Knowledge Object | Adab tekun memperbaiki bacaan | QJ1-P005-AKH01 | ACTIVE-DRAFT | supports LO-000005 |
| PO-000006 | Page Object | Halaman Keluarga Shad Berfathah | QJ1-P006 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000006 | Learning Object | Membedakan dan membaca صَ ضَ dengan review keluarga sebelumnya | QJ1-P006 | ACTIVE-DRAFT | uses KO-000041–KO-000047 |
| KO-000041 | Knowledge Object | Bentuk dasar pasangan ص ض | QJ1-P006 | ACTIVE-DRAFT | used-by LO-000006 |
| KO-000042 | Knowledge Object | Bunyi صَ | QJ1-P006 | ACTIVE-DRAFT | used-by LO-000006 |
| KO-000043 | Knowledge Object | Bunyi ضَ | QJ1-P006 | ACTIVE-DRAFT | used-by LO-000006 |
| KO-000044 | Knowledge Object | Diskriminasi titik dan bunyi ص ض | QJ1-P006 | ACTIVE-DRAFT | used-by LO-000006 |
| KO-000045 | Knowledge Object | Integrasi صَ ضَ dengan review سَ شَ dan keluarga sebelumnya | QJ1-P006 | ACTIVE-DRAFT | used-by LO-000006 |
| KO-000046 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P006 | QJ1-P006 | ACTIVE-DRAFT | used-by LO-000006 |
| KO-000047 | Knowledge Object | Adab bersungguh-sungguh menjaga ketepatan | QJ1-P006-AKH01 | ACTIVE-DRAFT | supports LO-000006 |
| PO-000007 | Page Object | Halaman Keluarga Tha Berfathah | QJ1-P007 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000007 | Learning Object | Membedakan dan membaca طَ ظَ dengan review keluarga sebelumnya | QJ1-P007 | ACTIVE-DRAFT | uses KO-000048–KO-000054 |
| KO-000048 | Knowledge Object | Bentuk dasar pasangan ط ظ | QJ1-P007 | ACTIVE-DRAFT | used-by LO-000007 |
| KO-000049 | Knowledge Object | Bunyi طَ | QJ1-P007 | ACTIVE-DRAFT | used-by LO-000007 |
| KO-000050 | Knowledge Object | Bunyi ظَ | QJ1-P007 | ACTIVE-DRAFT | used-by LO-000007 |
| KO-000051 | Knowledge Object | Diskriminasi titik dan bunyi ط ظ | QJ1-P007 | ACTIVE-DRAFT | used-by LO-000007 |
| KO-000052 | Knowledge Object | Integrasi طَ ظَ dengan review صَ ضَ dan keluarga sebelumnya | QJ1-P007 | ACTIVE-DRAFT | used-by LO-000007 |
| KO-000053 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P007 | QJ1-P007 | ACTIVE-DRAFT | used-by LO-000007 |
| KO-000054 | Knowledge Object | Adab tenang ketika menghadapi bacaan sulit | QJ1-P007-AKH01 | ACTIVE-DRAFT | supports LO-000007 |
| PO-000008 | Page Object | Halaman Keluarga ‘Ain Berfathah | QJ1-P008 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000008 | Learning Object | Membedakan dan membaca عَ غَ dengan review keluarga sebelumnya | QJ1-P008 | ACTIVE-DRAFT | uses KO-000055–KO-000061 |
| KO-000055 | Knowledge Object | Bentuk dasar pasangan ع غ | QJ1-P008 | ACTIVE-DRAFT | used-by LO-000008 |
| KO-000056 | Knowledge Object | Bunyi عَ | QJ1-P008 | ACTIVE-DRAFT | used-by LO-000008 |
| KO-000057 | Knowledge Object | Bunyi غَ | QJ1-P008 | ACTIVE-DRAFT | used-by LO-000008 |
| KO-000058 | Knowledge Object | Diskriminasi titik dan makhraj ع غ | QJ1-P008 | ACTIVE-DRAFT | used-by LO-000008 |
| KO-000059 | Knowledge Object | Integrasi عَ غَ dengan review طَ ظَ dan keluarga sebelumnya | QJ1-P008 | ACTIVE-DRAFT | used-by LO-000008 |
| KO-000060 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P008 | QJ1-P008 | ACTIVE-DRAFT | used-by LO-000008 |
| KO-000061 | Knowledge Object | Adab rendah hati menerima koreksi | QJ1-P008-AKH01 | ACTIVE-DRAFT | supports LO-000008 |

## 3. Aturan

1. Nomor enam digit bersifat global dalam setiap kelas.
2. ID tidak memuat jilid, halaman, bahasa, tahun, atau versi.
3. ID tidak boleh digunakan ulang.
4. Objek draf memakai status ACTIVE-DRAFT.
5. Perubahan makna material memperoleh ID baru.
6. Setiap ID wajib mempunyai sumber, pemilik, hubungan, status, dan riwayat.
7. Locator QJ1-Pxxx tetap digunakan pada produk, tetapi selalu dipetakan ke PO.
8. Penambahan ID final dilakukan melalui register ini, bukan secara manual pada hasil PDF.

## 4. Riwayat

| Versi | Tanggal | Ringkasan |
|---|---|---|
| 0.1.0-id | 27 Juli 2026 | Membentuk BO, CUR, CO, PO, LO, dan KO awal untuk QJ1-P001 |
| 0.2.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P002 |
| 0.3.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P003 |
| 0.4.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P004 |
| 0.5.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P005 |
| 0.6.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P006 |
| 0.7.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P007 |
| 0.8.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P008 |
