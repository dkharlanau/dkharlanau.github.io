"""A tiny deterministic eval runner for architecture routing decisions.

Run:
    python3 eval_runner.py
"""

CASES = [
    {
        "id": "case-1",
        "input": "Rewrite this paragraph in a shorter form.",
        "expected": "prompt",
    },
    {
        "id": "case-2",
        "input": "Answer from our private handbook that changes every week.",
        "expected": "retrieval",
    },
    {
        "id": "case-3",
        "input": "Read the current deployment status from the API.",
        "expected": "tool",
    },
    {
        "id": "case-4",
        "input": "Investigate the incident; the next check depends on each result.",
        "expected": "agent",
    },
]


def route(text: str) -> str:
    lower = text.lower()
    if "private" in lower or "handbook" in lower:
        return "retrieval"
    if "api" in lower or "current deployment status" in lower:
        return "tool"
    if "next check depends" in lower or "investigate" in lower:
        return "agent"
    return "prompt"


def run():
    passed = 0
    failures = []

    for case in CASES:
        actual = route(case["input"])
        ok = actual == case["expected"]
        print(f"{case['id']}: expected={case['expected']} actual={actual} {'PASS' if ok else 'FAIL'}")
        if ok:
            passed += 1
        else:
            failures.append({**case, "actual": actual})

    print(f"\nRESULT: {passed}/{len(CASES)} passed")
    if failures:
        print("FAILURES:")
        for failure in failures:
            print(failure)
        raise SystemExit(1)


if __name__ == "__main__":
    run()
