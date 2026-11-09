## Source discovery warning — historical direct download (2026-11-09)

A public inventory of KFGQPC developer resources (quran-ws/kfgqpc-resources, `metadata/quran-dev.json`, captured 2026-09-07) records the publisher-hosted direct URL `https://download.qurancomplex.gov.sa/resources_dev/UthmanicHafs_v2-0.zip`. **Do not use this as the v15.0 source**: the inventory identifies it as **Hafs update 13.0 (last modified 2023-09-19)**, with computed SHA-256 `a7b0e5591945712ec5e4d6142938ae4d1e9b49bdc89dff06222789bfebdfd72c`. This is not the expected v15.0 SHA-256 `227e6b1564d980f2bd09c2c35ebfb0330ac268c79a7c247cd1ab665bc635f245`.

The inventory is a third-party historical index, not publisher authorization or evidence of current file availability. The v15.0 direct ZIP URL is **not yet identified or verified**. Retain the strict SHA-256 gate and 0/16 HOLD; do not infer a filename by changing the old URL.

## Alternative official platform URL (unverified download)

KFGQPC's own technology news page also advertises `https://qurancomplex.gov.sa/techquran/dev` as a developer platform entry point. It may be checked if `/quran-dev/` is under maintenance, but **the existence of the link or indexed product description does not establish a downloadable or authenticated ZIP**. Continue to require the original Hafs Unicode v15.0 package with SHA-256 `227E6B1564D980F2BD09C2C35EBFB0330AC268C79A7C247CD1AB665BC635F245`. No substitute packages, third-party mirrors, or print approval are permitted. Source: https://qurancomplex.gov.sa/category/%D8%AA%D9%82%D9%86%D9%8A%D8%A9/

# P022 — KFGQPC Hafs Unicode verification (read-only)

## Verified publisher metadata (2026-11-05)

- Official publisher: King Fahd Glorious Qur'an Printing Complex (KFGQPC).
- Publisher page: https://qurancomplex.gov.sa/quran-dev/
- Product: Unicode Uthmanic Font (Hafs Narration), update 15.0.
- Publisher's last modification date: 2026-09-30.
- Published SHA-256: `227E6B1564D980F2BD09C2C35EBFB0330AC268C79A7C247CD1AB665BC635F245`.
- Published dataset columns include `sura_no`, `aya_no`, and `aya_text_unicode`.
- **Scope:** The publisher's metadata and checksum have been checked against the official page. **The actual ZIP has not been downloaded, hashed, or matched against the register as part of this metadata check.**

## Critical product distinction

The official publisher lists **two different Hafs downloads** on the same page:

- **Unicode Uthmanic Font (Hafs Narration)**: update **15.0**, last modified **2026-09-30**, SHA-256 **227E6B1564D980F2BD09C2C35EBFB0330AC268C79A7C247CD1AB665BC635F245**. **This is the only expected archive for the P022 verifier.**
- **Unicode Uthmanic Font (Hafs Narration) for smart devices**: update **6.0**, last modified **2022-06-30**, and the publisher lists MD5/SHA-1 for this different package. **Do not substitute this archive**, even though it also has Quran verse text and developer CSV/JSON files.

The publisher page's listed checksum is **metadata, not evidence that a local download has passed hashing**. No third-party mirror or similarly named archive can satisfy the source gate without matching the published SHA-256.

## Official-site maintenance contingency

If the publisher's download page displays **Website Under Maintenance**, do not substitute a different Quran package or approve any slot based on an indexed/cached web page. The publisher's general contact page also lists **info@qurancomplex.gov.sa** (https://qurancomplex.gov.sa/contact/); this is an escalation contact only, not an alternate source of Quran text. The publisher's official Quran Hafs app guide lists **developer@qurancomplex.gov.sa** as a developer contact. Ask the publisher for the original **Unicode Uthmanic Font (Hafs Narration) update 15.0** archive and verify its SHA-256 against the publisher's published value before using it. Treat an email attachment or alternate link as **unverified until its downloaded bytes pass the same SHA-256 gate**. The main register and print approval must remain unchanged while the archive is unavailable.

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

## Windows PowerShell: archive integrity gate (before extraction)

On Windows, after obtaining the original publisher archive, run the following command in PowerShell (replace the path with the actual ZIP location):

```powershell
$archive = 'C:\\Users\\YOUR_USER\\Downloads\\official-hafs-v15.zip'
$expected = '227E6B1564D980F2BD09C2C35EBFB0330AC268C79A7C247CD1AB665BC635F245'
if (-not (Test-Path -LiteralPath $archive -PathType Leaf)) { throw 'Archive not found: no verification performed' }
$actual = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash
if ($actual -ne $expected) { throw "SHA-256 mismatch. Expected $expected; got $actual. STOP: do not extract or audit." }
Write-Output 'SHA-256 VERIFIED: archive matches published KFGQPC Hafs Unicode v15.0 digest.'
```

**Important:** This confirms only the ZIP bytes match the published checksum, not that P022 is approved for print. If the site is under maintenance or no ZIP is available, do not run the screening on a substitute. Keep all slots HOLD until the dataset is verified and independently reviewed.

## Per-slot evidence checklist (not yet verified)

This table is a **tracking checklist**, not a transcription of Quran text. Every slot requires exact source matching and independent human tashih before any approval.

| Slot | Expected QS | Official ZIP SHA-256 verified | Exact Unicode substring | Independent tashih | Print status |
|---|---|---|---|---|---|
| K01 | 105:4 | PENDING | PENDING | PENDING | HOLD |
| K02 | 88:22 | PENDING | PENDING | PENDING | HOLD |
| K03 | 50:45 | PENDING | PENDING | PENDING | HOLD |
| K04 | 6:107 | PENDING | PENDING | PENDING | HOLD |
| K05 | 2:8 | PENDING | PENDING | PENDING | HOLD |
| K06 | 34:8 | PENDING | PENDING | PENDING | HOLD |
| K07 | 83:17 | PENDING | PENDING | PENDING | HOLD |
| K08 | 29:22 | PENDING | PENDING | PENDING | HOLD |
| K09 | 21:27 | PENDING | PENDING | PENDING | HOLD |
| K10 | 2:167 | PENDING | PENDING | PENDING | HOLD |
| K11 | 2:102 | PENDING | PENDING | PENDING | HOLD |
| K12 | 11:19 | PENDING | PENDING | PENDING | HOLD |
| K13 | 7:45 | PENDING | PENDING | PENDING | HOLD |
| K14 | 27:3 | PENDING | PENDING | PENDING | HOLD |
| K15 | 6:150 | PENDING | PENDING | PENDING | HOLD |
| K16 | 21:36 | PENDING | PENDING | PENDING | HOLD |

Never mark a row approved from CI unit tests alone. Attach the checker report with archive, dataset, and register hashes; review each failed slot individually without silently normalizing Quranic Unicode.

## Release gate

- A successful offline unit-test run proves only checker behavior with synthetic fixtures.
- A successful exact-Unicode substring screening proves only text matching for the supplied verified source.
- Neither outcome approves rasm, tajwid, pedagogy, nor printing.
- **All 16 P022 slots remain HOLD; print-approved 0/16 until independent verification and tashih are completed.**
