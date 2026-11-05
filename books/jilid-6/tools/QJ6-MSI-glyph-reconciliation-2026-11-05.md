# QJ6 — MSI glyph reconciliation checklist (2026-11-05)

## Official reference

LPMQ, *Pedoman Pentashihan Mushaf Al-Qur'an*, p.109, Table 39, enumerates six MSI waqf categories. Official PDF: https://tashih.lpmqkemenag.id/uploads/1/2019-12/buku_pedoman_pentashihan_mushaf_al_quran.pdf

The LPMQ FAQ also discusses six MSI marks: https://tashih.lpmqkemenag.id/uploads/1/2019-12/buku_tanya_jawab_tentang_mushaf_fth.pdf . Other LPMQ historical articles discuss seven categories in the 1980 simplification, including saktah. Do not conflate this historical discussion with the six-item Table 39. **Neither document supplies verified verse-specific placement for the three items below.**

## Exact Unicode present in the existing register

| Slot | Verse | Register sign | Unicode code point | Online evidence | Official MSI verse-level match |
|---|---|---|---|---|---|
| QJ6-P015-S01 | 6:36 | ۘ | U+06D8 | Prior Quran.com sign-position evidence recorded | PENDING |
| QJ6-P015-S06 | 10:65 | ۘ | U+06D8 | Prior Quran.com sign-position evidence recorded | PENDING |
| QJ6-P016-S03 | 61:7 | ۚ | U+06DA | Prior Quran.com sign-position evidence recorded | PENDING |

Unicode extraction is a mechanical observation of the register, **not** proof of MSI sign equivalence or a waqf ruling. Do not substitute a look-alike sign automatically.

## Evidence gate for each slot

1. Fix the RIQA reference mushaf edition and obtain its page image for the complete verse.
2. Record exact word before the sign, official MSI sign as printed, and whether the sign is at a verse boundary.
3. Compare against the register glyph at code-point level; note font and edition-specific rendering.
4. Assess the grammatical/semantic safety of stopping and restarting; name the precise stop and restart words.
5. Have a qualified reviewer sign off with date and source image/page reference.
6. Only then propose any change to CSV verification flags or Quranic text.

**Disposition:** all three remain CANDIDATE; no source or competency flag changed; no print approval. Register remains 335 filled / 25 EMPTY.
