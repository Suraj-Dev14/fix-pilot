from abc import ABC, abstractmethod

class SourceProvider(ABC):
  """Interface for accessing source control information."""

  @abstractmethod
  def get_repository_info(self) -> dict:
    """Return repository information."""
    raise NotImplementedError

  @abstractmethod
  def get_recent_commits(self, limit: int = 10) -> list[dict]:
        """Return recent commits."""
        raise NotImplementedError

  @abstractmethod
  def compare_versions(self, old_version: str, new_version: str) -> dict:
        """Compare two versions."""
        raise NotImplementedError

  @abstractmethod
  def get_file(self, path: str) -> str:
        """Return source-code contents for a file."""
        raise NotImplementedError