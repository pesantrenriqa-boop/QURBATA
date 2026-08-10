# JILID 2 — Three-Letter Semantic Lexeme Policy V1

Status: ACTIVE
Scope: QURBATA Jilid 2 and subsequent pages that use three-letter Arabic practice objects.

## Core rule

Every three-letter practice example MUST be a meaningful Arabic lexeme, not an arbitrary pronounceable combination.

A three-letter object is eligible only when all of the following are true:

1. The object consists of exactly three Arabic base letters after harakat/combining marks are removed.
2. The form is an attested/recognized Arabic lexical form with a documented meaning.
3. Its meaning is recorded in the page lexical registry (`meaning_id` or equivalent semantic field).
4. The object uses only letters and orthographic features already allowed by the current competency boundary.
5. A meaningful word MUST NOT be used when it leaks a letter, harakat, joining pattern, mad, tanwin, sukun, shaddah, or other feature that has not yet been acquired.
6. When several meaningful words are available, prefer common, pedagogically clear, Qur'anic/classical, or high-transfer vocabulary over rare forms.
7. Murojaah examples are subject to the same semantic requirement.

## Priority order

Competency sequence > orthographic legality > semantic validity > lexical familiarity > visual variety.

Meaning never overrides the competency staircase. If no suitable meaningful lexeme exists inside the current boundary, the page design/content allocation must be adjusted rather than inventing a meaningless three-letter string.

## Required page diagnostics

Every Jilid 2 page renderer that contains three-letter objects must report:

- `THREE_LETTER_SEMANTIC_POLICY=REQUIRED`
- `THREE_LETTER_OBJECTS=<count>`
- `THREE_LETTER_WITH_MEANING=<count>`
- `MEANINGLESS_THREE_LETTER_OBJECTS=0`
- `COMPETENCY_LEAKAGE=0`

Any page with a three-letter practice object lacking documented Arabic meaning MUST fail its lexical gate and MUST NOT be frozen.
