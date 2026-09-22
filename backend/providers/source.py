from abc import ABC, abstractmethod

class SourceProvider(ABC):
  """Interface for accessing source control information."""

  @abstractmethod
  def get_recent_commits(self, limit: int = 10) -> list[dict]:
      """Return recent commits from the repository."""
      raise NotImplementedError

  @abstractmethod
  def compare_versions(self, old_version: str, new_version: str) -> dict:
        """Compare two versions."""
        raise NotImplementedError
