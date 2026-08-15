"""A bounded read-only tool loop.

The 'model policy' is intentionally deterministic here. Replace it later with a real
model call and keep the same application boundaries.

Run:
    python3 tool_loop.py
"""

TOOLS = {
    "get_project": lambda args: {
        "project_id": args["project_id"],
        "status": "active",
        "owner": "team-a",
    },
    "get_open_tasks": lambda args: {
        "project_id": args["project_id"],
        "tasks": [
            {"id": "task-7", "title": "Fix login regression", "priority": "high"},
            {"id": "task-9", "title": "Update runbook", "priority": "medium"},
        ],
    },
}

MAX_STEPS = 4


def model_policy(question: str, evidence: list[dict]):
    """Stand-in for a model deciding what to read next."""
    tool_names = [item["tool"] for item in evidence]

    if "get_project" not in tool_names:
        return {"type": "tool", "name": "get_project", "args": {"project_id": "alpha"}}

    if "task" in question.lower() and "get_open_tasks" not in tool_names:
        return {"type": "tool", "name": "get_open_tasks", "args": {"project_id": "alpha"}}

    return {"type": "stop", "reason": "resolved"}


def run_agent(question: str):
    evidence = []
    seen_calls = set()

    for step in range(1, MAX_STEPS + 1):
        decision = model_policy(question, evidence)
        print(f"step={step} decision={decision}")

        if decision["type"] == "stop":
            return {"stop_reason": decision["reason"], "evidence": evidence}

        name = decision["name"]
        args = decision["args"]
        call_key = (name, tuple(sorted(args.items())))

        if call_key in seen_calls:
            return {"stop_reason": "duplicate_call", "evidence": evidence}

        if name not in TOOLS:
            return {"stop_reason": "tool_not_allowed", "evidence": evidence}

        seen_calls.add(call_key)
        result = TOOLS[name](args)
        evidence.append({"tool": name, "args": args, "result": result})

    return {"stop_reason": "budget_exhausted", "evidence": evidence}


if __name__ == "__main__":
    outcome = run_agent("What open tasks need attention in project alpha?")
    print("\nFINAL")
    print(outcome)
