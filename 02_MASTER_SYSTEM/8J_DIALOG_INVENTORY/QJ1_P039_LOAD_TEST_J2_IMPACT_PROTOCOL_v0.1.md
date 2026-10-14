# PROTOKOL UJI BEBAN P039 DAN KESINAMBUNGAN J2 — OPSI B v0.1

**Status:** DRAFT PROTOKOL VALIDASI; belum ada data uji lapangan.  
**Dasar:** J1 MAP v0.2, persetujuan arah Opsi B, J2 P001 baseline Quraisy 1–2 dalam AYAT-DISTRIBUTION-WORKING-v0.1.

## A. Pertanyaan uji

Apakah santri pemula J1 yang telah memperoleh Al-Ma'un 1–2 di P038 dapat menerima **Al-Ma'un 3–7 (lima ayat) di P039** melalui talqin bertahap, lalu mempertahankannya pada checkpoint P040 tanpa mengurangi waktu Tartil dan kesejahteraan belajar?

## B. Pelaksanaan

1. Gunakan nash dan audio yang telah ditashih oleh guru/ahli sebelum uji. Tidak mengklaim bacaan yang belum ditashih.
2. Catat identitas peserta dengan kode, bukan nama dalam dokumen evaluasi terbuka; kelompokkan menurut kemampuan hafalan awal tanpa memberi label negatif.
3. Pada P038, rekam penguasaan Al-Ma'un 1–2 sebagai baseline.
4. Pada P039, guru memberi contoh (sima'), santri menirukan (talqin), mengulang per potongan pendek sesuai jeda makna/waqaf yang telah disahkan, lalu menyambungkan potongan; guru tidak memaksa bacaan mandiri dari mushaf.
5. Ukur waktu talqin efektif, jumlah pengulangan, ketepatan urutan, kebutuhan prompt, dan kelelahan/keengganan yang teramati. Catat tanpa mengurangi alokasi Tartil.
6. Pada P040, lakukan murojaah tanpa target baru. Nilai retensi Al-Ma'un 1–7 serta corpus prioritas lain secara sampling berlapis.
7. Gunakan evaluasi kolektif, berpasangan, sampling acak guru, lalu pemeriksaan individu untuk peserta yang memerlukan dukungan; penilaian formal tetap sesuai kebijakan penguji.

## C. Lembar data per peserta (diisi saat pelaksanaan, bukan nilai buatan)

| Kode peserta | Baseline P038 | Waktu talqin P039 | Pengulangan | Kesalahan urutan/bunyi | Bantuan guru | Retensi P040 | Catatan kenyamanan |
|---|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... | ... |

## D. Rubrik pengamatan

- **Akurasi:** ayat dan urutan benar; koreksi yang dibutuhkan dicatat.
- **Kemandirian hafalan:** mandiri / dengan isyarat / perlu talqin ulang.
- **Retensi:** masih dapat mengulang pada P040; bandingkan dengan hasil P039.
- **Beban:** waktu yang diperlukan dan dampaknya pada target Tartil.
- **Kenyamanan:** tidak ada tekanan atau praktik mempermalukan peserta; berikan penyesuaian sesuai kebutuhan.

**Tidak ada ambang kelulusan numerik yang sudah disahkan di sumber.** Ahli/pemilik akademik harus menetapkan ambang dan ukuran sampel sebelum uji, bukan setelah melihat hasil.

## E. Keputusan pascauji

- **Layak:** pertahankan P039 kandidat jika retensi, beban, dan kesejahteraan belajar memenuhi ambang yang disahkan.
- **Layak dengan revisi:** pecah menjadi beberapa sesi talqin di P039 tanpa mengganggu Tartil; uji ulang dan catat revisi.
- **Tidak layak:** ajukan pemindahan sebagian Al-Ma'un ke J2; pertahankan P040 sebagai terminal review. Jangan langsung mengubah J2 tanpa persetujuan baru.

## F. Dampak J2 dan RIQA OS

- **Baseline J2 P001:** Quraisy 1–2 menurut `QURBATA-TAHFIDZ-AYAT-DISTRIBUTION-WORKING-v0.1.md`. Pindah target dari J1 ke J2 akan mengubah beban dan kemungkinan urutan awal J2; perlu matriks delta P039–P040 J1 dan P001–P005 J2.
- **RIQA OS:** belum melakukan migrasi/aktivasi. Siapkan field `target_version`, `source_decision_id`, `new_target`, `review_scope`, `validation_status`, dan `effective_at` untuk desain teknis, tanpa menyatakan skema ini sudah ada.
- **DEC-CUR-004:** objek Al-Fatihah tetap approved-for-validation, inactive; harus ada keputusan hubungan objek dengan target buku sebelum deployment.

## G. Gate penutupan

- [ ] Ahli menyetujui protokol dan ambang keberhasilan sebelum pengujian
- [ ] Izin dan safeguarding untuk pengumpulan data santri
- [ ] Uji P038/P039/P040 terlaksana dengan bukti
- [ ] Analisis beban, akurasi, retensi dan dampak Tartil
- [ ] Keputusan mempertahankan atau meredistribusi target
- [ ] Audit J2 dan RIQA OS
- [ ] Tashih dan keputusan freeze terpisah

**Status saat ditulis:** PROTOKOL SIAP DITINJAU; UJI BELUM DILAKUKAN.
