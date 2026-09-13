from enum import Enum
from pydantic import BaseModel


class ActionRisk(str, Enum):
    SAFE = "safe"
    REQUIRES_APPROVAL = "requires_approval"

class ProposedAction(BaseModel):
    name: str
    description: str
    risk: ActionRisk
    approved: bool = False

def requires_approval(risk: ActionRisk) -> bool:
    return risk == ActionRisk.REQUIRES_APPROVAL

def approve_action(action: ProposedAction) -> ProposedAction:
    return action.model_copy(update={"approved": True})

def execute_action(action: ProposedAction) -> dict:
    if (
        action.risk == ActionRisk.REQUIRES_APPROVAL
        and not action.approved
    ):
        return {
            "executed": False,
            "reason": "Human approval is required before executing this action.",
            "action": action.model_dump(),
        }

    return {
        "executed": True,
        "action": action.model_dump(),
    }