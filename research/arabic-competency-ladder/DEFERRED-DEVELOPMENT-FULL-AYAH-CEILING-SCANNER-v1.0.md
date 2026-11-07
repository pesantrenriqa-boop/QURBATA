# Deferred Development — Full-Ayah Ceiling Scanner v1.0

**Status:** DEFERRED / POST-OPENING DEVELOPMENT  
**Reason:** owner priority is immediate program opening. This feature is useful but is not an opening blocker.

## Preserved idea

Future engine should support queries such as:
- find full Qur'anic ayat whose required competency ceiling is <= Kn;
- optionally require a target competency Kx inside that ayah;
- reject ayat containing any required feature above the requested ceiling;
- rank surviving ayat from easier to harder;
- distinguish `target-example mode` (a span may instantiate Kx) from `full-ayah ceiling mode` (the whole ayah must remain within the ceiling).

Example request:

```json
{
  "target": "K10",
  "ceiling": "K10",
  "unit": "full_ayah",
  "count": 20,
  "future_features": "reject"
}
```

## Important requirement discovered during proof test

Ceiling validation must inspect **both morphology/token features and syntactic/relational structure**. A verse must not pass merely because its individual word categories look elementary.

## Re-entry condition

Do not resume this work before opening unless it becomes necessary for a concrete opening deliverable. Resume after opening under generator/corpus enhancement work.

## Core project impact

None. Arabic Competency Ladder / Generator Core v1.0 remains functionally closed. This scanner is an optional enhancement and does not reopen K01–K67.