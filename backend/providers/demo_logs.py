from backend.app.data.logs import LOGS

from .logs import LogProvider

class DemoLogProvider(LogProvider):
  """Log provider backed by simulated FixPilot demo data."""

  def search(
      self, 
      service: str, 
      search_term: str,
      start_time: int | None = None,
      end_time: int | None = None,
    ) -> list[dict]:
    results = []

    for log in LOGS:
      if log["service"] != service:
        continue

      if search_term.lower() in log["message"].lower():
        results.append(log)

    return results