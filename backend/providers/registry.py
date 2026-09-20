from backend.config import FixPilotConfig

from .api import ApiProvider
from .deployments import DeploymentProvider
from .logs import LogProvider
from .regression import RegressionProvider
from .source import SourceProvider

class ProviderRegistry:
    """Resolves configured provider implementations."""

    def __init__(self, config: FixPilotConfig):
        self.config = config

    def get_log_provider(self) -> LogProvider:
        provider_name = self.config.integrations.logs

        if provider_name == "demo":
            from .demo_logs import DemoLogProvider

            return DemoLogProvider()

        raise ValueError(
            f"Unsupported log provider: {provider_name}"
        )

    def get_deployment_provider(self) -> DeploymentProvider:
        provider_name = self.config.integrations.deployments

        if provider_name == "demo":
            from .demo_deployments import DemoDeploymentProvider

            return DemoDeploymentProvider()

        raise ValueError(
            f"Unsupported deployment provider: {provider_name}"
        )

    def get_source_provider(self) -> SourceProvider:
        provider_name = self.config.integrations.source_control

        if provider_name == "demo":
            from .demo_source import DemoSourceProvider

            return DemoSourceProvider()

        raise ValueError(
            f"Unsupported source provider: {provider_name}"
        )

    def get_api_provider(self) -> ApiProvider:
        provider_name = self.config.integrations.api

        if provider_name == "demo":
            from .demo_api import DemoApiProvider

            return DemoApiProvider()

        raise ValueError(
            f"Unsupported API provider: {provider_name}"
        )

    def get_regression_provider(self) -> RegressionProvider:
        provider_name = self.config.integrations.regression

        if provider_name == "demo":
            from .demo_regression import DemoRegressionProvider

            return DemoRegressionProvider()

        raise ValueError(
            f"Unsupported regression provider: {provider_name}"
        )