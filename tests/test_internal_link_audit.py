from pathlib import Path

from scripts.audit_internal_links import normalize_local_path


def test_normalize_local_path_preserves_static_file_extensions(tmp_path: Path):
    site_dir = tmp_path / "_site"
    page_dir = site_dir / "ai"
    page_dir.mkdir(parents=True)
    target = site_dir / "ai" / "catalog.json"
    target.write_text("{}", encoding="utf-8")

    resolved = normalize_local_path("/ai/catalog.json?version=1", site_dir, page_dir)

    assert resolved == target


def test_normalize_local_path_resolves_relative_pretty_urls(tmp_path: Path):
    site_dir = tmp_path / "_site"
    page_dir = site_dir / "atlas" / "diagnostics"
    target = site_dir / "atlas" / "concepts" / "index.html"
    target.parent.mkdir(parents=True)
    target.write_text("<html></html>", encoding="utf-8")

    resolved = normalize_local_path("../concepts/", site_dir, page_dir)

    assert resolved == target
