from backend.app.data.deployments import DEPLOYMENTS

from .deployments import DeploymentProvider

class DemoDeploymentProvider(DeploymentProvider):
  """Deployment provider backed by simulated FixPilot demo data."""

  def get_history(self, service: str) -> list[dict]:
    return [
      deployment for deployment in DEPLOYMENTS if deployment["service"] == service
    ]