from pydantic import BaseModel


class InvestigationReport(BaseModel):
    incident_id: str
    observed_evidence: list[str]
    inferences: list[str]
    unresolved_hypotheses: list[str]
    root_cause: str
    recommendations: list[str]