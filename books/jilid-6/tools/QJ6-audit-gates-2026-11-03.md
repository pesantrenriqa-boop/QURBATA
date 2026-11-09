# QURBATA Jilid 6 — Audit release gates (2026-11-03)

**Scope:** branch `work/qj6-register-9-slot-20261028`, register `books/jilid-6/tools/QJ6-slots.csv`. This document records evidence requirements; it does **not** authorize printing, change curriculum approvals, or verify any individual Quran glyph.

## Live register snapshot

- Total planned: 360 (40 pages × 9 slots).
- Filled: 335; EMPTY: 25.
- Filled entries are drafts/research records, not a certified publication-ready corpus.

| Page | EMPTY | Required gate |
|---|---:|---|
| QJ6-P017 | 7 | Direct MSI waqf-la glyph and placement proof |
| QJ6-P018 | 9 | Authorized Hafalan 1 unit list |
| QJ6-P036 | 9 | Approved P018 units + Hafalan 2/murojaah plan |

## P017 — waqf-la verification gate

1. Fix the **exact edition** of Mushaf Standar Indonesia used by QURBATA. A Quran.com or Madinah mark cannot substitute for MSI.
2. For each proposed example, record surah:ayah, source page/image or edition-specific official reference, the word immediately before the `لا` glyph, and word immediately after it.
3. Compare visual glyph placement against source, confirm the entire excerpt and Unicode/typography. In current CSV, P017-S02 and P017-S04 have secondary-source discussion but the `text_uthmani` field lacks an explicit `لا` waqf mark: **do not pass**.
4. Check whether stopping is semantically and pedagogically permissible, and confirm a safe restart (ibtida) with a qualified reviewer.
5. Review J1–J5 duplicates and competency prerequisites. Only then advance review status through human tashih; do not auto-set `source_verified=yes` or `competency_verified=yes`.

## P018 and P036 — hafalan approval gate

1. Obtain approved Jilid 6 hafalan syllabus listing each unit's surah and ayah range, sequence and approval authority.
2. P018: identify nine distinct approved slots or explicit review units; no arbitrary verses merely to fill quota.
3. P036: distinguish **new hafalan** from **murojaah**; where repeating P018, store a transparent source reference and repetition rationale.
4. Confirm exact Uthmani text against selected MSI edition, with competent teacher tashih and cross-volume duplication check.
5. Keep EMPTY while any gate fails. No printing from CANDIDATE or RESEARCH records.

## Official references and scope of evidence

- LPMQ's 2025 announcement of official Quran Kemenag API for MSI text: https://lajnah.kemenag.go.id/info-lpmq/berita-dan-artikel/berita/api-qur%E2%80%99an-kemenag-jadi-jembatan-digital-akses-mushaf-standar-indonesia.html
- LPMQ on MSI waqaf-ibtida, rasm and dhabt: https://lajnah.kemenag.go.id/info-lpmq/berita-dan-artikel/berita/diskusi-100-soal-jawab-penyusunan-buku-tanya-jawab-seputar-pentashihan-mushaf-al-qur-an.html
- LPMQ on the need to re-tashih even when using an approved master mushaf: https://lajnah.kemenag.go.id/info-lpmq/berita-dan-artikel/berita/lpmq-kemenag-sediakan-10-master-mushaf-al-qur-an-siap-cetak%2C-gratis.html

**Evidence limit:** These references establish the authoritative source and review process; they do **not** establish exact `لا` positions for any specific P017 verse or approve a memorization syllabus.
