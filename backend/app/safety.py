from enum import Enum
from pydantic import BaseModel


class ActionRisk(str, Enum):
    SAFE = "safe"
    REQUIRES_APPROVAL = "requires_approval"

class ProposedAction(BaseModel):
    name: str
    description: str
    risk: ActionRisk

def requires_approval(risk: ActionRisk) -> bool:
    return risk == ActionRisk.REQUIRES_APPROVAL