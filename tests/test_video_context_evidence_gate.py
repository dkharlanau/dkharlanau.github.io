"""Regression tests for the synthetic context-evidence teaching example."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "labs/ai-ready/video-lessons/examples/context-evidence-gate.py"
CASES = ROOT / "labs/ai-ready/video-lessons/examples/context-cases.json"


def load_module():
    spec = importlib.util.spec_from_file_location("context_evidence_gate", EXAMPLE)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_synthetic_cases_match_expected_status():
    module = load_module()
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    assert len(cases) == 3
    for case in cases:
        result = module.assess(case, now="2026-11-11T10:30:00Z")
        assert result["status"] == case["expected_status"]
        assert result["write_allowed"] is False


def test_stale_and_untrusted_target_evidence_cannot_support_diagnosis():
    module = load_module()
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    for case in cases[1:]:
        result = module.assess(case, now="2026-11-11T10:30:00Z")
        assert result["status"] == "insufficient_evidence"
        assert result["findings"]
        assert result["hypothesis"] == "insufficient_evidence"


def test_cross_case_evidence_is_rejected():
    module = load_module()
    case = json.loads(CASES.read_text(encoding="utf-8"))[0]
    case["evidence"][1]["case_id"] = "ANOTHER-CASE"
    result = module.assess(case, now="2026-11-11T10:30:00Z")
    assert result["status"] == "insufficient_evidence"
    assert "wrong case scope" in " ".join(result["findings"])


def test_fresh_matching_snapshots_point_to_determination_check():
    module = load_module()
    case = json.loads(CASES.read_text(encoding="utf-8"))[0]
    case["evidence"][1]["value"] = case["evidence"][0]["value"]
    result = module.assess(case, now="2026-11-11T10:30:00Z")
    assert result["hypothesis"] == "values_match_check_determination"
    assert result["write_allowed"] is False
