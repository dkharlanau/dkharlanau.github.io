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
