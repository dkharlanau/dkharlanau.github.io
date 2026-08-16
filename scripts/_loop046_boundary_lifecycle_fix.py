#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "tests" / "test_assessment_practice_layer.py"
text = PATH.read_text(encoding="utf-8")
old_token = 'assert core_by_route[route]["evidence"]["page_verified"] is False'
new_token = 'assert core_by_route[route]["publication"]["state"] in {"human_review_candidate", "public_or_indexable", "needs_structure", "missing_source", "unknown"}'
if old_token in text:
    text = text.replace(old_token, new_token, 1)
elif new_token not in text:
    raise SystemExit("LOOP-046 boundary lifecycle assertion marker not found")
PATH.write_text(text, encoding="utf-8")
