import hashlib
import json
from pathlib import Path
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "products" / "reference-cases" / "enterprise-change-evidence-pack"
MANIFEST = CASE_ROOT / "manifest.json"
ARTIFACTS = CASE_ROOT / "expected-artifacts.json"
PROJECTION = ROOT / "_data" / "portfolio_reference_case.yml"


def test_reference_case_projection_preserves_sources_edges_and_boundaries():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    artifacts = json.loads(ARTIFACTS.read_text(encoding="utf-8"))
    projection = yaml.safe_load(PROJECTION.read_text(encoding="utf-8"))

    source_hashes = {
        item["path"]: item["sha256"] for item in projection["projection"]["canonical_sources"]
    }
    assert source_hashes[
        "/products/reference-cases/enterprise-change-evidence-pack/manifest.json"
    ] == hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    assert source_hashes[
        "/products/reference-cases/enterprise-change-evidence-pack/expected-artifacts.json"
    ] == hashlib.sha256(ARTIFACTS.read_bytes()).hexdigest()

    assert projection["case_id"] == manifest["case_id"]
    assert projection["edges"] == manifest["edges"]
    assert projection["boundaries"] == manifest["boundaries"]
    assert projection["status_counts"] == {
        "implemented": 2,
        "demonstration-only": 2,
        "documented": 2,
    }
    assert projection["artifacts"]["file_count"] == len(artifacts["files"]) == 8
    assert projection["artifacts"]["total_bytes"] == sum(
        item["bytes"] for item in artifacts["files"]
    )
    assert projection["artifacts"]["files"] == artifacts["files"]
    assert projection["artifacts"]["assertions"] == artifacts["assertions"]


def test_reference_case_keeps_runtime_and_authority_claims_fail_closed():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    edges = {edge["id"]: edge for edge in manifest["edges"]}

    assert manifest["classification"] == "synthetic_public_reference_case"
    assert manifest["client_free"] is True
    assert manifest["boundaries"]["client_data_present"] is False
    assert manifest["boundaries"]["production_evidence_present"] is False
    assert manifest["boundaries"]["human_approval_present"] is False
    assert manifest["boundaries"]["authorization_or_execution_instruction_present"] is False
    assert edges["research-context-to-architecture-decision"]["status"] == "demonstration-only"
    assert edges["visual-render-to-project-assurance"]["status"] == "demonstration-only"
    assert edges["architecture-decision-to-visual-render"]["status"] == "implemented"
    assert edges["project-evidence-structural-analysis"]["status"] == "implemented"
    assert all(edge["boundary"].strip() for edge in edges.values())
    assert all(edge["verification_command"].strip() for edge in edges.values())
    assert all(edge["source_contract_url"].startswith("https://") for edge in edges.values())


def test_reference_case_projection_generator_check_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_portfolio_reference_case.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "projection is current" in result.stdout


def test_reference_case_page_uses_projection_and_preserves_noindex_boundary():
    page = (
        ROOT / "machine" / "portfolio" / "enterprise-change-evidence-pack" / "index.md"
    ).read_text(encoding="utf-8")
    head = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")

    assert "{% assign case = site.data.portfolio_reference_case %}" in page
    assert "status: needs_verification" in page
    assert "verified: false" in page
    assert "robots: noindex,follow" in page
    assert "sitemap: false" in page
    assert "case.edges" in page
    assert "case.artifacts.files" in page
    assert "python3 validate.py" in page
    assert "production authority are absent" in page
    assert "page.url contains '/machine/portfolio/'" in head
