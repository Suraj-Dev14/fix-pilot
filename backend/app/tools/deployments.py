from strands import tool

from backend.app.data.deployments import DEPLOYMENTS


@tool
def get_deployment_history(service: str) -> list[dict]:
    """Return deployment history for a service."""

    return [
        deployment
        for deployment in DEPLOYMENTS
        if deployment["service"] == service
    ]