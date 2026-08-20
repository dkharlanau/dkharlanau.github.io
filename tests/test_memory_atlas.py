from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "_data" / "career" / "memory_atlas.yml"
ROADMAP = ROOT / "_data" / "career" / "roadmap.yml"
PAGE = ROOT / "labs" / "interview-readiness" / "memory-atlas" / "index.md"
TODAY = ROOT / "labs" / "interview-readiness" / "today" / "index.md"
SCRIPT = ROOT / "assets" / "js" / "memory-atlas.js"
STYLE = ROOT / "assets" / "css" / "memory-atlas.css"


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_memory_atlas_contract_is_strict_and_local_first():
    data = load_yaml(ATLAS)
    contract = data["contract"]
    assert contract["storage_key"] == "sapLeadMemoryAtlasV1"
    assert contract["mastery_storage_key"] == "sapLeadMasteryHistoryV1"
    assert contract["pass_accuracy"] == 1.0
    assert contract["max_saved_runs"] >= 100


def test_memory_atlas_maps_have_valid_ordered_nodes_edges_and_skills():
    atlas = load_yaml(ATLAS)
    roadmap = load_yaml(ROADMAP)
    skill_ids = {item["id"] for item in roadmap["skills"]}
    maps = atlas["maps"]
    assert [item["id"] for item in maps] == ["o2c", "p2p", "integration"]

    for process_map in maps:
        nodes = process_map["nodes"]
        assert len(nodes) == 7
        node_ids = [item["id"] for item in nodes]
        assert len(node_ids) == len(set(node_ids))
        assert set(process_map["skills"]) <= skill_ids
        assert process_map["source"].startswith("/")
        assert process_map["boundary_prompt"].strip()
        assert process_map["lead_prompt"].strip()

        for node in nodes:
            assert node["skill_id"] in skill_ids
            assert node["source"].startswith("/")
            assert node["owner"].strip()
            assert node["cue"].strip()

        edges = process_map["edges"]
        assert len(edges) == len(nodes) - 1
        for index, edge in enumerate(edges):
            assert edge["from"] == node_ids[index]
            assert edge["to"] == node_ids[index + 1]
            assert edge["type"].strip()
            assert edge["label"].strip()


def test_memory_atlas_page_is_noindex_mapped_and_data_driven():
    page = PAGE.read_text(encoding="utf-8")
    assert "permalink: /labs/interview-readiness/memory-atlas/" in page
    assert "verified: false" in page
    assert "robots: noindex,follow" in page
    assert "sitemap: false" in page
    assert "career_impact: mapped" in page
    assert "site.data.career.memory_atlas" in page
    assert "site.data.career.mastery" in page
    assert 'id="memory-atlas-data"' in page
    assert "/assets/js/memory-atlas.js" in page
    assert "/assets/css/memory-atlas.css" in page
    assert "Rebuild from memory" in page
    assert "proven rebuild requires every node" in page


def test_memory_atlas_engine_records_reconstruction_not_answer_text():
    script = SCRIPT.read_text(encoding="utf-8")
    for symbol in ("atlasRuns", "masteryState", "resetRebuild", "checkRebuild", "passAccuracy"):
        assert symbol in script
    assert "localStorage" in script
    assert "sapLeadMemoryAtlasV1" in script
    assert "sapLeadMasteryHistoryV1" in script
    assert "accuracy" in script
    assert "answer:" not in script
    assert "dragstart" not in script
    assert "drop" not in script


def test_memory_atlas_is_reachable_from_mastery_today():
    today = TODAY.read_text(encoding="utf-8")
    assert '/labs/interview-readiness/memory-atlas/' in today


def test_memory_atlas_assets_expose_sequence_and_mobile_layout():
    style = STYLE.read_text(encoding="utf-8")
    assert "memory-atlas__sequence" in style
    assert "memory-atlas__rebuild" in style
    assert "memory-atlas-node" in style
    assert "@media" in style
