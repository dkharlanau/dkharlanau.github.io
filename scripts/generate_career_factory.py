#!/usr/bin/env python3
"""Generate a deterministic Lab-to-career coverage inventory for agents and UI."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "_data" / "career" / "roadmap.yml"
OUTPUT = ROOT / "ai" / "career-factory.json"
EXCLUDED_DIRS = {".git", "_site", "vendor", "node_modules", ".bundle", ".jekyll-cache"}
TOKEN_STOP = {"labs", "lab", "sap", "lead", "career", "interview", "enterprise", "context", "the", "and", "for", "with", "from"}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected YAML object")
    return data


def frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    data = yaml.safe_load(text[4:end]) or {}
    return data if isinstance(data, dict) else {}


def normalize_route(value: str) -> str:
    path = value.split("#", 1)[0].split("?", 1)[0].strip()
    if not path.startswith("/"):
        path = "/" + path
    if not Path(path).suffix:
        path = path.rstrip("/") + "/"
    return path


def route_for(path: Path, fm: dict[str, Any]) -> str:
    permalink = str(fm.get("permalink") or "").strip()
    if permalink:
        return normalize_route(permalink)
    rel = path.relative_to(ROOT).as_posix()
    if path.name in {"index.md", "index.html"}:
        return "/" + path.parent.relative_to(ROOT).as_posix().strip("/") + "/"
    return "/" + rel


def tokens(*values: str) -> set[str]:
    result: set[str] = set()
    for value in values:
        for token in re.findall(r"[a-z0-9][a-z0-9+-]{2,}", value.lower()):
            if token not in TOKEN_STOP:
                result.add(token)
    return result


def skills_by_lab_route(data: dict[str, Any]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for skill in data.get("skills") or []:
        if not isinstance(skill, dict):
            continue
        skill_id = str(skill.get("id") or "")
        for source in skill.get("sources") or []:
            if not isinstance(source, dict) or source.get("kind") != "lab":
                continue
            href = str(source.get("href") or "").strip()
            if href.startswith("/labs/"):
                result.setdefault(normalize_route(href), []).append(skill_id)
    return result


def exclusions(data: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for item in data.get("lab_exclusions") or []:
        if isinstance(item, dict) and item.get("href"):
            result[normalize_route(str(item["href"]))] = str(item.get("reason") or "")
    return result


def skill_signals(data: dict[str, Any]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for skill in data.get("skills") or []:
        if not isinstance(skill, dict) or not skill.get("id"):
            continue
        source_labels = " ".join(str(src.get("label") or "") for src in skill.get("sources") or [] if isinstance(src, dict))
        result[str(skill["id"])] = tokens(
            str(skill.get("id") or ""), str(skill.get("title") or ""), str(skill.get("why") or ""),
            str(skill.get("interview_signal") or ""), source_labels,
        )
    return result


def suggest_skills(path: Path, fm: dict[str, Any], signals: dict[str, set[str]], limit: int = 3) -> list[dict[str, Any]]:
    rel = path.relative_to(ROOT).as_posix()
    page_tokens = tokens(rel, str(fm.get("title") or ""), str(fm.get("description") or ""), " ".join(map(str, fm.get("tags") or [])))
    ranked: list[tuple[int, str, list[str]]] = []
    for skill_id, skill_tokens in signals.items():
        overlap = sorted(page_tokens & skill_tokens)
        if overlap:
            ranked.append((len(overlap), skill_id, overlap[:6]))
    ranked.sort(key=lambda row: (-row[0], row[1]))
    return [{"skill_id": skill_id, "score": score, "matched_terms": overlap} for score, skill_id, overlap in ranked[:limit]]


def discover_labs(data: dict[str, Any]) -> list[dict[str, Any]]:
    route_map = skills_by_lab_route(data)
    excluded = exclusions(data)
    signals = skill_signals(data)
    entries: list[dict[str, Any]] = []
    for path in sorted((ROOT / "labs").rglob("*")):
        if not path.is_file() or path.suffix not in {".md", ".html"}:
            continue
        rel_path = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS or part.startswith(".") for part in rel_path.parts):
            continue
        if rel_path.as_posix() == "labs/AGENTS.md":
            continue
        fm = frontmatter(path) if path.suffix == ".md" else {}
        route = route_for(path, fm)
        declared = str(fm.get("career_impact") or "")
        declared_skills = [str(item) for item in (fm.get("career_skills") or [])] if declared == "mapped" else []
        source_skills = route_map.get(route, [])
        mapped_skills = sorted(set(declared_skills + source_skills))
        if declared == "none" or route in excluded:
            state = "excluded"
        elif mapped_skills:
            state = "mapped"
        else:
            state = "needs_decision"
        entry = {
            "source_file": rel_path.as_posix(),
            "route": route,
            "title": str(fm.get("title") or path.parent.name.replace("-", " ").title()),
            "state": state,
            "career_impact": declared or "undeclared",
            "skills": mapped_skills,
            "reason": str(fm.get("career_reason") or excluded.get(route) or ""),
        }
        if state == "needs_decision":
            entry["suggested_skills"] = suggest_skills(path, fm, signals)
        entries.append(entry)
    return entries


def build(data: dict[str, Any]) -> dict[str, Any]:
    labs = discover_labs(data)
    skills = [item for item in data.get("skills") or [] if isinstance(item, dict)]
    tracks = data.get("tracks") if isinstance(data.get("tracks"), dict) else {}
    track_stats: dict[str, dict[str, Any]] = {}
    for track_id, track in tracks.items():
        track_skills = [skill for skill in skills if skill.get("track") == track_id]
        lab_routes = sorted({normalize_route(str(src.get("href"))) for skill in track_skills for src in skill.get("sources") or [] if isinstance(src, dict) and src.get("kind") == "lab" and str(src.get("href") or "").startswith("/labs/")})
        track_stats[track_id] = {"label": track.get("label", track_id), "skills": len(track_skills), "lab_routes": len(lab_routes)}
    counts = {state: sum(1 for item in labs if item["state"] == state) for state in ("mapped", "excluded", "needs_decision")}
    decided = counts["mapped"] + counts["excluded"]
    coverage = round((decided / len(labs)) * 100, 1) if labs else 100.0
    return {
        "schema": "dkharlanau.career.factory",
        "schema_version": "2.0",
        "generated_at": str(data.get("updated_at") or ""),
        "canonical_url": "https://dkharlanau.github.io/ai/career-factory.json",
        "roadmap_url": "https://dkharlanau.github.io/labs/interview-readiness/roadmap/",
        "summary": {"skills": len(skills), "tracks": len(tracks), "lab_pages": len(labs), "mapped": counts["mapped"], "excluded": counts["excluded"], "needs_decision": counts["needs_decision"], "decision_coverage_percent": coverage},
        "track_stats": track_stats,
        "lab_inventory": labs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        payload = build(load_yaml(ROADMAP))
        text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
        if args.check:
            if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != text:
                print("Career Factory inventory is stale. Run scripts/generate_career_factory.py")
                return 2
            print("Career Factory inventory is current.")
            return 0
        OUTPUT.write_text(text, encoding="utf-8")
        print(f"Career Factory inventory written: {payload['summary']}")
        return 0
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"Career Factory generation failed: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
