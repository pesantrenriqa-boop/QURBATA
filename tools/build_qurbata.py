#!/usr/bin/env python3
"""Validated production entry point for the QURBATA book renderer."""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

from object_engine import load_competency, prepare_page

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"YAML_NOT_FOUND: {path}")
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"YAML_ROOT_MUST_BE_MAPPING: {path}")
    return data


def validate_book(book_dir: Path) -> int:
    tokens = load_yaml(book_dir / "layout/design-tokens.yaml")
    rendering = tokens.get("arabic_rendering", {})
    if rendering.get("engine") != "QAE":
        raise ValueError("QAE_ENGINE_REQUIRED")
    if rendering.get("mark_renderer") != "inline-svg-path":
        raise ValueError("QAE_INLINE_SVG_PATH_REQUIRED")

    pages = sorted((book_dir / "data").glob("page-*.yaml"))
    if not pages:
        raise RuntimeError("NO_PAGE_DATA_FOUND")

    count = 0
    for page_path in pages:
        page = load_yaml(page_path)
        competency_rel = page.get("competency_path")
        if not isinstance(competency_rel, str) or not competency_rel:
            raise ValueError(f"COMPETENCY_PATH_REQUIRED: {page_path}")
        competency = load_competency(ROOT / competency_rel)
        prepared = prepare_page(page, competency)
        print(
            f"VALIDATED_PAGE={page_path.name} "
            f"COMPETENCY={prepared['competency']['id']} "
            f"OBJECTS={len(prepared['learning_objects'])}"
        )
        count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--book-dir", default="books/jilid-1")
    parser.add_argument("--output-dir", default="dist/jilid-1")
    parser.add_argument("--logo", default="books/shared/assets/qurbata-logo.svg")
    args = parser.parse_args()

    book_dir = ROOT / args.book_dir
    validated = validate_book(book_dir)
    print(f"OBJECT_ENGINE=ACTIVE PAGES={validated}")
    print("COMPETENCY_VALIDATOR=ACTIVE")

    command = [
        sys.executable,
        str(ROOT / "tools/render_qurbata_v2.py"),
        "--book-dir",
        args.book_dir,
        "--output-dir",
        args.output_dir,
        "--logo",
        args.logo,
    ]
    subprocess.run(command, cwd=ROOT, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
