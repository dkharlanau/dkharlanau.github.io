from pathlib import Path

from scripts import indexnow_submit


def _write_sitemap(site_dir: Path, urls: list[str]) -> None:
    site_dir.mkdir(parents=True, exist_ok=True)
    rows = "\n".join(f"  <url><loc>{url}</loc></url>" for url in urls)
    (site_dir / "sitemap-pages.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{rows}\n"
        "</urlset>\n",
        encoding="utf-8",
    )


def test_robots_change_expands_to_core_public_urls():
    urls, reason = indexnow_submit.public_url_for_path("robots.txt")

    assert reason is None
    assert f"{indexnow_submit.BASE_URL}/" in urls
    assert f"{indexnow_submit.BASE_URL}/about/" in urls
    assert f"{indexnow_submit.BASE_URL}/services/" in urls
    assert len(urls) > 1


def test_robots_change_survives_sitemap_filter(tmp_path: Path):
    site_dir = tmp_path / "_site"
    expected = [
        f"{indexnow_submit.BASE_URL}/",
        f"{indexnow_submit.BASE_URL}/about/",
        f"{indexnow_submit.BASE_URL}/services/",
    ]
    _write_sitemap(site_dir, expected)

    candidates, reason = indexnow_submit.public_url_for_path("robots.txt")
    selected, skipped = indexnow_submit.filter_urls_by_sitemap(candidates, site_dir)

    assert reason is None
    assert set(expected).issubset(selected)
    assert f"{indexnow_submit.BASE_URL}/robots.txt" in skipped


def test_release_waits_for_live_parity_and_keeps_failed_baseline(tmp_path, monkeypatch):
    import json

    release = indexnow_submit.indexnow_release
    page = release.SearchDocument(
        '<html><head><title>SAP ATP Is Not Inventory</title>'
        '<link rel="canonical" href="https://dkharlanau.github.io/atlas/concepts/sap-atp-is-not-inventory/">'
        '</head><body><main><h1>SAP ATP is not inventory</h1></main></body></html>'
    )
    url = page.canonicals[0]
    base = {"commit": "a" * 40, "pages": {}}
    candidate = {"commit": "b" * 40, "generator": release.GENERATOR, "digest": "c" * 64,
                 "pages": {url: {"signature": release.digest(page.parts), "lastmod": None}}}
    root = tmp_path / "release"
    root.mkdir()
    (root / "release.json").write_text(json.dumps({
        "state": "ready", "baseline": "accepted_manifest", "deployment": 1,
        "commit": candidate["commit"], "artifact": {},
    }))
    base["digest"] = "d" * 64
    monkeypatch.setattr(release, "load_manifest", lambda *args: base)
    monkeypatch.setattr(release, "build_manifest", lambda *args: candidate)
    monkeypatch.setattr(indexnow_submit, "load_key", lambda: "test-key")
    monkeypatch.setattr(indexnow_submit, "verify_active_pages", lambda *args: None)
    sent = []
    monkeypatch.setattr(indexnow_submit, "submit", lambda urls, key, dry_run: sent.extend(urls) or 200)
    report = tmp_path / "report.json"
    args = ["--pages-release", str(root), "--submit", "--report", str(report)]
    # The deployed response still exposes the old signature.
    def stale(*args):
        raise ValueError("Live canonical HTML differs from the release")

    monkeypatch.setattr(release, "verify_live", stale)
    assert indexnow_submit.main(args) == 1
    assert not sent
    assert not (root / "manifest.json").exists()
    assert json.loads(report.read_text())["status"] == "blocked"

    monkeypatch.setattr(release, "verify_live", lambda *args: True)
    assert indexnow_submit.main(args) == 0
    assert sent == [url]
    assert json.loads(report.read_text())["http_status"] == 200
    assert json.loads((root / "manifest.json").read_text()) == candidate

    monkeypatch.setattr(release, "load_manifest", lambda *args: candidate)
    assert indexnow_submit.main(args) == 0
    assert sent == [url]
    assert json.loads(report.read_text())["status"] == "no_changes"
