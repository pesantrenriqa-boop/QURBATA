# P022 — KFGQPC Hafs Unicode verification (read-only)

## Verified publisher metadata (2026-11-05)

- Official publisher: King Fahd Glorious Qur'an Printing Complex (KFGQPC).
- Publisher page: https://qurancomplex.gov.sa/quran-dev/
- Product: Unicode Uthmanic Font (Hafs Narration), update 15.0.
- Publisher's last modification date: 2026-09-30.
- Published SHA-256: `227E6B1564D980F2BD09C2C35EBFB0330AC268C79A7C247CD1AB665BC635F245`.
- Published dataset columns include `sura_no`, `aya_no`, and `aya_text_unicode`.
- **Scope:** The publisher's metadata and checksum have been checked against the official page. **The actual ZIP has not been downloaded, hashed, or matched against the register as part of this metadata check.**

## Safe local procedure

1. Obtain the **Hafs Unicode version 15.0** archive directly from the official publisher page above. Do not use a mirror or a similarly named Hafs product.
2. Keep the original ZIP unmodified. Compute its SHA-256 and require the exact published digest above.
3. Extract the developer dataset from that same ZIP (CSV or JSON containing the three required columns). Preserve its original bytes.
4. Run the read-only screening command, replacing the placeholders with the actual paths:

```bash
python tools/audit_p022_hafs_unicode.py \
  --archive /path/to/official-hafs-v15.zip \
  --data /path/to/extracted-verses.csv \
  --register 02_MASTER_SYSTEM/BANK_REFERENSI_PER_KOMPETENSI/REGISTER_24_KELOMPOK_JILID_4.md \
  --output /path/to/new-p022-screening-report.json
```

5. Inspect all 16 slot statuses, preserve the generated report and checksums, and conduct independent human tashih against the authoritative mushaf.

## Release gate

- A successful offline unit-test run proves only checker behavior with synthetic fixtures.
- A successful exact-Unicode substring screening proves only text matching for the supplied verified source.
- Neither outcome approves rasm, tajwid, pedagogy, nor printing.
- **All 16 P022 slots remain HOLD; print-approved 0/16 until independent verification and tashih are completed.**
