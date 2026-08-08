# QURBATA Jilid 1 — Layout Freeze V22

Status: FROZEN
Scope: Jilid 1 production reading pages
Effective layout baseline: V22 / optical collision-safe renderer

## Frozen geometry

The following parameters are locked for subsequent Jilid 1 production pages and must not be changed without a new layout version and visual QA:

- Practice font: 36 pt
- Focus/new-material font: 44 pt
- Pair outer box: 28 mm, 4 columns
- Pair internal token cell: 14 mm
- Triple outer box: 36 mm, 3 columns
- Triple internal token cell: 12 mm
- Triple rows: 5
- Triple row gap: 5.5 mm
- Horizontal placement: Canvas ink-bounds optical alignment
- Wide-glyph handling: collision-safe horizontal fitting only
- Reading direction: RTL
- Letters in Jilid 1 remain disconnected

## Allowed micro refinements after freeze

Only the following are permitted without creating a new major layout version:

1. Harakat micro-offsets that do not alter grid geometry or horizontal anchors.
2. Display-form correction for a single isolated letter glyph while canonical source data remains unchanged.
3. Footer typography/readability adjustments inside the existing lower information zone.
4. Special-page (20/40) clipping-safe adjustments that do not change reading-page geometry.
5. Bug fixes to validation where the intended frozen geometry is unchanged.

## Current scoped refinements

- Dammah: moved slightly downward toward its own base to avoid contact with the kasrah/marks in the row above.
- Kasrah: moved slightly upward toward its own base.
- Isolated heh display: two-eye form (U+06BE) for Jilid 1 print rendering only; canonical curriculum/source token remains semantically unchanged.
- Footer information text enlarged slightly and raised from the bottom rule.
- Pages 20 and 40: letter/name cards receive additional vertical breathing room so the card border does not visually cut the glyph.

## Validation contract

A production candidate must continue to pass:

- 40 pages rendered
- 722 reading objects
- 28 letter-name objects
- optical alignment present on all reading glyphs
- collision validation after final horizontal fit
- layout overflow = 0
- renderer = PASS

Any change that modifies the frozen grid requires a new explicit version (V23+ layout), comparison render, and human visual QA before freeze.
