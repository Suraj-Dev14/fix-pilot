from strands import tool

from backend.app.data.versions import VERSIONS


@tool
def compare_versions(
    service: str,
    old_version: str,
    new_version: str,
) -> dict:
    """Compare the code for two versions of a service."""

    old = VERSIONS.get(old_version)
    new = VERSIONS.get(new_version)

    if not old or not new:
        return {
            "error": "One or both versions were not found."
        }

    if old["service"] != service or new["service"] != service:
        return {
            "error": "Version does not belong to the requested service."
        }

    return {
        "service": service,
        "old_version": old_version,
        "new_version": new_version,
        "old_code": old["code"],
        "new_code": new["code"],
    }