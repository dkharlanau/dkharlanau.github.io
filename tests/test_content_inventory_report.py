"""Tests for scripts/content_inventory_report.py."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "content_inventory_report.py"


def write_fixture(repo_dir: Path, site_dir: Path) -> None:
    source_dir = repo_dir / "atlas" / "concepts"
    source_dir.mkdir(parents=True)
    (source_dir / "sample.md").write_text(
        """---
title: Sample Atlas Page
description: Source-backed sample description.
status: reviewed
verified: true
sitemap: true
permalink: /atlas/concepts/sample/
---

# Sample Atlas Page

This source body is used only for inventory matching.
""",
        encoding="utf-8",
    )

    page_dir = site_dir / "atlas" / "concepts" / "sample"
    page_dir.mkdir(parents=True)
    (page_dir / "index.html").write_text(
        """<!doctype html>
<html><head>
<title>Sample Atlas Page</title>
<meta name="description" content="Built sample description.">
<meta name="robots" content="index,follow">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article"}</script>
</head><body>
<main><h1>Sample Atlas Page</h1>
<p>This page has enough words for a small test fixture and links back to the home page.</p>
<a href="/">Home</a>
</main>
</body></html>
""",
        encoding="utf-8",
    )

    (site_dir / "index.html").write_text(
        """<!doctype html>
<html><head>
<title>Home</title>
<meta name="description" content="Home description.">
<meta name="robots" content="index,follow">
</head><body>
<main><h1>Home</h1><a href="/atlas/concepts/sample/">Sample</a></main>
</body></html>
""",
        encoding="utf-8",
    )


def test_summary_mode_writes_no_report_file(tmp_path: Path) -> None:
    repo_dir = tmp_path / "repo"
    site_dir = tmp_path / "site"
    repo_dir.mkdir()
    site_dir.mkdir()
    write_fixture(repo_dir, site_dir)
    output = tmp_path / "inventory.json"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo-dir",
            str(repo_dir),
            "--site-dir",
            str(site_dir),
            "--summary",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    summary = json.loads(result.stdout)
    assert summary["pages"] == 2
    assert summary["source_matched_pages"] == 1
    assert not output.exists()


def test_json_output_uses_explicit_path_and_core_fields(tmp_path: Path) -> None:
    repo_dir = tmp_path / "repo"
    site_dir = tmp_path / "site"
    repo_dir.mkdir()
    site_dir.mkdir()
    write_fixture(repo_dir, site_dir)
    output = tmp_path / "reports" / "inventory.json"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo-dir",
            str(repo_dir),
            "--site-dir",
            str(site_dir),
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    data = json.loads(output.read_text(encoding="utf-8"))
    assert data["schema"] == "dkharlanau.content_inventory_report"
    page = next(row for row in data["pages"] if row["url_path"] == "/atlas/concepts/sample/")
    assert page["section"] == "atlas"
    assert page["source_path"] == "atlas/concepts/sample.md"
    assert page["title"] == "Sample Atlas Page"
    assert page["status"] == "reviewed"
    assert page["verified"] is True
    assert page["schema_types"] == ["Article"]
    assert page["inlink_count"] == 1


def test_csv_output_contains_inventory_rows(tmp_path: Path) -> None:
    repo_dir = tmp_path / "repo"
    site_dir = tmp_path / "site"
    repo_dir.mkdir()
    site_dir.mkdir()
    write_fixture(repo_dir, site_dir)
    output = tmp_path / "inventory.csv"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--repo-dir",
            str(repo_dir),
            "--site-dir",
            str(site_dir),
            "--output",
            str(output),
            "--format",
            "csv",
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    text = output.read_text(encoding="utf-8")
    assert "page,url_path,url,section,source_path" in text
    assert "atlas/concepts/sample/index.html,/atlas/concepts/sample/" in text
