from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def _page(title: str, canonical: str, robots: str) -> str:
    return f'''<!doctype html>
<html><head>
<title>{title}</title>
<meta name="description" content="A complete test description for indexability audit behavior." />
<meta name="robots" content="{robots}" />
<link rel="canonical" href="{canonical}" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="A complete test description for indexability audit behavior." />
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"WebPage"}}</script>
</head><body><h1>{title}</h1><p>Legacy canonical regression fixture.</p></body></html>'''


def test_noindex_legacy_alias_may_share_primary_canonical(tmp_path: Path) -> None:
    site = tmp_path / "_site"
    canonical_url = "https://dkharlanau.github.io/primary/"
    primary = site / "primary"
    legacy = site / "legacy"
    primary.mkdir(parents=True)
    legacy.mkdir(parents=True)
    (primary / "index.html").write_text(
        _page("Primary page", canonical_url, "index,follow"), encoding="utf-8"
    )
    (legacy / "index.html").write_text(
        _page("Legacy redirect", canonical_url, "noindex,follow"), encoding="utf-8"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "audit_indexability.py"),
            "--site-dir",
            str(site),
            "--repo-dir",
            str(tmp_path),
            "--output-dir",
            str(tmp_path / "reports"),
            "--fail-on-critical",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Duplicate canonical" not in result.stdout
