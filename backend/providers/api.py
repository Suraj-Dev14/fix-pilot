from abc import ABC, abstractmethod

class ApiProvider(ABC):
  """Interface for inspecting application API responses."""

  @abstractmethod
  def inspect_response(self, service: str) -> dict:
    """Inspect the latest API response for a service."""
    raise NotImplementedError