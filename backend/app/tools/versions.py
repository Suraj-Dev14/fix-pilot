from strands import tool

from backend.providers.factory import registry


source_provider = registry.get_source_provider()

@tool
def get_recent_commits(limit: int = 10) -> list[dict]:
    """Return recent commits from the configured source repository."""
    return source_provider.get_recent_commits(limit=limit)

@tool
def compare_versions(
    old_version: str,
    new_version: str,
) -> dict:
    """Compare two versions in the configured source repository."""

    return source_provider.compare_versions(
        old_version=old_version,
        new_version=new_version,
    )