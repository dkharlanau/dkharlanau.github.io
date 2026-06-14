"""Tests for scripts/check_page_quality.py"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

import scripts.check_page_quality as pq


MINIMAL_ARTICLE = """<!doctype html>
<html lang="en"><head>
<title>Good Article Title</title>
<meta name="description" content="A useful description that is long enough to pass the quality gate without any issues.">
<link rel="canonical" href="https://dkharlanau.github.io/atlas/good-article/">
<meta property="og:title" content="Good Article Title">
<meta property="og:description" content="A useful description that is long enough to pass the quality gate without any issues.">
<meta property="og:url" content="https://dkharlanau.github.io/atlas/good-article/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Good Article Title",
  "description": "A useful description that is long enough to pass the quality gate without any issues.",
  "author": {"@type": "Person", "name": "Dzmitryi Kharlanau"},
  "publisher": {"@type": "Organization", "name": "Dzmitryi Kharlanau", "url": "https://dkharlanau.github.io"},
  "datePublished": "2026-01-15T00:00:00+00:00",
  "dateModified": "2026-02-20T00:00:00+00:00",
  "url": "https://dkharlanau.github.io/atlas/good-article/"
}
</script>
</head><body>
<main>
<h1>Good Article Title</h1>
<p class="lead">This is the lead paragraph that summarizes the article for the reader.</p>
<h2>Implementation guidance</h2>
<p>This is the first section of the article. It contains enough words to satisfy the minimum word count check and demonstrate a well structured page with meaningful content.</p>
<a href="/atlas/another-article/">Related article</a>
</main>
</body></html>
"""


def run_on_site(
    pages: dict[str, str],
    fail_on_critical: bool = False,
    warning_budget: Optional[int] = None,
) -> tuple[int, list[dict]]:
    from scripts.check_page_quality import main
    import sys
    import io

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel, content in pages.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

        argv = ["", "--site-dir", str(root)]
        if fail_on_critical:
            argv.append("--fail-on-critical")
        if warning_budget is not None:
            argv.extend(["--warning-budget", str(warning_budget)])
        argv.append("--json")

        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        old_argv = sys.argv
        try:
            sys.argv = argv
            code = main()
        finally:
            sys.stdout = old_stdout
            sys.argv = old_argv

        output = json.loads(buffer.getvalue())
        return code, output["findings"]


def test_minimal_article_passes():
    code, findings = run_on_site({"atlas/good-article/index.html": MINIMAL_ARTICLE})
    critical = [f for f in findings if f["severity"] == "critical"]
    assert code == 0
    assert not critical


def test_missing_h1_is_critical():
    content = MINIMAL_ARTICLE.replace("<h1>Good Article Title</h1>", "")
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_H1_MISSING" and f["severity"] == "critical" for f in findings)


def test_multiple_h1s_is_critical():
    content = MINIMAL_ARTICLE.replace("</h1>", "</h1>\n<h1>Second H1</h1>", 1)
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_H1_DUPLICATE" and f["severity"] == "critical" for f in findings)


def test_missing_meta_description_is_critical():
    content = MINIMAL_ARTICLE.replace(
        '<meta name="description" content="A useful description that is long enough to pass the quality gate without any issues.">',
        "",
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_META_DESCRIPTION_MISSING" and f["severity"] == "critical" for f in findings)


def test_missing_author_in_jsonld_is_critical():
    content = MINIMAL_ARTICLE.replace(
        '"author": {"@type": "Person", "name": "Dzmitryi Kharlanau"},',
        '"author": {"@type": "Person"},',
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_AUTHOR_NAME_MISSING" and f["severity"] == "critical" for f in findings)


def test_missing_publisher_in_jsonld_is_critical():
    content = MINIMAL_ARTICLE.replace(
        '"publisher": {"@type": "Organization", "name": "Dzmitryi Kharlanau", "url": "https://dkharlanau.github.io"},',
        "",
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_PUBLISHER_MISSING" and f["severity"] == "critical" for f in findings)


def test_date_modified_before_published_is_critical():
    content = MINIMAL_ARTICLE.replace(
        '"dateModified": "2026-02-20T00:00:00+00:00"',
        '"dateModified": "2026-01-10T00:00:00+00:00"',
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_DATE_ORDER_INVALID" and f["severity"] == "critical" for f in findings)


def test_placeholder_text_on_indexable_page_is_critical():
    content = MINIMAL_ARTICLE.replace(
        "<p class=\"lead\">This is the lead paragraph",
        "<p class=\"lead\">TODO: write the lead paragraph",
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "ARTICLE_PLACEHOLDER_TEXT" and f["severity"] == "critical" for f in findings)


def test_localhost_url_is_critical():
    content = MINIMAL_ARTICLE.replace(
        'href="https://dkharlanau.github.io/atlas/good-article/"',
        'href="http://localhost:4000/atlas/good-article/"',
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "LOCALHOST_URL" and f["severity"] == "critical" for f in findings)


def test_private_path_in_url_is_critical():
    content = MINIMAL_ARTICLE.replace(
        '<a href="/atlas/another-article/">Related article</a>',
        '<a href="/Users/dzmitryikharlanau/private.html">Related article</a>',
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "PRIVATE_PATH_LEAK" and f["severity"] == "critical" for f in findings)


def test_noindex_page_missing_title_is_not_critical():
    content = """<!doctype html>
<html><head>
<meta name="robots" content="noindex,follow">
<title></title>
</head><body>
<h1></h1>
</body></html>
"""
    code, findings = run_on_site({"atlas/diagnostics/review-candidate/index.html": content}, fail_on_critical=True)
    assert code == 0
    assert not any(f["severity"] == "critical" for f in findings)


def test_collection_page_missing_h1_is_critical():
    content = """<!doctype html>
<html><head>
<title>Collection Title</title>
<meta name="description" content="A collection of useful items for the site.">
<link rel="canonical" href="https://dkharlanau.github.io/skill-hub/">
</head><body>
<ul><li><a href="/skill-hub/item/">Item</a></li></ul>
</body></html>
"""
    code, findings = run_on_site({"skill-hub/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "COLLECTION_H1_MISSING" and f["severity"] == "critical" for f in findings)


def test_collection_page_does_not_require_article_jsonld():
    content = """<!doctype html>
<html><head>
<title>Collection Title</title>
<meta name="description" content="A collection of useful items for the site.">
<link rel="canonical" href="https://dkharlanau.github.io/skill-hub/">
</head><body>
<h1>Collection Title</h1>
<ul><li><a href="/skill-hub/item/">Item</a></li></ul>
</body></html>
"""
    code, findings = run_on_site({"skill-hub/index.html": content}, fail_on_critical=True)
    assert code == 0
    assert not any("ARTICLE" in f["rule"] and f["severity"] == "critical" for f in findings)


def test_warning_only_run_exits_zero():
    content = MINIMAL_ARTICLE.replace(
        '<meta name="description" content="A useful description that is long enough to pass the quality gate without any issues.">',
        '<meta name="description" content="A description that is short.">',
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 0
    assert any(f["rule"] == "ARTICLE_META_DESCRIPTION_SHORT" and f["severity"] == "warning" for f in findings)


def test_warning_budget_exceeded_exits_nonzero():
    content = MINIMAL_ARTICLE.replace(
        '<meta name="description" content="A useful description that is long enough to pass the quality gate without any issues.">',
        '<meta name="description" content="A description that is short.">',
    )
    code, findings = run_on_site(
        {"atlas/good-article/index.html": content},
        fail_on_critical=True,
        warning_budget=0,
    )
    assert code == 3
    assert any(f["severity"] == "warning" for f in findings)


def test_private_path_inside_code_block_is_not_critical():
    content = MINIMAL_ARTICLE.replace(
        "</main>",
        "<p>See <code>/Users/dzmitryikharlanau/private.md</code> for local notes.</p>\n</main>",
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 0
    assert not any(f["rule"] == "PRIVATE_PATH_LEAK" and f["severity"] == "critical" for f in findings)


def test_broken_template_token_outside_code_is_critical():
    content = MINIMAL_ARTICLE.replace(
        "<p class=\"lead\">This is the lead paragraph",
        "<p class=\"lead\">{{ page.lead }}</p>\n<p>This is the lead paragraph",
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 2
    assert any(f["rule"] == "BROKEN_TEMPLATE_TOKEN" and f["severity"] == "critical" for f in findings)


def test_placeholder_in_weak_example_is_not_critical():
    content = MINIMAL_ARTICLE.replace(
        "<p class=\"lead\">This is the lead paragraph",
        "<h3>Weak output</h3>\n<p>Owner: TBD.</p>\n<p class=\"lead\">This is the lead paragraph",
    )
    code, findings = run_on_site({"atlas/good-article/index.html": content}, fail_on_critical=True)
    assert code == 0
    assert not any(f["rule"] == "ARTICLE_PLACEHOLDER_TEXT" for f in findings)
