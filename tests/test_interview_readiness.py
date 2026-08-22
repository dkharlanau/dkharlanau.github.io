from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PUBLIC_PAGES = [
    ROOT / "labs/interview-readiness/index.md",
    ROOT / "labs/interview-readiness/roadmap/index.md",
]

UTILITY_PAGES = [
    ROOT / "labs/interview-readiness/today/index.md",
    ROOT / "labs/interview-readiness/questions/index.md",
    ROOT / "labs/interview-readiness/stories/index.md",
    ROOT / "labs/interview-readiness/practice/index.md",
    ROOT / "labs/interview-readiness/progress/index.md",
]

ALL_PAGES = PUBLIC_PAGES + UTILITY_PAGES


def test_public_interview_readiness_pages_are_reviewed_and_indexable():
    for page in PUBLIC_PAGES:
        assert page.exists(), page
        text = page.read_text(encoding="utf-8")
        assert "status: reviewed" in text
        assert "verified: true" in text
        assert "robots: index,follow" in text
        assert "sitemap: true" in text


def test_interview_readiness_utility_pages_remain_working_noindex_surfaces():
    for page in UTILITY_PAGES:
        assert page.exists(), page
        text = page.read_text(encoding="utf-8")
        assert "verified: false" in text
        assert "robots: noindex,follow" in text
        assert "sitemap: false" in text


def test_interview_readiness_has_all_primary_routes():
    hub = (ROOT / "labs/interview-readiness/index.md").read_text(encoding="utf-8")
    for route in ("today", "roadmap", "questions", "stories", "practice", "progress"):
        assert f'/labs/interview-readiness/{route}/' in hub


def test_interview_readiness_shared_state_model_is_stable():
    script = (ROOT / "assets/js/interview-readiness.js").read_text(encoding="utf-8")
    assert "sapInterviewReadinessV1" in script
    assert "sapInterviewPracticeV1" in script
    assert "sapInterviewStoryBankV1" in script
    for state in ("not-reviewed", "refreshed", "explain", "defend"):
        assert state in script
    for track in ("sales", "logistics", "integration", "ai", "leadership"):
        assert f"{track}:" in script


def test_interview_readiness_stays_in_the_labs_product_not_homepage_chrome():
    home = (ROOT / "index.md").read_text(encoding="utf-8")
    header = (ROOT / "_includes" / "header.html").read_text(encoding="utf-8")
    footer = (ROOT / "_includes" / "footer.html").read_text(encoding="utf-8")
    labs = (ROOT / "labs" / "index.md").read_text(encoding="utf-8")
    assert "SAP Lead interview preparation" not in home
    assert 'href="/labs/interview-readiness/"' not in header + footer
    assert 'href="/labs/interview-readiness/"' in labs


def test_labs_hub_exposes_interview_readiness():
    labs = (ROOT / "labs/index.md").read_text(encoding="utf-8")
    assert 'href="/labs/interview-readiness/"' in labs
    assert "SAP Lead Interview Readiness" in labs
