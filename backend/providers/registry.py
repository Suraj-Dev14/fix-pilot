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
        source_config = self.config.integrations.source_control
        provider_name = source_config.provider

        if provider_name == "demo":
            from .demo_source import DemoSourceProvider

            return DemoSourceProvider()

        if provider_name == "local_git":
            from .local_git import LocalGitProvider

            return LocalGitProvider(
                repository_path=source_config.repository_path,
            )

        if provider_name == "github":
            from .github import GitHubProvider

            if not source_config.repository:
                raise ValueError(
            "GitHub source provider requires a repository."
            )

            return GitHubProvider(
                repository=source_config.repository
            )

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
        regression_config = self.config.integrations.regression
        provider_name = regression_config.provider

        if provider_name == "local":
            from .local_regression import LocalRegressionProvider

            return LocalRegressionProvider(
                command=regression_config.command,
            )

        raise ValueError(
            f"Unsupported regression provider: {provider_name}"
        )