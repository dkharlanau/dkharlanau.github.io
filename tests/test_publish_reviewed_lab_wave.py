from pathlib import Path

import pytest

import scripts.publish_reviewed_lab_wave as publisher


def test_update_page_marks_reviewed_but_keeps_search_closed(tmp_path: Path, monkeypatch):
    monkeypatch.setattr(publisher, "ROOT", tmp_path)
    path = tmp_path / "labs" / "example" / "index.html"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\n"
        "title: Example\n"
        "status: draft\n"
        "verified: false\n"
        "robots: noindex,follow\n"
        "sitemap: false\n"
        "---\n"
        "<p>Working model</p>\n"
        "<p>Reviewed source-backed facts and an authored diagnostic frame.</p>\n",
        encoding="utf-8",
    )

    cfg = {
        "source_path": "labs/example/index.html",
        "search_intent": "Example search intent",
        "review_replacements": [
            {"from": "<p>Working model</p>", "to": "<p>Reviewed model</p>"}
        ],
    }

    changed = publisher.update_page(
        "/labs/example/", cfg, "example-wave", "2026-08-16"
    )
    assert changed == "labs/example/index.html"

    text = path.read_text(encoding="utf-8")
    assert "status: reviewed" in text
    assert "verified: true" in text
    assert "robots: noindex,follow" in text
    assert "sitemap: false" in text
    assert "<p>Reviewed model</p>" in text
    assert 'publication_wave: "example-wave"' in text
    assert 'search_intent: "Example search intent"' in text


def test_update_page_refuses_replacement_drift(tmp_path: Path, monkeypatch):
    monkeypatch.setattr(publisher, "ROOT", tmp_path)
    path = tmp_path / "labs" / "example" / "index.html"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\n"
        "title: Example\n"
        "status: draft\n"
        "verified: false\n"
        "robots: noindex,follow\n"
        "sitemap: false\n"
        "---\n"
        "<p>Different text</p>\n",
        encoding="utf-8",
    )

    cfg = {
        "source_path": "labs/example/index.html",
        "search_intent": "Example search intent",
        "review_replacements": [
            {"from": "<p>Working model</p>", "to": "<p>Reviewed model</p>"}
        ],
    }

    with pytest.raises(RuntimeError, match="expected review marker not found"):
        publisher.update_page("/labs/example/", cfg, "example-wave", "2026-08-16")


def test_validate_wave_requires_human_review_candidate():
    wave = {
        "reviewed_at": "2026-08-16",
        "min_structural_score": 5,
        "required_factual_status": "source_supported",
        "routes": {
            "/labs/example/": {
                "source_path": "labs/example/index.html",
                "search_intent": "Example search intent",
            }
        },
    }
    readiness = {
        "/labs/example/": {
            "route": "/labs/example/",
            "source_path": "labs/example/index.html",
            "state": "public_or_indexable",
            "priority": "P1",
            "structural_score": 5,
            "verified": True,
            "status": "reviewed",
            "factual_review": {"status": "source_supported"},
        }
    }

    with pytest.raises(RuntimeError, match="human_review_candidate"):
        publisher.validate_wave("example-wave", wave, readiness)
