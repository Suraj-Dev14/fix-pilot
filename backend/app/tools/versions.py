from strands import tool

from backend.providers.factory import registry


source_provider = registry.get_source_provider()


@tool
def compare_versions(
    service: str,
    old_version: str,
    new_version: str,
) -> dict:
    """Compare the code for two versions of a service."""

    result = source_provider.compare_versions(
        old_version=old_version,
        new_version=new_version,
    )

    if "error" in result:
        return result

    if result["service"] != service:
        return {
            "error": "Version does not belong to the requested service."
        }

    return result