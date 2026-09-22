from backend.config import load_config
from backend.providers.registry import ProviderRegistry


config = load_config()
registry = ProviderRegistry(config)

provider = registry.get_source_provider()

result = provider.compare_versions(
    old_version="43cc9a6",
    new_version="d6eb0e9",
)

print("Provider:", type(provider).__name__)
print("Old commit:", result["old_commit"])
print("New commit:", result["new_commit"])
print("Changed files:", result["changed_files"])