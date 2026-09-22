from strands import Agent
from strands.models.ollama import OllamaModel

from backend.app.models import InvestigationReport
from backend.app.tools.logs import search_logs
from backend.app.tools.deployments import get_deployment_history
from backend.app.tools.api import inspect_api_response
from backend.app.tools.versions import compare_versions, get_recent_commits
from backend.app.tools.regression import run_regression_test
from backend.app.tools.rollback import rollback_deployment


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
        get_recent_commits,
        compare_versions,
        run_regression_test,
        rollback_deployment,
    ],
    structured_output_model=InvestigationReport,
)