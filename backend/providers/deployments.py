from abc import ABC, abstractmethod

class DeploymentProvider(ABC):
  """Interface for retrieving deployment information."""

  @abstractmethod
  def get_history(self, service: str) -> list[dict]:
    """Return deployment history for a service."""
    raise NotImplementedError