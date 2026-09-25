#!/usr/bin/env python3
"""Validate the machine-readable UI component contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "config" / "ui-components.json"
CATALOG_PATH = ROOT / "docs" / "ui-component-catalog.md"

ALLOWED_STATUSES = {"stable", "domain", "candidate", "legacy", "deprecated"}
REQUIRED_COMPONENT_FIELDS = {
    "id",
    "title",
    "status",
    "scope",
    "intent",
    "selectors",
    "source_files",
    "use_when",
    "avoid_when",
    "accessibility",
    "responsive",
    "documentation_anchor",
}
CLASS_OR_ID_RE = re.compile(r"(?P<token>[.#][A-Za-z_][A-Za-z0-9_-]*)")


def load_registry() -> dict:
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def selector_tokens(selector: str) -> list[str]:
    return [match.group("token") for match in CLASS_OR_ID_RE.finditer(selector)]


def main() -> int:
    failures: list[str] = []

    if not REGISTRY_PATH.is_file():
        print("ERROR: missing registry: config/ui-components.json", file=sys.stderr)
        return 2
    if not CATALOG_PATH.is_file():
        print("ERROR: missing catalog: docs/ui-component-catalog.md", file=sys.stderr)
        return 2

    data = load_registry()
    if data.get("schema") != "dkharlanau.ui-components":
        failures.append("registry schema must be dkharlanau.ui-components")
    if not isinstance(data.get("version"), int) or data["version"] < 1:
        failures.append("registry version must be a positive integer")

    components = data.get("components")
    if not isinstance(components, list) or not components:
        failures.append("registry must contain a non-empty components list")
        components = []

    catalog = CATALOG_PATH.read_text(encoding="utf-8")
    seen_ids: set[str] = set()

    for component in components:
        cid = component.get("id", "<missing-id>")
        missing = sorted(REQUIRED_COMPONENT_FIELDS - set(component))
        if missing:
            failures.append(f"{cid}: missing fields: {', '.join(missing)}")
            continue

        if cid in seen_ids:
            failures.append(f"{cid}: duplicate component id")
        seen_ids.add(cid)

        if component["status"] not in ALLOWED_STATUSES:
            failures.append(f"{cid}: unsupported status {component['status']!r}")

        if not component["selectors"]:
            failures.append(f"{cid}: selectors must not be empty")
        if not component["source_files"]:
            failures.append(f"{cid}: source_files must not be empty")

        source_texts: list[str] = []
        for rel in component["source_files"]:
            path = ROOT / rel
            if not path.is_file():
                failures.append(f"{cid}: source file does not exist: {rel}")
                continue
            source_texts.append(path.read_text(encoding="utf-8", errors="ignore"))
        source_blob = "\n".join(source_texts)

        for selector in component["selectors"]:
            tokens = selector_tokens(selector)
            if not tokens:
                failures.append(f"{cid}: selector has no class/id token: {selector}")
                continue
            if not any(token in source_blob for token in tokens):
                failures.append(
                    f"{cid}: selector tokens not found in source files: {selector}"
                )

        anchor = component["documentation_anchor"]
        if f"## {anchor}" not in catalog:
            failures.append(f"{cid}: catalog section missing for anchor {anchor!r}")

        if component["status"] in {"stable", "domain"}:
            for field in ("use_when", "avoid_when", "accessibility", "responsive"):
                if not component[field]:
                    failures.append(f"{cid}: {field} must not be empty")
            examples = component.get("examples", [])
            if not examples:
                failures.append(f"{cid}: reusable component needs a reference example")
            for example in examples:
                source = example.get("source_file")
                route = example.get("route")
                if not source or not (ROOT / source).is_file():
                    failures.append(f"{cid}: example source file missing: {source!r}")
                if not isinstance(route, str) or not route.startswith("/"):
                    failures.append(f"{cid}: example route must start with '/': {route!r}")

    source_of_truth = data.get("source_of_truth", {})
    expected_docs = {
        "docs/editorial-design-system.md",
        "docs/ui-component-catalog.md",
        "docs/ui-agent-workflow.md",
        "docs/site-content-design-contract.md",
    }
    for key, rel in source_of_truth.items():
        if rel not in expected_docs:
            failures.append(
                f"source_of_truth {key!r} points to unexpected document: {rel}"
            )
        if not (ROOT / rel).is_file():
            failures.append(f"source_of_truth document missing: {rel}")

    if failures:
        print("UI component registry failed:", file=sys.stderr)
        for failure in failures:
            print(f"  ERROR {failure}", file=sys.stderr)
        return 1

    reusable = sum(c["status"] in {"stable", "domain"} for c in components)
    print(
        f"UI component registry passed: {len(components)} components; "
        f"{reusable} reusable."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
