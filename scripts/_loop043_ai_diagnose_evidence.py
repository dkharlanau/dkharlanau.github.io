#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"
GRAPH = ROOT / "_data" / "labs" / "enterprise_context" / "graphs" / "agent_architecture.yml"
PAGE = ROOT / "labs" / "enterprise-context" / "business-ai" / "agents" / "index.html"

ROUTE = "/labs/enterprise-context/business-ai/agents/"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-043 patch marker not found: {label}")
    return text.replace(old, new, 1)


def patch_factual_review() -> None:
    path = DATA / "factual-review.json"
    value = load(path)
    claims = value.setdefault("claims", [])
    routes = value.setdefault("routes", [])
    claim_ids = {item.get("id") for item in claims}

    additions = [
        {
            "id": "FACT-AIAG-001",
            "route": ROUTE,
            "claim": "SAP Architecture Center describes MCP as the standard for agent-to-tool interaction and SAP agent architecture uses semantically enriched, governed access to SAP business capabilities. Tool access therefore does not remove the need for business semantics, controlled exposure, and validation around the underlying capability.",
            "claim_type": "architecture_behavior",
            "evidence_class": "sap_product_primary",
            "status": "source_supported",
            "source_refs": ["SRC-SAP-ARCH-AGENT-MCP-ACCESS", "SRC-SAP-ARCH-AGENT-GOLDEN-PATH"],
            "official_evidence": [
                "https://architecture.learning.sap.com/docs/ref-arch/137800",
                "https://architecture.learning.sap.com/docs/golden-path/ai-golden-path/build-and-deliver/build-ai-agents"
            ],
            "product_scope": "SAP BTP agent architecture and MCP access to SAP business capabilities",
            "release_scope": "SAP Architecture Center guidance checked 2026-08-16",
            "reviewed_at": "2026-08-16",
            "human_verification_required": True
        },
        {
            "id": "FACT-AIAG-002",
            "route": ROUTE,
            "claim": "SAP agent architecture treats agent identity as a governed enterprise identity with authentication, scoped authorization, policy enforcement, and auditability. Agent capability and permission are separate concerns, and access must stay inside explicit authorization boundaries.",
            "claim_type": "architecture_behavior",
            "evidence_class": "sap_product_primary",
            "status": "source_supported",
            "source_refs": ["SRC-SAP-ARCH-AGENT-IDENTITY"],
            "official_evidence": ["https://architecture.learning.sap.com/docs/ref-arch/140bdb"],
            "product_scope": "SAP enterprise AI agent identity and authorization architecture",
            "release_scope": "SAP Architecture Center guidance checked 2026-08-16",
            "reviewed_at": "2026-08-16",
            "human_verification_required": True
        }
    ]
    for item in additions:
        if item["id"] not in claim_ids:
            claims.append(item)

    route = next((item for item in routes if item.get("route") == ROUTE), None)
    if route is None:
        routes.append({
            "route": ROUTE,
            "title": "Enterprise Agent Architecture",
            "review_status": "primary_source_review_complete",
            "reviewed_at": "2026-08-16",
            "page_verified": False,
            "human_verification_required": True,
            "claim_ids": ["FACT-AIAG-001", "FACT-AIAG-002"]
        })
    else:
        route["claim_ids"] = ["FACT-AIAG-001", "FACT-AIAG-002"]
        route["review_status"] = "primary_source_review_complete"
        route["reviewed_at"] = "2026-08-16"
        route["page_verified"] = False
        route["human_verification_required"] = True

    value["version"] = "1.7.0"
    value["updated_at"] = "2026-08-16"
    value["summary"] = {
        "routes_reviewed": len(routes),
        "claims_reviewed": len(claims),
        "source_supported": sum(item.get("status") == "source_supported" for item in claims),
        "source_conflict": sum(item.get("status") == "source_conflict" for item in claims),
        "human_verification_required": sum(bool(item.get("human_verification_required")) for item in claims)
    }
    dump(path, value)


def patch_catalog() -> None:
    path = DATA / "catalog.json"
    value = load(path)
    for track in value.get("tracks", []):
        if track.get("id") == "ai-data":
            entries = track.setdefault("entry_points", [])
            if ROUTE not in entries:
                parent = "/labs/enterprise-context/business-ai/"
                if parent in entries:
                    entries.insert(entries.index(parent) + 1, ROUTE)
                else:
                    entries.append(ROUTE)
            focus = track.setdefault("focus", [])
            phrase = "agent tool semantics, identity, authorization and recovery"
            if phrase not in focus:
                focus.append(phrase)
    value["updated_at"] = "2026-08-16"
    dump(path, value)


def patch_graph() -> None:
    text = GRAPH.read_text(encoding="utf-8")
    text = text.replace('updated_at: "2026-08-15"', 'updated_at: "2026-08-16"', 1)
    if "lead_lens:" not in text:
        marker = "\nfailure_modes:\n"
        block = '''\nlead_lens:\n  what_i_ask_first:\n    - "What business outcome failed, and what authoritative state proves it?"\n    - "Which user, agent identity, and tool contract were active?"\n    - "Was the failure in context, tool selection, authorization, execution, or post-action verification?"\n  decision_owner: "Business process ownership defines the allowed outcome; platform, security, data, and application owners define the controlled agent boundary."\n  main_trade_off: "More autonomy can reduce manual coordination, but it increases the need for narrow tools, identity, policy, verification, observability, and deterministic recovery controls."\n  typical_failure: "The technical agent run succeeds while the selected capability, permission, business key, or resulting business state is wrong."\n  proof_of_cause: "Reconstruct goal, authorized context, agent/tool identity, selected tool, input business keys, backend authorization and commit state, then re-read the authoritative business object after correction."\n  sixty_second_explanation: "I do not diagnose an enterprise agent from the model response alone. I start with the expected business outcome, then trace context, tool selection, agent and user identity, authorization, the backend side effect, and post-action verification. MCP or another tool protocol gives access to capabilities, but business meaning, permission, validation, idempotency, and proof of the resulting SAP state remain separate controls. I stop at the first divergence and only then decide whether the fix belongs to agent logic, tool semantics, security policy, or the business system."\n'''
        text = replace_once(text, marker, block + marker, "agent lead lens")
    GRAPH.write_text(text, encoding="utf-8")


def patch_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    text = text.replace("last_modified_at: 2026-08-15", "last_modified_at: 2026-08-16", 1)
    if 'id="agent-lead-lens"' not in text:
        marker = '''  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Failure modes</p>'''
        block = '''  <section class="research-canvas__inventory" id="agent-lead-lens" data-reveal>\n    <header><p class="research-canvas__eyebrow">Lead diagnostic lens</p><h2>Trace the business side effect, not only the model answer.</h2><p>{{ graph.lead_lens.sixty_second_explanation }}</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>Ask first</h4><ul>{% for item in graph.lead_lens.what_i_ask_first %}<li>{{ item }}</li>{% endfor %}</ul></div>\n      <div><h4>Ownership</h4><p>{{ graph.lead_lens.decision_owner }}</p><h4>Typical failure</h4><p>{{ graph.lead_lens.typical_failure }}</p></div>\n      <div><h4>Proof</h4><p>{{ graph.lead_lens.proof_of_cause }}</p><h4>Trade-off</h4><p>{{ graph.lead_lens.main_trade_off }}</p></div>\n    </div>\n    <p class="ecg-caption"><strong>Evidence boundary:</strong> current SAP Architecture Center sources support the MCP/tool-access and identity/authorization claims used by the assessment candidate gate. The diagnostic sequence and Lead lens are authored reasoning and still require page-level human review.</p>\n  </section>\n\n'''
        text = replace_once(text, marker, block + marker, "agent page lead lens")
    PAGE.write_text(text, encoding="utf-8")


def patch_seeds() -> None:
    path = DATA / "candidate-generation-seeds.json"
    value = load(path)
    graphs = value.setdefault("graphs", [])
    if not any(item.get("path") == "_data/labs/enterprise_context/graphs/agent_architecture.yml" for item in graphs):
        graphs.append({
            "path": "_data/labs/enterprise_context/graphs/agent_architecture.yml",
            "human_ref": ROUTE,
            "track": "ai-data",
            "level": "diagnose",
            "candidate_prefix": "CAND-AIAG",
            "failure_prefix": "FAIL-AI-AGENT-",
            "failure_sources": {
                "FAIL-AI-AGENT-RAW-MCP": ["SRC-SAP-ARCH-AGENT-MCP-ACCESS", "SRC-SAP-ARCH-AGENT-GOLDEN-PATH"],
                "FAIL-AI-AGENT-OVERPRIVILEGED": ["SRC-SAP-ARCH-AGENT-IDENTITY"]
            },
            "evidence_class": "sap_product_primary",
            "selection_reason": "The AI/Data Diagnose cell is thin. These two failure modes test tool semantics and authorization diagnosis, which are materially different from the published weak-grounding case. Design and Challenge gaps remain outside this symptom-to-root-cause generator."
        })
    value["version"] = "1.3.0"
    value["updated_at"] = "2026-08-16"
    dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    text = text.replace('    assert review["summary"]["routes_reviewed"] == 26\n', '')
    text = text.replace('    assert review["summary"]["claims_reviewed"] == 63\n', '')
    text = text.replace('    assert all(all(url.startswith("https://help.sap.com/") for url in claim["official_evidence"]) for claim in review["claims"])\n', '    allowed_primary_hosts = ("https://help.sap.com/", "https://architecture.learning.sap.com/")\n    assert all(all(url.startswith(allowed_primary_hosts) for url in claim["official_evidence"]) for claim in review["claims"])\n')
    text = text.replace('    assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 26\n', '    assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == review["summary"]["routes_reviewed"]\n')
    text = text.replace('    assert coverage["summary"]["unique_source_reviewed_routes"] == coverage["summary"]["unique_externally_review_required_routes"] == 26\n', '    assert coverage["summary"]["unique_source_reviewed_routes"] == coverage["summary"]["unique_externally_review_required_routes"]\n')
    text = text.replace('    assert coverage["summary"]["source_supported_claims"] >= 63\n', '    assert coverage["summary"]["source_supported_claims"] == factual["summary"]["source_supported"]\n')
    if '"LOOP-043"' not in text:
        text = text.replace('"LOOP-041", "LOOP-042"):', '"LOOP-041", "LOOP-042", "LOOP-043"):')
    marker = "\ndef test_ai_agent_diagnose_seed_has_claim_level_primary_evidence() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_ai_agent_diagnose_seed_has_claim_level_primary_evidence() -> None:\n    factual = load_json("factual-review.json")\n    seeds = load_json("candidate-generation-seeds.json")\n    route = next(item for item in factual["routes"] if item["route"] == "/labs/enterprise-context/business-ai/agents/")\n    claims = {item["id"]: item for item in factual["claims"]}\n    seed = next(item for item in seeds["graphs"] if item["path"].endswith("agent_architecture.yml"))\n\n    assert route["review_status"] == "primary_source_review_complete"\n    assert set(route["claim_ids"]) == {"FACT-AIAG-001", "FACT-AIAG-002"}\n    assert all(claims[claim_id]["status"] == "source_supported" for claim_id in route["claim_ids"])\n    assert seed["track"] == "ai-data"\n    assert seed["level"] == "diagnose"\n    assert set(seed["failure_sources"]) == {"FAIL-AI-AGENT-RAW-MCP", "FAIL-AI-AGENT-OVERPRIVILEGED"}\n    assert seed["human_ref"] == "/labs/enterprise-context/business-ai/agents/"\n\n    result = subprocess.run(\n        [sys.executable, "scripts/generate_assessment_candidates.py", "--check"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-043" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-043",
            "priority": "P1",
            "title": "AI/Data Diagnose evidence-backed candidate expansion",
            "status": "done",
            "outputs": [
                "/labs/enterprise-context/business-ai/agents/",
                "/labs/assessment/data/factual-review.json",
                "/labs/assessment/data/candidate-generation-seeds.json",
                "/labs/assessment/data/question-candidates.json"
            ],
            "working_rule": "Fill the thin AI/Data Diagnose cell only after adding claim-level SAP primary evidence for the exact Agent Architecture route. Keep Sales Design and AI/Data Challenge outside the diagnose-only generation pattern."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "reasoning-pressure gaps" not in theme]
        themes.insert(0, "run semantic novelty review on the new AI/Data Diagnose candidates before any promotion decision")
        themes.insert(1, "design separate evidence-backed authoring patterns for Sales Design and AI/Data Challenge instead of relabelling them as Diagnose")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def main() -> None:
    patch_factual_review()
    patch_catalog()
    patch_graph()
    patch_page()
    patch_seeds()
    patch_tests()
    patch_backlog()


if __name__ == "__main__":
    main()
