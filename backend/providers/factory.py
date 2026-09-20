from backend.config import load_config

from .registry import ProviderRegistry


config = load_config()

registry = ProviderRegistry(config)