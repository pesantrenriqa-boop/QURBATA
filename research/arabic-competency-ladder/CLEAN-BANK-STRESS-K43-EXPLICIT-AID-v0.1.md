# Clean Bank + Stress Test K43 — Explicit `عائد` v0.1

**Status:** WORKING RESEARCH — PRE-FREEZE  
**Baseline:** K1–K42 DRAFT-FROZEN.

## Objective

Validate that K43 can remain atomic as **identifying an explicit resumptive element inside a simple silah and linking it back to the isim maushul**, without importing omitted-resumptive theory or new clause structures.

## Role families audited

### A. Explicit resumptive as attached object pronoun

Pattern:
`اسم موصول` → silah with verb + attached object pronoun referring back to the maushul.

Dependency check:
- object suffix relation is already frozen;
- maushul boundary is frozen at K42;
- new operation is only co-reference back to the maushul.

**Status:** STRONG PASS when morphology and clause are otherwise simple.

### B. Explicit resumptive inside jar–majrur

Pattern:
`اسم موصول` → silah containing preposition + attached pronoun referring back to the maushul.

Dependency check:
- preposition + attached pronoun relation already frozen;
- PP attachment must remain within prior scope;
- new operation is the local co-reference.

**Status:** PASS if PP attachment is unambiguous and cumulative-clean.

### C. Explicit resumptive as mudaf ilayh suffix

Pattern:
`اسم موصول` → silah containing noun + attached possessive/genitive pronoun referring back to the maushul.

Dependency check:
- attached pronoun as mudaf ilayh is already frozen;
- idafah relation must be clean;
- co-reference is the only new operation.

**Status:** PASS if no additional nominal embedding is required.

### D. Explicit resumptive as subject-like overt pronoun

Potentially simple on the surface, but may overlap with discourse emphasis, detached pronoun syntax, or clause topic structure.

**Status:** REVIEW unless occurrence parsing is fully transparent.

## Failure modes

Exclude from core K43 when:
- resumptive is omitted/estimated;
- multiple pronouns compete as possible antecedent links;
- nested maushul appears;
- silah contains conditional structure;
- pronoun role itself needs a later K;
- local co-reference cannot be determined without broad discourse context;
- the example requires advanced ellipsis or semantic reconstruction.

## Stress-test result

K43 survives distinctness and dependency testing.

The competence is independently assessable from K42:
- K42 assessment: identify maushul and silah boundary.
- K43 assessment: identify the overt element inside that silah that refers back to the maushul.

No dependency reversal was found. Omitted `عائد` is not a prerequisite for explicit `عائد` recognition.

## Clean-bank policy

Preferred order of teaching evidence:
1. explicit attached object pronoun;
2. explicit pronoun after preposition;
3. explicit possessive/genitive suffix;
4. other overt roles only after separate role audit.

This order maximizes reuse of already-frozen competencies and minimizes new inference burden.

## Final gate recommendation

**READY FOR DRAFT-FREEZE** with the title:

**K43 — Mengidentifikasi `عائد` eksplisit dalam silah maushul sederhana.**

Locked for later:
- omitted `عائد`;
- deletion conditions;
- disputed resumptive analyses;
- nested relative constructions;
- advanced co-reference.

## Next frontier

After K43 freeze, rescan K44 among:
- emphatic lām in simple `إنّ` construction;
- omitted `عائد` recognition/reconstruction;
- simple conditional relation;
- other structural operations revealed by corpus evidence.

Do not assign K44 automatically.