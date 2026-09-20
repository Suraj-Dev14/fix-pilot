from strands import tool

from backend.providers.demo_api import DemoApiProvider

api_provider = DemoApiProvider()


@tool
def inspect_api_response(service: str) -> dict:
    """Inspect the latest API response for a service."""

    return api_provider.inspect_response(service)