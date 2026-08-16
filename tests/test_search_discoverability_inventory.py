from scripts.search_discoverability_inventory import classify


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
