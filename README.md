# FixPilot

## Autonomous Production Incident Investigation & Resolution Agent

FixPilot is an AI agent that investigates production incidents by autonomously gathering evidence from logs, API responses, deployment history, version differences, and regression tests.

The goal is to reduce the time engineers spend manually investigating production failures while keeping potentially dangerous production actions behind a human approval boundary.

> **Prototype:** FixPilot currently operates against a simulated production environment. It uses Qwen3 4B locally through Ollama and the Strands Agents SDK.

---

## Problem

Production incidents often require engineers to manually investigate multiple sources:

* Application logs
* API responses
* Recent deployments
* Code/version changes
* Regression tests

This investigation can be slow and fragmented. Engineers must determine which evidence to inspect, form hypotheses, validate them, and decide what action should be taken.

FixPilot explores how an autonomous AI agent can perform this investigation while preserving human control over risky actions.

---

## What FixPilot Does

Given an incident such as:

```text
Incident: INC-1001
Service: product-service
Error: KeyError: price
```

FixPilot can autonomously:

1. Search production logs.
2. Inspect API responses when relevant.
3. Inspect deployment history.
4. Compare service versions.
5. Run a regression test to validate a suspected failure.
6. Produce a structured investigation report.
7. Recommend remediation.
8. Identify actions that require human approval.

The agent decides which available tools to use rather than following a hardcoded investigation sequence.

---

## Architecture

```text
┌──────────────────────┐
│      React UI        │
│  Incident submission │
└──────────┬───────────┘
           │ HTTP
           ▼
┌──────────────────────┐
│       FastAPI        │
│    /investigate      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Strands Agent      │
│                      │
│ Objective + Tools    │
│ Autonomous Tool      │
│ Selection + Loop     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Qwen3 4B /        │
│       Ollama         │
└──────────┬───────────┘
           │
     ┌─────┴─────────────────────────┐
     │                               │
     ▼                               ▼
 Investigation Tools          Safety Boundary
     │                               │
     ├── Search Logs                 └── Rollback
     ├── Deployment History              ↓
     ├── API Inspection             Human Approval
     ├── Version Comparison
     └── Regression Test
```

---

## Agent Architecture

FixPilot is intentionally implemented as an agent rather than a deterministic workflow.

The LLM is responsible for deciding:

* Which investigation tool to call
* What arguments to provide
* What evidence is relevant
* What hypothesis should be investigated next
* When the available evidence is sufficient
* What the final investigation report should contain

Deterministic Python code is responsible for:

* Executing tools
* Accessing simulated production data
* Running regression tests
* Validating action permissions
* Enforcing human approval requirements

This separation allows the AI to reason about the investigation while keeping execution and safety controls deterministic.

---

## Investigation Tools

### `search_logs`

Searches production logs for a service and search term.

### `get_deployment_history`

Returns recent deployment information for a service.

### `inspect_api_response`

Inspects the latest simulated API response for a service.

### `compare_versions`

Compares the relevant code between two service versions.

### `run_regression_test`

Runs a regression test against the suspected failure.

### `rollback_deployment`

Simulates a deployment rollback.

Rollback is classified as a risky action and cannot execute without explicit human approval.

---

## Structured Investigation Report

FixPilot produces a structured report containing:

```text
Incident ID
Observed Evidence
Inferences
Unresolved Hypotheses
Root Cause
Recommendations
```

The report intentionally separates observed evidence from inference and unresolved hypotheses.

This helps prevent the agent from presenting an unverified assumption as a confirmed root cause.

---

## Human-in-the-Loop Safety

Investigation can be autonomous, but production-changing actions require human approval.

For example:

```text
Agent identifies rollback as a recommendation
                ↓
      Proposed Action
                ↓
        Risk Evaluation
                ↓
       Human Approval
          ↙         ↘
       Denied      Approved
         ↓            ↓
      Blocked       Execute
```

An unapproved rollback is rejected by the deterministic safety layer.

This creates a clear boundary:

**Autonomous investigation, human-controlled production changes.**

---

## Example Incident

For the simulated `product-service` incident:

```text
KeyError: price
```

FixPilot can discover evidence showing:

* The production logs contain the `KeyError`.
* The regression test reproduces the failure.
* The suspected code path accesses `price` directly.
* A remediation may involve rolling back to the previous version and/or adding input validation.

The final report distinguishes evidence from inference and provides remediation recommendations.

---

## Technology Stack

* **Python**
* **Strands Agents SDK**
* **Ollama**
* **Qwen3 4B**
* **FastAPI**
* **React**
* **Vite**
* **Pydantic**

---

## Running Locally

### Backend

From the project root:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start FastAPI:

```powershell
python -m uvicorn backend.app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Health check:

```text
GET /health
```

Investigation endpoint:

```text
POST /investigate
```

Example request:

```json
{
  "incident_id": "INC-1001",
  "service": "product-service",
  "observed_error": "KeyError: price"
}
```

### Frontend

```powershell
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## Project Structure

```text
Fix-Pilot/
├── backend/
│   └── app/
│       ├── agent.py
│       ├── main.py
│       ├── models.py
│       ├── safety.py
│       ├── data/
│       └── tools/
│
├── frontend/
│   └── src/
│
├── .env
├── .gitignore
├── README.md
└── requirement.txt
```

---

## Current Prototype Scope

FixPilot currently uses simulated production data so the complete investigation and safety workflow can be demonstrated without making uncontrolled changes to a real production environment.

The architecture is designed so these simulated tools can later be replaced by integrations with real observability, deployment, API, source-control, and testing systems.

---

## Future Improvements

Potential next steps include:

* Real log/observability integrations
* Real deployment history integrations
* Source-control integration
* More comprehensive regression-test generation
* Persistent incident history
* Improved evaluation datasets
* Agent reliability and latency optimization
* Production-grade authentication and authorization
* Human approval UI for risky actions
* Cloud deployment

---

## Hackathon Focus

FixPilot demonstrates how an AI agent can move beyond simple question answering and perform a multi-step production investigation using tools.

The central design principle is:

> **Let the agent decide what evidence to investigate, while deterministic software controls execution and safety.**
