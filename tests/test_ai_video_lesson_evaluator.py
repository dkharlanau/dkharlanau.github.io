"""Regression checks for the public, synthetic AI video lesson evaluator."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "labs" / "ai-ready" / "video-lessons" / "examples"
SCRIPT = BASE / "agent-eval.py"
DATASET = BASE / "agent-eval-cases.json"


def _load_module():
    spec = importlib.util.spec_from_file_location("ai_video_lesson_eval", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_cases_are_synthetic_and_have_unique_ids():
    data = json.loads(DATASET.read_text(encoding="utf-8"))
    assert data["schema"] == "dkharlanau.ai.agent-eval-fixtures"
    assert "synthetic" in data["note"].lower()
    cases = data["cases"]
    assert len(cases) == 12
    assert len({case["id"] for case in cases}) == len(cases)


def test_diagnostic_results_are_traceable_and_reject_unsafe_writes():
    cases = json.loads(DATASET.read_text(encoding="utf-8"))["cases"]
    module = _load_module()
    baseline = module.evaluate(cases, "baseline")
    candidate = module.evaluate(cases, "candidate")
    assert baseline["accepted"] == 4
    assert baseline["unsafe_writes"] == 2
    assert candidate["accepted"] == 11
    assert candidate["unsafe_writes"] == 0
    assert [item["id"] for item in candidate["failures"]] == ["SYN-012"]


def test_cli_runs_without_llm_or_sap_access():
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--gate", "--json"],
        check=True, capture_output=True, text=True, timeout=15,
    )
    results = json.loads(proc.stdout)
    assert results["synthetic"] is True
    assert results["results"][1]["accepted"] == 11
