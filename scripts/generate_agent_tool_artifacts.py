#!/usr/bin/env python3
"""Generate static public Agent Tools artifacts from the reviewed registry."""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/agent-tools/tools.json"
OUT = ROOT / "ai/agent-tools.json"

def build():
    data = json.loads(SOURCE.read_text())
    tools = sorted(data["tools"], key=lambda item: item["id"])
    ids = [item["id"] for item in tools]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate tool IDs")
    required = {"id", "name", "repository_url", "status", "domains", "access", "verification_date", "evidence_sources"}
    for tool in tools:
        missing = required - tool.keys()
        if missing: raise ValueError(f"{tool.get('id', '<unknown>')}: missing {sorted(missing)}")
    return {"schema":"dkharlanau.agent_tools","schema_version":"1.0","canonical_url":"https://dkharlanau.github.io/ai/agent-tools.json","description":"Reviewed registry of SAP-related MCP and agent tools. Entries are metadata, not an endorsement or runtime service.","source":"data/agent-tools/tools.json","verification_date":data["verification_date"],"count":len(tools),"counts_by_status":{status:sum(t["status"] == status for t in tools) for status in ("official","community","experimental")},"tools":tools}

def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--check", action="store_true"); args=parser.parse_args()
    generated=json.dumps(build(), indent=2)+"\n"
    if args.check:
        if not OUT.exists() or OUT.read_text() != generated:
            print("agent tool artifact is stale", file=sys.stderr); return 1
        print("agent tool artifact is current"); return 0
    OUT.write_text(generated); print(f"wrote {OUT.relative_to(ROOT)}")
if __name__ == "__main__": raise SystemExit(main())
