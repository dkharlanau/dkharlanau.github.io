from __future__ import annotations

from pathlib import Path

import scripts.check_analytics_coverage as analytics


GA4 = """<!doctype html>
<html><head>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T2TS9NCN2N"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  gtag('js', new Date());
  gtag('config', 'G-T2TS9NCN2N');
</script>
</head><body><h1>Page</h1></body></html>
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_complete_ga4_snippet_passes(tmp_path: Path):
    write(tmp_path / "index.html", GA4)

    code, summary, findings = analytics.check_site(tmp_path)

    assert code == 0
    assert summary["total_html_pages"] == 1
    assert summary["tagged_html_pages"] == 1
    assert not findings


def test_missing_html_tag_fails(tmp_path: Path):
    write(tmp_path / "index.html", "<html><head></head><body></body></html>")

    code, summary, findings = analytics.check_site(tmp_path)

    assert code == 2
    assert summary["missing_html_pages"] == 1
    assert findings[0].path == "index.html"


def test_duplicate_ga4_config_fails(tmp_path: Path):
    write(
        tmp_path / "index.html",
        GA4.replace(
            "gtag('config', 'G-T2TS9NCN2N');",
            "gtag('config', 'G-T2TS9NCN2N');\n  gtag('config', 'G-T2TS9NCN2N');",
        ),
    )

    code, summary, findings = analytics.check_site(tmp_path)

    assert code == 2
    assert summary["duplicate_tag_pages"] == 1
    assert "duplicate GA4" in findings[0].reason


def test_non_html_analytics_marker_fails(tmp_path: Path):
    write(tmp_path / "index.html", GA4)
    write(tmp_path / "llms.txt", "https://www.googletagmanager.com/gtag/js?id=G-T2TS9NCN2N")

    code, summary, findings = analytics.check_site(tmp_path)

    assert code == 2
    assert summary["non_html_files_with_analytics"] == 1
    assert any(f.path == "llms.txt" for f in findings)
