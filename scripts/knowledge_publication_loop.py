#!/usr/bin/env python3
"""Canonical publication loop for reviewed knowledge pages.

This is a compatibility layer over ai_search_trust_loop.py. It keeps the mature page and
sidecar generator while replacing two legacy policies:

1. provenance is resolved from explicit route -> registry bindings as well as Liquid refs;
2. editorial review dates never mutate content modification dates.

The wrapper can be removed once the underlying generator natively implements this contract.
"""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "scripts" / "ai_search_trust_loop.py"
BINDINGS = ROOT / "_data" / "labs" / "source_bindings.yml"
SOURCES = ROOT / "_data" / "labs" / "enterprise_context" / "sources"
URL_RE = re.compile(r"https?://[^\s\]\[\)\(<>\"']+")
SOURCE_ASSIGN_RE = re.compile(
    r"site\.data\.labs\.enterprise_context\.sources\.([A-Za-z0-9_]+)"
)


def load_yaml(path: Path):
    if not path.exists():
        return None
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_data(path: Path):
    if not path.exists():
        return None
    if path.suffix == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return load_yaml(path)


def load_base():
    spec = importlib.util.spec_from_file_location("legacy_ai_search_trust_loop", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {BASE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def registry_path(name: str) -> Path | None:
    for suffix in (".yml", ".yaml", ".json"):
        candidate = SOURCES / f"{name}{suffix}"
        if candidate.exists():
            return candidate
    return None


def registry_links(names: list[str]) -> list[dict]:
    found: list[dict] = []
    seen: set[str] = set()

    def walk(node, inherited_title=None):
        if isinstance(node, dict):
            title = node.get("title") or node.get("name") or inherited_title
            url = node.get("url") or node.get("href")
            if isinstance(url, str) and url.startswith("http") and url not in seen:
                seen.add(url)
                found.append({"title": str(title or url), "url": url})
            for value in node.values():
                walk(value, title)
        elif isinstance(node, list):
            for value in node:
                walk(value, inherited_title)
        elif isinstance(node, str):
            for url in URL_RE.findall(node):
                url = url.rstrip(".,;:")
                if url not in seen:
                    seen.add(url)
                    found.append({"title": str(inherited_title or url), "url": url})

    for name in names:
        path = registry_path(name)
        if not path:
            raise RuntimeError(f"Unknown source registry: {name}")
        walk(load_data(path), name.replace("_", " ").title())
    return found[:12]


def canonical_modified(fm: dict):
    return (
        fm.get("significant_lastmod")
        or fm.get("content_updated_at")
        or fm.get("schema_updated_at")
        or fm.get("last_modified_at")
        or fm.get("updated")
        or fm.get("date")
    )


def main() -> int:
    base = load_base()
    binding_doc = load_yaml(BINDINGS) or {}
    route_bindings = binding_doc.get("routes", {}) if isinstance(binding_doc, dict) else {}

    route_by_body: dict[str, str] = {}
    page_meta: dict[str, dict] = {}
    for _path, _text, fm, _raw, body in base.iter_sources():
        route = base.derive_route(_path, fm)
        route_by_body[body] = route
        page_meta[route] = fm

    def extract_source_links(body: str) -> list[dict]:
        route = route_by_body.get(body)
        names = set(SOURCE_ASSIGN_RE.findall(body))
        bound = route_bindings.get(route, {}) if route else {}
        if isinstance(bound, dict):
            names.update(str(item) for item in (bound.get("registries") or []))
        return registry_links(sorted(names))

    original_payload = base.sidecar_payload

    def sidecar_payload(record, relations, sources, readiness, entities):
        payload = original_payload(record, relations, sources, readiness, entities)
        fm = page_meta.get(record["route"], {})
        publication = payload.setdefault("publication", {})
        publication["date_published"] = base.iso(fm.get("date_published") or fm.get("date") or fm.get("published"))
        publication["content_updated_at"] = base.iso(fm.get("content_updated_at") or fm.get("last_modified_at") or fm.get("updated"))
        publication["last_reviewed_at"] = base.iso(fm.get("last_reviewed_at") or fm.get("last_reviewed"))
        publication["schema_updated_at"] = base.iso(fm.get("schema_updated_at"))
        publication["significant_lastmod"] = base.iso(canonical_modified(fm))
        # Keep legacy fields during transition, but do not conflate review with modification.
        publication["last_reviewed"] = publication["last_reviewed_at"]
        publication["last_modified_at"] = publication["significant_lastmod"]
        return payload

    base.extract_source_links = extract_source_links
    base.align_last_modified = lambda raw, fm: raw
    base.patch_sitemap = lambda text: text
    base.sidecar_payload = sidecar_payload
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
