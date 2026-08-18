from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PAGES = [
    ROOT / "labs/interview-readiness/index.md",
    ROOT / "labs/interview-readiness/roadmap/index.md",
    ROOT / "labs/interview-readiness/questions/index.md",
    ROOT / "labs/interview-readiness/stories/index.md",
    ROOT / "labs/interview-readiness/practice/index.md",
    ROOT / "labs/interview-readiness/progress/index.md",
]


def test_interview_readiness_pages_exist_and_remain_unreviewed_labs():
    for page in PAGES:
        assert page.exists(), page
        text = page.read_text(encoding="utf-8")
        assert "verified: false" in text
        assert "robots: noindex,follow" in text
        assert "sitemap: false" in text


def test_interview_readiness_has_all_primary_routes():
    hub = (ROOT / "labs/interview-readiness/index.md").read_text(encoding="utf-8")
    for route in ("roadmap", "questions", "stories", "practice", "progress"):
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


def test_homepage_exposes_crawlable_interview_entry_points():
    home = (ROOT / "index.md").read_text(encoding="utf-8")
    assert "SAP Lead interview preparation" in home
    assert 'href="/labs/interview-readiness/"' in home
    assert 'href="/labs/interview-readiness/roadmap/"' in home
    assert 'href="/labs/interview-readiness/questions/"' in home


def test_labs_hub_exposes_interview_readiness():
    labs = (ROOT / "labs/index.md").read_text(encoding="utf-8")
    assert 'href="/labs/interview-readiness/"' in labs
    assert "SAP Lead Interview Readiness" in labs
