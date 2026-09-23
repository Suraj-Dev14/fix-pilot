from pathlib import Path
import yaml

from pydantic import BaseModel, Field, ValidationError
from typing import Literal

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config.yaml"

class ProjectConfig(BaseModel):
  name: str = Field(min_length=1)

class ServiceConfig(BaseModel):
  name: str = Field(min_length=1)

class SourceControlConfig(BaseModel):
  provider: str = Field(min_length=1)
  repository_path: str = Field(min_length=1)

class RegressionConfig(BaseModel):
  provider: str = Field(min_length=1)
  command: str = Field(min_length=1)

class IntegrationsConfig(BaseModel):
  logs: str = Field(min_length=1)
  source_control: SourceControlConfig
  deployments: str = Field(min_length=1)
  api: str = Field(min_length=1)
  regression: RegressionConfig

class IncidentConfig(BaseModel):
  default_severity: str = Field(min_length=1)

class FixPilotConfig(BaseModel):
  project: ProjectConfig
  service: ServiceConfig
  environment: Literal["development", "staging", "production"]
  integrations: IntegrationsConfig
  incident: IncidentConfig

def load_config() -> FixPilotConfig:
  if not CONFIG_PATH.exists():
    raise RuntimeError(
      f"FixPilot configuration file not found: {CONFIG_PATH}"
    )
  try:

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
      raw_config = yaml.safe_load(file)

    return FixPilotConfig.model_validate(raw_config)
  
  except yaml.YAMLError as exc:
    raise RuntimeError(
      f"Invalid YAML configuration: {exc}"
    ) from exc

  except ValidationError as exc:
    raise RuntimeError(
      f"Invalid FixPilot configuration: \n{exc}"
    ) from exc