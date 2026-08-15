import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
MECHANISM_ROOT = ROOT / "mechanisms" / "sales_mechanisms"
SOURCE_ROOT = ROOT / "sources"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def source_ids() -> set[str]:
    ids: set[str] = set()
    for pattern in ("*.yml", "*.yaml", "*.json"):
        for path in SOURCE_ROOT.glob(pattern):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                continue
            for source in data.get("sources", []):
                if isinstance(source, dict) and isinstance(source.get("id"), str):
                    ids.add(source["id"])
    return ids


def test_billing_control_map_references_known_mechanisms_and_sources():
    index = load_json(MECHANISM_ROOT / "index.json")
    model = load_json(MECHANISM_ROOT / "billing_control_map.json")
    codes = set(index["mechanism_codes"])
    sources = source_ids()

    stage_ids = [stage["id"] for stage in model["stages"]]
    assert len(stage_ids) == len(set(stage_ids)), "Billing stage IDs must be unique"

    for stage in model["stages"]:
        assert stage["owner"] in codes, f"{stage['id']} has unknown owner {stage['owner']}"

    for boundary in model["copy_boundaries"]:
        assert boundary["owner"] in codes, f"Unknown copy-boundary owner {boundary['owner']}"
        for source_ref in boundary.get("source_refs", []):
            assert source_ref in sources, f"Unknown copy-boundary source {source_ref}"

    drill_ids = [drill["id"] for drill in model["failure_drills"]]
    assert len(drill_ids) == len(set(drill_ids)), "Billing failure-drill IDs must be unique"

    for drill in model["failure_drills"]:
        for step in drill["proof_path"]:
            if isinstance(step, str) and step.startswith("MEC."):
                assert step in codes, f"{drill['id']} references unknown mechanism {step}"

    for source_ref in model["source_refs"]:
        assert source_ref in sources, f"Billing control map has unknown source {source_ref}"


def test_billing_lane_contains_specialized_controls():
    index = load_json(MECHANISM_ROOT / "index.json")
    billing_lane = next(lane for lane in index["lanes"] if lane["id"] == "billing_control")

    expected = {
        "MEC.SD.BILLREL",
        "MEC.SD.BILLPLAN",
        "MEC.SD.BILLTYPE",
        "MEC.SD.COPY",
        "MEC.SD.BILLSPLIT",
        "MEC.SD.BILL",
    }
    assert set(billing_lane["codes"]) == expected
