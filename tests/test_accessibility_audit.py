"""Tests for scripts/accessibility_audit.py."""

import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "accessibility_audit.py"


def test_accessibility_audit_help():
    """Script should print usage with --help and exit 0."""
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--help"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "--site-dir" in result.stdout
    assert "--fail-on-critical" in result.stdout


def test_accessibility_audit_missing_site_dir(tmp_path):
    """Script should exit 1 when site directory does not exist."""
    missing = tmp_path / "missing"
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(missing)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "site directory not found" in result.stderr


def test_accessibility_audit_passes_valid_page(tmp_path):
    """A minimal valid page should produce no critical issues."""
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    (site_dir / "index.html").write_text(
        """<!DOCTYPE html>
<html lang="en">
<head><title>Test</title></head>
<body>
  <a class="skip-link" href="#content">Skip to main content</a>
  <header><nav><a href="/">Home</a></nav></header>
  <main id="content">
    <article>
      <h1>Title</h1>
      <p><a href="/about">About this site</a></p>
      <img src="/photo.jpg" alt="A descriptive photo">
    </article>
  </main>
  <footer><p>Footer</p></footer>
</body>
</html>
""",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site_dir), "--fail-on-critical"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "no critical issues" in result.stdout


def test_accessibility_audit_fails_critical_issues(tmp_path):
    """Missing critical landmarks should cause failure with --fail-on-critical."""
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    (site_dir / "bad.html").write_text(
        """<!DOCTYPE html>
<html lang="en">
<head><title>Bad</title></head>
<body>
  <div>no landmarks</div>
</body>
</html>
""",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site_dir), "--fail-on-critical"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "critical issue(s)" in result.stdout
    assert "bad.html: missing <main> landmark" in result.stdout


def test_accessibility_audit_excludes_prefix(tmp_path):
    """Excluded path prefixes should not be audited."""
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    docs_dir = site_dir / "docs"
    docs_dir.mkdir()
    (docs_dir / "bad.html").write_text(
        """<!DOCTYPE html>
<html lang="en"><body><div>no landmarks</div></body></html>
""",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site_dir), "--fail-on-critical"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "no critical issues" in result.stdout


def test_accessibility_audit_detects_warnings(tmp_path):
    """Common warnings should be reported without failing (non-critical)."""
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    (site_dir / "warnings.html").write_text(
        """<!DOCTYPE html>
<html lang="en">
<head><title>Warnings</title></head>
<body>
  <a class="skip-link" href="#content">Skip to main content</a>
  <header><nav><a href="/">Home</a></nav></header>
  <main id="content">
    <article>
      <h1>Title</h1>
      <h3>Skipped h3</h3>
      <a href="/more">read more</a>
      <img src="/photo.jpg">
    </article>
  </main>
  <footer><p>Footer</p></footer>
</body>
</html>
""",
        encoding="utf-8",
    )
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site_dir), "--fail-on-critical"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "warning(s)" in result.stdout
    assert "skipped heading level" in result.stdout
    assert "generic anchor text" in result.stdout
    assert "image missing alt text" in result.stdout


def test_accessibility_warning_budget_exits_nonzero(tmp_path):
    """Warning budget should fail when non-critical warnings exceed the budget."""
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    (site_dir / "warnings.html").write_text(
        """<!DOCTYPE html>
<html lang="en">
<head><title>Warnings</title></head>
<body>
  <a class="skip-link" href="#content">Skip to main content</a>
  <header><nav><a href="/">Home</a></nav></header>
  <main id="content">
    <article>
      <h1>Title</h1>
      <h3>Skipped h3</h3>
    </article>
  </main>
  <footer><p>Footer</p></footer>
</body>
</html>
""",
        encoding="utf-8",
    )
    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--site-dir",
            str(site_dir),
            "--fail-on-critical",
            "--warning-budget",
            "0",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 3
    assert "warning budget exceeded" in result.stderr
