from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_primary_atom_feed_uses_real_sources_not_build_clock():
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    feed = (ROOT / "feed.xml").read_text(encoding="utf-8")

    assert "path: /feed/jekyll-posts.xml" in config
    assert "permalink: /feed.xml" in feed
    assert "site.time" not in feed
    assert "site.data.changelog.entries" in feed
    assert "where: 'verified', true" in feed
    assert "where: 'status', 'reviewed'" in feed
    assert "limit: 30" in feed


def test_rss_feed_combines_trusted_publications_and_changelog():
    rss = (ROOT / "rss.xml").read_text(encoding="utf-8")

    assert '<rss version="2.0"' in rss
    assert 'type="application/rss+xml"' in rss
    assert "site.time" not in rss
    assert "site.data.changelog.entries" in rss
    assert "where: 'verified', true" in rss
    assert "where: 'status', 'reviewed'" in rss
    assert "entry.robots contains 'noindex'" in rss
    assert "entry.sitemap == false" in rss
    assert '<guid isPermaLink="true">' in rss
    assert '<guid isPermaLink="false">tag:dkharlanau.github.io' in rss
    assert "date_to_rfc822" in rss


def test_blog_atom_feed_uses_content_dates_not_build_clock():
    blog_feed = (ROOT / "blog" / "feed.xml").read_text(encoding="utf-8")

    assert "site.time" not in blog_feed
    assert "where: 'verified', true" in blog_feed
    assert "where: 'status', 'reviewed'" in blog_feed
    assert "last_modified_at" in blog_feed
    assert "entry.robots contains 'noindex'" in blog_feed
    assert "entry.sitemap == false" in blog_feed


def test_browser_autodiscovery_exposes_rss_from_common_template():
    machine_links = (ROOT / "_includes" / "seo" / "page-machine-links.html").read_text(encoding="utf-8")
    head = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")

    assert 'type="application/rss+xml"' in machine_links
    assert "'/rss.xml'" in machine_links
    assert 'type="application/atom+xml"' in head
    assert "'/feed.xml'" in head
    assert "'/blog/feed.xml'" in head
