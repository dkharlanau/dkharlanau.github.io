"""Validate model-like JSON before the application trusts it.

Run:
    python3 structured_output_validation.py
"""

import json

ALLOWED_CATEGORIES = {"bug", "question", "request"}
ALLOWED_PRIORITIES = {"low", "medium", "high"}
KNOWN_PROJECTS = {"alpha", "beta"}


def validate_schema(payload: dict) -> list[str]:
    errors = []
    required = {"category", "priority", "project_id", "summary"}

    missing = required - payload.keys()
    if missing:
        errors.append(f"missing fields: {sorted(missing)}")

    if payload.get("category") not in ALLOWED_CATEGORIES:
        errors.append("invalid category")

    if payload.get("priority") not in ALLOWED_PRIORITIES:
        errors.append("invalid priority")

    if not isinstance(payload.get("summary"), str):
        errors.append("summary must be a string")

    return errors


def validate_business_rules(payload: dict) -> list[str]:
    errors = []
    if payload.get("project_id") not in KNOWN_PROJECTS:
        errors.append("unknown project_id")
    return errors


def process(raw: str) -> None:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        print("REJECT: invalid JSON", exc)
        return

    schema_errors = validate_schema(payload)
    if schema_errors:
        print("REJECT: schema", schema_errors)
        return

    business_errors = validate_business_rules(payload)
    if business_errors:
        print("REJECT: business rules", business_errors)
        return

    print("ACCEPT:", payload)


if __name__ == "__main__":
    examples = [
        '{"category":"bug","priority":"high","project_id":"alpha","summary":"Login fails"}',
        '{"category":"bug","priority":"urgent","project_id":"alpha","summary":"Login fails"}',
        '{"category":"bug","priority":"high","project_id":"invented","summary":"Login fails"}',
    ]

    for example in examples:
        print("\nINPUT:", example)
        process(example)
