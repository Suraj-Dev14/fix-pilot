from strands import tool

from backend.providers.factory import registry


log_provider = registry.get_log_provider()


@tool
def search_logs(
    service: str, 
    search_term: str,
    start_time: int | None = None,
    end_time: int | None = None,
) -> list[dict]:
    """Search logs for a service and return entries containing the search term."""
    return log_provider.search(
        service=service,
        search_term=search_term,
        start_time=start_time,
        end_time=end_time,
    )