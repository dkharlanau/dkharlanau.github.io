#!/usr/bin/env python3
"""Fail CI when a Lab route becomes indexable before the publication gate is complete."""

from __future__ import annotations

import argparse
from pathlib import Path

from search_discoverability_inventory import build_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".")
    args = parser.parse_args()

    repo = Path(args.repo_dir).resolve()
    lab_records = [r for r in build_records(repo) if r.route.startswith("/labs/")]

    blockers = [
        r for r in lab_records
        if r.classification in {"BLOCK_INDEX", "MERGE_OR_FIX_ROUTE", "REVIEW_METADATA"}
        or (r.critical and r.indexable)
    ]

    if blockers:
        print(f"Lab publication gate failed: {len(blockers)} route(s)")
        for record in blockers[:50]:
            print(f"  - {record.route} [{record.classification}] {'; '.join(record.reasons)}")
        return 2

    publishable_hidden = [r for r in lab_records if r.classification == "REVIEW_TO_INDEX"]
    print(f"Lab publication gate passed for {len(lab_records)} route(s).")
    if publishable_hidden:
        print(f"  Reviewed+verified but still noindex: {len(publishable_hidden)}")
        for record in publishable_hidden[:20]:
            print(f"  - {record.route}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
