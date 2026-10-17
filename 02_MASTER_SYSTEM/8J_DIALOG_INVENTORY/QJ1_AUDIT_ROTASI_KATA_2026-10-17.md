# Audit rotasi kata Jilid 1 — 17 Oktober 2026

Status: **BELUM FINAL**. Pemeriksaan terhadap inventaris pada commit 810b19e.

- Semua 40 halaman mempunyai 24 kelompok latihan.
- P001: 12 kelompok unik, pengulangan sengaja karena hanya 3 huruf.
- P002–P040: 24 kelompok unik **di dalam tiap halaman**, tetapi kata masih berulang lintas halaman.
- Frekuensi lintas halaman paling tinggi: خَ سِ رَ (14), جَ عَ لَ (13), جَ لَ سَ (13), سَ جَ دَ (13), شَ كَ رَ (13), صَ بِ رَ (13), طَ لَ بَ (13), قَ دِ رَ (13), نَ دِ مَ (13), نَ صَ رَ (13).

## Gate kurasi berikutnya

1. Inventaris **50 kandidat** tidak mencukupi untuk menghasilkan 24 latihan bervariasi × 27 halaman tanpa pengulangan tinggi.
2. Bedakan **kata Qur'ani terverifikasi**, **kata Arab bermakna yang belum dibuktikan dalam mushaf**, dan **rangkaian fonetik**.
3. Tidak boleh memperbanyak daftar dengan mengarang bentuk kata atau menyatakan bentuk pasif otomatis bermakna Qur'ani.
4. Catat surah:ayat untuk setiap bentuk yang diberi label Qur'ani dan periksa harakat tepat, bukan akar kata saja.
5. Setelah sumber bertambah, lakukan rotasi dengan batas pengulangan dan review pedagogis terencana; pertahankan 24 kelompok dan whitelist halaman frozen.

**Keputusan:** audit jumlah/keunikan dalam halaman lulus, tetapi gate kekayaan leksikal dan bukti Qur'ani belum lulus.


## Audit ulang sesudah commit c334f08

- 40 halaman × 24 = **960 kelompok**; tidak ditemukan kompetensi harakat prematur pada kelompok yang diperiksa.
- Rotasi sebelumnya **belum berhasil menurunkan pengulangan global**: جَ عَ لَ 16 kali; سَ جَ دَ 15 kali; شَ رِ بَ 15 kali; لَ عِ بَ 15 kali.
- Penyebab: pool kata terbatas dan algoritme masih mengisi kekurangan dari kata lama, sehingga kata bermakna berulang. Klaim bahwa variasi sudah memadai **ditolak**.
- **Tindakan berikutnya yang sah:** perluasan bank kata dengan attestasi sumber, penyaringan sesuai whitelist harakat per halaman, kemudian penggantian contoh repetitif dan audit ulang metrik global. Jangan mengarang kata baru hanya untuk mengejar angka.
