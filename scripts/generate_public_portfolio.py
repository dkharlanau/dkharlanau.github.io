#!/usr/bin/env python3
"""Generate the Jekyll public-portfolio projection from products/manifest.json."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "products" / "manifest.json"
OUTPUT_PATH = ROOT / "_data" / "public_portfolio.yml"
PROJECTION_SCHEMA_VERSION = "1.0"


def load_manifest(path: Path = MANIFEST_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_projection(manifest: dict, manifest_bytes: bytes) -> dict:
    reader_map = manifest["reader_map"]
    products = {product["id"]: product for product in manifest["products"]}
    projected_projects = []

    for track in reader_map["tracks"]:
        for role, field in (("primary", "primary_projects"), ("supporting", "supporting_projects")):
            for project_id in track[field]:
                product = products[project_id]
                projected_projects.append(
                    {
                        "id": product["id"],
                        "title": product["title"],
                        "track_id": track["id"],
                        "role": role,
                        "description": product["summary"],
                        "repository_url": product["repository"],
                        "public_url": product["page"],
                    }
                )

    return {
        "schema_version": PROJECTION_SCHEMA_VERSION,
        "id": reader_map["id"],
        "projection": {
            "canonical_source": "/products/manifest.json",
            "canonical_schema_version": manifest["schema_version"],
            "canonical_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
            "policy": (
                "Generated presentation projection. Edit products/manifest.json, then run "
                "python3 scripts/generate_public_portfolio.py."
            ),
        },
        "title": reader_map["title"],
        "description": reader_map["description"],
        "observed_at": reader_map["observed_at"],
        "human_url": reader_map["human_url"],
        "machine_url": reader_map["machine_url"],
        "scope": {
            "account": manifest["owner"],
            "repository_count": reader_map["repository_count"],
            "selection": reader_map["selection"],
            "excluded_repositories": reader_map["excluded_repositories"],
        },
        "boundaries": reader_map["boundaries"],
        "reference_case": reader_map["reference_case"],
        "actions": reader_map["actions"],
        "homepage": reader_map["homepage"],
        "tracks": reader_map["tracks"],
        "projects": projected_projects,
    }


def render_projection(projection: dict) -> str:
    header = "# Generated from products/manifest.json. Do not edit by hand.\n"
    return header + yaml.safe_dump(
        projection,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    )


def generate(manifest_path: Path = MANIFEST_PATH) -> str:
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    return render_projection(build_projection(manifest, manifest_bytes))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if _data/public_portfolio.yml is not the current deterministic projection.",
    )
    args = parser.parse_args()
    rendered = generate()

    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(
                "public portfolio projection is stale; run "
                "python3 scripts/generate_public_portfolio.py"
            )
            return 1
        print("public portfolio projection is current")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
