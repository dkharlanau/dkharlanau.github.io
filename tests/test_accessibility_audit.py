"""Tests for scripts/accessibility_audit.py."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "accessibility_audit.py"


def run_audit(site_dir: Path):
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site_dir), "--fail-on-critical"],
        capture_output=True,
        text=True,
        check=False,
    )


def write_valid_shell(site_dir: Path, body: str, *, filename: str = "index.html") -> None:
    (site_dir / filename).write_text(
        f"""<!DOCTYPE html>
<html lang="en">
<head><title>Test</title></head>
<body>
  <a class="skip-link" href="#content">Skip to main content</a>
  <header><nav><a href="/">Home</a></nav></header>
  <main id="content"><article>{body}</article></main>
  <footer><p>Footer</p></footer>
</body>
</html>
""",
        encoding="utf-8",
    )


def test_accessibility_audit_help():
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
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    write_valid_shell(
        site_dir,
        """
      <h1>Title</h1>
      <p><a href="/about">About this site</a></p>
      <img src="/photo.jpg" alt="A descriptive photo">
""",
    )
    result = run_audit(site_dir)
    assert result.returncode == 0
    assert "no critical issues" in result.stdout


def test_accessibility_audit_fails_critical_issues(tmp_path):
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    (site_dir / "bad.html").write_text(
        """<!DOCTYPE html>
<html lang="en">
<head><title>Bad</title></head>
<body><div>no landmarks</div></body>
</html>
""",
        encoding="utf-8",
    )
    result = run_audit(site_dir)
    assert result.returncode == 2
    assert "critical issue(s)" in result.stdout
    assert "bad.html: missing <main> landmark" in result.stdout


def test_accessibility_audit_excludes_prefix(tmp_path):
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
    result = run_audit(site_dir)
    assert result.returncode == 0
    assert "no critical issues" in result.stdout


def test_accessibility_audit_detects_warnings(tmp_path):
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    write_valid_shell(
        site_dir,
        """
      <h1>Title</h1>
      <h3>Skipped h3</h3>
      <a href="/more">read more</a>
      <img src="/photo.jpg">
""",
        filename="warnings.html",
    )
    result = run_audit(site_dir)
    assert result.returncode == 0
    assert "warning(s)" in result.stdout
    assert "skipped heading level" in result.stdout
    assert "generic anchor text" in result.stdout
    assert "image missing alt text" in result.stdout


def test_accessibility_audit_ignores_markup_strings_inside_script_and_style(tmp_path):
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    write_valid_shell(
        site_dir,
        """
      <h1>Title</h1>
      <h2>Rendered section</h2>
      <script>
        const fake = '<h4>Not rendered as static HTML</h4><a href="/more">read more</a><img src="/fake.jpg">';
      </script>
      <style>.demo::after { content: '<h5>also not markup</h5>'; }</style>
""",
    )
    result = run_audit(site_dir)
    assert result.returncode == 0
    assert "no warnings" in result.stdout


def test_accessibility_audit_detects_skip_after_heading_depth_resets(tmp_path):
    site_dir = tmp_path / "_site"
    site_dir.mkdir()
    write_valid_shell(
        site_dir,
        """
      <h1>Title</h1>
      <h2>First section</h2>
      <h3>Nested topic</h3>
      <h2>Second section</h2>
      <h4>This skips H3 after the new H2</h4>
""",
    )
    result = run_audit(site_dir)
    assert result.returncode == 0
    assert "skipped heading level (h2 to h4)" in result.stdout
