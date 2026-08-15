"""Bind approval to an exact prepared action and a state precondition.

Run:
    python3 approval_state.py
"""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import uuid


@dataclass
class Resource:
    resource_id: str
    version: int
    status: str


@dataclass
class Change:
    change_id: str
    resource_id: str
    expected_version: int
    new_status: str
    approved_by: str | None = None
    approved_until: datetime | None = None
    executed: bool = False


RESOURCE = Resource(resource_id="service-alpha", version=7, status="running")
CHANGES: dict[str, Change] = {}
REQUESTS: set[str] = set()


def prepare_change(resource: Resource, new_status: str) -> Change:
    change = Change(
        change_id=str(uuid.uuid4()),
        resource_id=resource.resource_id,
        expected_version=resource.version,
        new_status=new_status,
    )
    CHANGES[change.change_id] = change
    return change


def approve(change_id: str, approver: str, minutes: int = 10) -> None:
    change = CHANGES[change_id]
    change.approved_by = approver
    change.approved_until = datetime.now(timezone.utc) + timedelta(minutes=minutes)


def execute(change_id: str, request_id: str, resource: Resource) -> str:
    if request_id in REQUESTS:
        return "already_processed"

    change = CHANGES[change_id]
    now = datetime.now(timezone.utc)

    if not change.approved_by or not change.approved_until:
        return "approval_required"
    if change.approved_until < now:
        return "approval_expired"
    if resource.resource_id != change.resource_id:
        return "wrong_target"
    if resource.version != change.expected_version:
        return "stale_precondition"
    if change.executed:
        return "already_executed"

    resource.status = change.new_status
    resource.version += 1
    change.executed = True
    REQUESTS.add(request_id)
    return "executed"


if __name__ == "__main__":
    prepared = prepare_change(RESOURCE, "maintenance")
    print("prepared:", prepared)

    approve(prepared.change_id, approver="operator-42")
    print("approved by:", prepared.approved_by)

    result = execute(prepared.change_id, "req-100", RESOURCE)
    print("first execution:", result, RESOURCE)

    duplicate = execute(prepared.change_id, "req-100", RESOURCE)
    print("same request again:", duplicate)

    stale = prepare_change(RESOURCE, "running")
    approve(stale.change_id, approver="operator-42")
    RESOURCE.version += 1  # another process changed the object after approval
    print("stale execution:", execute(stale.change_id, "req-101", RESOURCE))
