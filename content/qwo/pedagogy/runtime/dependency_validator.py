#!/usr/bin/env python3
from __future__ import annotations
import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass
class GraphResult:
    valid: bool
    errors: list[str]
    order: list[str]

def load_dependencies(path: str|Path):
    with open(path, encoding="utf-8", newline="") as f:
        rows=list(csv.DictReader(f))
    return {r["CompetencyID"]:[x for x in r["PrerequisiteIDs"].split("|") if x] for r in rows}

def validate_graph(graph: dict[str,list[str]]) -> GraphResult:
    errors=[]
    nodes=set(graph)
    for node,deps in graph.items():
        for dep in deps:
            if dep not in nodes: errors.append(f"MISSING:{node}->{dep}")
    state={}; order=[]
    def visit(n,trail):
        if state.get(n)==1:
            errors.append("CYCLE:"+"->".join(trail+[n])); return
        if state.get(n)==2:return
        state[n]=1
        for d in graph.get(n,[]): visit(d,trail+[n])
        state[n]=2; order.append(n)
    for n in graph: visit(n,[])
    return GraphResult(not errors,errors,order)

def prerequisites_satisfied(competency_id: str, mastered: set[str], graph) -> bool:
    return all(dep in mastered for dep in graph.get(competency_id,[]))
