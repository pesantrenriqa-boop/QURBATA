#!/usr/bin/env python3
"""Compose QURBATA page object plans from labelled Quran objects.

V1 rules:
- competency order controls selection;
- canonical objects are never repeated as primary objects;
- review repeats competencies through different Quran objects;
- object scope must match the requested page stage;
- output remains a draft page plan, not print-ready content.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PageRequest:
    page_number: int
    target_competency: str
    review_competencies: tuple[str, ...]
    object_scope: str
    object_count: int


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def matches(row: dict[str, str], competency: str) -> bool:
    secondary = set(filter(None, row.get("SecondaryCompetencyIDs", "").split("|")))
    return row.get("PrimaryCompetencyID") == competency or competency in secondary


def select_objects(
    rows: list[dict[str, str]],
    competencies: tuple[str, ...],
    needed: int,
    consumed: set[str],
) -> list[dict[str, str]]:
    candidates = [
        row for row in rows
        if row.get("CanonicalKey") not in consumed
        and any(matches(row, competency) for competency in competencies)
        and row.get("Status", "CANDIDATE") == "CANDIDATE"
    ]
    candidates.sort(
        key=lambda row: (
            float(row.get("DifficultyScore") or 999),
            -int(float(row.get("OccurrenceCount") or 0)),
            row.get("SourceRef", ""),
            row.get("QWO_ID", ""),
        )
    )
    selected = candidates[:needed]
    consumed.update(row["CanonicalKey"] for row in selected)
    return selected


def compose(
    rows: list[dict[str, str]],
    requests: list[PageRequest],
) -> list[dict[str, str]]:
    consumed: set[str] = set()
    output: list[dict[str, str]] = []

    for request in requests:
        target_count = max(1, round(request.object_count * 0.6))
        review_count = request.object_count - target_count

        chosen = select_objects(
            rows,
            (request.target_competency,),
            target_count,
            consumed,
        )
        if review_count and request.review_competencies:
            chosen.extend(
                select_objects(
                    rows,
                    request.review_competencies,
                    review_count,
                    consumed,
                )
            )

        if len(chosen) < request.object_count:
            raise ValueError(
                f"Page {request.page_number}: only {len(chosen)} of "
                f"{request.object_count} unique objects available"
            )

        for position, row in enumerate(chosen, start=1):
            output.append({
                "PageNumber": str(request.page_number),
                "Position": str(position),
                "ObjectScope": request.object_scope,
                "TargetCompetencyID": request.target_competency,
                "ReviewCompetencyIDs": "|".join(request.review_competencies),
                "QWO_ID": row["QWO_ID"],
                "ArabicObject": row["ArabicWord"],
                "CanonicalKey": row["CanonicalKey"],
                "SourceRef": row["SourceRef"],
                "PrimaryCompetencyID": row["PrimaryCompetencyID"],
                "SecondaryCompetencyIDs": row.get("SecondaryCompetencyIDs", ""),
                "Status": "DRAFT_SELECTED",
            })
    return output


def read_plan(path: Path) -> list[PageRequest]:
    requests: list[PageRequest] = []
    for row in read_rows(path):
        requests.append(PageRequest(
            page_number=int(row["PageNumber"]),
            target_competency=row["TargetCompetencyID"],
            review_competencies=tuple(filter(None, row.get("ReviewCompetencyIDs", "").split("|"))),
            object_scope=row["ObjectScope"],
            object_count=int(row["ObjectCount"]),
        ))
    return requests


def write_output(path: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ValueError("Composer produced no rows")
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("labelled_qwo", type=Path)
    parser.add_argument("page_plan", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    write_output(args.output, compose(read_rows(args.labelled_qwo), read_plan(args.page_plan)))


if __name__ == "__main__":
    main()
