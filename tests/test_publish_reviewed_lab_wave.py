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
    assert 'evidence_review_mode: "product_primary"' in text


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


def wave_fixture() -> dict:
    return {
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


def readiness_fixture(
    *,
    state="human_review_candidate",
    score=5,
    verified=False,
    status="draft",
    priority="P1",
    factual_status="source_supported",
    source_debt=True,
) -> dict:
    return {
        "/labs/example/": {
            "route": "/labs/example/",
            "source_path": "labs/example/index.html",
            "state": state,
            "priority": priority,
            "structural_score": score,
            "verified": verified,
            "status": status,
            "factual_review": {"status": factual_status},
            "evidence_profile": {"counts_as_source_review_debt": source_debt},
        }
    }


def test_validate_wave_requires_human_review_candidate():
    with pytest.raises(RuntimeError, match="human_review_candidate"):
        publisher.validate_wave(
            "example-wave",
            wave_fixture(),
            readiness_fixture(state="public_or_indexable", verified=True, status="reviewed"),
        )


def test_preflight_can_defer_structure_but_full_gate_cannot():
    wave = wave_fixture()
    readiness = readiness_fixture(score=4)

    publisher.validate_wave(
        "example-wave", wave, readiness, require_structure=False
    )

    with pytest.raises(RuntimeError, match="structural score below 5"):
        publisher.validate_wave(
            "example-wave", wave, readiness, require_structure=True
        )


def selective_wave_fixture() -> dict:
    return {
        "reviewed_at": "2026-08-16",
        "review_mode": "selective_or_heuristic",
        "min_structural_score": 5,
        "routes": {
            "/labs/example/": {
                "source_path": "labs/example/index.html",
                "search_intent": "Example authored framework",
            }
        },
    }


def test_selective_wave_requires_explicit_public_framework_and_no_open_source_debt():
    wave = selective_wave_fixture()
    readiness = readiness_fixture(
        priority="P2",
        factual_status="not_reviewed",
        source_debt=False,
    )

    publisher.validate_wave(
        "selective-wave",
        wave,
        readiness,
        public_frameworks={"/labs/example/"},
    )

    with pytest.raises(RuntimeError, match="not an explicit public framework"):
        publisher.validate_wave(
            "selective-wave",
            wave,
            readiness,
            public_frameworks=set(),
        )

    debt = readiness_fixture(
        priority="P2",
        factual_status="not_reviewed",
        source_debt=True,
    )
    with pytest.raises(RuntimeError, match="primary-source review debt"):
        publisher.validate_wave(
            "selective-wave",
            wave,
            debt,
            public_frameworks={"/labs/example/"},
        )


def test_selective_finalize_records_editorial_evidence_mode_without_opening_search(tmp_path: Path, monkeypatch):
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
        "<h1>Example</h1>\n",
        encoding="utf-8",
    )
    cfg = {
        "source_path": "labs/example/index.html",
        "search_intent": "Example authored framework",
    }

    publisher.finalize_page(
        "/labs/example/",
        cfg,
        "selective-wave",
        "2026-08-16",
        publisher.SELECTIVE_OR_HEURISTIC,
    )
    text = path.read_text(encoding="utf-8")
    assert 'evidence_review_mode: "selective_or_heuristic"' in text
    assert "selective external evidence + page-level editorial review" in text
    assert "robots: noindex,follow" in text
    assert "sitemap: false" in text
