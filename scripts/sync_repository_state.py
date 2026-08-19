#!/usr/bin/env python3
"""Synchronize deterministic repository metadata with canonical source content."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "_data" / "labs" / "enterprise_context" / "sources"
ASSESSMENT_DATA = ROOT / "labs" / "assessment" / "data"
MANIFEST = ASSESSMENT_DATA / "case-sets.json"


def slug(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "-", value.upper()).strip("-")


def source_type_for(source: dict[str, Any]) -> str:
    publisher = str(source.get("publisher") or "").strip().lower()
    url = str(source.get("url") or "").strip().lower()
    if publisher == "sap":
        if "help.sap.com" in url or "learning.sap.com" in url:
            return "official_help"
        return "official_documentation"
    return "primary_source"


def collect_source_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(SOURCE_ROOT.glob("*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            continue
        for source in data.get("sources", []) or []:
            if isinstance(source, dict) and isinstance(source.get("id"), str) and source["id"]:
                ids.add(source["id"])
    return ids


def normalize_decision_sources() -> list[str]:
    changed: list[str] = []
    known_ids = collect_source_ids()
    for path in sorted(SOURCE_ROOT.glob("decision_*.yml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("sources"), list):
            continue
        default_date = data.get("reviewed_at") or data.get("updated_at")
        prefix = f"SRC-DEC-{slug(path.stem.removeprefix('decision_'))}"
        touched = False
        for index, source in enumerate(data["sources"], start=1):
            if not isinstance(source, dict):
                continue
            if not source.get("id"):
                candidate = f"{prefix}-{index:02d}"
                suffix = 2
                while candidate in known_ids:
                    candidate = f"{prefix}-{index:02d}-{suffix}"
                    suffix += 1
                source["id"] = candidate
                known_ids.add(candidate)
                touched = True
            if not source.get("source_type"):
                source["source_type"] = source_type_for(source)
                touched = True
            if not source.get("accessed_at"):
                derived_date = source.get("verified_at") or default_date
                if not derived_date:
                    raise RuntimeError(f"{path}: cannot derive accessed_at for {source.get('id')}")
                source["accessed_at"] = derived_date
                touched = True
            if not source.get("status"):
                source["status"] = "source_verified" if source.get("verified_at") else "researching"
                touched = True
        if touched:
            path.write_text(
                yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000),
                encoding="utf-8",
            )
            changed.append(path.relative_to(ROOT).as_posix())
    return changed


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSONL in {path} line {number}: {exc}") from exc
        if not isinstance(row, dict) or not row.get("id"):
            raise RuntimeError(f"Invalid assessment case in {path} line {number}")
        rows.append(row)
    return rows


def sync_assessment_manifest() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    total = 0
    for case_set in manifest["sets"]:
        case_path = ROOT / str(case_set["url"]).lstrip("/")
        count = len(load_jsonl(case_path))
        case_set["count"] = count
        total += count
    manifest["total_cases"] = total
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return total


def sync_assessment_copy(total: int) -> list[str]:
    changed: list[str] = []
    files = [
        ROOT / "labs" / "assessment" / "index.md",
        ROOT / "labs" / "assessment" / "start-here" / "index.md",
        ROOT / "machine" / "assessment" / "index.md",
    ]
    for path in files:
        if not path.exists():
            continue
        before = path.read_text(encoding="utf-8")
        after = before
        after = re.sub(
            r"(<span>03</span><strong>)\d+(</strong><small>Structured practice cases</small>)",
            rf"\g<1>{total}\g<2>", after,
        )
        after = re.sub(
            r"(<span>03</span><strong>)\d+(</strong><small>Structured cases</small>)",
            rf"\g<1>{total}\g<2>", after,
        )
        after = re.sub(r"\b\d+(?= structured cases\b)", str(total), after)
        after = re.sub(
            r"(<strong>Case Set Manifest</strong><small>)\d+( cases\b)",
            rf"\g<1>{total}\g<2>", after,
        )
        if after != before:
            path.write_text(after, encoding="utf-8")
            changed.append(path.relative_to(ROOT).as_posix())
    return changed


def run(*args: str) -> None:
    command = [sys.executable, *args]
    print("+", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> int:
    source_changes = normalize_decision_sources()
    total = sync_assessment_manifest()
    copy_changes = sync_assessment_copy(total)
    print(f"Assessment manifest synchronized to {total} cases")
    print(f"Normalized decision source registries: {len(source_changes)}")
    print(f"Updated assessment count pages: {len(copy_changes)}")

    run("scripts/validate_enterprise_context.py")
    run("scripts/knowledge_publication_loop.py")
    run("scripts/generate_assessment_candidates.py")
    run("scripts/audit_assessment_promotion_readiness.py")
    run("scripts/generate_assessment_core_study_map.py")
    run("scripts/generate_assessment_reasoning_coverage.py")
    run("scripts/generate_assessment_promotion_review_packet.py")
    run("scripts/generate_atlas_artifacts.py")
    run("scripts/generate_career_factory.py")

    run("scripts/knowledge_publication_loop.py", "--check")
    run("scripts/generate_assessment_candidates.py", "--check")
    run("scripts/audit_assessment_promotion_readiness.py", "--check")
    run("scripts/generate_assessment_core_study_map.py", "--check")
    run("scripts/generate_assessment_reasoning_coverage.py", "--check")
    run("scripts/generate_assessment_promotion_review_packet.py", "--check")
    run("scripts/generate_atlas_artifacts.py", "--check")
    run("scripts/generate_career_factory.py", "--check")
    run("scripts/validate_assessment_reasoning_coverage.py")
    run("scripts/validate_assessment_promotion_review_packet.py")
    run("scripts/validate_enterprise_context.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
