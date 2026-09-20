from strands import tool

from backend.providers.factory import registry


deployment_provider = registry.get_deployment_provider()


@tool
def get_deployment_history(service: str) -> list[dict]:
    """Return deployment history for a service."""
    return deployment_provider.get_history(
        service=service,
    )