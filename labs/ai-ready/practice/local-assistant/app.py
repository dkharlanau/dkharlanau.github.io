#!/usr/bin/env python3
"""Small local AI-application skeleton with deterministic planning.

The planner is intentionally deterministic so retrieval, tools, approval,
idempotency, state, and traces can be tested without a model API.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
STOP = {"a","an","the","is","are","to","of","and","or","for","in","on","after","before","during"}


class BudgetExceeded(RuntimeError):
    pass


class ToolBudget:
    def __init__(self, maximum: int = 6) -> None:
        self.maximum = maximum
        self.used = 0

    def consume(self, tool: str) -> None:
        if self.used >= self.maximum:
            raise BudgetExceeded(f"tool budget exhausted before {tool}")
        self.used += 1


def canonical_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower())
        if token not in STOP and len(token) > 1
    }


class Workspace:
    def __init__(self, data: dict) -> None:
        self.data = copy.deepcopy(data)
        self.executed: dict[str, dict] = {}

    @classmethod
    def load(cls) -> "Workspace":
        return cls(json.loads((BASE_DIR / "workspace.json").read_text(encoding="utf-8")))

    def incident(self, incident_id: str) -> dict:
        if incident_id not in self.data["incidents"]:
            raise KeyError(f"unknown incident: {incident_id}")
        return copy.deepcopy(self.data["incidents"][incident_id])

    def service(self, service_id: str) -> dict:
        if service_id not in self.data["services"]:
            raise KeyError(f"unknown service: {service_id}")
        return copy.deepcopy(self.data["services"][service_id])


class LocalAssistant:
    def __init__(self, workspace: Workspace, max_tools: int = 6) -> None:
        self.workspace = workspace
        self.runbooks = read_jsonl(BASE_DIR / "knowledge.jsonl")
        self.budget = ToolBudget(max_tools)
        self.trace: list[dict[str, Any]] = []
        self.approvals: dict[str, dict] = {}

    def emit(self, event: str, **data: Any) -> None:
        self.trace.append({"event": event, **data})

    def get_incident(self, incident_id: str) -> dict:
        self.budget.consume("get_incident")
        value = self.workspace.incident(incident_id)
        self.emit("tool", name="get_incident", incident_id=incident_id)
        return value

    def get_service_state(self, service_id: str) -> dict:
        self.budget.consume("get_service_state")
        value = self.workspace.service(service_id)
        self.emit("tool", name="get_service_state", service_id=service_id, version=value["version"])
        return value

    def search_runbooks(self, query: str, top_k: int = 2) -> list[dict]:
        self.budget.consume("search_runbooks")
        q = tokens(query)
        ranked = []
        for doc in self.runbooks:
            if doc.get("trust") != "trusted":
                continue
            d = tokens(doc["title"] + " " + doc["text"])
            score = len(q & d)
            if score > 0:
                ranked.append((score, doc["id"], doc))
        ranked.sort(key=lambda item: (-item[0], item[1]))
        result = [copy.deepcopy(item[2]) for item in ranked[:top_k]]
        self.emit("tool", name="search_runbooks", evidence=[doc["id"] for doc in result])
        return result

    def investigate(self, incident_id: str) -> dict:
        incident = self.get_incident(incident_id)
        state = self.get_service_state(incident["service"])
        evidence = self.search_runbooks(incident["symptom"])
        result = {
            "incident_id": incident_id,
            "incident": incident,
            "service_state": state,
            "evidence": evidence,
        }
        self.emit("investigation_complete", incident_id=incident_id)
        return result

    def propose_change(self, investigation: dict) -> dict | None:
        incident = investigation["incident"]
        evidence_ids = [doc["id"] for doc in investigation["evidence"]]
        if (
            incident["service"] == "worker-api"
            and "rb-worker-restart" in evidence_ids
            and investigation["service_state"]["status"] == "degraded"
        ):
            payload = {
                "action": "restart_worker",
                "target": incident["service"],
                "parameters": {"incident_id": investigation["incident_id"]},
                "expected_version": investigation["service_state"]["version"],
                "evidence_ids": evidence_ids,
            }
            change = {
                "change_id": canonical_hash(payload)[:16],
                "payload": payload,
                "payload_hash": canonical_hash(payload),
            }
            self.emit("change_prepared", change_id=change["change_id"], action=payload["action"])
            return change
        self.emit("no_change_proposed", incident_id=investigation["incident_id"])
        return None

    def approve_change(self, change: dict, actor: str) -> dict:
        approval = {
            "change_id": change["change_id"],
            "payload_hash": canonical_hash(change["payload"]),
            "actor": actor,
            "decision": "approved",
        }
        self.approvals[change["change_id"]] = approval
        self.emit("change_approved", change_id=change["change_id"], actor=actor)
        return copy.deepcopy(approval)

    def execute_change(self, change: dict, approval: dict) -> dict:
        payload = change["payload"]
        if payload["action"] != "restart_worker":
            raise PermissionError("action is not allowed")
        if approval.get("decision") != "approved":
            raise PermissionError("change is not approved")
        if approval.get("change_id") != change["change_id"]:
            raise PermissionError("approval references another change")
        current_hash = canonical_hash(payload)
        if approval.get("payload_hash") != current_hash or change.get("payload_hash") != current_hash:
            raise PermissionError("approved payload was changed")

        if change["change_id"] in self.workspace.executed:
            replay = copy.deepcopy(self.workspace.executed[change["change_id"]])
            replay["idempotent_replay"] = True
            self.emit("write_replayed", change_id=change["change_id"])
            return replay

        service = self.workspace.data["services"][payload["target"]]
        if service["version"] != payload["expected_version"]:
            raise RuntimeError("service version changed after preparation")

        service["version"] += 1
        service["status"] = "healthy"
        result = {
            "change_id": change["change_id"],
            "status": "executed",
            "target": payload["target"],
            "new_version": service["version"],
            "idempotent_replay": False,
        }
        self.workspace.executed[change["change_id"]] = copy.deepcopy(result)
        self.emit("write_executed", change_id=change["change_id"], new_version=service["version"])
        return result


def run_scenario(incident_id: str, approve: bool = False, max_tools: int = 6) -> dict:
    assistant = LocalAssistant(Workspace.load(), max_tools=max_tools)
    investigation = assistant.investigate(incident_id)
    change = assistant.propose_change(investigation)
    execution = None
    if change and approve:
        approval = assistant.approve_change(change, actor="local-demo-user")
        execution = assistant.execute_change(change, approval)
    return {
        "investigation": investigation,
        "prepared_change": change,
        "execution": execution,
        "trace": assistant.trace,
    }


def self_test() -> None:
    assistant = LocalAssistant(Workspace.load())
    investigation = assistant.investigate("inc-101")
    evidence_ids = [doc["id"] for doc in investigation["evidence"]]
    assert "rb-worker-restart" in evidence_ids
    assert "rb-hostile-note" not in evidence_ids
    change = assistant.propose_change(investigation)
    assert change and change["payload"]["action"] == "restart_worker"
    approval = assistant.approve_change(change, actor="tester")
    first = assistant.execute_change(change, approval)
    second = assistant.execute_change(change, approval)
    assert first["status"] == "executed"
    assert second["idempotent_replay"] is True

    assistant = LocalAssistant(Workspace.load())
    change = assistant.propose_change(assistant.investigate("inc-101"))
    assert change is not None
    approval = assistant.approve_change(change, actor="tester")
    tampered = copy.deepcopy(change)
    tampered["payload"]["parameters"]["incident_id"] = "inc-999"
    try:
        assistant.execute_change(tampered, approval)
        raise AssertionError("tampered payload should be rejected")
    except PermissionError:
        pass

    assistant = LocalAssistant(Workspace.load())
    change = assistant.propose_change(assistant.investigate("inc-101"))
    assert change is not None
    approval = assistant.approve_change(change, actor="tester")
    assistant.workspace.data["services"]["worker-api"]["version"] += 1
    try:
        assistant.execute_change(change, approval)
        raise AssertionError("stale change should be rejected")
    except RuntimeError:
        pass

    try:
        run_scenario("inc-101", max_tools=2)
        raise AssertionError("budget should stop the investigation")
    except BudgetExceeded:
        pass

    rate_result = run_scenario("inc-202", approve=True)
    assert rate_result["prepared_change"] is None
    print("local-assistant self-test: ok")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--incident", default="inc-101")
    parser.add_argument("--approve", action="store_true")
    parser.add_argument("--max-tools", type=int, default=6)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0

    result = run_scenario(args.incident, approve=args.approve, max_tools=args.max_tools)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
