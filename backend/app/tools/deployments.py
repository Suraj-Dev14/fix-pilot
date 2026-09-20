from strands import tool

from backend.providers.demo_deployments import DemoDeploymentProvider

deployment_provider = DemoDeploymentProvider()


@tool
def get_deployment_history(service: str) -> list[dict]:
    """Return deployment history for a service."""

    return deployment_provider.get_history(service)