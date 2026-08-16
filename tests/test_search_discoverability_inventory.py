from pathlib import Path

from scripts.search_discoverability_inventory import build_records, classify


def test_draft_lab_stays_noindex():
    classification, reasons, critical, governed, indexable = classify(
        "labs/example/index.md",
        "/labs/example/",
        {
            "title": "Example Lab",
            "description": "Working example.",
            "status": "draft",
            "verified": False,
            "robots": "noindex,follow",
            "sitemap": False,
        },
    )
    assert governed is True
    assert indexable is False
    assert classification == "KEEP_NOINDEX"
    assert critical is False
    assert reasons == []


def test_draft_lab_cannot_escape_to_index():
    classification, reasons, critical, governed, indexable = classify(
        "labs/example/index.md",
        "/labs/example/",
        {
            "title": "Example Lab",
            "description": "Working example.",
            "status": "draft",
            "verified": False,
            "robots": "index,follow",
            "sitemap": True,
        },
    )
    assert governed is True
    assert indexable is True
    assert classification == "BLOCK_INDEX"
    assert critical is True
    assert any("publication gate" in reason for reason in reasons)


def test_reviewed_lab_can_be_indexed():
    classification, reasons, critical, governed, indexable = classify(
        "labs/example/index.md",
        "/labs/example/",
        {
            "title": "Example Lab",
            "description": "Reviewed example.",
            "status": "reviewed",
            "verified": True,
            "robots": "index,follow",
            "sitemap": True,
        },
    )
    assert governed is True
    assert indexable is True
    assert classification == "INDEX"
    assert critical is False
    assert reasons == []


def test_reviewed_lab_hidden_enters_review_queue():
    classification, reasons, critical, governed, indexable = classify(
        "labs/example/index.md",
        "/labs/example/",
        {
            "title": "Example Lab",
            "description": "Reviewed example.",
            "status": "reviewed",
            "verified": True,
            "robots": "noindex,follow",
            "sitemap": False,
        },
    )
    assert governed is True
    assert indexable is False
    assert classification == "REVIEW_TO_INDEX"
    assert critical is False
    assert any("still hidden" in reason for reason in reasons)


def test_html_lab_source_is_in_inventory(tmp_path: Path):
    (tmp_path / "_config.yml").write_text("url: https://example.com\n", encoding="utf-8")
    source = tmp_path / "labs" / "example" / "index.html"
    source.parent.mkdir(parents=True)
    source.write_text(
        "---\n"
        "layout: default\n"
        "title: Example HTML Lab\n"
        "description: HTML source with Jekyll front matter.\n"
        "status: draft\n"
        "verified: false\n"
        "robots: noindex,follow\n"
        "sitemap: false\n"
        "---\n"
        "<h1>Example</h1>\n",
        encoding="utf-8",
    )

    records = build_records(tmp_path)
    matching = [record for record in records if record.route == "/labs/example/"]
    assert len(matching) == 1
    assert matching[0].source_path == "labs/example/index.html"
    assert matching[0].classification == "KEEP_NOINDEX"
