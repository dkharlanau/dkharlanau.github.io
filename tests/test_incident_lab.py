import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from generate_incident_lab_artifacts import build


def test_incident_lab_builds_from_synthetic_cases():
    artifact = build()
    assert artifact["schema"] == "dkharlanau.incident_lab"
    assert artifact["count"] >= 4
    assert all(case["id"] for case in artifact["cases"])
    assert all(url.startswith("/atlas/") for case in artifact["cases"] for url in case["expected_atlas_urls"])


def test_incident_lab_committed_artifact_is_current():
    expected = build()
    committed = json.loads((REPO_ROOT / "ai/incident-lab.json").read_text(encoding="utf-8"))
    assert committed == expected
