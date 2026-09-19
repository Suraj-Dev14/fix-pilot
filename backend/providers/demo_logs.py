from .logs import LogProvider

class DemoLogProvider(LogProvider):
  """Log provider backed by simulated FixPilot demo data."""

  def __init__(self):
    self.logs = [
      {
        "service": "product-service",
        "level": "ERROR",
        "message": "KeyError: price",
      },
      {
        "service": "product-service",
        "level": "INFO",
        "message": "Request completed successfully",
      },
      {
        "service": "payment-service",
        "level": "ERROR",
        "message": "Database connection timeout",
      },
    ]

  def search(self, service: str, search_term: str) -> list[dict]:
    results = []

    for log in self.logs:
      if log["service"] != service:
        continue

      if search_term.lower() in log["message"].lower():
        results.append(log)

    return results