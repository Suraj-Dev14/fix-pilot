from strands import tool

from backend.app.data.api_responses import API_RESPONSES


@tool
def inspect_api_response(service: str) -> dict:
    """Inspect the latest API response for a service."""

    return API_RESPONSES.get(
        service,
        {
            "status_code": 404,
            "body": {},
        },
    )