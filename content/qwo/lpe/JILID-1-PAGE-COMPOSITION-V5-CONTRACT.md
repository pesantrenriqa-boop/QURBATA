# QURBATA Jilid 1 — Page Composition v5 Contract

Status: **REVIEW CANDIDATE — supersedes the 8-L1/8-L2/8-L3 visual composition for Jilid 1**

## Reading-page visual structure

Every ordinary reading page uses six instructional rows:

1. **Row 1 — New Material Focus**: one full-width material-focus slot. It presents only the current/new material and is visually slightly larger than the practice text.
2. **Row 2 — New Material Pair Habituation**: four practice slots. Each slot contains exactly two independent Arabic letter-units. This row is dedicated to the current/new material.
3. **Rows 3–6 — Triple Practice**: twelve practice slots arranged as 3 columns × 4 rows. Each slot contains exactly three independent Arabic letter-units.

Pages 20 and 40 remain dedicated `LETTER_NAMES` pages.

## Arabic shaping

Jilid 1 remains fully disconnected:

- every Arabic letter-unit is rendered independently;
- no joining or contextual Arabic shaping may occur between units;
- visible inter-unit gap is minimal (`DISCONNECTED_NO_SPACE`);
- the renderer MUST use `Unit1`, `Unit2`, and `Unit3`, never shape the audit string as a word.

## Typography

- All practice units in Row 2 and Rows 3–6 use **one identical Arabic font size**.
- The size must be the largest safe size that passes geometric containment/overflow validation.
- Row 1 current/new material may be slightly larger than the common practice size.
- Pair objects and triple objects MUST NOT use different font sizes merely because their unit lengths differ.

## Current material

If `NewLetters` is non-empty, current material is those newly introduced letters under the page's current harakat stage.

If `NewLetters` is empty, current material is the page's current harakat competency (`KASRAH`, `DHAMMAH`, or `MIXED`) applied to already active letters.

## Cumulative review

The governing 50:50 rule remains in force across the **16 exercise slots** of a reading page after the foundation page:

- 8 current/new competency objects;
- 8 cumulative-review objects.

Because Row 2 contains four current/new pair objects, Rows 3–6 contain:

- 4 current/new triple objects;
- 8 cumulative-review triple objects.

Page 1 is a foundation exception because no earlier competency exists.

Review means prior competency with fresh surface combinations where possible; it does not mean copying the exact same example.

## Hard failures

A production build fails if:

- an ordinary reading page does not contain exactly 4 pair objects + 12 triple objects;
- Row 2 contains review/future material;
- Rows 3–6 do not satisfy the required current/review distribution after page 1;
- practice font sizes differ by unit length;
- Arabic units join contextually;
- a future letter appears before activation;
- pages 20 or 40 contain ordinary reading objects;
- layout containment fails.
