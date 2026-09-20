from abc import ABC, abstractmethod

class SourceProvider(ABC):
  """Interface for accessing source control information."""

  @abstractmethod
  def compare_versions(self, old_version: str, new_version: str) -> dict:
        """Compare two versions."""
        raise NotImplementedError
