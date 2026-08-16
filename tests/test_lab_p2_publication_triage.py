from scripts.lab_p2_publication_triage import (
    KEEP_INTERNAL_NOINDEX,
    KEEP_PRACTICE_NOINDEX,
    NEEDS_POLICY_DECISION,
    POLICY_ERROR,
    PUBLIC_REVIEW_NEXT,
    classify_item,
)


def item(route: str, *, source_debt: bool = False, factual_status: str = "not_reviewed") -> dict:
    return {
        "route": route,
        "factual_review": {"status": factual_status},
        "evidence_profile": {"counts_as_source_review_debt": source_debt},
    }


def test_public_framework_without_source_debt_can_enter_editorial_review():
    route = "/labs/ai-ready/"
    public = {
        route: {
            "search_intent": "practical AI architecture",
            "reason": "Public authored framework.",
        }
    }
    decision, _, intent = classify_item(item(route), public, set(), set())
    assert decision == PUBLIC_REVIEW_NEXT
    assert intent == "practical AI architecture"


def test_public_framework_with_required_unreviewed_source_debt_is_blocked():
    route = "/labs/example/"
    public = {route: {"search_intent": "example framework"}}
    decision, _, _ = classify_item(
        item(route, source_debt=True, factual_status="needs_source_review"),
        public,
        set(),
        set(),
    )
    assert decision == POLICY_ERROR


def test_practice_route_stays_noindex():
    route = "/labs/assessment/mock/"
    decision, _, _ = classify_item(item(route), {}, {route}, set())
    assert decision == KEEP_PRACTICE_NOINDEX


def test_authoring_and_assessment_routes_stay_internal():
    authoring = "/labs/assessment/factual-review/"
    decision, _, _ = classify_item(item(authoring), {}, set(), {authoring})
    assert decision == KEEP_INTERNAL_NOINDEX

    other = "/labs/assessment/custom-control/"
    decision, _, _ = classify_item(item(other), {}, set(), set())
    assert decision == KEEP_INTERNAL_NOINDEX


def test_unknown_non_assessment_candidate_requires_policy_decision():
    decision, _, _ = classify_item(
        item("/labs/unknown-framework/"), {}, set(), set()
    )
    assert decision == NEEDS_POLICY_DECISION
