from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRACTICE = ROOT / "labs" / "ai-ready" / "practice"


def run(script: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def test_ai_ready_practice_self_tests() -> None:
    result = run(PRACTICE / "run_all.py")
    assert result.returncode == 0, result.stderr + result.stdout
    assert "all self-tests passed" in result.stdout


def test_practice_datasets_are_valid_json() -> None:
    json_files = [
        PRACTICE / "retrieval-benchmark" / "concepts.json",
        PRACTICE / "local-assistant" / "workspace.json",
        ROOT / "labs" / "ai-ready" / "data" / "practice-map.json",
    ]
    for path in json_files:
        json.loads(path.read_text(encoding="utf-8"))

    jsonl_files = [
        PRACTICE / "model-benchmark" / "cases.jsonl",
        PRACTICE / "model-benchmark" / "recorded_outputs.jsonl",
        PRACTICE / "context-experiment" / "documents.jsonl",
        PRACTICE / "context-experiment" / "cases.jsonl",
        PRACTICE / "retrieval-benchmark" / "documents.jsonl",
        PRACTICE / "retrieval-benchmark" / "queries.jsonl",
        PRACTICE / "local-assistant" / "knowledge.jsonl",
        PRACTICE / "local-assistant" / "scenarios.jsonl",
    ]
    for path in jsonl_files:
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        assert rows, f"{path} is empty"
