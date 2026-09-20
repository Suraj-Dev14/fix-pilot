from backend.config import load_config
from backend.providers.registry import ProviderRegistry


config = load_config()

registry = ProviderRegistry(config)

print(type(registry.get_log_provider()).__name__)
print(type(registry.get_deployment_provider()).__name__)
print(type(registry.get_source_provider()).__name__)
print(type(registry.get_api_provider()).__name__)
print(type(registry.get_regression_provider()).__name__)