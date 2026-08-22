#!/usr/bin/env python3
"""Validate the SAP Lead career roadmap and the Lab-to-career contract."""
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
EXCLUDED_DIRS = {".git", "_site", "vendor", "node_modules", ".bundle", ".jekyll-cache"}
EXCLUDED_PREFIXES = {("docs", "templates")}
LAB_POLICY_FILES = {"labs/AGENTS.md"}


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


def normalize_route(href: str) -> str:
    return href.split("#", 1)[0].split("?", 1)[0].rstrip("/") + "/"


def discover_permalink_map() -> dict[str, str]:
    routes: dict[str, str] = {}
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS or part.startswith(".") for part in rel.parts):
            continue
        if any(rel.parts[:len(prefix)] == prefix for prefix in EXCLUDED_PREFIXES):
            continue
        permalink = str(parse_frontmatter(path).get("permalink") or "").strip()
        if permalink:
            routes[normalize_route(permalink)] = rel.as_posix()
        elif path.name == "index.md":
            routes["/" + rel.parent.as_posix().strip("/") + "/"] = rel.as_posix()
    return routes


def internal_route_exists(href: str, routes: dict[str, str]) -> bool:
    normalized = normalize_route(href)
    if normalized in routes:
        return True
    directory = ROOT / normalized.lstrip("/")
    return (directory / "index.html").exists() or (directory / "index.md").exists()


def roadmap_lab_routes(data: dict[str, Any]) -> set[str]:
    mapped: set[str] = set()
    for skill in data.get("skills") or []:
        if not isinstance(skill, dict):
            continue
        for source in skill.get("sources") or []:
            if not isinstance(source, dict):
                continue
            href = str(source.get("href") or "").strip()
            if href.startswith("/labs/"):
                mapped.add(normalize_route(href))
    return mapped


def validate_lab_exclusions(data: dict[str, Any], routes: dict[str, str]) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    excluded: set[str] = set()
    raw = data.get("lab_exclusions") or []
    if not isinstance(raw, list):
        return ["roadmap.yml: lab_exclusions must be a list when present"], excluded
    for index, item in enumerate(raw, start=1):
        where = f"roadmap.yml lab_exclusions #{index}"
        if not isinstance(item, dict):
            errors.append(f"{where}: expected an object")
            continue
        href = str(item.get("href") or "").strip()
        reason = str(item.get("reason") or "").strip()
        if not href.startswith("/labs/"):
            errors.append(f"{where}: href must be a /labs/ route")
            continue
        if len(reason) < 12:
            errors.append(f"{where}: reason must explain why the route is not career material")
        if not internal_route_exists(href, routes):
            errors.append(f"{where}: route does not exist: {href}")
        excluded.add(normalize_route(href))
    return errors, excluded


def validate_roadmap(data: dict[str, Any]) -> tuple[list[str], set[str]]:
    errors: list[str] = []
    tracks = data.get("tracks") if isinstance(data.get("tracks"), dict) else {}
    tiers = data.get("tiers") if isinstance(data.get("tiers"), dict) else {}
    stages = data.get("stages") if isinstance(data.get("stages"), list) else []
    skills = data.get("skills") if isinstance(data.get("skills"), list) else []
    if not tracks:
        errors.append("roadmap.yml: tracks must be a non-empty mapping")
    if not tiers:
        errors.append("roadmap.yml: tiers must be a non-empty mapping")
    if not stages:
        errors.append("roadmap.yml: stages must be a non-empty list")
    if not skills:
        errors.append("roadmap.yml: skills must be a non-empty list")

    stage_ids = {str(item.get("id")) for item in stages if isinstance(item, dict) and item.get("id")}
    skill_ids: set[str] = set()
    routes = discover_permalink_map()

    for index, skill in enumerate(skills, start=1):
        if not isinstance(skill, dict):
            errors.append(f"roadmap.yml skill #{index}: expected an object")
            continue
        skill_id = str(skill.get("id") or "").strip()
        if not skill_id:
            errors.append(f"roadmap.yml skill #{index}: missing id")
            continue
        where = f"roadmap.yml skill {skill_id}"
        if skill_id in skill_ids:
            errors.append(f"{where}: duplicate id")
        skill_ids.add(skill_id)
        if str(skill.get("track") or "") not in tracks:
            errors.append(f"{where}: unknown track {skill.get('track')!r}")
        if str(skill.get("tier") or "") not in tiers:
            errors.append(f"{where}: unknown tier {skill.get('tier')!r}")
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
                if not internal_route_exists(href, routes):
                    errors.append(f"{where}: source route does not exist: {href}")
            elif not re.match(r"^https://", href):
                errors.append(f"{where}: source href must be an internal route or HTTPS URL: {href}")

    exclusion_errors, _ = validate_lab_exclusions(data, routes)
    errors.extend(exclusion_errors)
    if len(tracks) < 5:
        errors.append("roadmap.yml: expected at least five career tracks")
    if len(skill_ids) < 30:
        errors.append("roadmap.yml: expected at least 30 skills for a Lead-level roadmap")
    return errors, skill_ids


def validate_metadata(rel: str, fm: dict[str, Any], skill_ids: set[str]) -> list[str]:
    errors: list[str] = []
    impact = fm.get("career_impact")
    if impact not in {"mapped", "none"}:
        return [f"{rel}: career_impact must be mapped or none"]
    if impact == "mapped":
        mapped = fm.get("career_skills")
        if not isinstance(mapped, list) or not mapped:
            return [f"{rel}: career_impact mapped requires career_skills"]
        unknown = sorted({str(item) for item in mapped} - skill_ids)
        if unknown:
            errors.append(f"{rel}: unknown career skill IDs: {', '.join(unknown)}")
    else:
        reason = str(fm.get("career_reason") or "").strip()
        if len(reason) < 12:
            errors.append(f"{rel}: career_impact none requires a useful career_reason")
    return errors


def validate_declared_lab_metadata(skill_ids: set[str]) -> list[str]:
    errors: list[str] = []
    for path in sorted((ROOT / "labs").rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        if rel in LAB_POLICY_FILES:
            continue
        fm = parse_frontmatter(path)
        if fm.get("career_impact") is not None:
            errors.extend(validate_metadata(rel, fm, skill_ids))
    return errors


def changed_lab_content(base: str) -> list[str]:
    command = ["git", "diff", "--name-status", "--find-renames", f"{base}...HEAD", "--", "labs"]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git diff failed")
    paths: list[str] = []
    for line in result.stdout.splitlines():
        parts = line.split("\t")
        if not parts:
            continue
        status = parts[0]
        candidate = parts[1] if status.startswith("A") and len(parts) >= 2 else parts[2] if status.startswith("R") and len(parts) >= 3 else ""
        if not candidate.startswith("labs/") or candidate in LAB_POLICY_FILES:
            continue
        if candidate.endswith(".md") or candidate.endswith(".html"):
            paths.append(candidate)
    return sorted(set(paths))


def html_route(rel: str) -> str:
    path = Path(rel)
    if path.name == "index.html":
        return "/" + path.parent.as_posix().strip("/") + "/"
    return "/" + path.as_posix().lstrip("/")


def validate_new_lab_contract(base: str, skill_ids: set[str], data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    routes = discover_permalink_map()
    mapped_routes = roadmap_lab_routes(data)
    _, excluded_routes = validate_lab_exclusions(data, routes)
    for rel in changed_lab_content(base):
        path = ROOT / rel
        if not path.exists():
            continue
        if rel.endswith(".md"):
            fm = parse_frontmatter(path)
            if fm.get("career_impact") not in {"mapped", "none"}:
                errors.append(
                    f"{rel}: new Lab Markdown must declare career_impact: mapped|none. "
                    "If mapped, add career_skills. If none, add career_reason."
                )
                continue
            errors.extend(validate_metadata(rel, fm, skill_ids))
            continue
        route = normalize_route(html_route(rel))
        if route not in mapped_routes and route not in excluded_routes:
            errors.append(
                f"{rel}: new static Lab route {route} needs a career decision. "
                "Reference the route from a skill source in roadmap.yml, or add lab_exclusions with a useful reason."
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Lab-to-career roadmap factory.")
    parser.add_argument("--changed-from", help="Git base ref used to enforce the contract on newly added Lab content.")
    args = parser.parse_args()
    try:
        data = load_yaml(ROADMAP_PATH)
        errors, skill_ids = validate_roadmap(data)
        errors.extend(validate_declared_lab_metadata(skill_ids))
        new_pages: list[str] = []
        if args.changed_from:
            new_pages = changed_lab_content(args.changed_from)
            errors.extend(validate_new_lab_contract(args.changed_from, skill_ids, data))
    except (OSError, ValueError, yaml.YAMLError, RuntimeError) as exc:
        print(f"Career Factory failed: {exc}", file=sys.stderr)
        return 2
    if errors:
        print(f"Career Factory failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 2
    print(f"Career Factory passed: {len(skill_ids)} skills across {len(data.get('tracks') or {})} tracks.")
    if args.changed_from:
        print(f"New Lab content checked for explicit career impact: {len(new_pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
