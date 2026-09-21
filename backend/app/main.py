from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.agent import agent
from backend.app.models import Incident
from backend.app.investigation import (build_investigation_prompt, create_investigation_context)


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


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/investigate")
def investigate_incident(incident: Incident):
    context = create_investigation_context(incident)
    response = agent(
        build_investigation_prompt(context.incident),
    )

    return response.structured_output.model_dump()