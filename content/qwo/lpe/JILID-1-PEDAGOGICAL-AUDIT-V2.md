# QURBATA Jilid 1 — Pedagogical Audit V2

Status: **REVIEW CANDIDATE — NOT FINAL BOOK CONTENT**

## Evidence from Composer V3 audit

The current LPE gate passes structurally, but the generated distribution still contains pedagogical problems that must be corrected before rendering.

### 1. Page 20 and page 40 are not yet true special pages

Current output still places 24 reading objects on both pages while merely attaching `LETTER_NAMES` metadata.

Decision:

- page 20 MUST be a `LETTER_NAMES` special-content page, not a normal 24-reading-slot page;
- page 40 MUST be a `LETTER_NAMES` special-content/final-review page, not a normal 24-reading-slot page;
- reading-object rows on these pages MUST be zero unless a later explicit pedagogical decision changes this rule;
- letter-name content MUST come from an explicit registry, not from Quran-object selection.

### 2. Review progression is too coarse

Current pages 1–4 are 24/24 NEW with no review. Pages 31–40 are almost entirely REVIEW. This is mechanically valid but not yet an approved QURBATA progression.

Decision:

- the composition matrix remains `REVIEW_CANDIDATE`;
- new/review ratios require explicit pedagogical approval;
- the engine must support cumulative review without forcing long blocks of 100% NEW or 100% REVIEW unless the page role explicitly requires it.

### 3. Single-letter pool is too permissive for Jilid 1

Audit output contains forms such as `ىَ`, `ىُ`, `ىِ` and later fragment forms beginning with bare hamzah. These may be Unicode-valid and corpus-derived but are not automatically appropriate as early Jilid 1 teaching units.

Decision:

- Jilid 1 MUST use an explicit canonical-letter registry;
- the Pedagogical Unit Engine may remain Unicode-aware, but the LPE/Composer must additionally filter by the Jilid 1 teaching registry;
- technical validity MUST NOT be treated as pedagogical admissibility.

### 4. Competency descriptions are too terse

Current descriptions such as `Fathah`, `Kasrah`, `Dhammah`, and `Tiga huruf` are insufficient for production display.

Decision:

Production metadata must use human-readable descriptions such as:

- `C0002 — Membaca huruf tunggal berharakat fathah`;
- `C0003 — Membaca huruf tunggal berharakat kasrah`;
- `C0004 — Membaca huruf tunggal berharakat dhammah`;
- `C0005 — Membaca dua unit huruf dengan pola non-connector sesuai tahap Jilid 1`;
- `C0006 — Membaca dua unit huruf tersambung sesuai tahap Jilid 1`;
- `C0007 — Membaca objek tiga unit berharakat pendek sesuai tahap Jilid 1`.

### 5. Harakat typography remains unresolved

The current renderer is technically functional but the vowel marks are not final-production quality.

Decision:

Harakat rendering requires a separate typography gate covering recognizable shape, stroke weight, anchor placement, and visual distinction of fathah/kasrah/dhammah before final book freeze.

## Anti-regression rules to add

A Jilid 1 production candidate must fail if:

- page count is not 40;
- Awailus Suwar appears;
- page 20 or 40 contains normal reading rows while configured as `LETTER_NAMES_ONLY`;
- an L1/L2 object uses a base form outside the approved Jilid 1 canonical-letter registry;
- a competency code is printed with only a terse label instead of a production description;
- the composition matrix is treated as final without pedagogical approval;
- harakat typography has not passed visual QA.

## Current status

The V3 Composer/LPE gate is a **structural success**, not a final pedagogical approval. The next build must implement special-only pages 20/40, canonical-letter filtering, production competency descriptions, and revised review distribution before visual rendering resumes.
