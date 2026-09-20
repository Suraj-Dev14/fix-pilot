from strands import tool

from backend.providers.demo_regression import DemoRegressionProvider


regression_provider = DemoRegressionProvider()


@tool
def run_regression_test() -> dict:
    """Run a regression test for the missing price incident."""
    return regression_provider.run()