# QURBATA J1 — FREQUENCY & COVERAGE AUDIT P001–P009

Status: **QA AUDIT v0.1**  
Source audited: `QURBATA-J1-READING-EXERCISE-DATA-WORKING-v0.1.md` status v0.3.

## Prinsip audit
Audit menghitung setiap unit huruf+fathah sebagai satu kemunculan. Target halaman memang lebih sering daripada review; pemerataan berarti **huruf lama tidak hilang dari rotasi**, bukan semua huruf harus memiliki frekuensi identik pada setiap halaman.

## Frekuensi per halaman
| Page | Target | Frekuensi TARGET | Review lama yang muncul |
|---|---|---:|---|
| P001 | ب ت ث | ب22 ت22 ث22 | — |
| P002 | ء أ | ء18 أ18 | ب11 ت10 ث9 |
| P003 | ج ح خ | ج16 ح16 خ16 | ب5 ت4 ث4 أ3 ء2 |
| P004 | د ذ ر ز | د12 ذ12 ر13 ز11 | ب4 ت2 ث2 ج2 ح2 خ2 أ2 ء2 |
| P005 | س ش | س17 ش17 | أ3 ء3 ب2 ت2 ث2 ج4 ح4 خ4 د2 ذ2 ر2 ز2 |
| P006 | ص ض | ص17 ض17 | أ3 ء3 ب2 ت2 ث2 ج4 ح3 خ3 د2 ذ2 ر2 ز2 س1 ش1 |
| P007 | ط ظ | ط17 ظ17 | أ3 ء3 ب2 ت2 ث2 ج3 ح2 خ3 د1 ذ1 ر1 ز1 س2 ش2 ص2 ض2 |
| P008 | ع غ | ع17 غ17 | أ2 ء2 ب3 ت2 ث2 ج1 ح2 خ2 د2 ذ2 ر1 ز1 س2 ش2 ص2 ض2 ط1 ظ1 |
| P009 | ف ق | ف17 ق17 | أ2 ء2 ب2 ت2 ث2 ج2 ح2 خ2 د1 ذ1 ر1 ز1 س2 ش2 ص2 ض2 ط1 ظ1 ع1 غ1 |

## Temuan utama
1. **Masalah Alif/Hamzah yang sebelumnya terjadi sudah terdeteksi dan dikoreksi pada data v0.3.** `أ` dan `ء` masing-masing muncul pada setiap halaman P005–P009: P005=3/3, P006=3/3, P007=3/3, P008=2/2, P009=2/2.
2. P005–P009 tidak lagi didominasi review ب/ت/ث saja. Review P003 dan P004 ikut berputar.
3. Mulai P007, jumlah kompetensi lama sudah besar; frekuensi 1 pada beberapa huruf per halaman **diterima hanya jika** huruf tersebut muncul lagi dalam rolling window berikutnya.
4. P008 dan P009 berhasil membawa kembali seluruh keluarga kompetensi lama dalam satu halaman: P001, P002, P003, P004, P005, P006, dan target-target sesudahnya.
5. Frekuensi kumulatif P001–P009 secara alami lebih tinggi untuk huruf yang diperkenalkan lebih awal. Karena itu total kumulatif tidak boleh dipakai sebagai tuntutan 'sama rata'. Ukuran QA yang benar adalah coverage sejak introduksi + jarak kemunculan kembali.

## Frekuensi kumulatif P001–P009
ب53 · ت48 · ث47 · ء35 · أ36 · ج32 · ح31 · خ32 · د20 · ذ20 · ر20 · ز18 · س24 · ش24 · ص23 · ض23 · ط19 · ظ19 · ع18 · غ18 · ف17 · ق17

## Coverage gate untuk halaman berikutnya
Mulai P010 dan seterusnya, setiap bank latihan harus mempunyai metadata QA:
- `introduced_page`
- `count_on_page`
- `last_seen_page`
- `pages_since_seen`
- `rolling_coverage`

### Hard gate yang disarankan
- Kompetensi lama yang sudah diperkenalkan tidak boleh mempunyai `pages_since_seen > 2` pada fase latihan fathah, kecuali halaman khusus/evaluasi memiliki aturan tersendiri.
- Untuk halaman regular, setiap review slot diprioritaskan kepada huruf dengan `pages_since_seen` terbesar dan frekuensi rolling terendah.
- `أ` dan `ء` tidak boleh digabung sebagai satu kategori statistik.
- TARGET tetap dominan; coverage review tidak boleh membuat fokus kompetensi baru hilang.
- Zero duplicate tetap wajib.

## Keputusan QA P001–P009
**COVERAGE AUDIT: PASS BERSYARAT untuk DATA v0.3.**

PASS berarti masalah hilangnya huruf lama dari rotasi P005–P009 sudah diperbaiki secara data. BERSYARAT berarti data belum boleh dirender menjadi buku final sebelum validator otomatis untuk `last_seen`/rolling coverage dibuat dan checkpoint P010 disusun secara curated.
