from backend.app.data.versions import VERSIONS

from .source import SourceProvider

class DemoSourceProvider(SourceProvider):
  """"Source provider backed by simulated FixPilot version data."""

  def get_recent_commits(self, limit: int = 10) -> list[dict]:
    """Return recent simulated versions."""
    return [
        {
            "version": version,
            "service": data["service"],
        }
        for version, data in list(VERSIONS.items())[:limit]
    ]

  def compare_versions(
      self,
      old_version: str,
      new_version: str,
  ) -> dict:
    old = VERSIONS.get(old_version)
    new = VERSIONS.get(new_version)

    if not old or not new:
      return {
        "error": "One or both versions were not found."
      }

    if old["service"] != new["service"]:
      return {
        "error": "Version does not belong to the requested service."
      }

    return {
      "old_version": old_version,
      "new_version": new_version,
      "changed_files": [],
      "diff": (
        f"--- {old_version}\n"
        f"{old['code']}\n"
        f"+++ {new_version}\n"
        f"{new['code']}"
      ),
    }