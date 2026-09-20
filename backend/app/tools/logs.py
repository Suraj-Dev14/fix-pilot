from strands import tool

from backend.providers.demo_logs import DemoLogProvider

log_provider = DemoLogProvider()

@tool
def search_logs(service: str, search_term: str) -> list[dict]:
    """Search logs for a service and return entries containing the search term."""

    return log_provider.search(service, search_term)