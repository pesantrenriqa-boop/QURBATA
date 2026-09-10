# L19 Canonical Function Matrix — K41–K57 v1.0

**Status:** FUNCTION-LEVEL REALIGNMENT — NOT PRODUCTION ENABLED  
**Checkpoint:** L19  
**Authoritative band:** K41–K57  
**Historical source:** L19 P01–P36 (R0 full)

## 1. Rule

Coverage credit is based on the canonical learner operation, not numerical similarity between an old target label and the recovered authoritative K number.

Actions:
- **KEEP** — historical item directly instantiates the canonical function.
- **REMAP** — historical item is useful but belongs to a different canonical K than its legacy label.
- **REWRITE** — verse/function can be retained but prompt/rubric must be rewritten.
- **NEW** — no surviving L19 item defensibly instantiates the canonical function.

All items remain `production_enabled=false`.

## 2. Matrix

| K | Canonical function | Best surviving candidate | Function verdict | Action |
|---|---|---|---|---|
| K41 | Recover basic hidden fa'il in simple active verb | none in L19 bank isolates hidden fa'il as target | Missing | **NEW** |
| K42 | Identify isim maushul and delimit minimal silah | P03 `الذين أنعمت عليهم`; also P15 `الذين يؤمنون...` | Strong direct match if rubric stops at silah boundary | **REMAP/KEEP-AS-K42** |
| K43 | Identify overt `عائد` inside silah and link to maushul | P03 `الذين أنعمت عليهم` with `هم` in `عليهم` | Viable explicit return-link example; old P03 label K42 only partially described this | **REWRITE/REMAP-AS-K43 alternate** |
| K44 | Identify emphatic lām inside mastered simple `إنّ` frame | none | Missing | **NEW** |
| K45 | Recover one locally omitted resumptive slot in simple relative construction | none of P01–P36 explicitly requires omitted-`عائد` recovery | Missing | **NEW** |
| K46 | Identify short verbal clause as khabar of explicit mubtada' with mastered local link | none isolated cleanly; old P07/P24 concern other structures | Missing | **NEW** |
| K47 | Delimit conditional marker, condition clause, response clause, and condition→result dependency | P14 QS 3:160; P20 QS 4:59; P02 QS 110 | Direct canonical match after relabeling | **REMAP/KEEP-AS-K47** |
| K48 | Classify overt `فـ` as فاء جواب الشرط and mark response onset | P14/P20 explicitly identify result `فـ` | Strong candidate but prompt must explicitly classify `فاء جواب الشرط`, not merely generic result marker | **REWRITE/REMAP-AS-K48** |
| K49 | Connect transparent final sukūn on mudhari' to local jazm | none; existing conditional items focus relation, not mood sign | Missing | **NEW** |
| K50 | Reconstruct deleted final weak segment as jazm effect | none | Missing | **NEW** |
| K51 | Detect deletion of expected inflectional nūn as jazm effect | none; old P13 is conditional-domain analysis, not delete-nūn morphology | Missing | **NEW** |
| K52 | Connect overt nāṣib + transparent final fatḥah to nasb | none; old P14 is condition-result, not nasb morphology | Missing | **NEW** |
| K53 | Reconstruct validated hidden `أن` and connect it to nasb | none; old P15 is relative-clause integration | Missing | **NEW** |
| K54 | Predict fā' for nominal conditional response, then verify it | P14 QS 3:160 `فلا غالب لكم` | Good environment because response is nominal; old prompt only maps relation, so prediction rule must be added | **REWRITE/REMAP-AS-K54** |
| K55 | Identify visible ḍammah as raf' where no active nāṣib/jāzim applies | none explicitly targets mood environment + visible ḍammah | Missing | **NEW** |
| K56 | Identify retained inflectional nūn as raf' sign | P04/P15 contain forms such as `يؤمنون/يقيمون`, but old scoring tests coordination/relative scope rather than raf' by thubūt al-nūn | Verse material reusable, target not yet present | **REWRITE** |
| K57 | Identify estimated ḍammah as raf' on familiar weak-final mudhari' | none | Missing | **NEW** |

## 3. Canonical coverage count after function audit

Defensible direct/repairable coverage candidates:
- K42 ✓ candidate
- K43 ✓ candidate with rewrite
- K47 ✓ candidate
- K48 ✓ candidate with rewrite
- K54 ✓ candidate with rewrite
- K56 ✓ verse material candidate with rewrite

**Functionally represented or repairable from surviving bank: 6/17 = 35.29%.**

Canonical nodes requiring genuinely new item construction:
- K41
- K44
- K45
- K46
- K49
- K50
- K51
- K52
- K53
- K55
- K57

**NEW required: 11/17 = 64.71%.**

This percentage supersedes any earlier inference that old L19 numbering provided full K41–K57 coverage.

## 4. Historical items reclassified

Examples of important remaps:
- old P02 `condition-result` is **not K41**; it belongs primarily to K47 and can support K48 after rewrite.
- old P03 `embedded relative` can support K42 and, with explicit return-link scoring, K43.
- old P14 `condition-result transfer` is **not K52**; it is a strong K47/K48 environment and a potential K54 environment.
- old P15 `relative inside larger clause` is **not K53**; it supports K42 transfer.
- old P16 `fronting scope` is **not K54**; its legacy target is out of canonical function and it should remain a diagnostic rather than K54 evidence.
- old P17 `complexity negative control` is **not K55**.
- old P18/P19 capstone/routing items are **not K56/K57 evidence** merely because of their old labels.

## 5. Repair execution order

### Repair A — prerequisite/dependency cluster
Create new items for K41, K44, K45, K46.

### Repair B — mood morphology cluster
Create new items for K49, K50, K51, K52, K53, K55, K57 and rewrite K56 using a clean nūn-bearing mudhari' environment.

### Repair C — reuse verified conditional/relative environments
- K42 from P03/P15;
- K43 rewrite from P03 or another explicit `عائد` span;
- K47 from P14/P20;
- K48 rewrite P14/P20;
- K54 rewrite P14 with nominal response prediction.

## 6. Completion definition

L19 reaches 100% **draft canonical coverage** only when every K41–K57 row has at least one explicit item whose prompt and scoring key directly instantiate that K operation.

Historical pool size remains 36/36 and is not reduced. New repair items may increase the research bank beyond the historical 180 slots; this is acceptable because canonical correctness takes precedence over preserving an arbitrary item count.

## 7. Decision

**L19 canonical functional coverage after audit: 6/17 repairable/represented = 35.29%; 11/17 require NEW items.**

Proceed to targeted canonical repair rather than relabeling legacy items by number.