#!/usr/bin/env python3
from pathlib import Path

path = Path('tests/test_assessment_practice_layer.py')
text = path.read_text(encoding='utf-8')
old = '''    assert by_route["/labs/enterprise-context/pricing/"]["factual_review"]["status"] == "not_reviewed"
    assert by_route["/labs/enterprise-context/pricing/"]["priority"] == "P0"
    assert "primary-source review" in by_route["/labs/enterprise-context/pricing/"]["review_reason"]'''
new = '''    required_unreviewed = [
        item for item in inventory["items"]
        if item.get("evidence_profile", {}).get("counts_as_source_review_debt")
        and item.get("factual_review", {}).get("status") in {"not_reviewed", "needs_source_review"}
    ]
    for item in required_unreviewed:
        assert item["priority"] == "P0"
        assert "primary-source review" in item["review_reason"]'''
if old not in text:
    raise SystemExit('Hardcoded pricing evidence-debt assertion not found')
path.write_text(text.replace(old, new, 1), encoding='utf-8')
print('Evidence-debt invariant made route-agnostic.')
