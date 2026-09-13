from backend.app.safety import (
    ActionRisk,
    ProposedAction,
    requires_approval,
)
from backend.app.tools.rollback import rollback_deployment


safe_action = ProposedAction(
    name="search_logs",
    description="Search product-service logs",
    risk=ActionRisk.SAFE,
)

risky_action = ProposedAction(
    name="rollback_deployment",
    description="Rollback product-service to v1.1.0",
    risk=ActionRisk.REQUIRES_APPROVAL,
)

print("Safe action:", requires_approval(safe_action.risk))
print("Risky action:", requires_approval(risky_action.risk))


print("\nAttempting rollback without approval:")

result = rollback_deployment(
    "product-service",
    "v1.1.0",
)

print(result)


print("\nAttempting rollback with approval:")

result = rollback_deployment(
    "product-service",
    "v1.1.0",
    approved=True,
)

print(result)