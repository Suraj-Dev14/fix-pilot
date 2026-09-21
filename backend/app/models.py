from pydantic import BaseModel

class Incident(BaseModel):
    """Generic production incident."""
    incident_id: str
    service: str
    observed_error: str

class InvestigationReport(BaseModel):
    incident_id: str
    observed_evidence: list[str]
    inferences: list[str]
    unresolved_hypotheses: list[str]
    root_cause: str
    recommendations: list[str]

class InvestigationContext(BaseModel):
    """State associated with an incident investigation."""

    incident: Incident
    evidence: list[dict] = []
    hypotheses: list[dict] = []