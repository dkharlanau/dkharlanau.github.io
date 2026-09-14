from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_root_feed_owns_primary_subscription_path():
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    feed = (ROOT / "feed.xml").read_text(encoding="utf-8")

    assert "path: /feed/jekyll-posts.xml" in config
    assert "permalink: /feed.xml" in feed
    assert "where: 'verified', true" in feed
    assert "where: 'status', 'reviewed'" in feed
    assert "limit: 20" in feed


def test_rss_feed_uses_same_verified_publication_boundary():
    rss = (ROOT / "rss.xml").read_text(encoding="utf-8")

    assert '<rss version="2.0"' in rss
    assert 'type="application/rss+xml"' in rss
    assert "where: 'verified', true" in rss
    assert "where: 'status', 'reviewed'" in rss
    assert '<guid isPermaLink="true">' in rss
    assert "date_to_rfc822" in rss


def test_browser_autodiscovery_points_to_real_feed_surfaces():
    head = (ROOT / "_includes" / "head.html").read_text(encoding="utf-8")
    blog_feed = (ROOT / "blog" / "feed.xml").read_text(encoding="utf-8")

    assert 'href="{{ \'/feed.xml\' | absolute_url }}"' in head
    assert 'href="{{ \'/blog/feed.xml\' | absolute_url }}"' in head
    assert "where: 'verified', true" in blog_feed
    assert "where: 'status', 'reviewed'" in blog_feed
