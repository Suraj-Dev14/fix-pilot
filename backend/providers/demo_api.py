from backend.app.data.api_responses import API_RESPONSES

from .api import ApiProvider

class DemoApiProvider(ApiProvider):
  """API provider backed by simulated FixPilot demo data."""

  def inspect_response(self, service: str) -> dict:
    return API_RESPONSES.get(service, {
      "status_code": 404,
      "body": {},
    })