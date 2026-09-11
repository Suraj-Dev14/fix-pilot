from strands import Agent
from strands.models.ollama import OllamaModel

from backend.app.tools.logs import search_logs


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:4b",
)

agent = Agent(
    model=model,
    tools=[search_logs],
)

response = agent(
    """
    Investigate this production incident.

    Incident: INC-1001
    Service: product-service
    Observed error: KeyError: price

    You have access to a production log search tool.
    Investigate the incident using the available evidence.
    Explain what you find.
    """
)

print(response)