from strands import tool

from backend.providers.demo_source import DemoSourceProvider

source_provider = DemoSourceProvider()

@tool
def compare_versions(
    service: str,
    old_version: str,
    new_version: str,
) -> dict:
    """Compare the code for two versions of a service."""

    result = source_provider.compare_versions(old_version, new_version)

    if "error" in result:
        return result

    if result["service"] != service:
        return {"error": "Version does not belong to the requested service."}

    return result