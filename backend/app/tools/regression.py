from strands import tool

from backend.providers.factory import registry


regression_provider = registry.get_regression_provider()


@tool
def run_regression_test() -> dict:
    """Run a regression test."""
    return regression_provider.run()