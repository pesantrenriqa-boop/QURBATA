# AUD-HAD-QJ1-001 — Pra-Audit Kandidat dan Murojaah Hadis Akhlak Jilid 1

**Audit-ID:** AUD-HAD-QJ1-001  
**Status:** INTERNAL-PRECHECK COMPLETE — EXPERT VALIDATION OPEN  
**Tanggal:** 29 Juli 2026  
**Cakupan:** REG-HAD-001, BAT-HAD-001–005, MAP-HAD-QJ1-001 v0.2.0-id, REV-HAD-QJ1-001

## 1. Batas Audit

Audit ini memeriksa struktur data, keunikan identitas, kelengkapan locator awal, konsistensi mapping, beban jadwal, dan risiko yang tampak. Audit internal tidak mengesahkan kesahihan hadis, matan, grading, terjemah, hukum, atau kelayakan usia.

## 2. Hasil Kuantitatif

| Pemeriksaan | Hasil | Status |
|---|---:|---|
| Hadith-ID | 40/40 unik | PASS-STRUCTURE |
| Full-Hadith-ID kandidat | 40/40 unik secara administratif | EXPERT DEDUP OPEN |
| Halaman intro | P001–P040, satu objek per halaman | PASS-STRUCTURE |
| Locator awal | 40/40 | SOURCE-PRECHECK |
| Objek APPROVED | 0/40 | HOLD |
| Izin teks peserta | 0/40 | HOLD |
| Form keputusan ahli | 40/40 baris | READY-FOR-EXPERT |
| Evidence-ID/Decision-ID | 0/40 | OPEN |
| Maksimum prompt review per halaman setelah koreksi | 8 | DESIGN-PASS / PILOT OPEN |
| Checkpoint | P008, P016, P024, P032, P040 | COMPLETE-DRAFT |
| Carryover objek akhir | diwajibkan ke Jilid 2 | MAP-QJ2 OPEN |

## 3. Temuan dan Koreksi

### HAD-AUD-001 — Beban checkpoint berlebih

- **Temuan awal:** rancangan v0.1 meminta seluruh kolam pada checkpoint sehingga P040 dapat memuat 39 prompt.
- **Dampak:** tidak realistis untuk segmen lima menit dan berisiko mengubah murojaah menjadi penyebutan dangkal tanpa umpan balik.
- **Koreksi:** MAP-HAD-QJ1-001 v0.2 membatasi maksimal delapan prompt; interval 1/3/7/14 dipertahankan dan sisa kapasitas diberikan kepada objek berfrekuensi terendah.
- **Sisa bukti:** uji kelas, durasi aktual, tingkat bantuan, dan retensi.
- **Status:** CORRECTED-DESIGN / PILOT OPEN.

### HAD-AUD-002 — Ketimpangan alami objek akhir

- **Temuan:** objek awal memiliki lebih banyak kesempatan review; HAD-000040 tidak mungkin direview setelah intro di dalam Jilid 1.
- **Koreksi:** pemerataan dinilai berdasarkan kesempatan sejak intro, bukan angka mentah; HAD-000037–HAD-000040 wajib dibawa ke awal Jilid 2.
- **Sisa bukti:** MAP-HAD-QJ2 dan frekuensi aktual.
- **Status:** CONTROLLED / FOLLOW-UP OPEN.

### HAD-AUD-003 — Klaster makna berdekatan

| Klaster | Objek | Keputusan ahli yang diperlukan |
|---|---|---|
| kelembutan | HAD-000006, HAD-000033, HAD-000034 | bedakan sifat, penerapan, dan prinsip memudahkan |
| kebaikan umum/kecil | HAD-000002, HAD-000008, HAD-000026, HAD-000035, HAD-000040 | pastikan outcome dan penggalan tidak redundan |
| kasih sayang | HAD-000001, HAD-000029, HAD-000036, HAD-000038 | tetapkan lingkup orang dekat, umum, lintas usia, dan anak yatim |
| bantuan sosial | HAD-000014, HAD-000021, HAD-000027, HAD-000039 | bedakan bantuan individual, saling menguatkan, perlindungan, dan pelayanan rentan |
| lisan | HAD-000002, HAD-000016, HAD-000032 | bedakan ucapan baik, diam dari keburukan, dan nasihat tulus |

Full-Hadith-ID administratif berbeda tidak membuktikan bahwa beban pedagogisnya tidak berulang. PROP-HAD-QJ1-001 kini menyediakan outcome, prompt pembeda, prioritas pemindahan/penggantian, dan form keputusan. Panel ahli tetap harus memilih APPROVE, RESEQUENCE, REPLACE, atau MERGE-THEME.

### HAD-AUD-004 — Penggalan dan varian

Objek bertanda EXCERPT, VARIANT, WORDING, CONTEXT, atau LOCATOR memerlukan perbandingan matan lengkap, jalur/riwayat, edisi, dan batas makna. Penggalan tidak boleh disahkan hanya karena kalimatnya pendek.

- **Status:** EXPERT OPEN.
- **Penutup:** SRC + MAT + GRD + DUP pada REV-HAD-QJ1-001.

### HAD-AUD-005 — Beban usia dan teologis

Perhatian khusus diperlukan untuk:

- HAD-000024: konsep ihsan dalam konteks yang lebih luas;
- HAD-000028: larangan zalim dengan bahasa sesuai usia;
- HAD-000036: `لَيْسَ مِنَّا` tidak boleh dijelaskan sebagai takfir;
- HAD-000037: jual beli dan penagihan;
- HAD-000039: istilah janda, miskin, dan mujahid;
- HAD-000040: penyebutan neraka dalam bingkai rahmah.

- **Status:** PEDAGOGY + SYAR‘I REVIEW OPEN.

### HAD-AUD-006 — Privasi dan non-stigmatisasi

HAD-000038–HAD-000040 tidak boleh memicu identifikasi anak yatim, pengungkapan ekonomi keluarga, pungutan, kompetisi sedekah, atau rasa malu. Contoh tindakan harus berbasis kelas yang aman dan dikoordinasikan orang dewasa.

- **Status:** SAFEGUARDING REVIEW OPEN.

### HAD-AUD-007 — Kanal guru dan peserta

Semua kandidat masih HOLD-PARTICIPANT. Penyebutan tema, makna, atau teks Arab dalam layout peserta harus menunggu keputusan per objek. Template buku tidak boleh mengimpor otomatis kolom Arabic-Text dari register kandidat.

- **Status:** RENDER WHITELIST OPEN.

## 4. Gerbang Tindak Lanjut

| Urutan | Pekerjaan | Pemilik | Bukti keluar |
|---:|---|---|---|
| 1 | takhrij dan audit Full-Hadith-ID | ahli hadis | SRC/MAT/GRD/DUP + Evidence-ID |
| 2 | validasi makna dan terjemah | ahli syar‘i/bahasa | TRN + koreksi |
| 3 | keputusan redundansi tema | panel akademik | APPROVE/RESEQUENCE/REPLACE |
| 4 | uji durasi dan retensi mapping | pedagogi | log per halaman/per peserta |
| 5 | safeguarding | Safeguarding Lead | SAFE decision |
| 6 | whitelist kanal dan render | editorial/produksi | AUD decision + proof |
| 7 | otorisasi | Pemilik Akademik + Document Controller | Decision-ID dan audit trail |

## 5. Kesimpulan

Struktur kandidat Jilid 1 lengkap, tetapi validitas ilmiah masih 0/40 karena belum ada keputusan ahli. Koreksi beban checkpoint telah menghilangkan masalah desain paling jelas. Blocker utama berikutnya adalah takhrij/deduplikasi ilmiah, pemilahan klaster tema, validasi usia, uji retensi, dan whitelist peserta.
