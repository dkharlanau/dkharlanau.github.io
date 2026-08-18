#!/usr/bin/env python3
"""Validate the SAP Lead career roadmap and Lab-to-career contract.

The career roadmap is a skills layer over Labs, Assessment, Frameworks, and
other public evidence. Existing Lab pages are grandfathered. Every newly added
Lab Markdown file must make an explicit career decision:

  career_impact: mapped
  career_skills: [skill-id, ...]

or:

  career_impact: none
  career_reason: "Why this Lab is not interview/career material."

This keeps future agents from expanding Labs without considering the career
roadmap while avoiding a forced rewrite of the existing corpus.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROADMAP_PATH = ROOT / "_data" / "career" / "roadmap.yml"
EXCLUDED_DIRS = {
    ".git",
    "_site",
    "vendor",
    "node_modules",
    ".bundle",
    ".jekyll-cache",
}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a YAML object")
    return data


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data, dict) else {}


def discover_permalink_map() -> dict[str, str]:
    routes: dict[str, str] = {}
    for path in ROOT.rglob("*.md"):
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS or part.startswith(".") for part in rel_parts):
            continue
        fm = parse_frontmatter(path)
        permalink = str(fm.get("permalink") or "").strip()
        if permalink:
            routes[permalink.rstrip("/") + "/"] = path.relative_to(ROOT).as_posix()
    return routes


def validate_roadmap(data: dict[str, Any]) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    tracks = data.get("tracks")
    tiers = data.get("tiers")
    stages = data.get("stages")
    skills = data.get("skills")

    if not isinstance(tracks, dict) or not tracks:
        errors.append("roadmap.yml: tracks must be a non-empty mapping")
        tracks = {}
    if not isinstance(tiers, dict) or not tiers:
        errors.append("roadmap.yml: tiers must be a non-empty mapping")
        tiers = {}
    if not isinstance(stages, list) or not stages:
        errors.append("roadmap.yml: stages must be a non-empty list")
        stages = []
    if not isinstance(skills, list) or not skills:
        errors.append("roadmap.yml: skills must be a non-empty list")
        skills = []

    stage_ids = {str(item.get("id")) for item in stages if isinstance(item, dict) and item.get("id")}
    skill_ids: set[str] = set()
    routes = discover_permalink_map()

    for index, skill in enumerate(skills, start=1):
        where = f"roadmap.yml skill #{index}"
        if not isinstance(skill, dict):
            errors.append(f"{where}: expected an object")
            continue
        skill_id = str(skill.get("id") or "").strip()
        if not skill_id:
            errors.append(f"{where}: missing id")
            continue
        where = f"roadmap.yml skill {skill_id}"
        if skill_id in skill_ids:
            errors.append(f"{where}: duplicate id")
        skill_ids.add(skill_id)

        track = str(skill.get("track") or "")
        if track not in tracks:
            errors.append(f"{where}: unknown track {track!r}")
        tier = str(skill.get("tier") or "")
        if tier not in tiers:
            errors.append(f"{where}: unknown tier {tier!r}")
        for field in ("title", "why", "interview_signal"):
            if not str(skill.get(field) or "").strip():
                errors.append(f"{where}: missing {field}")

        capabilities = skill.get("capabilities")
        if not isinstance(capabilities, list) or not capabilities:
            errors.append(f"{where}: capabilities must be a non-empty list")
        else:
            unknown = sorted({str(item) for item in capabilities} - stage_ids)
            if unknown:
                errors.append(f"{where}: unknown capability stage(s): {', '.join(unknown)}")

        sources = skill.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{where}: sources must be a non-empty list")
            continue
        for source_index, source in enumerate(sources, start=1):
            if not isinstance(source, dict):
                errors.append(f"{where} source #{source_index}: expected an object")
                continue
            label = str(source.get("label") or "").strip()
            href = str(source.get("href") or "").strip()
            kind = str(source.get("kind") or "").strip()
            if not label or not href or not kind:
                errors.append(f"{where} source #{source_index}: kind, label, and href are required")
                continue
            if href.startswith("/"):
                normalized = href.split("#", 1)[0].split("?", 1)[0].rstrip("/") + "/"
                if normalized not in routes:
                    errors.append(f"{where}: source route does not exist: {href}")
            elif not re.match(r"^https://", href):
                errors.append(f"{where}: source href must be an internal route or HTTPS URL: {href}")

    if len(tracks) < 5:
        errors.append("roadmap.yml: expected at least five career tracks")
    if len(skill_ids) < 30:
        errors.append("roadmap.yml: expected at least 30 skills for a Lead-level roadmap")
    return errors, skill_ids


def validate_declared_lab_metadata(skill_ids: set[str]) -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "labs").rglob("*.md")):
        fm = parse_frontmatter(path)
        impact = fm.get("career_impact")
        if impact is None:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if impact not in {"mapped", "none"}:
            errors.append(f"{rel}: career_impact must be mapped or none")
            continue
        if impact == "mapped":
            mapped = fm.get("career_skills")
            if not isinstance(mapped, list) or not mapped:
                errors.append(f"{rel}: career_impact mapped requires career_skills")
                continue
            unknown = sorted({str(item) for item in mapped} - skill_ids)
            if unknown:
                errors.append(f"{rel}: unknown career skill IDs: {', '.join(unknown)}")
        else:
            reason = str(fm.get("career_reason") or "").strip()
            if len(reason) < 12:
                errors.append(f"{rel}: career_impact none requires a useful career_reason")
    return errors


def changed_lab_markdown(base: str) -> list[str]:
    command = ["git", "diff", "--name-status", "--find-renames", f"{base}...HEAD", "--", "labs"]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        status = parts[0]
        if status.startswith("A") and len(parts) >= 2:
            candidate = parts[1]
        elif status.startswith("R") and len(parts) >= 3:
            candidate = parts[2]
        else:
            continue
        if candidate.startswith("labs/") and candidate.endswith(".md"):
            paths.append(candidate)
    return sorted(set(paths))


def validate_new_lab_contract(base: str, skill_ids: set[str]) -> list[str]:
    errors: list[str] = []
    for rel in changed_lab_markdown(base):
        path = ROOT / rel
        if not path.exists():
            continue
        fm = parse_frontmatter(path)
        impact = fm.get("career_impact")
        if impact not in {"mapped", "none"}:
            errors.append(
                f"{rel}: new Lab Markdown must declare career_impact: mapped|none. "
                "If mapped, add career_skills. If none, add career_reason."
            )
            continue
        if impact == "mapped":
            mapped = fm.get("career_skills")
            if not isinstance(mapped, list) or not mapped:
                errors.append(f"{rel}: career_impact mapped requires career_skills")
                continue
            unknown = sorted({str(item) for item in mapped} - skill_ids)
            if unknown:
                errors.append(f"{rel}: unknown career skill IDs: {', '.join(unknown)}")
        else:
            reason = str(fm.get("career_reason") or "").strip()
            if len(reason) < 12:
                errors.append(f"{rel}: career_impact none requires a useful career_reason")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Lab-to-career roadmap factory.")
    parser.add_argument("--changed-from", help="Git base ref used to enforce the contract on new Lab Markdown files.")
    args = parser.parse_args()

    try:
        data = load_yaml(ROADMAP_PATH)
        errors, skill_ids = validate_roadmap(data)
        errors.extend(validate_declared_lab_metadata(skill_ids))
        new_pages: list[str] = []
        if args.changed_from:
            new_pages = changed_lab_markdown(args.changed_from)
            errors.extend(validate_new_lab_contract(args.changed_from, skill_ids))
    except (OSError, ValueError, yaml.YAMLError, RuntimeError) as exc:
        print(f"Career Factory failed: {exc}", file=sys.stderr)
        return 2

    if errors:
        print(f"Career Factory failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 2

    track_count = len(data.get("tracks") or {})
    print(f"Career Factory passed: {len(skill_ids)} skills across {track_count} tracks.")
    if args.changed_from:
        print(f"New Lab Markdown checked for explicit career impact: {len(new_pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
