from strands import tool
from backend.app.safety import (
    ActionRisk,
    ProposedAction,
    execute_action,
)

@tool
def rollback_deployment(
    service: str,
    target_version: str,
    approved: bool = False,
) -> dict:
    """Simulate rolling a service back to a previous version."""

    action = ProposedAction(
        name="rollback_deployment",
        description=f"Rollback {service} to {target_version}",
        risk=ActionRisk.REQUIRES_APPROVAL,
        approved=approved,
    )

    result = execute_action(action)

    if not result["executed"]:
        return {
            **result,
            "requires_approval": True,
        }

    return {
        **result,
        "requires_approval": True,
        "message": f"Successfully rolled back {service} to {target_version}.",
    }