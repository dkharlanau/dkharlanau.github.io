#!/usr/bin/env python3
"""Load the bounded public repository inventory used by portfolio operations."""

from __future__ import annotations

import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit


@dataclass(frozen=True)
class RepositorySpec:
    name: str
    repository_url: str
    page_url: str | None
    live_docs_url: str | None
    agent_manifest_url: str | None
    pages_expected: bool
    expected_links: tuple[str, ...]
    inventory_source: str


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def repository_name(repository_url: str, owner: str) -> str:
    parts = urlsplit(repository_url)
    segments = [segment for segment in parts.path.split("/") if segment]
    if parts.scheme != "https" or parts.netloc != "github.com" or len(segments) != 2:
        raise ValueError("repository URL must be https://github.com/<owner>/<repository>")
    if segments[0] != owner:
        raise ValueError(f"repository owner must be {owner}")
    return segments[1].removesuffix(".git")


def _spec_from_product(product: dict[str, Any], owner: str, source: str) -> RepositorySpec:
    name = repository_name(str(product.get("repository", "")), owner)
    expected = set(product.get("consumes", []) or []) | set(product.get("derived_from", []) or [])
    expected.discard(name)
    return RepositorySpec(
        name=name,
        repository_url=str(product["repository"]),
        page_url=str(product["page"]) if product.get("page") else None,
        live_docs_url=str(product["page"]) if product.get("page") else None,
        agent_manifest_url=str(product["agent_manifest"]) if product.get("agent_manifest") else None,
        pages_expected=bool(product.get("page")),
        expected_links=tuple(sorted(expected)),
        inventory_source=source,
    )


def _spec_from_additional(item: dict[str, Any], owner: str, source: str) -> RepositorySpec:
    name = repository_name(str(item.get("repository", "")), owner)
    page = str(item["page"]) if item.get("page") else None
    live_docs = str(item["live_docs_url"]) if item.get("live_docs_url") else page
    return RepositorySpec(
        name=name,
        repository_url=str(item["repository"]),
        page_url=page,
        live_docs_url=live_docs,
        agent_manifest_url=str(item["agent_manifest"]) if item.get("agent_manifest") else None,
        pages_expected=bool(item.get("pages_expected", page is not None)),
        expected_links=tuple(sorted(set(item.get("expected_links", []) or []))),
        inventory_source=source,
    )


def load_inventory(root: Path, config_path: Path) -> tuple[dict[str, Any], list[RepositorySpec]]:
    config = load_json(config_path)
    if config.get("schema_version") != "0.1":
        raise ValueError("portfolio health config schema_version must be 0.1")
    owner = str(config.get("owner", "")).strip()
    if not owner:
        raise ValueError("portfolio health config owner is required")

    manifest_rel = Path(str(config.get("portfolio_manifest", "")))
    manifest_path = root / manifest_rel
    manifest = load_json(manifest_path)
    specs: dict[str, RepositorySpec] = {}
    for product in manifest.get("products", []):
        if not isinstance(product, dict) or not product.get("repository"):
            continue
        spec = _spec_from_product(product, owner, manifest_rel.as_posix())
        if spec.name in specs:
            raise ValueError(f"duplicate repository in portfolio manifest: {spec.name}")
        specs[spec.name] = spec

    config_source = config_path.relative_to(root).as_posix() if config_path.is_relative_to(root) else config_path.name
    for item in config.get("additional_repositories", []):
        if not isinstance(item, dict):
            raise ValueError("additional_repositories entries must be objects")
        spec = _spec_from_additional(item, owner, config_source)
        if spec.name in specs:
            raise ValueError(f"additional repository duplicates portfolio manifest: {spec.name}")
        specs[spec.name] = spec

    excluded = set(config.get("excluded_repositories", []) or [])
    for name in excluded:
        specs.pop(str(name), None)

    repository_overrides = config.get("repository_overrides", {}) or {}
    if not isinstance(repository_overrides, dict):
        raise ValueError("repository_overrides must be an object")
    unknown_repository_overrides = sorted(set(repository_overrides) - set(specs))
    if unknown_repository_overrides:
        raise ValueError(
            f"repository_overrides contains unknown repositories: {', '.join(unknown_repository_overrides)}"
        )

    overlays = config.get("required_contract_links", {}) or {}
    unknown_overlays = sorted(set(overlays) - set(specs))
    if unknown_overlays:
        raise ValueError(f"required_contract_links contains unknown repositories: {', '.join(unknown_overlays)}")

    known_names = set(specs)
    result: list[RepositorySpec] = []
    for name, spec in sorted(specs.items()):
        override = repository_overrides.get(name, {}) or {}
        if not isinstance(override, dict):
            raise ValueError(f"{name}: repository override must be an object")
        expected = (
            set(spec.expected_links)
            | set(override.get("expected_links", []) or [])
            | set(overlays.get(name, []) or [])
        )
        unknown_links = sorted(expected - known_names)
        if unknown_links:
            raise ValueError(f"{name}: unknown expected repository links: {', '.join(unknown_links)}")
        expected.discard(name)
        result.append(
            replace(
                spec,
                live_docs_url=(
                    str(override["live_docs_url"]) if override.get("live_docs_url") else spec.live_docs_url
                ),
                agent_manifest_url=(
                    str(override["agent_manifest_url"])
                    if override.get("agent_manifest_url")
                    else spec.agent_manifest_url
                ),
                pages_expected=bool(override.get("pages_expected", spec.pages_expected)),
                expected_links=tuple(sorted(expected)),
            )
        )

    expected_count = int(config.get("expected_repository_count", 0))
    if expected_count and len(result) != expected_count:
        raise ValueError(f"portfolio inventory contains {len(result)} repositories; expected {expected_count}")
    if excluded & {item.name for item in result}:
        raise ValueError("excluded repositories remain in portfolio inventory")
    release_required = set(config.get("release_required_repositories", []) or [])
    unknown_release_required = sorted(release_required - {item.name for item in result})
    if unknown_release_required:
        raise ValueError(
            "release_required_repositories contains unknown repositories: "
            + ", ".join(unknown_release_required)
        )
    return config, result


def author_footer(config: dict[str, Any]) -> str:
    lines = config.get("author_footer_lines")
    if not isinstance(lines, list) or not lines or not all(isinstance(line, str) for line in lines):
        raise ValueError("author_footer_lines must be a non-empty list of strings")
    return "\n".join(lines)
