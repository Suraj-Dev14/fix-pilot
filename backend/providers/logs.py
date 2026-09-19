from abc import ABC, abstractmethod

class LogProvider(ABC):
  """Interface for retrieving application logs."""

  @abstractmethod
  def search(self, service: str, search_term: str) -> list[dict]:
    """Search logs for a service."""
    raise NotImplementedError