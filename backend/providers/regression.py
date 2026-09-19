from abc import ABC, abstractmethod


class RegressionProvider(ABC):
    """Interface for running regression validation."""

    @abstractmethod
    def run(self, command: str | None = None) -> dict:
        """Run a controlled regression test."""
        raise NotImplementedError