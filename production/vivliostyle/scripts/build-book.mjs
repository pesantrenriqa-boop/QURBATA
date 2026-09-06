import fs from "node:fs/promises";
import path from "node:path";
import QRCode from "qrcode";

const root = path.resolve(import.meta.dirname, "..");
const data = JSON.parse(await fs.readFile(path.join(root, "data/jilid-1.json"), "utf8"));
const template = await fs.readFile(path.join(root, "templates/book.html"), "utf8");
const css = await fs.readFile(path.join(root, "styles/book.css"), "utf8");

const escapeHtml = (value = "") => String(value)
  .replaceAll("&", "&amp;")
  .replaceAll("<", "&lt;")
  .replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;");

const arabicLetters = (value) => Array.from(value.normalize("NFD"))
  .filter((character) => /\p{Script=Arabic}/u.test(character) && !/\p{Mark}/u.test(character));

const renderPracticeArabic = (value = "") => escapeHtml(value)
  // U+06BE gives the requested two-aperture isolated ha, but its combining
  // fathah is not reliably positioned by the bundled KFGQPC font.
  // Keep the glyph and render the fathah explicitly as a positioned mark.
  .replaceAll("ھَ", '<span class="ha-two-fatha"><span class="ha-two">ھ</span><span class="ha-fatha">َ</span></span>');

const card = (label, value) => `
  <section class="integration-card integration-card--${label.toLowerCase()}">
    <h2>${escapeHtml(label)}</h2>
    <p class="integration-title">${escapeHtml(value.title)}</p>
    <p class="arabic integration-arabic" lang="ar" dir="rtl">${escapeHtml(value.arabic)}</p>
    <p class="integration-instruction">${escapeHtml(value.instruction)}</p>
  </section>`;

const frontMatterData = [
  {
    title: "SAMBUTAN PENDIRI QURBATA & RIQA",
    type: "founder",
    arabic: `بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ

الْحَمْدُ لِلَّهِ الَّذِي أَنْزَلَ الْقُرْآنَ هُدًى وَبُرْهَانًا، وَجَعَلَهُ لِلْقُلُوبِ نُورًا وَلِلصُّدُورِ إِيمَانًا، وَأَنْزَلَهُ بِلِسَانٍ عَرَبِيٍّ مُبِينٍ فَزَادَهُ فَصَاحَةً وَبَيَانًا، وَيَسَّرَهُ لِلذِّكْرِ تِلَاوَةً وَحِفْظًا وَإِمْعَانًا، وَجَعَلَ الْعِلْمَ بِهِ هُدًى وَعِرْفَانًا، وَالْعَمَلَ بِهِ رُشْدًا وَإِذْعَانًا، وَالتَّخَلُّقَ بِآدَابِهِ لِلنُّفُوسِ زِينَةً، وَلِلسُّلُوكِ تَهْذِيبًا، وَلِلْحَيَاةِ صَلَاحًا وَاتِّزَانًا.

نَحْمَدُهُ سُبْحَانَهُ حَمْدَ الشَّاكِرِينَ، وَنَسْأَلُهُ تِلَاوَةً يَخْشَعُ لَهَا الْجَنَانُ وَيَلِينُ، وَعَرَبِيَّةً يَفْصُحُ بِهَا اللِّسَانُ وَيَسْتَبِينُ، وَحِفْظًا يَثْبُتُ فِي الصُّدُورِ وَلَا يَهُونُ، وَخُلُقًا يَسْمُو بِهِ الْمَرْءُ وَيَزِينُ، وَعِلْمًا يُثْمِرُ عَمَلًا وَيَقِينًا، وَتَعْلِيمًا يَبْقَى نَفْعُهُ عَلَى مَرِّ السِّنِينِ؛ حَتَّى تَحْيَا بِالْقُرْآنِ قُلُوبُنَا، وَتَسْتَنِيرَ بِنُورِهِ دُرُوبُنَا، وَتَنْطِقَ بِالْعَرَبِيَّةِ أَلْسِنَتُنَا، وَتَعْمُرَ بِآيَاتِهِ صُدُورُنَا، وَتَسْتَقِيمَ بِهَدْيِهِ أَخْلَاقُنَا، فَنَكُونَ بِهِ فِي الدُّنْيَا مِنَ الْمُهْتَدِينَ، وَفِي الْآخِرَةِ مِنَ الْفَائِزِينَ.

وَالصَّلَاةُ وَالسَّلَامُ عَلَى سَيِّدِنَا مُحَمَّدٍ، الَّذِي تَلَا الْقُرْآنَ فَأَجَادَ تِلَاوَتَهُ، وَبَيَّنَ آيَاتِهِ فَأَظْهَرَ هِدَايَتَهُ، وَعَلَّمَ أُمَّتَهُ فَأَحْكَمَ تَرْبِيَتَهَا، وَعَمِلَ بِوَحْيِ رَبِّهِ فَاسْتَقَامَ عَلَى هَدْيِهِ، وَتَخَلَّقَ بِآدَابِهِ فَكَانَ قُدْوَةً فِي مَكَارِمِ الْأَخْلَاقِ؛ وَعَلَى آلِهِ وَصَحْبِهِ مَصَابِيحِ الْهُدَى، وَمَنَابِعِ الْعِلْمِ وَالتُّقَى، وَمَنْ تَبِعَهُمْ بِإِحْسَانٍ وَاقْتَفَى أَثَرَهُمْ إِلَى يَوْمِ اللِّقَاءِ.

أَمَّا بَعْدُ؛`,
    source: "",
    paragraphs: [
      "QURBATA lahir dari ikhtiar panjang untuk menghadirkan pembelajaran Al-Qur’an yang tidak berhenti pada kemampuan melafalkan huruf dan menyelesaikan halaman. Kami menginginkan proses belajar yang menumbuhkan kedekatan dengan Al-Qur’an: bacaan dibenahi melalui talaqqi, bahasa Al-Qur’an mulai dihidupkan dalam keseharian belajar, ayat-ayat dijaga melalui hafalan, dan adab dibentuk melalui pembiasaan yang terus menerus.",
      "Karena itu, QURBATA menempatkan Qur’an/Tartil sebagai poros utama, sementara Bahasa Arab, Tahfidz, dan Akhlak hadir sebagai unsur yang saling menguatkan. Integrasi bukan berarti mencampurkan semua pelajaran tanpa batas, melainkan mempertemukan setiap unsur pada tempat dan fungsi yang tepat sehingga satu pertemuan Al-Qur’an dapat sekaligus menjadi ruang tumbuhnya lisan, ingatan, sikap, dan kebiasaan yang Qur’ani.",
      "Kami meyakini bahwa keberhasilan pendidikan Al-Qur’an tidak hanya tampak ketika seorang peserta mampu membaca dengan benar, tetapi juga ketika ilmu itu meninggalkan bekas pada dirinya. Bacaan yang baik perlu melahirkan kecintaan; hafalan perlu melahirkan penjagaan; bahasa perlu membuka jalan kepada pemahaman; dan ilmu perlu berbuah amal serta akhlak.",
      "Pesan KH. Basori Alwi, «لِكُلِّ شَيْءٍ زَكَاةٌ، وَزَكَاةُ الْعِلْمِ التَّعْلِيمُ», mengingatkan bahwa ilmu memiliki tanggung jawab untuk diteruskan. Dari semangat itulah QURBATA membawa ruh: «تَعَلَّمْ — اِعْمَلْ — عَلِّمْ» — belajar dengan sungguh-sungguh, mengamalkan dengan kesadaran, kemudian mengajarkan kebaikan kepada yang lain.",
      "Semoga buku ini menjadi wasilah bagi guru, peserta didik, orang tua, dan lembaga pendidikan untuk membangun pembelajaran Al-Qur’an yang tertib, hangat, bertahap, dan berkesinambungan. Semoga setiap huruf yang dipelajari menjadi cahaya, setiap ayat yang dihafal menjadi penjaga, setiap ungkapan Arab mendekatkan kepada bahasa Al-Qur’an, dan setiap adab yang dibiasakan menjadi jalan menuju kemuliaan akhlak."
    ]
  },
  {
    title: "PENDAHULUAN",
    arabic: "خَيْرُكُمْ مَنْ تَعَلَّمَ الْقُرْآنَ وَعَلَّمَهُ",
    source: "HR. al-Bukhari",
    paragraphs: [
      "Pembelajaran Al-Qur’an pada dasarnya bukan sebuah proses yang berdiri sendiri. Anak yang belajar membaca Al-Qur’an sedang berhadapan dengan bahasa wahyu, mengulang bunyi dan ayat, menyimpan sebagian darinya dalam ingatan, sekaligus menerima contoh sikap dari guru dan lingkungan belajarnya. Karena itu, QURBATA disusun untuk mengelola unsur-unsur tersebut sebagai satu ekosistem pendidikan yang saling mendukung.",
      "QURBATA tidak menggeser tujuan pokok pembelajaran Tartil. Ketepatan membaca tetap menjadi kompetensi inti yang dibangun melalui tangga materi secara bertahap. Bahasa Arab, Tahfidz, dan Akhlak tidak mengambil alih ruang latihan bacaan, tetapi hadir secara terukur untuk memperkaya pengalaman belajar dan menghubungkan keterampilan membaca dengan kehidupan peserta.",
      "Bahasa Arab dalam buku ini terutama hadir sebagai bi’ah ‘Arabiyah: ungkapan sederhana yang digunakan berulang di dalam kelas sehingga peserta mengalami bahasa Al-Qur’an sebagai bahasa yang hidup. Tahfidz dirancang bergerak sedikit demi sedikit, disertai murojaah, agar hafalan tidak terpisah dari proses membaca. Akhlak dihadirkan melalui hadis, nasihat, dan pembiasaan yang dipertahankan selama beberapa pertemuan agar nilai tidak hanya diketahui, tetapi dilatih.",
      "Jilid 1 menjadi fondasi bagi perjalanan tersebut. Materi disusun dengan prinsip dari yang paling sederhana menuju bentuk yang lebih kompleks, dengan pengulangan yang cukup dan kontrol kompetensi sebelum peserta berpindah. Guru tidak dituntut mengejar halaman; guru dituntut memastikan bahwa halaman yang dilewati benar-benar meninggalkan kemampuan.",
      "Buku cetak ini juga dirancang sebagai bagian dari ekosistem RIQA OS. QR kompetensi, rekam perkembangan, materi pendamping, dan asesmen digital memungkinkan pembelajaran fisik terhubung dengan pencatatan perkembangan. Teknologi ditempatkan sebagai alat bantu; hubungan guru dan peserta melalui talqin, talaqqi, koreksi, dan keteladanan tetap menjadi pusat proses pendidikan.",
      "Dengan demikian, QURBATA Jilid 1 diharapkan menjadi gerbang yang kokoh: peserta mulai membaca dengan benar, akrab dengan ungkapan Arab, menjaga hafalan, dan tumbuh dalam kebiasaan baik. Fondasi inilah yang kemudian dikembangkan secara bertahap pada jilid-jilid berikutnya."
    ]
  },
  {
    title: "MENGENAL QURBATA",
    arabic: "إِنَّا أَنْزَلْنَاهُ قُرْآنًا عَرَبِيًّا لَعَلَّكُمْ تَعْقِلُونَ",
    source: "QS. Yusuf [12]: 2",
    paragraphs: [
      "QURBATA adalah metode integratif pembelajaran Al-Qur’an yang mempertemukan empat unsur: Qur’an/Tartil, Bahasa Arab, Tahfidz, dan Akhlak. Keempatnya tidak ditempatkan dengan bobot yang sama. Tartil merupakan jalur kompetensi inti, sedangkan tiga unsur lainnya memperkuat ekosistem pembelajaran.",
      "Qur’an/Tartil disusun sebagai tangga kompetensi. Setiap halaman memiliki sasaran bacaan tertentu dan peserta bergerak setelah kemampuan sebelumnya cukup kokoh. Pola ini menjaga agar proses belajar tidak berubah menjadi sekadar mengejar jumlah halaman.",
      "Bahasa Arab QURBATA adalah Bahasa Arab untuk menghidupkan suasana belajar Al-Qur’an. Ungkapan dipilih karena dapat langsung digunakan guru dan peserta dalam interaksi kelas. Jalur ini berbeda dari Bahasa Arab RIQA, yang merupakan jalur kompetensi Bahasa Arab Qur’ani tersendiri berbasis peta dan korpus Al-Qur’an.",
      "Tahfidz menyertai perjalanan belajar secara bertahap. Pada Jilid 1, hafalan dimulai dari Surah An-Nas dan berkembang ayat demi ayat sesuai peta. Hafalan baru selalu berhubungan dengan murojaah agar yang telah diperoleh tetap terjaga.",
      "Akhlak QURBATA bukan tambahan dekoratif pada halaman. Hadis atau nasihat dipilih sebagai pesan yang dipahami, diulang, dan dibiasakan. Satu pesan dapat hidup selama beberapa pertemuan hingga guru melihat perubahan sikap. Jalur pembiasaan ini berbeda dari pembelajaran Hadis RIQA yang memiliki kompetensi tersendiri.",
      "Pertemuan empat unsur tersebut membentuk karakter QURBATA: membaca dengan benar, berinteraksi dengan bahasa Al-Qur’an, menjaga ayat dalam dada, dan menghadirkan nilai Al-Qur’an dalam perilaku."
    ]
  },
  {
    title: "LANDASAN & PRINSIP PEMBELAJARAN",
    arabic: "وَلَقَدْ يَسَّرْنَا الْقُرْآنَ لِلذِّكْرِ فَهَلْ مِنْ مُدَّكِرٍ",
    source: "QS. Al-Qamar [54]: 17",
    paragraphs: [
      "QURBATA dibangun di atas keyakinan bahwa belajar Al-Qur’an memerlukan kemudahan yang terstruktur, pengulangan yang cukup, dan pendampingan yang benar. Materi karena itu dipecah menjadi kompetensi kecil yang dapat diamati dan dilatih.",
      "Prinsip pertama adalah bertahap. Peserta tidak melompati kompetensi hanya karena telah mengenal bentuknya. Prinsip kedua adalah talaqqi: bacaan diterima dari guru, dicontohkan, ditirukan, lalu dikoreksi. Prinsip ketiga adalah pengulangan: materi lama tetap hadir di tengah materi baru agar kemampuan tidak rapuh.",
      "Prinsip keempat adalah integrasi proporsional. Bahasa Arab, Tahfidz, dan Akhlak hadir untuk menguatkan pembelajaran, tetapi latihan Tartil tetap memperoleh ruang terbesar. Prinsip kelima adalah keterukuran. Tanggal, nilai, tanda tangan, aktivitas, QR kompetensi, dan rekam RIQA OS membantu guru melihat perkembangan secara nyata.",
      "Prinsip keenam adalah keteladanan. Akhlak tidak cukup dibacakan; guru perlu menampakkannya dalam cara menyapa, menyimak, mengoreksi, menunggu, dan menghargai peserta. Dengan demikian, pembelajaran bergerak dari ilmu menuju amal dan dari amal menuju kebiasaan."
    ]
  },
  {
    title: "GAMBARAN QURBATA JILID 1",
    arabic: "تَعَلَّمْ — اِعْمَلْ — عَلِّمْ",
    source: "Ruh QURBATA",
    paragraphs: [
      "Jilid 1 merupakan tahap fondasi. Peserta diperkenalkan kepada bentuk dan bunyi melalui urutan kompetensi yang dirancang untuk membangun ketepatan sejak awal. Porsi terbesar halaman adalah Latihan Tartil karena keterampilan membaca memerlukan paparan dan pengulangan yang cukup.",
      "Di sekitar latihan inti tersebut, peserta memperoleh target Tahfidz yang ringan dan berkesinambungan, ungkapan Bahasa Arab yang dapat segera digunakan dalam kelas, serta pesan Akhlak yang dibawa ke dalam aktivitas keseharian. Unsur-unsur ini tidak harus selesai sekaligus dalam satu pertemuan; guru menyesuaikan ritme dengan kesiapan peserta.",
      "Setiap halaman juga berfungsi sebagai catatan perjalanan. Tanggal menunjukkan waktu belajar, nilai merekam hasil, tanda tangan memberi validasi pendamping, dan QR menghubungkan halaman dengan kompetensi digital. Dengan cara ini, buku bukan hanya tempat latihan, tetapi menjadi bagian dari rekam perkembangan peserta.",
      "Keberhasilan Jilid 1 tidak dinilai dari seberapa cepat buku selesai. Ukurannya adalah terbentuknya fondasi: bacaan semakin tepat, peserta nyaman mengikuti talaqqi, hafalan terjaga, ungkapan Arab mulai menjadi kebiasaan, dan nilai Akhlak mulai terlihat dalam perilaku belajar."
    ],
    structured: {
      kind: "list",
      items: [
        ["Tartil", "Kompetensi inti; latihan membaca mendapat porsi terbesar dan bergerak bertahap."],
        ["Tahfidz", "Dimulai dari Surah An-Nas dan berkembang ayat demi ayat disertai murojaah."],
        ["Bahasa Arab", "Ungkapan fungsional untuk membangun bi’ah ‘Arabiyah selama pembelajaran."],
        ["Akhlak", "Hadis atau nasihat dibiasakan beberapa pertemuan hingga tampak dalam perilaku."],
        ["Rekam Belajar", "Tanggal, nilai, tanda tangan, QR kompetensi, dan RIQA OS mencatat perkembangan."]
      ]
    }
  },
  {
    title: "PETUNJUK PENGGUNAAN BUKU",
    arabic: "تَعَلَّمْ — اِعْمَلْ — عَلِّمْ",
    source: "Belajarlah · Amalkan · Ajarkan",
    paragraphs: [
      "Buku QURBATA digunakan bersama guru atau pendamping. Peserta tidak dianjurkan mendahului kompetensi baru secara mandiri, karena bentuk, bunyi, dan cara membaca perlu diterima melalui contoh yang benar. Guru membuka halaman sesuai posisi kompetensi peserta, bukan semata-mata mengikuti pertemuan kelompok.",
      "Bagian Latihan Tartil merupakan area utama. Guru mencontohkan bacaan melalui talqin, peserta menirukan, kemudian membaca kembali melalui talaqqi. Kesalahan dikoreksi pada saat yang tepat dan bagian yang belum mantap diulang. Ukuran huruf dan jarak latihan sengaja memberi ruang agar perhatian peserta terarah pada bentuk dan harakat.",
      "Bagian Tahfidz menunjukkan target hafalan yang menyertai halaman. Guru membacakan ayat dengan benar, peserta mengikuti, lalu mengulang hingga cukup kuat. Hafalan lama tetap dimurojaah sebelum atau sesudah penambahan target baru.",
      "Bagian Bahasa Arab/Bi’ah memuat ungkapan yang digunakan dalam suasana belajar. Guru tidak cukup meminta peserta menghafalkannya; ungkapan tersebut dipakai secara nyata ketika membuka pelajaran, memberi instruksi, bertanya, menjawab, atau menutup kegiatan. Pengulangan alami membentuk bi’ah ‘Arabiyah tanpa mengubah sesi Tartil menjadi pelajaran nahwu.",
      "Bagian Akhlak membawa hadis atau nasihat terpilih ke dalam pembiasaan. Guru menjelaskan makna secara sederhana, memberi contoh perilaku, lalu memilih aktivitas yang dapat dilakukan. Satu nilai boleh dipertahankan pada beberapa pertemuan sampai menjadi kebiasaan.",
      "Kolom Aktivitas Bi’ah menjadi catatan praktik, bukan sekadar ruang yang harus diisi. Tanggal menunjukkan pelaksanaan, nilai merekam capaian sesuai standar guru, dan tanda tangan menjadi pengesahan pendamping. Catatan singkat dapat digunakan bila ada bagian yang perlu diulang.",
      "QR kompetensi menghubungkan buku dengan RIQA OS. Melalui sistem ini, peserta dan pendamping dapat diarahkan kepada materi pendukung, contoh, asesmen, atau rekam perkembangan yang relevan. QR tidak menggantikan guru dan tidak mengubah buku menjadi pembelajaran mandiri sepenuhnya.",
      "Bagi orang tua atau pendamping di rumah, tugas utama adalah membantu pengulangan materi yang telah diajarkan, menjaga rutinitas, mendengarkan hafalan, dan menguatkan pembiasaan Akhlak. Hindari mengajarkan kompetensi baru sebelum guru membukanya agar pola belajar tetap konsisten."
    ],
    structured: {
      kind: "table",
      headers: ["Bagian", "Cara Menggunakan"],
      rows: [
        ["Latihan Tartil", "Guru talqin → peserta menirukan → talaqqi → koreksi → pengulangan."],
        ["Tahfidz", "Dengar → tiru → ulang → sambung → murojaah hafalan sebelumnya."],
        ["Bahasa Arab / Bi’ah", "Gunakan ungkapan secara nyata dalam instruksi dan interaksi kelas."],
        ["Akhlak", "Pahami pesan → beri contoh → praktikkan → pertahankan sampai menjadi kebiasaan."],
        ["Aktivitas Bi’ah", "Catat praktik yang benar-benar dilakukan peserta."],
        ["Tanggal · Nilai · TTD", "Isi setelah verifikasi sebagai rekam perkembangan."],
        ["QR Kompetensi", "Hubungkan halaman fisik dengan materi, asesmen, dan rekam RIQA OS."],
        ["Pendamping di Rumah", "Ulangi yang sudah diajarkan; jangan mendahului kompetensi baru."]
      ]
    }
  },
  {
    title: "PANDUAN PENGAJARAN QURBATA",
    arabic: "وَإِنَّكَ لَعَلَى خُلُقٍ عَظِيمٍ",
    source: "QS. Al-Qalam [68]: 4",
    paragraphs: [
      "Guru memulai dengan membangun kesiapan: salam, adab duduk, perhatian, dan murojaah singkat. Suasana kelas perlu tenang tetapi hangat. Bahasa Arab yang sudah dikenal dapat digunakan sejak pembukaan agar bi’ah tumbuh secara alami.",
      "Pada tahap talqin, guru memberikan model bacaan yang jelas dan tidak berlebihan jumlahnya. Peserta mendengar sebelum menirukan. Pada tahap talaqqi, peserta membaca dan guru menyimak secara langsung. Koreksi diprioritaskan pada kompetensi halaman yang sedang dilatih.",
      "Latihan kemudian diperluas melalui pengulangan contoh pada halaman. Guru menjaga agar peserta tidak menebak atau menghafal urutan visual. Bila diperlukan, guru menunjuk contoh secara acak. Materi lama dapat disisipkan untuk memastikan kemampuan sebelumnya tetap stabil.",
      "Tahfidz dilakukan dengan pola dengar, tiru, ulang, sambung, dan murojaah. Bahasa Arab digunakan dalam instruksi yang sesuai tingkat peserta. Akhlak dihidupkan melalui satu perilaku yang dapat diamati selama proses belajar, misalnya adab mendengar, menunggu giliran, menjaga kebersihan, atau menghormati guru dan teman.",
      "Di akhir pertemuan guru melakukan verifikasi singkat. Peserta yang telah memenuhi target dapat melanjutkan; peserta yang belum mantap diberi pengulangan terarah tanpa stigma. Nilai dan catatan digunakan untuk membantu keputusan pembelajaran, bukan sekadar administrasi.",
      "Guru QURBATA tidak mengejar selesainya halaman. Tugas utamanya adalah menjaga kesinambungan kompetensi. Pergantian guru pun tidak boleh memutus perkembangan peserta karena posisi kompetensi, catatan, dan rekam RIQA OS menjadi rujukan bersama."
    ],
    structured: {
      kind: "steps",
      items: [
        ["01", "Pembukaan & kesiapan", "Salam, adab, perhatian, dan murojaah singkat."],
        ["02", "Talqin", "Guru memberi model bacaan yang jelas dan terukur."],
        ["03", "Talaqqi", "Peserta membaca; guru menyimak dan mengoreksi langsung."],
        ["04", "Latihan & murojaah", "Perbanyak praktik dan sisipkan materi lama."],
        ["05", "Tahfidz", "Dengar, tiru, ulang, sambung, lalu murojaah."],
        ["06", "Bi’ah ‘Arabiyah", "Gunakan ungkapan Arab sesuai tingkat peserta."],
        ["07", "Akhlak", "Latih satu perilaku yang dapat diamati."],
        ["08", "Verifikasi", "Nilai capaian; lanjut bila kompeten, ulangi bila belum mantap."]
      ]
    }
  },
  {
    title: "PETA KOMPETENSI JILID 1",
    arabic: "قُرْآنًا عَرَبِيًّا",
    source: "Qur’an · Bahasa Arab · Tahfidz · Akhlak",
    paragraphs: [
      "Peta kompetensi Jilid 1 dibaca dalam empat jalur yang berjalan berdampingan. Jalur pertama adalah Tartil sebagai kompetensi inti: peserta bergerak dari kemampuan dasar menuju bentuk yang lebih kompleks secara berurutan. Jalur kedua adalah Tahfidz yang bergerak ayat demi ayat dan selalu disertai murojaah.",
      "Jalur ketiga adalah Bahasa Arab QURBATA sebagai bi’ah kelas. Targetnya bukan menyelesaikan bab tata bahasa, tetapi membuat ungkapan sederhana hadir dalam pengalaman belajar sehari-hari. Jalur keempat adalah Akhlak: nilai dipilih, dipahami, dipraktikkan, dan dipertahankan hingga menjadi kebiasaan.",
      "Guru menggunakan peta ini untuk melihat hubungan antarkompetensi, sedangkan rincian latihan tetap berada pada halaman materi. Peta bukan alasan untuk mempercepat peserta; ia berfungsi memastikan arah perkembangan tetap jelas dari awal hingga akhir Jilid 1."
    ],
    structured: {
      kind: "table",
      headers: ["Jalur", "Fungsi", "Arah Perkembangan"],
      rows: [
        ["Tartil", "Kompetensi inti", "Dasar → bertahap → lebih kompleks; tidak melompati kompetensi."],
        ["Tahfidz", "Menjaga ayat dalam hafalan", "An-Nas → ayat demi ayat → murojaah berkelanjutan."],
        ["Bahasa Arab", "Bi’ah kelas", "Ungkapan sederhana → penggunaan berulang → kebiasaan berbahasa."],
        ["Akhlak", "Pembiasaan nilai", "Mendengar → memahami → mempraktikkan → membiasakan."]
      ]
    }
  },
  {
    title: "DAFTAR ISI",
    arabic: "تَعَلَّمْ — اِعْمَلْ — عَلِّمْ",
    source: "QURBATA Jilid 1",
    paragraphs: [
      "Sambutan Pendiri QURBATA & RIQA · Pendahuluan · Mengenal QURBATA · Landasan & Prinsip Pembelajaran · Gambaran QURBATA Jilid 1 · Petunjuk Penggunaan Buku · Panduan Pengajaran QURBATA · Peta Kompetensi Jilid 1."
    ]
  }
];

function renderStructured(s) {
  if (s.kind === "table") return `<table class="front-table"><thead><tr>${s.headers.map(h=>`<th>${escapeHtml(h)}</th>`).join("")}</tr></thead><tbody>${s.rows.map(r=>`<tr>${r.map(c=>`<td>${escapeHtml(c)}</td>`).join("")}</tr>`).join("")}</tbody></table>`;
  if (s.kind === "steps") return `<ol class="front-steps">${s.items.map(r=>`<li><b>${escapeHtml(r[0])}</b><span><strong>${escapeHtml(r[1])}</strong><small>${escapeHtml(r[2])}</small></span></li>`).join("")}</ol>`;
  return `<ul class="front-list">${s.items.map(r=>`<li><strong>${escapeHtml(r[0])}</strong><span>${escapeHtml(r[1])}</span></li>`).join("")}</ul>`;
}

const frontMatter = frontMatterData.map((item, index) => `
  <article class="book-page front-matter-page">
    <header class="page-header"><div class="header-line"></div><div class="book-name"><span class="qurbata-brand-text"><strong>QURBATA</strong><small>Qur’an · Bahasa Arab · Tahfidz · Akhlak</small></span></div><div class="page-number">${String(index + 1).padStart(2, "0")}</div></header>
    <section class="front-matter-content official-front">
      <h1>${escapeHtml(item.title)}</h1>
      <div class="official-epigraph"><p class="arabic front-arabic" lang="ar" dir="rtl">${escapeHtml(item.arabic)}</p>${item.source ? `<p class="front-source">${escapeHtml(item.source)}</p>` : ""}</div>
      ${item.structured ? renderStructured(item.structured) : (item.paragraphs || [item.body]).filter(Boolean).map(p => `<p class="front-body">${escapeHtml(p)}</p>`).join("\n")}
      ${index === 0 ? `<div class="front-motto"><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah · Amalkan · Ajarkan</small></div>` : ""}
    </section>
    <footer class="page-footer"><p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p><small>Belajarlah • Amalkan • Ajarkan</small></footer>
  </article>`).join("\n");

const pages = await Promise.all(data.pages.map(async (page) => {
  if (!page.title || !page.titleArabic || arabicLetters(page.titleArabic).length === 0) {
    throw new Error(`${page.pageId}: judul Indonesia dan judul Arab wajib diisi terpisah.`);
  }
  if (page.rows.length !== 8 || page.rows.some((row) => row.length !== 3)) {
    throw new Error(`${page.pageId}: grid wajib tepat 8 baris x 3 kolom.`);
  }
  const items = page.rows.flat();
  if (items.length !== 24) {
    throw new Error(`${page.pageId}: halaman wajib mempunyai tepat 24 tangga.`);
  }
  const pageNo = Number(page.pageNumber);
  const firstEightValid = items.slice(0, 8).every((item) => arabicLetters(item).length === 2);
  const lastSixteenValid = items.slice(8).every((item) => arabicLetters(item).length === 3);
  const allThreeValid = items.every((item) => arabicLetters(item).length === 3);
  const patternValid = pageNo >= 14 ? allThreeValid : (firstEightValid && lastSixteenValid);
  if (!patternValid) {
    throw new Error(`${page.pageId}: pola tangga tidak sesuai fase halaman (P014+ wajib seluruhnya tiga huruf).`);
  }
  if (!/^https:\/\/www\.rumahilmualquran\.com\/q\/[A-Z0-9-]+$/.test(page.riqaOsUrl)) {
    throw new Error(`${page.pageId}: URL RIQA OS tidak mengikuti kontrak /q/{pageId}.`);
  }

  const qr = await QRCode.toDataURL(page.riqaOsUrl, {
    errorCorrectionLevel: "H",
    margin: 1,
    width: 240,
    color: { dark: "#075985", light: "#ffffff" }
  });

  const rows = page.rows.map((row) => `
    <div class="practice-row">
      ${row.map((item) => `<div class="practice-cell arabic" lang="ar" dir="rtl">${renderPracticeArabic(item)}</div>`).join("")}
    </div>`).join("");

  const activities = page.activities.map((item, index) => `
    <div class="activity"><span>${index + 1}</span>${escapeHtml(item)}</div>`).join("");

  return `
  <article class="book-page" data-page-id="${escapeHtml(page.pageId)}">
    <header class="page-header">
      <div class="header-line"></div>
      <div class="book-name"><span class="qurbata-brand-logo"><svg viewBox="0 0 1956 2048" aria-label="Logo QURBATA"><path fill="#0f8f91" fill-rule="evenodd" d="M1034,1576 958,1652 1035,1729 1111,1652Z M1637,1221 1629,1213 1608,1204 1573,1202 1541,1207 1506,1223 1483,1249 1473,1276 1509,1265 1540,1264 1570,1269 1588,1277 1543,1317 1469,1361 1502,1360 1539,1353 1564,1344 1597,1324 1619,1301 1638,1266 1644,1240Z M1483,800 1340,868 1217,936 1138,991 1107,1021 1093,1044 1457,852Z M1816,838 1790,819 1754,801 1703,789 1662,799 1625,820 1589,856 1560,909 1542,976 1541,1041 1552,1080 1569,1107 1598,1132 1630,1147 1664,1154 1704,1155 1827,1145 1854,1154 1872,1172 1882,1199 1883,1245 1829,1296 1769,1337 1688,1384 1556,1453 1455,1522 1386,1586 1308,1681 1250,1741 1143,1837 1059,1905 1001,1928 948,1937 904,1933 875,1921 854,1906 827,1875 810,1844 800,1795 800,1758 806,1712 826,1644 864,1564 938,1453 876,1514 830,1576 790,1651 767,1718 756,1798 756,1846 761,1886 772,1923 784,1948 802,1974 824,1996 851,2015 893,2035 925,2044 954,2047 988,2046 1032,2036 1098,2005 1139,1977 1186,1937 1233,1889 1345,1762 1471,1646 1581,1565 1688,1505 1760,1458 1831,1400 1881,1347 1919,1297 1945,1236 1955,1179 1953,1100 1930,1020 1898,946 1860,885Z M1604,968 1614,953 1636,934 1658,925 1680,922 1720,934 1749,950 1779,980 1793,1009 1725,1020 1652,1019 1624,1009 1611,997 1604,982Z M1602,582 1527,658 1604,734 1680,657Z M1807,579 1730,655 1806,732 1883,656Z M476,251 401,328 478,403 554,327Z M639,250 564,326 641,402 717,325Z M1294,287 1271,261 1244,245 1211,236 1176,233 1100,255 1015,299 935,358 849,439 782,514 663,662 606,725 518,813 411,904 315,971 205,1030 105,1068 1,1092 51,1104 103,1111 203,1109 240,1103 308,1083 390,1043 458,995 540,917 592,855 683,732 777,615 845,538 933,453 988,412 1046,384 1105,370 1160,374 1187,386 1213,407 1239,442 1249,464 1250,501 1241,538 1220,582 1201,611 1161,660 1107,714 1057,758 962,831 919,634 898,566 882,528 847,702 847,728 875,843 879,893 765,973 690,1032 624,1090 563,1152 513,1214 482,1265 462,1314 457,1373 463,1400 473,1418 494,1436 529,1448 577,1450 655,1437 707,1419 774,1380 839,1319 891,1245 932,1160 945,1248 974,1337 1015,1407 1063,1458 1121,1497 1191,1525 1253,1523 1283,1515 1317,1498 1354,1465 1379,1429 1402,1377 1415,1303 1415,1246 1402,1168 1381,1105 1352,1043 1298,1219 1337,1283 1356,1339 1307,1375 1259,1394 1210,1397 1170,1388 1125,1365 1104,1347 1076,1308 1047,1246 1009,1113 974,904 976,898 1079,816 1161,736 1216,669 1263,594 1296,516 1313,437 1314,349 1306,313Z M904,988 910,1032 903,1115 895,1138 843,1189 762,1251 728,1270 682,1289 638,1299 592,1300 567,1297 527,1284 538,1262 575,1212 656,1132 788,1027 891,955Z M1766,124 1738,112 1706,128 1671,157 1646,193 1641,219 1648,239 1675,270 1700,289 1656,344 1614,385 1541,443 1470,491 1363,555 1416,546 1451,535 1497,514 1543,486 1591,448 1641,399 1715,307 1729,325 1734,341 1731,373 1674,466 1662,497 1658,529 1666,550 1682,562 1713,560 1729,554 1746,541 1765,507 1772,463 1760,483 1743,501 1723,510 1699,504 1692,494 1692,482 1710,443 1746,392 1762,352 1762,311 1755,292 1737,268 1766,213 1776,181 1777,143Z M1731,152 1744,171 1746,192 1740,215 1721,249 1691,227 1671,197 1698,166Z M740,0 588,73 457,147 382,203 361,225 350,244 714,52Z"/></svg></span><span class="qurbata-brand-text"><strong>${escapeHtml(data.book.title)}</strong><small>Qur’an · Bahasa Arab · Tahfidz · Akhlak</small></span></div>
      <div class="page-number">${escapeHtml(page.pageNumber)}</div>
    </header>

    <section class="lesson-heading">
      <h1><span>${escapeHtml(page.title)}</span> <span class="arabic lesson-title-arabic" lang="ar" dir="rtl">${escapeHtml(page.titleArabic)}</span></h1>
      <p><strong>Kompetensi Tartil:</strong> ${escapeHtml(page.tartilCompetency)}</p>
    </section>

    <div class="integration-grid">
      ${card("TAHFIDZ", page.integration.tahfidz)}
      ${card("BAHASA ARAB", page.integration.arabic)}
      ${card("AKHLAK", page.integration.akhlak)}
    </div>

    ${page.review ? `<section class="review-strip"><header><h2>${escapeHtml(page.review.title)}</h2><p>${escapeHtml(page.review.instruction)}</p></header><div class="review-letters arabic" lang="ar" dir="rtl">${page.review.letters.map(x=>`<span>${escapeHtml(x)}</span>`).join("")}</div><div class="review-harakat">${page.review.harakat.map(x=>`<div><b>${escapeHtml(x.name)}</b><span class="arabic" lang="ar">${escapeHtml(x.mark)}</span></div>`).join("")}</div></section>` : ""}

    <section class="practice-panel">
      <header><h2>LATIHAN TARTIL</h2><p>Bacalah dengan tartil dan jelas.</p></header>
      <div class="practice-grid">${rows}</div>
    </section>

    <section class="activity-strip">
      <div class="activity-content">
        <h2>AKTIVITAS BI’AH QURBATA</h2>
        <div class="activity-grid">${activities}</div>
      </div>
      <a class="qr-link" href="${escapeHtml(page.riqaOsUrl)}" aria-label="Buka kompetensi ${escapeHtml(page.pageId)} di RIQA OS">
        <img src="${qr}" alt="QR ${escapeHtml(page.pageId)}">
        <span>Pindai di RIQA OS</span>
      </a>
      <div class="learning-record" aria-label="Catatan hasil belajar">
        <div><span>Tanggal</span><i></i></div>
        <div><span>Nilai</span><i></i></div>
        <div><span>TTD Guru</span><i></i></div>
      </div>
    </section>

    <footer class="page-footer">
      <div><span class="page-id">${escapeHtml(page.pageId)}</span><span>${escapeHtml(data.book.status)}</span></div>
      <p class="arabic" lang="ar" dir="rtl">تَعَلَّمْ — اِعْمَلْ — عَلِّمْ</p>
      <small>Belajarlah • Amalkan • Ajarkan</small>
    </footer>
  </article>`;
}));

const html = template
  .replace("/*__BOOK_CSS__*/", css)
  .replace("<!--__BOOK_PAGES__-->", process.env.QURBATA_FRONT_MATTER_ONLY === "1" ? frontMatter : `${frontMatter}\n${pages.join("\n")}`);

await fs.mkdir(path.join(root, "dist"), { recursive: true });
await fs.mkdir(path.join(root, "dist/fonts"), { recursive: true });
await fs.copyFile(
  path.join(root, "fonts/KFGQPC-Uthman-Taha-Naskh.woff2"),
  path.join(root, "dist/fonts/KFGQPC-Uthman-Taha-Naskh.woff2")
);
await fs.writeFile(path.join(root, "dist/index.html"), html);
console.log(`Dibangun: ${data.pages.length} halaman -> dist/index.html`);
