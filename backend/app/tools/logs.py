from strands import tool

LOGS = [
    {
        "service": "product-service",
        "level": "ERROR",
        "message": "KeyError: price",
    },
    {
        "service": "product-service",
        "level": "INFO",
        "message": "Request completed successfully",
    },
    {
        "service": "user-service",
        "level": "ERROR",
        "message": "Database connection timeout",
    },
]

@tool
def search_logs(service: str, search_term: str) -> list[dict]:
    """Search logs for a service and return entries containing the search term."""

    results = []

    for log in LOGS:
        if (
            log["service"] == service
            and search_term.lower() in log["message"].lower()
        ):
            results.append(log)

    return results