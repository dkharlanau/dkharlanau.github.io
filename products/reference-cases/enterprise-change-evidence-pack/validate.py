#!/usr/bin/env python3
"""Validate the bounded synthetic enterprise-change reference case."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parent
VALID_EDGE_STATUSES = {"implemented", "documented", "demonstration-only"}
REQUIRED_EDGE_IDS = {
    "research-context-to-architecture-decision",
    "architecture-decision-to-visual-render",
    "visual-render-to-project-assurance",
    "project-evidence-structural-analysis",
    "optional-reconciliation-to-cutover",
    "optional-cutover-to-project-assurance",
}
TRACE_TYPES = {"requirement", "decision", "mapping", "interface", "test", "defect", "change", "evidence"}
TEXT_SUFFIXES = {".json", ".md", ".py", ".svg"}
CYRILLIC = re.compile(r"[\u0400-\u04ff]")
SENSITIVE_TEXT = (
    re.compile("/" + "Users/"),
    re.compile(r"[A-Za-z]:\\" + r"Users\\", re.IGNORECASE),
    re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._~-]+", re.IGNORECASE),
)
FORBIDDEN_KEYS = {
    "client_name",
    "customer_name",
    "email",
    "phone",
    "password",
    "secret",
    "token",
    "credential",
    "authorization_header",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name}: expected a JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_payload_digest(payload: dict[str, Any]) -> str:
    data = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(data).hexdigest()


def validate_eac_reference(value: str) -> list[str]:
    errors: list[str] = []
    parsed = urlsplit(value)
    segments = [segment for segment in parsed.path.split("/") if segment]
    if parsed.scheme != "eac":
        errors.append("scheme must be eac")
    if parsed.netloc != "dkharlanau":
        errors.append("authority must be dkharlanau")
    if len(segments) < 4:
        errors.append("path must contain repository, kind, and a non-empty local identity")
    elif segments[:3] != ["dkharlanau.github.io", "reference-case", "enterprise-change-evidence-pack"]:
        errors.append("identity must remain owned by this reference case")
    query = parse_qs(parsed.query, keep_blank_values=True)
    if set(query) != {"version"} or query.get("version") != ["1.0.0"]:
        errors.append("query must contain exactly version=1.0.0")
    if parsed.fragment:
        errors.append("fragment is not allowed")
    return errors


def iter_keys(node: Any):
    if isinstance(node, dict):
        for key, value in node.items():
            yield str(key)
            yield from iter_keys(value)
    elif isinstance(node, list):
        for item in node:
            yield from iter_keys(item)


def validate_expected_file(root: Path, record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    relative = Path(str(record.get("path", "")))
    resolved = (root / relative).resolve()
    if not relative.as_posix() or not resolved.is_relative_to(root.resolve()):
        return ["expected artifact path escapes the case directory"]
    if not resolved.is_file():
        return [f"{relative.as_posix()}: expected file is missing"]
    digest = sha256_file(resolved)
    if digest != record.get("sha256"):
        errors.append(f"{relative.as_posix()}: SHA-256 mismatch")
    if resolved.stat().st_size != record.get("bytes"):
        errors.append(f"{relative.as_posix()}: byte-size mismatch")
    if not str(record.get("source_contract_url", "")).startswith("https://"):
        errors.append(f"{relative.as_posix()}: source_contract_url must use HTTPS")
    return errors


def validate_research_packet(packet: dict[str, Any], expected: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    integrity = packet.get("integrity")
    if not isinstance(integrity, dict):
        return ["research context integrity must be an object"]
    payload = {key: value for key, value in packet.items() if key != "integrity"}
    actual_payload_digest = canonical_payload_digest(payload)
    if actual_payload_digest != integrity.get("digest"):
        errors.append("research context canonical payload digest is invalid")
    if actual_payload_digest != expected.get("payload_digest"):
        errors.append("research context payload digest differs from expected metadata")
    if packet.get("schema_version") != expected.get("schema_version"):
        errors.append("research context schema version differs from expected metadata")
    boundary = packet.get("operational_boundary")
    if not isinstance(boundary, dict):
        errors.append("research context operational_boundary must be an object")
    else:
        if boundary.get("trust_level") != expected.get("trust_level"):
            errors.append("research context trust level is invalid")
        if boundary.get("requires_human_review") is not True:
            errors.append("research context must require human review")
        required_prohibitions = {"authorization", "execution", "production incident evidence", "automatic policy change"}
        if not required_prohibitions.issubset(set(boundary.get("prohibited_uses", []))):
            errors.append("research context is missing required prohibited uses")
    return errors


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if manifest.get("classification") != "synthetic_public_reference_case":
        errors.append("manifest classification must be synthetic_public_reference_case")
    if manifest.get("client_free") is not True or manifest.get("language") != "en":
        errors.append("manifest must be client-free and English-only")
    products = manifest.get("products", [])
    product_ids = {item.get("id") for item in products if isinstance(item, dict)}
    if len(product_ids) != len(products):
        errors.append("manifest products must have unique IDs")
    edges = manifest.get("edges", [])
    edge_ids = {item.get("id") for item in edges if isinstance(item, dict)}
    if edge_ids != REQUIRED_EDGE_IDS:
        errors.append("manifest edge inventory is incomplete or contains unexpected edges")
    for edge in edges:
        if not isinstance(edge, dict):
            errors.append("manifest edges must be objects")
            continue
        edge_id = str(edge.get("id", "unnamed"))
        if edge.get("producer") not in product_ids or edge.get("consumer") not in product_ids:
            errors.append(f"{edge_id}: producer and consumer must exist in products")
        if edge.get("status") not in VALID_EDGE_STATUSES:
            errors.append(f"{edge_id}: unsupported status")
        if not str(edge.get("source_contract_url", "")).startswith("https://"):
            errors.append(f"{edge_id}: source_contract_url must use HTTPS")
        if not str(edge.get("verification_command", "")).strip():
            errors.append(f"{edge_id}: verification_command is required")
        if not str(edge.get("boundary", "")).strip():
            errors.append(f"{edge_id}: boundary is required")
        for evidence_path in edge.get("evidence_paths", []):
            resolved = (ROOT / str(evidence_path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                errors.append(f"{edge_id}: evidence path is missing or escapes the case directory")
    identities = manifest.get("case_owned_identities", [])
    if len(identities) != len(set(identities)):
        errors.append("case-owned identities must be unique")
    for value in identities:
        errors.extend(f"{value}: {error}" for error in validate_eac_reference(str(value)))
    boundaries = manifest.get("boundaries", {})
    required_false = {
        "client_data_present",
        "production_evidence_present",
        "human_approval_present",
        "authorization_or_execution_instruction_present",
        "universal_eac_resolver_assumed",
    }
    for key in required_false:
        if boundaries.get(key) is not False:
            errors.append(f"manifest boundary {key} must be false")
    return errors


def validate_blueprint(blueprint: dict[str, Any], expected: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if blueprint.get("schemaVersion") != expected.get("schema_version"):
        errors.append("Composer blueprint schema version differs from expected metadata")
    decisions = blueprint.get("decisionRecords", [])
    matches = [item for item in decisions if item.get("id") == expected.get("decision_id")]
    if len(matches) != 1:
        errors.append("Composer blueprint must contain exactly one expected decision record")
    else:
        decision = matches[0]
        if decision.get("status") != expected.get("decision_status"):
            errors.append("Composer decision status differs from expected metadata")
        if decision.get("effectiveDecision") != expected.get("effective_decision"):
            errors.append("Composer effective decision differs from expected metadata")
        rationale = str(decision.get("rationale", "")).lower()
        if "synthetic" not in rationale or "not a production approval" not in rationale:
            errors.append("Composer decision rationale must retain the synthetic non-approval boundary")
    integrations = (blueprint.get("blueprint") or {}).get("integrations", [])
    sales_order = [item for item in integrations if item.get("id") == "integration.sales-order-request"]
    if len(sales_order) != 1:
        errors.append("Composer blueprint is missing integration.sales-order-request")
    else:
        analysis = sales_order[0].get("decisionAnalysis") or {}
        if analysis.get("effectivePatternId") != expected.get("effective_decision"):
            errors.append("Composer integration does not use the expected effective decision")
        if analysis.get("humanDecisionStatus") != expected.get("decision_status"):
            errors.append("Composer integration does not retain the expected synthetic decision status")
    return errors


def validate_project_graph(graph: dict[str, Any], manifest: dict[str, Any], expected_files: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    nodes = graph.get("nodes", [])
    node_ids = [str(item.get("id", "")) for item in nodes if isinstance(item, dict)]
    if len(node_ids) != len(set(node_ids)) or any(not item for item in node_ids):
        errors.append("Project Evidence nodes must have unique non-empty IDs")
    known = set(node_ids)
    for node in nodes:
        if node.get("type") not in TRACE_TYPES:
            errors.append(f"{node.get('id')}: unsupported Project Evidence node type")
    seen_links: set[tuple[str, str, str]] = set()
    for link in graph.get("links", []):
        key = (str(link.get("from", "")), str(link.get("type", "")), str(link.get("to", "")))
        if key in seen_links:
            errors.append(f"duplicate Project Evidence link: {key}")
        seen_links.add(key)
        if key[0] not in known or key[2] not in known:
            errors.append(f"broken Project Evidence link: {key}")
    identities = set(manifest.get("case_owned_identities", []))
    digest_paths = {
        "EVID-RESEARCH-001": "fixtures/research-context.json",
        "EVID-DECISION-BASIS-001": "fixtures/decision-basis.json",
        "EVID-BLUEPRINT-001": "artifacts/architecture.blueprint.json",
        "EVID-VISUAL-SOURCE-001": "artifacts/architecture.visual.txt",
        "EVID-VISUAL-RENDER-001": "artifacts/architecture.executive.svg",
    }
    indexed = {item.get("id"): item for item in nodes if isinstance(item, dict)}
    for node_id, path in digest_paths.items():
        node = indexed.get(node_id, {})
        if node.get("artifact_ref") not in identities:
            errors.append(f"{node_id}: artifact_ref must be a case-owned identity")
        expected_digest = expected_files[path]["sha256"]
        if node.get("document_sha256") != f"sha256:{expected_digest}":
            errors.append(f"{node_id}: document digest does not match expected metadata")
    decision = indexed.get("DEC-ARCH-001", {})
    if decision.get("production_decision") is not False or decision.get("human_approval") is not False:
        errors.append("Project Evidence decision must remain synthetic and unapproved")
    boundary = graph.get("boundary", {})
    if boundary.get("visual_to_assurance_adapter") != "absent":
        errors.append("Project Evidence boundary must declare the absent visual-to-assurance adapter")
    if boundary.get("production_readiness_claimed") is not False or boundary.get("authorization_claimed") is not False:
        errors.append("Project Evidence boundary must not claim production readiness or authorization")
    return errors


def validate_public_text() -> list[str]:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES or "__pycache__" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT).as_posix()
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.rstrip(" \t") != line:
                errors.append(f"{relative}:{line_number}: trailing whitespace")
        if CYRILLIC.search(text):
            errors.append(f"{relative}: contains Cyrillic text")
        for pattern in SENSITIVE_TEXT:
            if pattern.search(text):
                errors.append(f"{relative}: contains a forbidden sensitive-text pattern")
        if path.suffix == ".json":
            data = json.loads(text)
            forbidden = sorted({key.lower() for key in iter_keys(data)} & FORBIDDEN_KEYS)
            if forbidden:
                errors.append(f"{relative}: contains forbidden keys: {', '.join(forbidden)}")
    return errors


def validate_case() -> list[str]:
    errors: list[str] = []
    manifest = load_json(ROOT / "manifest.json")
    expected = load_json(ROOT / "expected-artifacts.json")
    expected_records = expected.get("files", [])
    expected_files = {str(record.get("path")): record for record in expected_records if isinstance(record, dict)}
    if len(expected_files) != len(expected_records):
        errors.append("expected artifact paths must be unique")
    for record in expected_records:
        if isinstance(record, dict):
            errors.extend(validate_expected_file(ROOT, record))
        else:
            errors.append("expected artifact records must be objects")
    errors.extend(validate_manifest(manifest))

    research = load_json(ROOT / "fixtures" / "research-context.json")
    errors.extend(validate_research_packet(research, expected["assertions"]["research_context"]))
    basis = load_json(ROOT / "fixtures" / "decision-basis.json")
    claim_ids = {item.get("id") for item in research.get("claims", []) if isinstance(item, dict)}
    selected = {item.get("claim_id") for item in basis.get("selected_claims", []) if isinstance(item, dict)}
    if not selected or not selected.issubset(claim_ids):
        errors.append("decision-basis selected claims must exist in the research packet")
    basis_boundary = basis.get("boundary", {})
    if basis_boundary.get("runtime_adapter_exists") is not False or basis_boundary.get("automatic_adoption") is not False:
        errors.append("decision-basis must retain the demonstration-only adapter boundary")
    if basis.get("architecture_context", {}).get("human_review_status") != "not_performed":
        errors.append("decision-basis must not imply completed human review")

    blueprint = load_json(ROOT / "artifacts" / "architecture.blueprint.json")
    errors.extend(validate_blueprint(blueprint, expected["assertions"]["architecture_blueprint"]))

    visual = (ROOT / "artifacts" / "architecture.visual.txt").read_text(encoding="utf-8")
    visual_assertions = expected["assertions"]["visual_projection"]
    if f'"title": "{visual_assertions["title"]}"' not in visual:
        errors.append("visual projection title differs from expected metadata")
    for view_id in visual_assertions["named_views"]:
        if f'"id": "{view_id}"' not in visual:
            errors.append(f"visual projection is missing named view {view_id}")
    if "Create sales order · Synchronous API" not in visual:
        errors.append("visual projection does not retain the effective synthetic architecture decision")
    svg = (ROOT / "artifacts" / "architecture.executive.svg").read_text(encoding="utf-8")
    if f"<title id=\"vwb-title\">{visual_assertions['executive_render_title']}</title>" not in svg:
        errors.append("executive SVG title differs from expected metadata")

    graph = load_json(ROOT / "fixtures" / "project-evidence.json")
    errors.extend(validate_project_graph(graph, manifest, expected_files))
    analysis = load_json(ROOT / "artifacts" / "project-evidence.analysis.json")
    analysis_expected = expected["assertions"]["project_evidence_analysis"]
    validation = analysis.get("validation", {})
    traceability = analysis.get("traceability", {})
    for key in ("valid", "node_count", "link_count"):
        if validation.get(key) != analysis_expected.get(key):
            errors.append(f"Project Evidence analysis {key} differs from expected metadata")
    for key in ("test_coverage", "evidence_coverage"):
        if traceability.get(key) != analysis_expected.get(key):
            errors.append(f"Project Evidence analysis {key} differs from expected metadata")

    errors.extend(validate_public_text())
    return errors


def main() -> int:
    try:
        errors = validate_case()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"reference-case validation failed: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    expected = load_json(ROOT / "expected-artifacts.json")
    manifest = load_json(ROOT / "manifest.json")
    print(
        "OK: enterprise-change-evidence-pack "
        f"({len(expected['files'])} hashed files, {len(manifest['edges'])} bounded edges)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
