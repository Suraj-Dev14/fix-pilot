from strands import tool
from backend.app.safety import ActionRisk, ProposedAction

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
    )

    if not approved:
        return {
            "executed": False,
            "requires_approval": True,
            "action": action.model_dump(),
        }

    return {
        "executed": True,
        "requires_approval": True,
        "action": action.model_dump(),
        "message": f"Successfully rolled back {service} to {target_version}.",
    }