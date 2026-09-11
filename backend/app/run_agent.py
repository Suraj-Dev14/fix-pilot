from strands import Agent
from strands.models.ollama import OllamaModel

from backend.app.tools.logs import search_logs
from backend.app.tools.deployments import get_deployment_history


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:4b",
)

agent = Agent(
    model=model,
    tools=[search_logs, get_deployment_history],
)

response = agent(
    """
    Investigate this production incident.

    Incident: INC-1001
    Service: product-service
    Observed error: KeyError: price

    You have access to production investigation tools.

    Investigate the incident using the available tools.

    Do not assume the first piece of evidence is the root cause.
    Gather additional evidence when another available tool could help validate or narrow the hypothesis.

    Clearly distinguish:
    - observed evidence
    - your inference
    - unresolved hypotheses

    Only conclude a root cause when the available evidence supports it.
    Explain what you find.
    """
)

print(response)