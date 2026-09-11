from strands import Agent
from strands.models.ollama import OllamaModel


model = OllamaModel(
    host="http://localhost:11434",
    model_id="qwen3:4b",
)

agent = Agent(
    model=model,
)

response = agent("Explain what a production incident is in one paragraph.")

print(response)