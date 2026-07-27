# REG-CUR-001 — Register Objek Isi Buku QURBATA

**Kode Dokumen:** REG-CUR-001  
**Judul:** Register Objek Isi Buku QURBATA  
**Bahasa Induk:** Bahasa Indonesia  
**Status:** Draf Terkendali  
**Versi:** 0.29.0-id  
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
| PO-000009 | Page Object | Halaman Keluarga Fa–Qaf Berfathah | QJ1-P009 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000009 | Learning Object | Membedakan dan membaca فَ قَ dengan review keluarga sebelumnya | QJ1-P009 | ACTIVE-DRAFT | uses KO-000062–KO-000068 |
| KO-000062 | Knowledge Object | Bentuk dasar pasangan ف ق | QJ1-P009 | ACTIVE-DRAFT | used-by LO-000009 |
| KO-000063 | Knowledge Object | Bunyi فَ | QJ1-P009 | ACTIVE-DRAFT | used-by LO-000009 |
| KO-000064 | Knowledge Object | Bunyi قَ | QJ1-P009 | ACTIVE-DRAFT | used-by LO-000009 |
| KO-000065 | Knowledge Object | Diskriminasi titik, bentuk, dan makhraj ف ق | QJ1-P009 | ACTIVE-DRAFT | used-by LO-000009 |
| KO-000066 | Knowledge Object | Integrasi فَ قَ dengan review عَ غَ dan keluarga sebelumnya | QJ1-P009 | ACTIVE-DRAFT | used-by LO-000009 |
| KO-000067 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P009 | QJ1-P009 | ACTIVE-DRAFT | used-by LO-000009 |
| KO-000068 | Knowledge Object | Adab menjaga semangat sampai selesai | QJ1-P009-AKH01 | ACTIVE-DRAFT | supports LO-000009 |
| PO-000010 | Page Object | Evaluasi Fathah I | QJ1-P010 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000010 | Learning Object | Menunjukkan penguasaan awal huruf berfathah ءَ–قَ | QJ1-P010 | ACTIVE-DRAFT | uses KO-000069–KO-000073 |
| KO-000069 | Knowledge Object | Integrasi huruf berfathah QJ1-P001–P009 | QJ1-P010 | ACTIVE-DRAFT | used-by LO-000010 |
| KO-000070 | Knowledge Object | Diskriminasi bentuk dan titik ء–ق | QJ1-P010 | ACTIVE-DRAFT | used-by LO-000010 |
| KO-000071 | Knowledge Object | Ketepatan makhraj huruf ءَ–قَ | QJ1-P010 | ACTIVE-DRAFT | used-by LO-000010 |
| KO-000072 | Knowledge Object | Kelancaran rangkaian dua dan tiga huruf terpisah | QJ1-P010 | ACTIVE-DRAFT | used-by LO-000010 |
| KO-000073 | Knowledge Object | Adab jujur dan tenang ketika dievaluasi | QJ1-P010-AKH01 | ACTIVE-DRAFT | supports LO-000010 |
| PO-000011 | Page Object | Halaman Keluarga Kaf–Lam Berfathah | QJ1-P011 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000011 | Learning Object | Membedakan dan membaca كَ لَ dengan review keluarga sebelumnya | QJ1-P011 | ACTIVE-DRAFT | uses KO-000074–KO-000080 |
| KO-000074 | Knowledge Object | Bentuk dasar ك dan ل | QJ1-P011 | ACTIVE-DRAFT | used-by LO-000011 |
| KO-000075 | Knowledge Object | Bunyi كَ | QJ1-P011 | ACTIVE-DRAFT | used-by LO-000011 |
| KO-000076 | Knowledge Object | Bunyi لَ | QJ1-P011 | ACTIVE-DRAFT | used-by LO-000011 |
| KO-000077 | Knowledge Object | Diskriminasi bentuk dan makhraj ك ل | QJ1-P011 | ACTIVE-DRAFT | used-by LO-000011 |
| KO-000078 | Knowledge Object | Integrasi كَ لَ dengan review فَ قَ dan keluarga sebelumnya | QJ1-P011 | ACTIVE-DRAFT | used-by LO-000011 |
| KO-000079 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P011 | QJ1-P011 | ACTIVE-DRAFT | used-by LO-000011 |
| KO-000080 | Knowledge Object | Adab istiqamah setelah evaluasi | QJ1-P011-AKH01 | ACTIVE-DRAFT | supports LO-000011 |
| PO-000012 | Page Object | Halaman Keluarga Mim–Nun Berfathah | QJ1-P012 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000012 | Learning Object | Membedakan dan membaca مَ نَ dengan review keluarga sebelumnya | QJ1-P012 | ACTIVE-DRAFT | uses KO-000081–KO-000087 |
| KO-000081 | Knowledge Object | Bentuk dasar م dan ن | QJ1-P012 | ACTIVE-DRAFT | used-by LO-000012 |
| KO-000082 | Knowledge Object | Bunyi مَ | QJ1-P012 | ACTIVE-DRAFT | used-by LO-000012 |
| KO-000083 | Knowledge Object | Bunyi نَ | QJ1-P012 | ACTIVE-DRAFT | used-by LO-000012 |
| KO-000084 | Knowledge Object | Diskriminasi bentuk, titik, dan makhraj م ن | QJ1-P012 | ACTIVE-DRAFT | used-by LO-000012 |
| KO-000085 | Knowledge Object | Integrasi مَ نَ dengan review كَ لَ dan keluarga sebelumnya | QJ1-P012 | ACTIVE-DRAFT | used-by LO-000012 |
| KO-000086 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P012 | QJ1-P012 | ACTIVE-DRAFT | used-by LO-000012 |
| KO-000087 | Knowledge Object | Adab menjaga kebersihan lisan | QJ1-P012-AKH01 | ACTIVE-DRAFT | supports LO-000012 |
| PO-000013 | Page Object | Halaman Keluarga Ha–Waw–Ya Berfathah | QJ1-P013 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000013 | Learning Object | Membedakan dan membaca هَ وَ يَ dengan review keluarga sebelumnya | QJ1-P013 | ACTIVE-DRAFT | uses KO-000088–KO-000095 |
| KO-000088 | Knowledge Object | Bentuk dasar ه و ي | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000089 | Knowledge Object | Bunyi هَ | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000090 | Knowledge Object | Bunyi وَ | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000091 | Knowledge Object | Bunyi يَ | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000092 | Knowledge Object | Diskriminasi visual dan fonetik ه و ي | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000093 | Knowledge Object | Integrasi هَ وَ يَ dengan review مَ نَ dan keluarga sebelumnya | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000094 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P013 | QJ1-P013 | ACTIVE-DRAFT | used-by LO-000013 |
| KO-000095 | Knowledge Object | Adab amanah mengikuti contoh bacaan | QJ1-P013-AKH01 | ACTIVE-DRAFT | supports LO-000013 |
| PO-000014 | Page Object | Integrasi Seluruh Huruf Berfathah | QJ1-P014 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000014 | Learning Object | Mengintegrasikan seluruh huruf berfathah QJ1-P001–QJ1-P013 | QJ1-P014 | ACTIVE-DRAFT | uses KO-000096–KO-000101 |
| KO-000096 | Knowledge Object | Integrasi seluruh bentuk dan bunyi fathah QJ1-P001–QJ1-P013 | QJ1-P014 | ACTIVE-DRAFT | used-by LO-000014 |
| KO-000097 | Knowledge Object | Diskriminasi keluarga bentuk dan titik | QJ1-P014 | ACTIVE-DRAFT | used-by LO-000014 |
| KO-000098 | Knowledge Object | Ketepatan makhraj lintas keluarga huruf | QJ1-P014 | ACTIVE-DRAFT | used-by LO-000014 |
| KO-000099 | Knowledge Object | Konsistensi fathah pendek tanpa mad | QJ1-P014 | ACTIVE-DRAFT | used-by LO-000014 |
| KO-000100 | Knowledge Object | Kelancaran rangkaian dua dan tiga huruf terpisah QJ1-P014 | QJ1-P014 | ACTIVE-DRAFT | used-by LO-000014 |
| KO-000101 | Knowledge Object | Adab istiqamah dan teliti sampai akhir | QJ1-P014-AKH01 | ACTIVE-DRAFT | supports LO-000014 |
| PO-000015 | Page Object | Otomatisasi Fathah | QJ1-P015 | ACTIVE-DRAFT | child-of CO-000001 |
| LO-000015 | Learning Object | Mengotomatisasikan seluruh huruf berfathah melalui kontras bentuk dan makhraj | QJ1-P015 | ACTIVE-DRAFT | uses KO-000102–KO-000107 |
| KO-000102 | Knowledge Object | Otomatisasi seluruh bunyi fathah QJ1-P001–QJ1-P014 | QJ1-P015 | ACTIVE-DRAFT | used-by LO-000015 |
| KO-000103 | Knowledge Object | Kontras cepat keluarga bentuk dan titik | QJ1-P015 | ACTIVE-DRAFT | used-by LO-000015 |
| KO-000104 | Knowledge Object | Kontras makhraj lintas keluarga huruf | QJ1-P015 | ACTIVE-DRAFT | used-by LO-000015 |
| KO-000105 | Knowledge Object | Konsistensi fathah pendek pada peningkatan kelancaran | QJ1-P015 | ACTIVE-DRAFT | used-by LO-000015 |
| KO-000106 | Knowledge Object | Baca mandiri rangkaian dua dan tiga huruf terpisah QJ1-P015 | QJ1-P015 | ACTIVE-DRAFT | used-by LO-000015 |
| KO-000107 | Knowledge Object | Adab mendahulukan ketepatan daripada kecepatan | QJ1-P015-AKH01 | ACTIVE-DRAFT | supports LO-000015 |
| CO-000002 | Chapter Object | Fase Kasrah Jilid 1 | QJ1-P016–P025 | ACTIVE-DRAFT | child-of BO-000001 |
| PO-000016 | Page Object | Bunyi Kasrah Awal | QJ1-P016 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000016 | Learning Object | Membedakan dan membaca ءِ إِ بِ تِ ثِ dengan review fathah padanannya | QJ1-P016 | ACTIVE-DRAFT | uses KO-000108–KO-000118 |
| KO-000108 | Knowledge Object | Bentuk kasrah pada hamza mandiri ءِ dan hamza di bawah alif إِ | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000109 | Knowledge Object | Bentuk kasrah pada keluarga ب ت ث | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000110 | Knowledge Object | Bunyi ءِ | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000111 | Knowledge Object | Bunyi إِ | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000112 | Knowledge Object | Bunyi بِ | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000113 | Knowledge Object | Bunyi تِ | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000114 | Knowledge Object | Bunyi ثِ | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000115 | Knowledge Object | Kontras visual dan fonetik kasrah–fathah | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000116 | Knowledge Object | Integrasi ءِ إِ بِ تِ ثِ dengan review fathah padanannya | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000117 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P016 | QJ1-P016 | ACTIVE-DRAFT | used-by LO-000016 |
| KO-000118 | Knowledge Object | Adab rendah hati memulai bunyi baru | QJ1-P016-AKH01 | ACTIVE-DRAFT | supports LO-000016 |
| PO-000017 | Page Object | Kasrah Keluarga Tenggorokan | QJ1-P017 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000017 | Learning Object | Membedakan dan membaca جِ حِ خِ عِ غِ هِ dengan review terkait | QJ1-P017 | ACTIVE-DRAFT | uses KO-000119–KO-000130 |
| KO-000119 | Knowledge Object | Bentuk kasrah keluarga ج ح خ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000120 | Knowledge Object | Bentuk kasrah keluarga ع غ dan ه | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000121 | Knowledge Object | Bunyi جِ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000122 | Knowledge Object | Bunyi حِ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000123 | Knowledge Object | Bunyi خِ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000124 | Knowledge Object | Bunyi عِ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000125 | Knowledge Object | Bunyi غِ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000126 | Knowledge Object | Bunyi هِ | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000127 | Knowledge Object | Diskriminasi bentuk, titik, dan makhraj keluarga tenggorokan | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000128 | Knowledge Object | Integrasi kasrah baru dengan kasrah awal dan fathah terkait | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000129 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P017 | QJ1-P017 | ACTIVE-DRAFT | used-by LO-000017 |
| KO-000130 | Knowledge Object | Adab sabar tanpa memaksa suara | QJ1-P017-AKH01 | ACTIVE-DRAFT | supports LO-000017 |
| PO-000018 | Page Object | Hafalan 1 — Materi Menunggu Keputusan | QJ1-P018 | BLOCKED-DRAFT | child-of CO-000002 |
| LO-000018 | Learning Object | Menirukan, mengurutkan, dan mengingat materi hafalan pendek yang disahkan | QJ1-P018 | BLOCKED-DRAFT | uses KO-000131–KO-000136 |
| KO-000131 | Knowledge Object | Kriteria pemilihan dan pengesahan materi Hafalan 1 | QJ1-P018 | ACTIVE-DRAFT | used-by LO-000018 |
| KO-000132 | Knowledge Object | Simakan model hafalan utuh dan per potongan | QJ1-P018 | ACTIVE-DRAFT | used-by LO-000018 |
| KO-000133 | Knowledge Object | Talqin–ittiba’ materi hafalan | QJ1-P018 | ACTIVE-DRAFT | used-by LO-000018 |
| KO-000134 | Knowledge Object | Penggabungan serta penguatan urutan potongan | QJ1-P018 | ACTIVE-DRAFT | used-by LO-000018 |
| KO-000135 | Knowledge Object | Recall mandiri dan retensi hafalan | QJ1-P018 | ACTIVE-DRAFT | used-by LO-000018 |
| KO-000136 | Knowledge Object | Adab amanah, rahmah, dan tanpa mempermalukan dalam hafalan | QJ1-P018-AKH01 | ACTIVE-DRAFT | supports LO-000018 |
| PO-000019 | Page Object | Kasrah Ujung Lidah | QJ1-P019 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000019 | Learning Object | Membedakan dan membaca دِ ذِ رِ زِ سِ شِ dengan review terkait | QJ1-P019 | ACTIVE-DRAFT | uses KO-000137–KO-000147 |
| KO-000137 | Knowledge Object | Bentuk kasrah pasangan د ذ، ر ز، dan س ش | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000138 | Knowledge Object | Bunyi دِ | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000139 | Knowledge Object | Bunyi ذِ | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000140 | Knowledge Object | Bunyi رِ | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000141 | Knowledge Object | Bunyi زِ | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000142 | Knowledge Object | Bunyi سِ | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000143 | Knowledge Object | Bunyi شِ | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000144 | Knowledge Object | Diskriminasi bentuk, titik, dan makhraj ujung lidah | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000145 | Knowledge Object | Integrasi kasrah baru dengan kasrah sebelumnya dan fathah terkait | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000146 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P019 | QJ1-P019 | ACTIVE-DRAFT | used-by LO-000019 |
| KO-000147 | Knowledge Object | Adab teliti melihat titik sebelum membaca | QJ1-P019-AKH01 | ACTIVE-DRAFT | supports LO-000019 |
| PO-000020 | Page Object | Evaluasi Fathah–Kasrah | QJ1-P020 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000020 | Learning Object | Menunjukkan penguasaan formatif atas fathah dan kasrah QJ1-P001–QJ1-P019 | QJ1-P020 | ACTIVE-DRAFT | uses KO-000148–KO-000154 |
| KO-000148 | Knowledge Object | Integrasi cakupan fathah QJ1-P001–QJ1-P015 | QJ1-P020 | ACTIVE-DRAFT | used-by LO-000020 |
| KO-000149 | Knowledge Object | Integrasi cakupan kasrah QJ1-P016–QJ1-P019 | QJ1-P020 | ACTIVE-DRAFT | used-by LO-000020 |
| KO-000150 | Knowledge Object | Diskriminasi visual bentuk, titik, dan posisi harakat | QJ1-P020 | ACTIVE-DRAFT | used-by LO-000020 |
| KO-000151 | Knowledge Object | Kontras fonetik fathah–kasrah | QJ1-P020 | ACTIVE-DRAFT | used-by LO-000020 |
| KO-000152 | Knowledge Object | Ketepatan makhraj dan panjang-pendek | QJ1-P020 | ACTIVE-DRAFT | used-by LO-000020 |
| KO-000153 | Knowledge Object | Kelancaran serta kemandirian pada sampel dua dan tiga huruf | QJ1-P020 | ACTIVE-DRAFT | used-by LO-000020 |
| KO-000154 | Knowledge Object | Adab jujur dan tenang dalam evaluasi | QJ1-P020-AKH01 | ACTIVE-DRAFT | supports LO-000020 |
| PO-000021 | Page Object | Kasrah Huruf Tebal | QJ1-P021 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000021 | Learning Object | Membedakan dan membaca صِ ضِ طِ ظِ dengan review terkait | QJ1-P021 | ACTIVE-DRAFT | uses KO-000155–KO-000164 |
| KO-000155 | Knowledge Object | Bentuk kasrah keluarga ص ض ط ظ | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000156 | Knowledge Object | Bunyi صِ | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000157 | Knowledge Object | Bunyi ضِ | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000158 | Knowledge Object | Bunyi طِ | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000159 | Knowledge Object | Bunyi ظِ | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000160 | Knowledge Object | Diskriminasi titik, bentuk, makhraj, dan ketebalan relatif | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000161 | Knowledge Object | Kontras kasrah–fathah pada ص ض ط ظ | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000162 | Knowledge Object | Integrasi kasrah baru dengan kasrah sebelumnya | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000163 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P021 | QJ1-P021 | ACTIVE-DRAFT | used-by LO-000021 |
| KO-000164 | Knowledge Object | Adab bersungguh-sungguh tanpa memaksa suara | QJ1-P021-AKH01 | ACTIVE-DRAFT | supports LO-000021 |
| PO-000022 | Page Object | Kasrah Fa–Qaf–Kaf–Lam | QJ1-P022 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000022 | Learning Object | Membedakan dan membaca فِ قِ كِ لِ dengan review terkait | QJ1-P022 | ACTIVE-DRAFT | uses KO-000165–KO-000174 |
| KO-000165 | Knowledge Object | Bentuk kasrah ف ق ك ل | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000166 | Knowledge Object | Bunyi فِ | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000167 | Knowledge Object | Bunyi قِ | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000168 | Knowledge Object | Bunyi كِ | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000169 | Knowledge Object | Bunyi لِ | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000170 | Knowledge Object | Diskriminasi ف/ق، ق/ك، dan ك/ل | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000171 | Knowledge Object | Kontras kasrah–fathah pada ف ق ك ل | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000172 | Knowledge Object | Integrasi kasrah baru dengan kasrah sebelumnya | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000173 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P022 | QJ1-P022 | ACTIVE-DRAFT | used-by LO-000022 |
| KO-000174 | Knowledge Object | Adab menjaga ketelitian pada bentuk dan bunyi mirip | QJ1-P022-AKH01 | ACTIVE-DRAFT | supports LO-000022 |
| PO-000023 | Page Object | Kasrah Mim–Nun–Waw–Ya | QJ1-P023 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000023 | Learning Object | Membedakan dan membaca مِ نِ وِ يِ dengan review terkait | QJ1-P023 | ACTIVE-DRAFT | uses KO-000175–KO-000184 |
| KO-000175 | Knowledge Object | Bentuk kasrah م ن و ي | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000176 | Knowledge Object | Bunyi مِ | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000177 | Knowledge Object | Bunyi نِ | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000178 | Knowledge Object | Bunyi وِ | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000179 | Knowledge Object | Bunyi يِ | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000180 | Knowledge Object | Diskriminasi م/ن dan و/ي | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000181 | Knowledge Object | Kontras kasrah–fathah pada م ن و ي | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000182 | Knowledge Object | Integrasi kasrah baru dengan kasrah sebelumnya | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000183 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P023 | QJ1-P023 | ACTIVE-DRAFT | used-by LO-000023 |
| KO-000184 | Knowledge Object | Adab membaca tanpa menambah panjang | QJ1-P023-AKH01 | ACTIVE-DRAFT | supports LO-000023 |
| PO-000024 | Page Object | Integrasi Seluruh Huruf Berkasrah | QJ1-P024 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000024 | Learning Object | Mengintegrasikan seluruh huruf berkasrah QJ1-P016–QJ1-P023 | QJ1-P024 | ACTIVE-DRAFT | uses KO-000185–KO-000190 |
| KO-000185 | Knowledge Object | Integrasi seluruh bentuk dan bunyi kasrah QJ1-P016–QJ1-P023 | QJ1-P024 | ACTIVE-DRAFT | used-by LO-000024 |
| KO-000186 | Knowledge Object | Diskriminasi keluarga bentuk dan titik | QJ1-P024 | ACTIVE-DRAFT | used-by LO-000024 |
| KO-000187 | Knowledge Object | Ketepatan makhraj lintas keluarga huruf | QJ1-P024 | ACTIVE-DRAFT | used-by LO-000024 |
| KO-000188 | Knowledge Object | Konsistensi kasrah pendek tanpa mad | QJ1-P024 | ACTIVE-DRAFT | used-by LO-000024 |
| KO-000189 | Knowledge Object | Kelancaran rangkaian dua dan tiga huruf terpisah QJ1-P024 | QJ1-P024 | ACTIVE-DRAFT | used-by LO-000024 |
| KO-000190 | Knowledge Object | Adab istiqamah dan teliti sampai akhir | QJ1-P024-AKH01 | ACTIVE-DRAFT | supports LO-000024 |
| PO-000025 | Page Object | Kontras Fathah–Kasrah | QJ1-P025 | ACTIVE-DRAFT | child-of CO-000002 |
| LO-000025 | Learning Object | Membedakan dan membaca seluruh huruf dalam kontras fathah–kasrah | QJ1-P025 | ACTIVE-DRAFT | uses KO-000191–KO-000196 |
| KO-000191 | Knowledge Object | Integrasi seluruh padanan fathah–kasrah QJ1-P001–QJ1-P024 | QJ1-P025 | ACTIVE-DRAFT | used-by LO-000025 |
| KO-000192 | Knowledge Object | Diskriminasi posisi fathah dan kasrah | QJ1-P025 | ACTIVE-DRAFT | used-by LO-000025 |
| KO-000193 | Knowledge Object | Peralihan fonetik fathah–kasrah dengan makhraj tetap | QJ1-P025 | ACTIVE-DRAFT | used-by LO-000025 |
| KO-000194 | Knowledge Object | Konsistensi bunyi pendek tanpa mad | QJ1-P025 | ACTIVE-DRAFT | used-by LO-000025 |
| KO-000195 | Knowledge Object | Kelancaran rangkaian dua dan tiga huruf terpisah QJ1-P025 | QJ1-P025 | ACTIVE-DRAFT | used-by LO-000025 |
| KO-000196 | Knowledge Object | Adab teliti melihat harakat sebelum membaca | QJ1-P025-AKH01 | ACTIVE-DRAFT | supports LO-000025 |
| CO-000003 | Chapter Object | Fase Dhammah Jilid 1 | QJ1-P026–P035 | ACTIVE-DRAFT | child-of BO-000001 |
| PO-000026 | Page Object | Bunyi Dhammah Awal | QJ1-P026 | ACTIVE-DRAFT | child-of CO-000003 |
| LO-000026 | Learning Object | Membedakan dan membaca أُ بُ تُ ثُ dengan review padanan fathah–kasrah | QJ1-P026 | ACTIVE-DRAFT | uses KO-000197–KO-000206 |
| KO-000197 | Knowledge Object | Bentuk dhammah pada أ ب ت ث | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000198 | Knowledge Object | Bunyi أُ | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000199 | Knowledge Object | Bunyi بُ | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000200 | Knowledge Object | Bunyi تُ | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000201 | Knowledge Object | Bunyi ثُ | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000202 | Knowledge Object | Diskriminasi bentuk dan titik أ ب ت ث | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000203 | Knowledge Object | Kontras dhammah–fathah–kasrah pada أ ب ت ث | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000204 | Knowledge Object | Integrasi dhammah baru dengan review padanan | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000205 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P026 | QJ1-P026 | ACTIVE-DRAFT | used-by LO-000026 |
| KO-000206 | Knowledge Object | Adab rendah hati ketika memulai bunyi baru | QJ1-P026-AKH01 | ACTIVE-DRAFT | supports LO-000026 |
| PO-000027 | Page Object | Dhammah Keluarga Jim dan Tenggorokan | QJ1-P027 | ACTIVE-DRAFT | child-of CO-000003 |
| LO-000027 | Learning Object | Membedakan dan membaca جُ حُ خُ عُ غُ هُ dengan review harakat sebelumnya | QJ1-P027 | ACTIVE-DRAFT | uses KO-000207–KO-000218 |
| KO-000207 | Knowledge Object | Bentuk dhammah keluarga ج ح خ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000208 | Knowledge Object | Bentuk dhammah keluarga ع غ dan ه | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000209 | Knowledge Object | Bunyi جُ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000210 | Knowledge Object | Bunyi حُ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000211 | Knowledge Object | Bunyi خُ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000212 | Knowledge Object | Bunyi عُ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000213 | Knowledge Object | Bunyi غُ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000214 | Knowledge Object | Bunyi هُ | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000215 | Knowledge Object | Diskriminasi bentuk, titik, dan makhraj keluarga tenggorokan | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000216 | Knowledge Object | Integrasi dhammah baru dengan dhammah awal dan padanan fathah–kasrah | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000217 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P027 | QJ1-P027 | ACTIVE-DRAFT | used-by LO-000027 |
| KO-000218 | Knowledge Object | Adab sabar tanpa memaksa suara | QJ1-P027-AKH01 | ACTIVE-DRAFT | supports LO-000027 |
| PO-000028 | Page Object | Bahasa Arab 1 — Materi Menunggu Keputusan | QJ1-P028 | BLOCKED-DRAFT | child-of CO-000003 |
| LO-000028 | Learning Object | Menyimak, memahami, dan menggunakan mufradat lisan yang disahkan | QJ1-P028 | BLOCKED-DRAFT | uses KO-000219–KO-000225 |
| KO-000219 | Knowledge Object | Kriteria pemilihan dan pengesahan materi Bahasa Arab 1 | QJ1-P028 | ACTIVE-DRAFT | used-by LO-000028 |
| KO-000220 | Knowledge Object | Simakan mufradat dan hubungan bunyi–makna | QJ1-P028 | ACTIVE-DRAFT | used-by LO-000028 |
| KO-000221 | Knowledge Object | Talqin–ittiba’ pelafalan mufradat | QJ1-P028 | ACTIVE-DRAFT | used-by LO-000028 |
| KO-000222 | Knowledge Object | Pemahaman lisan melalui respons bermakna | QJ1-P028 | ACTIVE-DRAFT | used-by LO-000028 |
| KO-000223 | Knowledge Object | Produksi lisan terkendali dalam konteks sederhana | QJ1-P028 | ACTIVE-DRAFT | used-by LO-000028 |
| KO-000224 | Knowledge Object | Pemisahan pembelajaran lisan dari materi baca prematur | QJ1-P028 | ACTIVE-DRAFT | used-by LO-000028 |
| KO-000225 | Knowledge Object | Adab santun dan percaya diri dalam komunikasi | QJ1-P028-AKH01 | ACTIVE-DRAFT | supports LO-000028 |
| PO-000029 | Page Object | Dhammah Dal–Syin | QJ1-P029 | ACTIVE-DRAFT | child-of CO-000003 |
| LO-000029 | Learning Object | Membedakan dan membaca دُ ذُ رُ زُ سُ شُ dengan review dhammah sebelumnya | QJ1-P029 | ACTIVE-DRAFT | uses KO-000226–KO-000236 |
| KO-000226 | Knowledge Object | Bentuk dhammah pasangan د ذ، ر ز، dan س ش | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000227 | Knowledge Object | Bunyi دُ | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000228 | Knowledge Object | Bunyi ذُ | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000229 | Knowledge Object | Bunyi رُ | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000230 | Knowledge Object | Bunyi زُ | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000231 | Knowledge Object | Bunyi سُ | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000232 | Knowledge Object | Bunyi شُ | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000233 | Knowledge Object | Diskriminasi bentuk, titik, dan makhraj ujung lidah | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000234 | Knowledge Object | Integrasi dhammah baru dengan dhammah sebelumnya dan padanan fathah–kasrah | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000235 | Knowledge Object | Rangkaian dua dan tiga huruf terpisah QJ1-P029 | QJ1-P029 | ACTIVE-DRAFT | used-by LO-000029 |
| KO-000236 | Knowledge Object | Adab teliti melihat titik dan tanda sebelum membaca | QJ1-P029-AKH01 | ACTIVE-DRAFT | supports LO-000029 |

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
| 0.9.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P009 |
| 0.10.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk Evaluasi Fathah I QJ1-P010 |
| 0.11.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P011 |
| 0.12.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P012 |
| 0.13.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P013 |
| 0.14.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk integrasi fathah QJ1-P014 |
| 0.15.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk otomatisasi fathah QJ1-P015 |
| 0.16.0-id | 27 Juli 2026 | Membentuk CO fase kasrah serta menambahkan PO, LO, dan KO untuk QJ1-P016 |
| 0.17.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P017 |
| 0.18.0-id | 27 Juli 2026 | Menambahkan spesifikasi terkendali PO, LO, dan KO Hafalan 1 QJ1-P018; materi masih terblokir keputusan |
| 0.19.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P019 |
| 0.20.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk Evaluasi Fathah–Kasrah QJ1-P020 |
| 0.21.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P021 |
| 0.22.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P022 |
| 0.23.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P023 |
| 0.24.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk integrasi kasrah QJ1-P024 |
| 0.25.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk kontras fathah–kasrah QJ1-P025 |
| 0.26.0-id | 27 Juli 2026 | Membentuk CO fase dhammah serta menambahkan PO, LO, dan KO untuk QJ1-P026 |
| 0.27.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P027 |
| 0.28.0-id | 27 Juli 2026 | Menambahkan spesifikasi terkendali PO, LO, dan KO Bahasa Arab 1 QJ1-P028; materi masih terblokir keputusan |
| 0.29.0-id | 27 Juli 2026 | Menambahkan PO, LO, dan KO untuk QJ1-P029 |
