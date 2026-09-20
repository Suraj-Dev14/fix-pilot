from strands import tool

from backend.providers.factory import registry


api_provider = registry.get_api_provider()


@tool
def inspect_api_response(service: str) -> dict:
    """Inspect the latest API response for a service."""
    return api_provider.inspect_response(
        service=service,
    )