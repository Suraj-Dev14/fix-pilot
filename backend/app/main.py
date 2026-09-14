from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.app.agent import agent


app = FastAPI(
    title="FixPilot API",
    description="Autonomous production incident investigation API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IncidentRequest(BaseModel):
    incident_id: str
    service: str
    observed_error: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/investigate")
def investigate_incident(incident: IncidentRequest):
    response = agent(
        f"""
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
    )

    return response.structured_output.model_dump()