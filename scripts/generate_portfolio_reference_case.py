#!/usr/bin/env python3
"""Generate the Jekyll projection for the enterprise change reference case."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CASE_ROOT = ROOT / "products" / "reference-cases" / "enterprise-change-evidence-pack"
MANIFEST_PATH = CASE_ROOT / "manifest.json"
ARTIFACTS_PATH = CASE_ROOT / "expected-artifacts.json"
OUTPUT_PATH = ROOT / "_data" / "portfolio_reference_case.yml"
PROJECTION_SCHEMA_VERSION = "1.0"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_projection(manifest: dict, artifacts: dict) -> dict:
    status_counts = Counter(str(edge["status"]) for edge in manifest["edges"])
    files = artifacts["files"]
    return {
        "schema_version": PROJECTION_SCHEMA_VERSION,
        "projection": {
            "canonical_sources": [
                {
                    "path": "/products/reference-cases/enterprise-change-evidence-pack/manifest.json",
                    "sha256": sha256(MANIFEST_PATH),
                },
                {
                    "path": "/products/reference-cases/enterprise-change-evidence-pack/expected-artifacts.json",
                    "sha256": sha256(ARTIFACTS_PATH),
                },
            ],
            "policy": (
                "Generated presentation projection. Edit the reference-case manifest or "
                "expected-artifacts inventory, then run python3 "
                "scripts/generate_portfolio_reference_case.py."
            ),
        },
        "case_id": manifest["case_id"],
        "title": manifest["title"],
        "classification": manifest["classification"],
        "client_free": manifest["client_free"],
        "products": manifest["products"],
        "status_definitions": manifest["status_definitions"],
        "status_counts": {
            status: status_counts.get(status, 0)
            for status in ("implemented", "demonstration-only", "documented")
        },
        "edges": manifest["edges"],
        "boundaries": manifest["boundaries"],
        "artifacts": {
            "algorithm": artifacts["algorithm"],
            "digest_scope": artifacts["digest_scope"],
            "file_count": len(files),
            "total_bytes": sum(int(item["bytes"]) for item in files),
            "files": files,
            "assertions": artifacts["assertions"],
        },
        "urls": {
            "human": "/machine/portfolio/enterprise-change-evidence-pack/",
            "manifest": "/products/reference-cases/enterprise-change-evidence-pack/manifest.json",
            "expected_artifacts": "/products/reference-cases/enterprise-change-evidence-pack/expected-artifacts.json",
            "source": "https://github.com/dkharlanau/dkharlanau.github.io/tree/main/products/reference-cases/enterprise-change-evidence-pack",
            "integration_proposal": "https://github.com/dkharlanau/dkharlanau.github.io/issues/new?template=portfolio-integration.yml",
        },
    }


def render_projection(projection: dict) -> str:
    header = (
        "# Generated from the enterprise change reference-case manifest and artifact inventory. "
        "Do not edit by hand.\n"
    )
    return header + yaml.safe_dump(
        projection,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    )


def generate() -> str:
    return render_projection(build_projection(load_json(MANIFEST_PATH), load_json(ARTIFACTS_PATH)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when the Jekyll projection is stale.")
    args = parser.parse_args()
    rendered = generate()

    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(
                "portfolio reference-case projection is stale; run "
                "python3 scripts/generate_portfolio_reference_case.py"
            )
            return 1
        print("portfolio reference-case projection is current")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
