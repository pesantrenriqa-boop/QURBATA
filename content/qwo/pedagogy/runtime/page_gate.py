#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class PageDecision:
    passed: bool
    errors: list[str]

def validate_page(objects, target_competency, mastered, graph, object_validator, used_keys):
    errors=[]
    if not all(dep in mastered for dep in graph.get(target_competency,[])):
        errors.append("PREREQUISITE_NOT_MASTERED")
    local=set()
    for i,obj in enumerate(objects,1):
        key=obj["canonical_key"]
        if key in used_keys or key in local:
            errors.append(f"DUPLICATE_OBJECT:{i}:{key}")
        local.add(key)
        decision=object_validator(obj["text"],obj["object_type"],target_competency)
        if not decision.passed:
            errors.append(f"OBJECT_REJECTED:{i}:{'|'.join(decision.reasons)}")
        if not obj.get("source_ref"):
            errors.append(f"MISSING_SOURCE:{i}")
    return PageDecision(not errors,errors)
