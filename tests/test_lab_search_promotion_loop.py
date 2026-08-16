import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from scripts.lab_search_promotion_loop import PromotionCandidate, apply_promotions


def candidate(source_path: str) -> PromotionCandidate:
    return PromotionCandidate(
        route="/labs/example/",
        source_path=source_path,
        title="Example",
        search_intent="Example search intent",
        publication_state="READY_TO_PROMOTE",
        assessment_priority="P1",
        factual_status="source_supported",
        human_verification_required=True,
        score=90,
        word_count=1200,
        internal_links=5,
        external_links=3,
        evidence_urls=6,
        h1_count=1,
        reasons=[],
    )


def test_apply_refuses_unreviewed_page(tmp_path: Path):
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

    with pytest.raises(RuntimeError):
        apply_promotions(tmp_path, [candidate("labs/example/index.html")])

    text = path.read_text(encoding="utf-8")
    assert "robots: noindex,follow" in text
    assert "sitemap: false" in text


def test_apply_only_opens_search_after_review(tmp_path: Path):
    path = tmp_path / "labs" / "example" / "index.html"
    path.parent.mkdir(parents=True)
    path.write_text(
        "---\n"
        "title: Example\n"
        "status: reviewed\n"
        "verified: true\n"
        "robots: noindex,follow\n"
        "sitemap: false\n"
        "---\n"
        "<h1>Example</h1>\n",
        encoding="utf-8",
    )

    changed = apply_promotions(tmp_path, [candidate("labs/example/index.html")])
    assert changed == ["labs/example/index.html"]

    text = path.read_text(encoding="utf-8")
    assert "robots: index,follow" in text
    assert "sitemap: true" in text
