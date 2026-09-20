from backend.app.data.versions import VERSIONS

from .source import SourceProvider

class DemoSourceProvider(SourceProvider):
  """"Source provider backed by simulated FixPilot version data."""

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
      "service": old["service"],
      "old_version": old_version,
      "new_version": new_version,
      "old_code": old["code"],
      "new_code": new["code"],
    }