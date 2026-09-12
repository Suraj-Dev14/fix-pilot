from strands import Agent
from strands.models.ollama import OllamaModel

from backend.app.tools.logs import search_logs
from backend.app.tools.deployments import get_deployment_history
from backend.app.tools.api import inspect_api_response
from backend.app.tools.versions import compare_versions
from backend.app.tools.regression import run_regression_test

from backend.app.models import InvestigationReport


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:4b",
)

agent = Agent(
    model=model,
    tools=[
        search_logs,
        get_deployment_history,
        inspect_api_response,
        compare_versions,
        run_regression_test,
      ],
      structured_output_model=InvestigationReport,
)

response = agent(
    """
    Investigate this production incident.

    Incident: INC-1001
    Service: product-service
    Observed error: KeyError: price

    You have access to production investigation tools.

    Investigate the incident using the available tools.

    Follow this investigation policy:

    1. Gather evidence from production logs.
    2. Inspect relevant API responses when the error may involve input data.
    3. Inspect deployment history when a recent deployment may be involved.
    4. Compare the relevant versions when a code change may explain the error.
    5. Before concluding the root cause, run the available regression test when it can reproduce or validate the suspected failure.

    Do not assume the first piece of evidence is the root cause.

    Clearly distinguish:
    - observed evidence
    - inference
    - unresolved hypotheses
    - validated conclusions

    A code diff can explain why an error is possible, but a regression test should be used when available to verify that the suspected failure actually occurs.

    Only claim that a hypothesis is validated when the available evidence supports it.

    Explain your final findings.
    """
)

print(type(response))
print(response.structured_output)