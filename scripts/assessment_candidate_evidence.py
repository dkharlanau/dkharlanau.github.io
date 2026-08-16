#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def collect_source_records(value: Any, result: dict[str, dict[str, Any]]) -> None:
    if isinstance(value, dict):
        source_id = value.get("id")
        if isinstance(source_id, str) and source_id.startswith("SRC-"):
            result[source_id] = value
        for item in value.values():
            collect_source_records(item, result)
    elif isinstance(value, list):
        for item in value:
            collect_source_records(item, result)


def source_registry(root: Path) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    source_root = root / "_data" / "labs" / "enterprise_context" / "sources"
    for path in sorted(source_root.glob("*.yml")):
        collect_source_records(load_yaml(path), result)
    return result


def factual_review_index(root: Path) -> dict[str, dict[str, Any]]:
    path = root / "labs" / "assessment" / "data" / "factual-review.json"
    payload = load_json(path)
    claims = {item["id"]: item for item in payload.get("claims", []) if item.get("id")}
    result: dict[str, dict[str, Any]] = {}
    for route in payload.get("routes", []):
        route_id = str(route.get("route", ""))
        route_claims = [claims[item] for item in route.get("claim_ids", []) if item in claims]
        statuses = {item.get("status", "not_reviewed") for item in route_claims}
        if route_claims and statuses == {"source_supported"}:
            status = "source_supported"
        elif "source_conflict" in statuses:
            status = "source_conflict"
        elif "release_scope_unclear" in statuses:
            status = "release_scope_unclear"
        else:
            status = "needs_source_review"
        result[route_id] = {
            "status": status,
            "claim_count": len(route_claims),
            "reviewed_at": route.get("reviewed_at"),
        }
    return result


def evidence_profile_payload(root: Path) -> dict[str, Any]:
    return load_json(root / "labs" / "assessment" / "data" / "evidence-profile.json")


def route_profile(route: str, payload: dict[str, Any]) -> dict[str, Any]:
    override = payload.get("route_overrides", {}).get(route)
    if override:
        return override
    if route.startswith("/labs/enterprise-context/"):
        return payload.get("defaults", {}).get("enterprise_context", {})
    return {
        "expected_evidence_classes": ["author_heuristic"],
        "external_review_mode": "not_primary_gate",
        "counts_as_source_review_debt": False,
    }


def unique_source_refs(seed: dict[str, Any]) -> list[str]:
    refs: set[str] = set()
    for values in seed.get("failure_sources", {}).values():
        refs.update(str(item) for item in values)
    return sorted(refs)


def validate_seed_evidence_contract(root: Path, seeds: dict[str, Any]) -> dict[str, dict[str, Any]]:
    sources = source_registry(root)
    factual = factual_review_index(root)
    profiles = evidence_profile_payload(root)
    gates: dict[str, dict[str, Any]] = {}

    for seed in seeds.get("graphs", []):
        graph_path = str(seed.get("path", ""))
        route = str(seed.get("human_ref", ""))
        evidence_class = str(seed.get("evidence_class", ""))
        if not graph_path or not route or not evidence_class:
            raise ValueError(f"Candidate seed is missing path, human_ref, or evidence_class: {seed}")

        profile = route_profile(route, profiles)
        expected_classes = list(profile.get("expected_evidence_classes", []))
        if evidence_class not in expected_classes:
            raise ValueError(
                f"Candidate seed {graph_path} uses evidence class {evidence_class!r}, "
                f"but route {route} expects {expected_classes}."
            )
        if evidence_class == "author_heuristic" and not seed.get("allow_author_heuristic_generation", False):
            raise ValueError(
                f"Candidate seed {graph_path} cannot generate from author_heuristic evidence without explicit approval."
            )

        external_required = bool(profile.get("counts_as_source_review_debt", False))
        route_review = factual.get(route, {"status": "not_reviewed", "claim_count": 0, "reviewed_at": None})
        if external_required and route_review["status"] != "source_supported":
            raise ValueError(
                f"Candidate seed {graph_path} is blocked: route {route} requires external review "
                f"but factual-review status is {route_review['status']}."
            )

        refs = unique_source_refs(seed)
        if not refs:
            raise ValueError(f"Candidate seed {graph_path} has no source references.")
        unverified: list[str] = []
        missing: list[str] = []
        for source_ref in refs:
            source = sources.get(source_ref)
            if source is None:
                missing.append(source_ref)
            elif source.get("status") != "source_verified":
                unverified.append(source_ref)
        if missing:
            raise ValueError(f"Candidate seed {graph_path} references unknown sources: {', '.join(missing)}")
        if unverified:
            raise ValueError(
                f"Candidate seed {graph_path} references sources that are not source_verified: {', '.join(unverified)}"
            )

        gates[graph_path] = {
            "eligible": True,
            "route": route,
            "evidence_class": evidence_class,
            "expected_evidence_classes": expected_classes,
            "external_review_required": external_required,
            "route_review_status": route_review["status"],
            "route_reviewed_claims": route_review["claim_count"],
            "route_reviewed_at": route_review["reviewed_at"],
            "verified_source_count": len(refs),
            "source_status": "source_verified",
        }

    return gates
