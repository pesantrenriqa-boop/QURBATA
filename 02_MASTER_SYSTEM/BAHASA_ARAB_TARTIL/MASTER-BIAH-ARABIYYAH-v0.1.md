# MASTER BĪ'AH 'ARABIYYAH QURBATA TARTIL v0.1

Status: WORKING DRAFT
Scope: QURBATA Tartil Jilid 1–8

## A. Prinsip

Bahasa Arab hadir sebagai bahasa aktivitas belajar. Target awal bukan penjelasan nahwu, tetapi pemahaman instruksi, respons spontan, pembiasaan ekspresi, dan paparan berulang dalam konteks nyata.

## B. Registry inti instruksi

| ID | Arab | Fungsi kelas | Respons awal peserta |
|---|---|---|---|
| INS-001 | السَّلَامُ عَلَيْكُمْ | salam pembuka | وَعَلَيْكُمُ السَّلَامُ |
| INS-002 | اُنْظُرْ | perhatikan/lihat | tindakan melihat |
| INS-003 | اِسْتَمِعْ | dengarkan | tindakan mendengar |
| INS-004 | رَدِّدْ | tirukan/ulangi | mengulangi model guru |
| INS-005 | اِقْرَأْ | bacalah | membaca |
| INS-006 | أَعِدْ | ulangi | mengulang |
| INS-007 | اِفْتَحْ | bukalah | membuka buku/halaman |
| INS-008 | أَغْلِقْ | tutuplah | menutup buku |
| INS-009 | مَرَّةً أُخْرَى | sekali lagi | mengulangi aktivitas |
| INS-010 | أَحْسَنْتَ | bagus (lk.) | menerima penguatan |
| INS-011 | أَحْسَنْتِ | bagus (pr.) | menerima penguatan |
| INS-012 | نَعَمْ | ya | respons lisan |
| INS-013 | لَا | tidak | respons lisan |

## C. Registry mufradat lingkungan awal

| ID | Arab | Makna/konteks |
|---|---|---|
| VOC-001 | كِتَابٌ | buku |
| VOC-002 | صَفْحَةٌ | halaman |
| VOC-003 | قَلَمٌ | pena |
| VOC-004 | مُعَلِّمٌ | guru laki-laki |
| VOC-005 | مُعَلِّمَةٌ | guru perempuan |
| VOC-006 | طَالِبٌ | peserta laki-laki |
| VOC-007 | طَالِبَةٌ | peserta perempuan |
| VOC-008 | دَرْسٌ | pelajaran |

## D. Aturan distribusi

- Input baru per pertemuan harus kecil.
- Instruksi yang sudah diperkenalkan tidak hilang; tetap digunakan secara kumulatif.
- Prioritas tertinggi adalah ungkapan yang benar-benar dibutuhkan dalam metode Tartil: melihat, mendengar, menirukan, membaca, dan mengulang.
- Terjemahan adalah scaffolding, bukan target akhir.
- Guru diarahkan mengurangi terjemahan setelah respons peserta mulai otomatis.
- Materi baru harus lolos uji `USED_IN_REAL_TARTIL_ACTIVITY`.

## E. Template unit halaman

Setiap halaman menggunakan schema minimal:

```yaml
jilid: J1
page: P001
tartil_activity: TBD
review_language: []
new_instruction: []
new_vocabulary: []
teacher_language: []
student_response: []
usage_count_target: TBD
notes: null
```

## F. Gate kualitas

Sebuah unit tidak boleh berstatus FROZEN jika:

- instruksi tidak digunakan dalam aktivitas Tartil nyata;
- terlalu banyak input baru;
- tidak ada murojaah kumulatif;
- respons peserta tidak didefinisikan;
- tidak memiliki pasangan Jilid/Page Tartil;
- tercampur dengan target buku Bahasa Arab standalone atau corpus paragraf tanpa alasan integrasi.
