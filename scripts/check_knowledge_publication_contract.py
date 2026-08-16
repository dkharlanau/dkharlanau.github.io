#!/usr/bin/env python3
"""Validate the strict publication contract for reviewed, indexable Lab pages."""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FRONT_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
H1_RE = re.compile(r"<h1\b|^#\s+", re.I | re.M)
META_KEYWORDS_RE = re.compile(r"<meta\s+[^>]*name=[\"']keywords[\"']", re.I)
AUTHOR_ID = "https://dkharlanau.github.io/#dkharlanau"


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else None


def parse_page(path: Path):
    text = path.read_text(encoding="utf-8")
    match = FRONT_RE.search(text)
    if not match:
        return None
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {"error": f"invalid YAML: {exc}"}
    return {"front": fm, "body": text[match.end():]}


def route_for(path: Path, fm: dict) -> str:
    if fm.get("permalink"):
        route = str(fm["permalink"])
        return route if route.startswith("/") else "/" + route
    rel = path.relative_to(ROOT).as_posix()
    if rel.endswith("/index.md") or rel.endswith("/index.html"):
        return "/" + rel.rsplit("/index.", 1)[0] + "/"
    if rel.endswith(".md"):
        return "/" + rel[:-3] + "/"
    return "/" + rel


def strict_page(fm: dict) -> bool:
    robots = str(fm.get("robots", ""))
    return (
        fm.get("status") == "reviewed"
        and fm.get("verified") is True
        and "noindex" not in robots
        and fm.get("sitemap") is not False
    )


def sidecar_file(value: str) -> Path:
    return ROOT / value.lstrip("/")


def load_json_no_duplicates(path: Path):
    duplicates = []

    def hook(pairs):
        obj = {}
        for key, value in pairs:
            if key in obj:
                duplicates.append(key)
            obj[key] = value
        return obj

    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=hook)
    return data, duplicates


def validate_lastmod_semantics(errors: list[str]):
    for name in ("sitemap-pages.xml", "sitemap-atlas.xml"):
        path = ROOT / name
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        if "last_reviewed" in text:
            errors.append(f"{name}: review date must not drive sitemap lastmod")
        if "significant_lastmod" not in text:
            errors.append(f"{name}: missing significant_lastmod precedence")
    graph = ROOT / "_includes" / "seo" / "structured-data-sitewide-graph.html"
    graph_text = graph.read_text(encoding="utf-8") if graph.exists() else ""
    if "graph_modified = page.last_reviewed" in graph_text:
        errors.append("structured-data-sitewide-graph.html: review date must not drive dateModified")


def main() -> int:
    entities_doc = load_yaml(ROOT / "_data" / "knowledge_entities.yml") or {}
    entities = entities_doc.get("entities", {}) if isinstance(entities_doc, dict) else {}
    errors: list[str] = []
    strict_records = []

    for path in sorted((ROOT / "labs").rglob("*")):
        if path.suffix not in {".md", ".html"}:
            continue
        parsed = parse_page(path)
        if not parsed:
            continue
        if parsed.get("error"):
            errors.append(f"{path.relative_to(ROOT)}: {parsed['error']}")
            continue
        fm, body = parsed["front"], parsed["body"]
        route = route_for(path, fm)
        if not route.startswith("/labs/") or not strict_page(fm):
            continue

        title = str(fm.get("seo_title") or fm.get("title") or "").strip()
        description = str(fm.get("description") or "").strip()
        primary = str(fm.get("primary_topic") or fm.get("primary_entity") or "").strip()
        intent = str(fm.get("search_intent") or "").strip()
        reviewed = str(fm.get("last_reviewed_at") or fm.get("last_reviewed") or "").strip()
        sidecar = str(fm.get("ai_sidecar") or "").strip()
        links = fm.get("semantic_links") or []
        structured = fm.get("structured_data") or {}

        for field, value in (
            ("title", title), ("description", description), ("primary_topic", primary),
            ("search_intent", intent), ("last_reviewed", reviewed), ("ai_sidecar", sidecar),
        ):
            if not value:
                errors.append(f"{route}: missing {field}")
        if len(H1_RE.findall(body)) != 1:
            errors.append(f"{route}: expected exactly one H1")
        if len(links) < 2:
            errors.append(f"{route}: fewer than two semantic links")
        if primary and primary not in entities:
            errors.append(f"{route}: unknown primary_topic {primary}")
        if isinstance(structured, dict) and structured.get("type") not in {None, "TechArticle", "techarticle"}:
            errors.append(f"{route}: reviewed Lab page must resolve to TechArticle")

        if sidecar:
            spath = sidecar_file(sidecar)
            if not spath.exists():
                errors.append(f"{route}: sidecar does not exist ({sidecar})")
            else:
                try:
                    data, duplicates = load_json_no_duplicates(spath)
                except json.JSONDecodeError as exc:
                    errors.append(f"{route}: invalid sidecar JSON: {exc}")
                    data, duplicates = {}, []
                if duplicates:
                    errors.append(f"{route}: duplicate sidecar JSON keys: {sorted(set(duplicates))}")
                expected_url = "https://dkharlanau.github.io" + route
                if data.get("url") != expected_url:
                    errors.append(f"{route}: sidecar URL mismatch")
                if (data.get("author") or {}).get("id") != AUTHOR_ID:
                    errors.append(f"{route}: sidecar author must use canonical Person ID")
                if primary and (data.get("primary_entity") or {}).get("key") != primary:
                    errors.append(f"{route}: sidecar primary entity mismatch")
                if intent and (data.get("search") or {}).get("intent") != intent:
                    errors.append(f"{route}: sidecar search intent mismatch")
                factual = data.get("factual_review") or {}
                if factual.get("status") == "source_supported" and not data.get("sources"):
                    errors.append(f"{route}: source-supported review has no sidecar sources")

        strict_records.append((route, title, description, intent))

    for label, index in (("title", 1), ("description", 2), ("search_intent", 3)):
        values = defaultdict(list)
        for row in strict_records:
            value = row[index]
            if value:
                values[value.casefold()].append(row[0])
        for routes in values.values():
            if len(routes) > 1:
                errors.append(f"duplicate {label}: {', '.join(sorted(routes))}")

    for root in (ROOT / "_includes", ROOT / "_layouts"):
        for path in root.rglob("*.html"):
            if META_KEYWORDS_RE.search(path.read_text(encoding="utf-8", errors="ignore")):
                errors.append(f"{path.relative_to(ROOT)}: meta keywords are not allowed")

    validate_lastmod_semantics(errors)

    if errors:
        print(f"Knowledge publication contract failed with {len(errors)} issue(s):")
        for item in errors[:200]:
            print(f"- {item}")
        return 2

    print(f"Knowledge publication contract passed for {len(strict_records)} reviewed, indexable Lab pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
