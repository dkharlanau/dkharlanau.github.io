import json
import os
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Optional
from unittest.mock import MagicMock, patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

# Import the module under test; if it doesn't exist yet, tests will fail
# and serve as a spec for the hardened script.
indexnow_mod = pytest.importorskip("scripts.indexnow_submit", reason="indexnow_submit.py not importable as module")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_md(tmp_path: Path, rel: str, frontmatter: str) -> Path:
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(f"---\n{frontmatter}\n---\n# Content\n", encoding="utf-8")
    return p


def _make_site_sitemap(tmp_path: Path, urls: list[str]) -> Path:
    """Create a minimal _site/sitemap-pages.xml with the given URLs."""
    site_dir = tmp_path / "_site"
    site_dir.mkdir(exist_ok=True)
    body = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        body += f"  <url><loc>{url}</loc></url>\n"
    body += "</urlset>\n"
    (site_dir / "sitemap-pages.xml").write_text(body, encoding="utf-8")
    return site_dir


@contextmanager
def _patch_sitemap_bypass():
    """Context manager patches that bypass sitemap and built-site noindex checks."""
    with patch.object(
        indexnow_mod, "filter_urls_by_sitemap", lambda urls, site_dir: (urls, {})
    ):
        with patch.object(
            indexnow_mod, "check_url_noindex_in_site", lambda url, site_dir: (True, None)
        ):
            yield


def _make_built_html(tmp_path: Path, rel_url: str, robots: Optional[str] = None) -> Path:
    """Create a built HTML file under _site for a canonical URL path."""
    site_dir = tmp_path / "_site"
    rel = rel_url.lstrip("/")
    if not rel:
        html_path = site_dir / "index.html"
    else:
        html_path = site_dir / rel / "index.html"
    html_path.parent.mkdir(parents=True, exist_ok=True)
    meta = ""
    if robots:
        meta = f'<meta name="robots" content="{robots}">'
    html_path.write_text(f"<!DOCTYPE html><html><head>{meta}<title>t</title></head><body></body></html>", encoding="utf-8")
    return html_path


# ---------------------------------------------------------------------------
# IndexNow: default dry-run / no submit without --submit
# ---------------------------------------------------------------------------


def test_indexnow_defaults_to_dry_run_no_submit(monkeypatch, capsys):
    """Without --submit, the script must default to dry-run and not call the API."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    with _patch_sitemap_bypass():
        with patch.object(indexnow_mod, "submit") as mock_submit:
            try:
                result = indexnow_mod.main([])
            except SystemExit as exc:
                result = exc.code
            # dry_run=True means submit is called with dry_run=True
            mock_submit.assert_called_once()
            # dry_run is passed as keyword argument
            assert mock_submit.call_args[1].get("dry_run") is True
            assert result in (0, None)


def test_indexnow_explicit_submit_calls_api(monkeypatch):
    """With --submit, the script must call the API."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    with _patch_sitemap_bypass():
        with patch.object(indexnow_mod, "submit") as mock_submit:
            try:
                result = indexnow_mod.main(["--submit", "--all"])
            except SystemExit as exc:
                result = exc.code
            mock_submit.assert_called_once()
            assert mock_submit.call_args[1].get("dry_run") is False


# ---------------------------------------------------------------------------
# IndexNow: rejects missing key for real submit
# ---------------------------------------------------------------------------


def test_indexnow_rejects_missing_key_for_real_submit(monkeypatch, capsys):
    """Real submit (--submit) without a key must exit with error."""
    monkeypatch.delenv("INDEXNOW_KEY", raising=False)
    with patch.object(indexnow_mod, "load_key", return_value=""):
        result = indexnow_mod.main(["--submit", "--all"])
        assert result != 0


def test_indexnow_dry_run_allows_missing_key(monkeypatch, capsys):
    """Dry-run without a key must succeed and not call the API."""
    monkeypatch.delenv("INDEXNOW_KEY", raising=False)
    with patch.object(indexnow_mod, "load_key", return_value=""):
        with _patch_sitemap_bypass():
            with patch.object(indexnow_mod, "submit") as mock_submit:
                try:
                    result = indexnow_mod.main([])
                except SystemExit as exc:
                    result = exc.code
                mock_submit.assert_called_once()
                assert mock_submit.call_args[1].get("dry_run") is True
                assert result in (0, None)


# ---------------------------------------------------------------------------
# IndexNow: filters noindex / research / unverified Atlas
# ---------------------------------------------------------------------------


def test_indexnow_filters_noindex_pages(tmp_path, monkeypatch):
    """Markdown files with robots:noindex must be skipped."""
    monkeypatch.chdir(tmp_path)
    md = _make_md(tmp_path, "notes/noindex.md", 'robots: noindex\npermalink: /notes/noindex/')
    assert indexnow_mod.is_indexable("notes/noindex.md", md)[0] is False


def test_indexnow_filters_research_pages(tmp_path, monkeypatch):
    """Paths under research/ must be skipped regardless of frontmatter."""
    monkeypatch.chdir(tmp_path)
    md = _make_md(tmp_path, "research/experiment.md", 'permalink: /research/experiment/')
    assert indexnow_mod.is_indexable("research/experiment.md", md)[0] is False


def test_indexnow_filters_unverified_atlas(tmp_path, monkeypatch):
    """Atlas pages that are not verified + reviewed must be skipped."""
    monkeypatch.chdir(tmp_path)
    md = _make_md(tmp_path, "atlas/draft.md", 'permalink: /atlas/draft/\nverified: false\nstatus: draft')
    assert indexnow_mod.is_indexable("atlas/draft.md", md)[0] is False


def test_indexnow_allows_verified_atlas(tmp_path, monkeypatch):
    """Verified and reviewed Atlas pages must be indexable."""
    monkeypatch.chdir(tmp_path)
    md = _make_md(tmp_path, "atlas/reviewed.md", 'permalink: /atlas/reviewed/\nverified: true\nstatus: reviewed')
    assert indexnow_mod.is_indexable("atlas/reviewed.md", md)[0] is True


# ---------------------------------------------------------------------------
# IndexNow: --from-git-diff maps changed files safely
# ---------------------------------------------------------------------------


def test_indexnow_from_git_diff_maps_changed_files(monkeypatch, tmp_path):
    """--from-git-diff must convert changed file paths to canonical URLs."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    fake_git_output = "about.md\nnotes/hello.md\n"
    with patch("subprocess.check_output", return_value=fake_git_output):
        with _patch_sitemap_bypass():
            with patch.object(indexnow_mod, "submit") as mock_submit:
                try:
                    indexnow_mod.main(["--submit", "--from-git-diff", "HEAD~1", "HEAD"])
                except SystemExit as exc:
                    pass
                mock_submit.assert_called_once()
                urls = mock_submit.call_args[0][0]
                assert any("/about/" in u for u in urls)


def test_indexnow_from_git_diff_ignores_non_public_files(monkeypatch):
    """--from-git-diff must ignore vendor, .git, _site, scripts, tests paths."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    # Include one valid file so submit gets called; rest should be skipped
    fake_git_output = "about.md\nvendor/bundle.js\n.git/config\n_site/index.html\nscripts/test.py\n"
    with patch("subprocess.check_output", return_value=fake_git_output):
        with _patch_sitemap_bypass():
            with patch.object(indexnow_mod, "submit") as mock_submit:
                try:
                    indexnow_mod.main(["--submit", "--from-git-diff", "HEAD~1", "HEAD"])
                except SystemExit as exc:
                    pass
                mock_submit.assert_called_once()
                urls = mock_submit.call_args[0][0]
                assert not any("vendor" in u for u in urls)
                assert not any("/.git/" in u for u in urls)
                assert not any("_site" in u for u in urls)


# ---------------------------------------------------------------------------
# IndexNow: reports skipped files with reasons
# ---------------------------------------------------------------------------


def test_indexnow_reports_skipped_files(capsys, monkeypatch, tmp_path):
    """When files are skipped, the script should print the path and reason."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_md(tmp_path, "research/skip.md", 'permalink: /research/skip/')
    with patch.object(indexnow_mod, "submit"):
        try:
            indexnow_mod.main(["--submit", "--urls", "research/skip.md"])
        except SystemExit:
            pass
    captured = capsys.readouterr()
    assert "skip" in captured.out.lower() or "skip" in captured.err.lower()


# ---------------------------------------------------------------------------
# IndexNow: --max-urls enforcement
# ---------------------------------------------------------------------------


def test_indexnow_max_urls_enforcement(monkeypatch):
    """--max-urls N must limit the number of submitted URLs."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    fake_urls = {
        "https://dkharlanau.github.io/a/",
        "https://dkharlanau.github.io/b/",
        "https://dkharlanau.github.io/c/",
    }
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with _patch_sitemap_bypass():
            with patch.object(indexnow_mod, "submit") as mock_submit:
                try:
                    indexnow_mod.main(["--submit", "--all", "--max-urls", "2"])
                except SystemExit as exc:
                    pass
                mock_submit.assert_called_once()
                urls = mock_submit.call_args[0][0]
                assert len(urls) <= 2


def test_indexnow_max_urls_zero_means_no_submit(monkeypatch):
    """--max-urls 0 should result in no URLs submitted."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    fake_urls = {"https://dkharlanau.github.io/a/"}
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit") as mock_submit:
            try:
                indexnow_mod.main(["--submit", "--all", "--max-urls", "0"])
            except SystemExit as exc:
                pass
            mock_submit.assert_not_called()


# ---------------------------------------------------------------------------
# IndexNow: --require-key-file behavior
# ---------------------------------------------------------------------------


def test_indexnow_require_key_file_allows_when_file_exists(monkeypatch, tmp_path):
    """--require-key-file with key file present should succeed."""
    monkeypatch.setenv("INDEXNOW_KEY", "env-key")
    key_file = tmp_path / "env-key.txt"
    key_file.write_text("env-key", encoding="utf-8")
    with patch.object(indexnow_mod, "REPO_ROOT", tmp_path):
        with patch.object(indexnow_mod, "submit"):
            try:
                result = indexnow_mod.main(["--submit", "--require-key-file", "--all"])
            except SystemExit as exc:
                result = exc.code
            assert result in (0, None)


def test_indexnow_require_key_file_rejects_when_file_missing(monkeypatch, tmp_path):
    """--require-key-file must fail if key file is missing."""
    monkeypatch.setenv("INDEXNOW_KEY", "env-key")
    with patch.object(indexnow_mod, "REPO_ROOT", tmp_path):
        result = indexnow_mod.main(["--submit", "--require-key-file", "--all"])
        assert result != 0


def test_indexnow_require_key_file_accepts_file(monkeypatch, tmp_path):
    """--require-key-file with a .env.local file present should succeed."""
    env_local = tmp_path / ".env.local"
    env_local.write_text('INDEXNOW_KEY="file-key"\n', encoding="utf-8")
    key_file = tmp_path / "file-key.txt"
    key_file.write_text("file-key", encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("INDEXNOW_KEY", raising=False)
    with patch.object(indexnow_mod, "REPO_ROOT", tmp_path):
        with patch.object(indexnow_mod, "submit"):
            try:
                result = indexnow_mod.main(["--submit", "--require-key-file", "--all"])
            except SystemExit as exc:
                result = exc.code
            assert result in (0, None)


# ---------------------------------------------------------------------------
# IndexNow: sitemap-backed filtering
# ---------------------------------------------------------------------------


def test_indexnow_sitemap_filter_excludes_missing_urls(monkeypatch, tmp_path):
    """URLs not present in the generated sitemap must be skipped."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_site_sitemap(tmp_path, ["https://dkharlanau.github.io/about/"])
    _make_built_html(tmp_path, "/about/")
    _make_built_html(tmp_path, "/notes/excluded/")
    fake_urls = {
        "https://dkharlanau.github.io/about/",
        "https://dkharlanau.github.io/notes/excluded/",
    }
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit") as mock_submit:
            try:
                indexnow_mod.main(["--submit", "--all", "--site-dir", str(tmp_path / "_site")])
            except SystemExit as exc:
                pass
            mock_submit.assert_called_once()
            urls = mock_submit.call_args[0][0]
            assert "https://dkharlanau.github.io/about/" in urls
            assert "https://dkharlanau.github.io/notes/excluded/" not in urls


def test_indexnow_sitemap_filter_includes_public_urls(monkeypatch, tmp_path):
    """URLs present in the generated sitemap must be included."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_site_sitemap(tmp_path, [
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/services/",
    ])
    _make_built_html(tmp_path, "")
    _make_built_html(tmp_path, "/services/")
    fake_urls = {
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/services/",
    }
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit") as mock_submit:
            try:
                indexnow_mod.main(["--submit", "--all", "--site-dir", str(tmp_path / "_site")])
            except SystemExit as exc:
                pass
            mock_submit.assert_called_once()
            urls = mock_submit.call_args[0][0]
            assert "https://dkharlanau.github.io/" in urls
            assert "https://dkharlanau.github.io/services/" in urls


# ---------------------------------------------------------------------------
# IndexNow: fail-closed guardrails on selected URLs
# ---------------------------------------------------------------------------


def test_indexnow_fails_if_noindex_url_selected(monkeypatch, tmp_path):
    """If a selected URL has robots:noindex in built HTML, submission must fail."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_site_sitemap(tmp_path, ["https://dkharlanau.github.io/notes/bad/"])
    _make_built_html(tmp_path, "/notes/bad/", robots="noindex, follow")
    fake_urls = {"https://dkharlanau.github.io/notes/bad/"}
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit") as mock_submit:
            result = indexnow_mod.main(["--submit", "--all", "--site-dir", str(tmp_path / "_site")])
            assert result != 0
            mock_submit.assert_not_called()


def test_indexnow_fails_if_sitemap_false_url_selected(monkeypatch, tmp_path):
    """If a selected URL has robots:noindex (sitemap:false pages typically also noindex), submission must fail."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_site_sitemap(tmp_path, ["https://dkharlanau.github.io/notes/private/"])
    _make_built_html(tmp_path, "/notes/private/", robots="noindex")
    fake_urls = {"https://dkharlanau.github.io/notes/private/"}
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit") as mock_submit:
            result = indexnow_mod.main(["--submit", "--all", "--site-dir", str(tmp_path / "_site")])
            assert result != 0
            mock_submit.assert_not_called()


# ---------------------------------------------------------------------------
# IndexNow: INDEXNOW_KEY_LOCATION support
# ---------------------------------------------------------------------------


def test_indexnow_reads_key_from_location(monkeypatch, tmp_path):
    """INDEXNOW_KEY_LOCATION env var should be used as an alternative key source."""
    key_file = tmp_path / "key.txt"
    key_file.write_text("location-key", encoding="utf-8")
    monkeypatch.delenv("INDEXNOW_KEY", raising=False)
    monkeypatch.setenv("INDEXNOW_KEY_LOCATION", str(key_file))
    with patch.object(indexnow_mod, "submit"):
        try:
            result = indexnow_mod.main(["--submit", "--all"])
        except SystemExit as exc:
            result = exc.code
        assert result in (0, None)


# ---------------------------------------------------------------------------
# IndexNow: report artifact
# ---------------------------------------------------------------------------


def test_indexnow_dry_run_writes_report(monkeypatch, tmp_path):
    """Dry-run mode must write a JSON report with submitted and skipped URLs."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_site_sitemap(tmp_path, ["https://dkharlanau.github.io/about/"])
    _make_built_html(tmp_path, "/about/")
    fake_urls = {"https://dkharlanau.github.io/about/"}
    report_path = tmp_path / "report.json"
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit"):
            try:
                indexnow_mod.main([
                    "--all",
                    "--site-dir", str(tmp_path / "_site"),
                    "--report", str(report_path),
                ])
            except SystemExit as exc:
                pass
    assert report_path.exists()
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["mode"] == "dry-run"
    assert "https://dkharlanau.github.io/about/" in report["submitted"]
    assert report["summary"]["submitted_count"] == 1


def test_indexnow_submit_writes_report(monkeypatch, tmp_path):
    """Submit mode must write a JSON report with mode=submit."""
    monkeypatch.setenv("INDEXNOW_KEY", "test-key-123")
    monkeypatch.chdir(tmp_path)
    _make_site_sitemap(tmp_path, ["https://dkharlanau.github.io/services/"])
    _make_built_html(tmp_path, "/services/")
    fake_urls = {"https://dkharlanau.github.io/services/"}
    report_path = tmp_path / "report.json"
    with patch.object(indexnow_mod, "discover_indexable_urls", return_value=(fake_urls, {})):
        with patch.object(indexnow_mod, "submit"):
            try:
                indexnow_mod.main([
                    "--submit",
                    "--all",
                    "--site-dir", str(tmp_path / "_site"),
                    "--report", str(report_path),
                ])
            except SystemExit as exc:
                pass
    assert report_path.exists()
    report = json.loads(report_path.read_text(encoding="utf-8"))
    assert report["mode"] == "submit"
    assert "https://dkharlanau.github.io/services/" in report["submitted"]
    assert report["summary"]["submitted_count"] == 1
