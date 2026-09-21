from backend.app.models import Incident, InvestigationContext

def create_investigation_context(
  incident: Incident,
) -> InvestigationContext:
    """Create intial investigation state from an incident."""

    return InvestigationContext(incident=incident)


def build_investigation_prompt(incident: Incident) -> str:
    """Build the investigation request for the agent."""

    return f"""
Investigate this production incident.

Incident ID: {incident.incident_id}
Service: {incident.service}
Observed error: {incident.observed_error}

Gather evidence using the available investigation tools.

Before concluding the root cause, run the available regression
test when it can validate the suspected failure.

Keep intermediate reasoning concise.
Do not explain your reasoning before using a tool.
Use tools directly when evidence is needed.
Only provide the detailed explanation in the final structured report.

Clearly distinguish:
- observed evidence
- inferences
- unresolved hypotheses
- validated root cause
- recommendations

Do not execute production-changing actions without explicit human approval.
"""