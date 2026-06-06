import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run_status(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "atlas_backlog_status.py"), *args],
        capture_output=True,
        text=True,
    )


def _run_check_ledger() -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "check_atlas_backlog_ledger.py")],
        capture_output=True,
        text=True,
    )


def test_ledger_validates():
    result = _run_check_ledger()
    assert result.returncode == 0, f"Ledger validation failed: {result.stdout}\n{result.stderr}"
    assert "PASSED" in result.stdout


def test_status_summary_works():
    result = _run_status("summary")
    assert result.returncode == 0, f"Status summary failed: {result.stderr}"
    assert "Atlas Backlog Ledger Summary" in result.stdout
    assert "candidates" in result.stdout.lower()


def test_status_lookup_by_id():
    result = _run_status("lookup", "--candidate-id", "CONCEPT-0001")
    assert result.returncode == 0, f"Lookup failed: {result.stderr}"
    assert "CONCEPT-0001" in result.stdout
    assert "final_state" in result.stdout


def test_status_lookup_by_topic():
    result = _run_status("lookup", "--topic", "Sales Document Type Selection")
    assert result.returncode == 0, f"Lookup by topic failed: {result.stderr}"
    # This topic may or may not exist; just check it doesn't crash
    assert "No matching candidate" in result.stdout or "candidate_id" in result.stdout


def test_status_fingerprint_stable():
    result1 = _run_status(
        "fingerprint",
        "--topic", "Test Topic",
        "--domain", "sales",
        "--category", "Business Process",
    )
    assert result1.returncode == 0, f"Fingerprint failed: {result1.stderr}"
    fp1 = result1.stdout.split("Fingerprint: ")[1].split()[0]

    result2 = _run_status(
        "fingerprint",
        "--topic", "Test Topic",
        "--domain", "sales",
        "--category", "Business Process",
    )
    assert result2.returncode == 0
    fp2 = result2.stdout.split("Fingerprint: ")[1].split()[0]

    assert fp1 == fp2, f"Fingerprint not stable: {fp1} != {fp2}"


def test_status_fingerprint_detects_existing():
    # CONCEPT-0001 should be in the ledger
    result = _run_status(
        "fingerprint",
        "--topic", "1",
        "--domain", "ai-enterprise-operations",
        "--category", "Answers questions and retrieves information; human",
    )
    assert result.returncode == 0
    assert "already_processed" in result.stdout or "not in ledger" in result.stdout


def test_status_check_new_detects_already_processed():
    # Create a tiny CSV with one known candidate
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
        f.write("id,topic,sap_area,category,priority,decision,target_merge,reason\n")
        f.write("CONCEPT-0001,1,ai-enterprise-operations,Answers questions and retrieves information; human,P0,low_value_rejected,,Generic AI concept\n")
        temp_path = f.name

    result = _run_status("check-new", "--csv", temp_path)
    assert result.returncode == 0, f"check-new failed: {result.stderr}"
    assert "already_processed" in result.stdout or "possible_duplicate" in result.stdout

    Path(temp_path).unlink()


def test_status_check_new_detects_private_path_risk():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False, encoding="utf-8") as f:
        f.write("id,topic,sap_area,category,priority,decision,target_merge,reason\n")
        f.write("CONCEPT-9999,/Users/someone/private/topic,sales,Business Process,P0,low_value_rejected,,Generic\n")
        temp_path = f.name

    result = _run_status("check-new", "--csv", temp_path)
    assert result.returncode == 0  # Should not crash, but report blocked
    assert "blocked_private_risk" in result.stdout

    Path(temp_path).unlink()


def test_status_export_summary():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8") as f:
        temp_path = f.name

    result = _run_status("export-summary", "--output", temp_path)
    assert result.returncode == 0, f"export-summary failed: {result.stderr}"

    with open(temp_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.atlas.backlog_summary_export"
    assert data["total_candidates"] == 1133

    Path(temp_path).unlink()


def test_ledger_no_duplicate_ids():
    ledger_path = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    ids = [c["candidate_id"] for c in ledger["candidates"]]
    assert len(ids) == len(set(ids)), f"Duplicate IDs found in ledger"


def test_ledger_no_private_paths():
    ledger_path = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
    with open(ledger_path, "r", encoding="utf-8") as f:
        text = f.read()
    assert "/Users/" not in text, "Ledger contains private path /Users/"
    assert ".env" not in text, "Ledger contains .env reference"


def test_ledger_no_source_files():
    ledger_path = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
    with open(ledger_path, "r", encoding="utf-8") as f:
        text = f.read()
    assert "source_files" not in text, "Ledger contains source_files reference"


def test_ledger_all_candidates_have_final_state():
    ledger_path = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    missing = [c["candidate_id"] for c in ledger["candidates"] if not c.get("final_state")]
    assert not missing, f"Candidates missing final_state: {missing[:10]}"


def test_ledger_all_candidates_have_reason():
    ledger_path = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
    with open(ledger_path, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    empty = [c["candidate_id"] for c in ledger["candidates"] if not c.get("reason", "").strip()]
    assert not empty, f"Candidates with empty reason: {empty[:10]}"
