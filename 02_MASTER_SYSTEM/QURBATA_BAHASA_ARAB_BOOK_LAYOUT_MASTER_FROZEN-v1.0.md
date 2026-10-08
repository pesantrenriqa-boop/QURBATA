# QURBATA — Bahasa Arab Qurani
## MASTER PEDOMAN RESMI PENULISAN, PEDAGOGI, DAN LAYOUT BUKU
**Kode:** QRT-ARB-LAYOUT-MASTER-v1.0
**Status:** FROZEN — disahkan atas instruksi pengguna 8 Oktober 2026
**Cakupan:** Seri Bahasa Arab QURBATA Jilid 1–8; rancangan halaman satu-per-satu.
**Batasan:** Pembekuan ini berlaku untuk **pedoman produksi**, bukan persetujuan otomatis atas materi halaman, korpus, maupun draf register J2–J8.

### 1. Identitas dan arsitektur
- Judul seri: **QURBATA — Bahasa Arab Qurani**; buku ajar santri terpisah dari buku Tartil.
- Delapan jilid, **target kerja awal 40 halaman inti per jilid**; perubahan struktur membutuhkan revisi pedoman.
- Pendekatan Qurani, komunikatif, bertahap, berbasis kompetensi; Arab sebagai bahasa utama dan Indonesia sebagai bantuan.
- Alur belajar: **Lihat → Dengar → Tirukan → Pahami → Gunakan → Latih → Evaluasi**.
- **Pisahkan** register 320 panel Bi’ah Arabiyah (ungkapan instruksional) dari kurikulum Bahasa Arab Qurani (lema, pola, 4 keterampilan). Panel dapat diintegrasikan tetapi **tidak** memenuhi otomatis target 640 lema.
- Satu halaman satu fokus utama dan target terukur; prasyarat eksplisit, tidak melompat.
- Bahasa Arab harus akurat; kutipan ayat hanya setelah verifikasi mushaf, dengan surah/ayat; kalimat buatan dilabeli latihan, bukan ayat.

### 2. Spesifikasi layout terkunci
- **B5 potret: 176 × 250 mm.** Margin dalam 20 mm, luar 15 mm, atas 15 mm, bawah 17 mm.
- Latar putih atau putih gading. Warna utama **#245B4A**, sage **#DCE9DF**, aksen emas lembut **#B89B61**.
- Huruf Arab **KFGQPC Uthman Taha** (sesuai standar QURBATA); teks Latin **Noto Sans** atau sans-serif profesional.
- Tipografi Arab lebih dominan; Indonesia kecil namun terbaca; teks Arab berharakat sesuai level.
- Header konsisten: QURBATA, jilid, kode kompetensi/halaman. Footer konsisten: nomor halaman dan **تعلّم – اِعمل – علِّم**.
- Grid, posisi, hirarki visual dan area aman cetak konsisten. Tanpa ornamen ramai, efek 3D, atau ilustrasi dekoratif.
- Gambar hanya jika menambah kejelasan; ruang latihan tidak boleh dikorbankan demi dekorasi.
- Setiap halaman memakai enam zona: **identitas, kompetensi, materi inti, penggunaan/komunikasi, latihan/evaluasi, footer**. Komposisi dapat disesuaikan agar tidak padat, tanpa menghilangkan fungsi wajib.
- Desain halaman contoh berfungsi sebagai **uji prototipe**, bukan mengubah pedoman yang sudah FROZEN.

### 3. Standar pedagogi dan registrasi
1. Tiap halaman mencatat prasyarat, target, lema baru, review, fungsi komunikasi, sumber, dan bukti keberhasilan.
2. Tidak mengulang lema/kompetensi lama sebagai **baru**; pengulangan berlabel **murojaah/transfer**.
3. Urutan dari reseptif ke produktif: menyimak, menirukan, memahami, lalu menggunakan dan menulis.
4. Latihan harus menguji target halaman, ringan dan dapat diamati guru.
5. Materi mengikuti progresi kompetensi Arab QURBATA dan target 640 lema, **bukan** semata-mata 320 ungkapan panel.
6. Tidak mengajarkan nahwu-sharaf berat pada halaman pemula; gunakan pola, contoh, dan komunikasi.
7. Korpus Qurani: bedakan **kutipan ayat terverifikasi**, **lema berjejak Qurani**, dan **kalimat kelas buatan**. Tidak ada klaim korpus tanpa bukti.
8. Semua materi yang telah FROZEN di repo tetap tidak disentuh tanpa revisi disetujui.

### 4. MASTER PROMPT PRODUKSI SATU HALAMAN (wajib dipakai)
**Input yang harus tersedia:** jilid, halaman P001–P040, kode kompetensi, judul Arab/Indonesia, prasyarat, satu target terukur, lema baru, lema/kompetensi review, sumber ayat terverifikasi jika digunakan, ungkapan Bi’ah Arabiyah terkait.

**Instruksi produksi:**
> Buat **SATU HALAMAN SAJA** buku ajar QURBATA — Bahasa Arab Qurani, B5 potret 176×250 mm, margin dalam 20 mm, luar 15 mm, atas 15 mm, bawah 17 mm. Latar putih gading, aksen #245B4A, #DCE9DF dan #B89B61. Font Arab KFGQPC Uthman Taha; Latin Noto Sans. Gunakan enam zona tetap: header identitas; kompetensi/judul; materi inti Arab dominan; penggunaan dalam dialog bermakna; latihan sederhana yang langsung menguji target; footer nomor halaman dan تعلّم – اِعمل – علِّم. Berikan harakat yang tepat, terjemahan ringkas, hierarki visual dan ruang baca lega. Integrasikan ungkapan Bi’ah Arabiyah jika relevan. Jangan menambahkan kompetensi yang belum memiliki prasyarat; jangan menghitung materi lama sebagai baru; jangan menciptakan kutipan Al-Qur'an. Jangan melanjutkan halaman berikutnya. Hasil pertama berstatus DRAF.

### 5. Quality gate & otorisasi
- Tahap: **DRAF → REVIEW (bahasa Arab, pedagogi, sumber, layout, keterbacaan) → APPROVED → FROZEN**.
- Periksa keakuratan harakat, bentuk sapaan, struktur Arab, kesesuaian usia, lema unik, prasyarat, ayat dan atribusi, kecukupan latihan, konsistensi layout dan margin.
- Persetujuan halaman tidak otomatis menyetujui halaman berikutnya. Perubahan pedoman hanya melalui versi baru dengan catatan perubahan, **bukan edit diam-diam terhadap v1.0**.
- **P001 prototipe** akan dibuat setelah pedoman ini dibekukan; contoh konten harus tetap DRAF hingga diperiksa.

### 6. Ketentuan prototipe
- Uji **Jilid 1 P001** terlebih dahulu, **tanpa** menyalin panel Bi’ah J1 P001 sebagai seluruh kompetensi Bahasa Arab.
- Pilih materi dari progresi Bahasa Arab dan register lema; periksa prasyarat dan contoh Qurani. Jangan mengklaim prototipe sebagai halaman final sebelum validasi.
