"""Adversarial fixtures: audit findings must not manufacture quality or 404s."""
import json
from pathlib import Path

from scripts.lib.content_model import ContentPage
from scripts.lib.content_signals import RenderedPage, prose_lines, rendered_review, source_review_signals
from scripts.content_quality import check_source_pages, load_config, semantic_signal_groups


def page(body, route="/guide/", **extra):
    values = dict(source_path=Path(route.strip("/") + ".md"), body=body, permalink=route,
                  canonical_url="https://example.test" + route, title="A diagnostic question",
                  description="A complete practical description.", content_model="diagnostic")
    values.update(extra)
    return ContentPage(**values)


def test_fence_length_and_marker_must_match():
    lines, fence = prose_lines("````md\n```\nTODO\n~~~~\n````\nActual prose.")
    assert fence is None
    assert lines == [(6, "Actual prose.")]
    assert prose_lines("~~~sql\nSELECT 1\n```")[1] == ("~", 3, 1)


def test_integrity_signals_do_not_scan_code_examples_as_authoring_residue():
    good = page("# Guide\n\n```text\nTODO: example issue\nAs an AI model\n```\n\nCompleted answer.")
    assert not any(item["rule_id"].startswith("INTEGRITY") for item in source_review_signals([good])["findings"])
    broken = page("# Guide\n\nTODO: finish\n\n## Last section")
    rules = {item["rule_id"] for item in source_review_signals([broken])["findings"]}
    assert {"INTEGRITY002_EMPTY_END_SECTION", "INTEGRITY003_DRAFT_MARKER"} <= rules


def test_html_code_templates_do_not_create_false_unclosed_fences_or_tables():
    body = '<p>A complete opening paragraph explains the practical problem and offers the reader a useful decision with explicit conditions for checking the result.</p>\n<pre><code>```\n[example]\n```</code></pre>\n<pre><code>| A | B |\n|---|---|\n</code></pre>'
    report = source_review_signals([page(body)])
    assert not any(item["rule_id"].startswith("INTEGRITY") for item in report["findings"])
    assert report["pages"]["guide.md"]["intro_paragraph_present"] is True


def test_short_reference_is_not_called_low_quality():
    report = source_review_signals([page("A compact definition.", content_model="reference")])
    assert all(item["severity"] == "warning" for item in report["findings"])
    assert "score" not in report["pages"]["guide.md"]
    assert not any(item["rule_id"] == "SEMANTIC002_EXAMPLE_REVIEW" for item in report["findings"])


def test_repeated_paragraphs_are_hash_only_candidates_and_noindex_excluded():
    paragraph = " ".join(["Synthetic useful evidence explains a repeatable decision."] * 12)
    pages = [page(paragraph, f"/guide-{i}/") for i in range(3)]
    pages += [page(paragraph, "/private-draft/", robots="noindex,follow")]
    report = source_review_signals(pages)
    assert len(report["exact_body_candidates"]) == 1
    assert len(report["repeated_paragraph_candidates"][0]["paths"]) == 3
    assert paragraph not in json.dumps(report)


def test_all_configured_semantic_rules_have_an_implementation():
    config = load_config()
    required = {rule for model in config["content_models"].values() for rule in model["required_signals"]}
    assert required <= set(semantic_signal_groups(None))
    findings, _ = check_source_pages([page("A bland sentence.", content_model="technical_guide")], [], config)
    assert {"CONTENT_STEPS", "CONTENT_CONSTRAINTS", "CONTENT_NEXT_ACTION"} <= {item.rule_id for item in findings}


def test_main_extraction_excludes_navigation_and_json_but_keeps_readable_examples():
    html = '<nav><a href="/x/">Global</a></nav><main><h1>Answer</h1><p>Direct explanation.</p><pre>SELECT 1</pre><a href="/useful/">Action</a><aside><a href="/x/">Sidebar</a></aside><script type="application/ld+json">{"@type":"Article"}</script></main>'
    result = RenderedPage(html)
    assert ("/x/", False) in result.links
    assert ("/useful/", True) in result.links
    assert "Direct explanation." in " ".join(result.text)
    assert "SELECT 1" in " ".join(result.text)
    assert "Article" not in " ".join(result.text)
    assert len(result.jsonld) == 1


def emit(root, route, body, robots="index,follow,max-image-preview:large", canonical=None):
    path = root / route.strip("/") / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'<html><head><link href="{canonical or "https://example.test" + route}" rel="canonical"><meta content="{robots}" name="robots"></head><body>{body}</body></html>')


def sitemap(root, urls):
    (root / "sitemap.xml").write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{url}</loc></url>' for url in urls) + '</urlset>')


def test_rendered_graph_resolves_relative_query_and_same_host_links(tmp_path):
    emit(tmp_path, "/hub/", '<main><a href="../guide/?context=hub#step">Guide</a><a href="https://external.test/">Other</a></main>')
    emit(tmp_path, "/guide/", '<main>Answer</main><nav><a href="/hub/">Home</a></nav>')
    sitemap(tmp_path, ["https://example.test/guide/"])
    report = rendered_review(tmp_path, [page("Answer")], "https://example.test")
    assert report["contextual_edges"] == 1
    assert report["pages"][0]["contextual_inbound_pages"] == 1
    assert report["pages"][0]["crawl_policy"]["Googlebot"] is None
    assert report["issues"] == []


def test_sitemap_rejects_noindex_noncanonical_and_missing_targets(tmp_path):
    emit(tmp_path, "/guide/", "<main>Draft</main>", robots="noindex", canonical="https://example.test/canonical/")
    sitemap(tmp_path, ["https://example.test/guide/", "https://example.test/missing/"])
    report = rendered_review(tmp_path, [page("Draft")], "https://example.test")
    assert {item["rule_id"] for item in report["issues"]} == {"DISCOVERY003_NOINDEX_SITEMAP", "DISCOVERY004_CANONICAL_SITEMAP", "DISCOVERY005_MISSING_SITEMAP_TARGET"}


def test_sitemap_index_is_recursive_and_accepts_relative_build_directory(tmp_path, monkeypatch):
    emit(tmp_path, "/guide/", "<main>Answer</main>")
    (tmp_path / "sitemap.xml").write_text('<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><sitemap><loc>https://example.test/nested.xml</loc></sitemap></sitemapindex>')
    (tmp_path / "nested.xml").write_text('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://example.test/guide/</loc></url></urlset>')
    (tmp_path / "robots.txt").write_text("User-agent: OAI-SearchBot\nDisallow: /guide/\nUser-agent: *\nAllow: /\n")
    monkeypatch.chdir(tmp_path)
    report = rendered_review(Path("."), [page("Answer")], "https://example.test")
    assert report["sitemap"]["urls"] == 1
    assert report["pages"][0]["crawl_policy"] == {"Googlebot": True, "OAI-SearchBot": False, "Bingbot": True}


def test_bad_sitemap_is_reported_not_silently_empty(tmp_path):
    (tmp_path / "sitemap.xml").write_text("not XML")
    report = rendered_review(tmp_path, [], "https://example.test")
    assert report["issues"][0]["rule_id"] == "DISCOVERY001_SITEMAP_UNREADABLE"


def test_changed_scope_never_hides_hard_publication_failure(monkeypatch):
    import scripts.content_quality as quality
    audit = {"summary": {"changed_paths": ["changed.md"]}, "findings": [{"severity": "error", "source_path": "unchanged.md", "rule_id": "PRIVACY002_SENSITIVE_VALUE", "message": "Redacted safety finding."}]}
    monkeypatch.setattr(quality, "run_audit", lambda *args: audit)
    assert quality.main(["check", "--changed-from", "origin/main"]) == 2
