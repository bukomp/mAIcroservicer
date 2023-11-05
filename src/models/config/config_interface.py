from .AI.AI_Config_interface import AI_Config
from .AI.AI_Entity_interface import AI_Entity
from .Secrets_interface import Secrets


class Config:
  def __init__(
          self,
          config: dict,
          secrets: Secrets,
  ):
    self._secrets = secrets
    self._ai_config = get_config_return_AI_Config(config["ai_config"])
    self._base_dir = str(config["base_dir"])
    self._base_path_to_prompts = str(config["base_path_to_prompts"])

  @property
  def secrets(self) -> Secrets:
    return self._secrets

  @property
  def ai_config(self) -> AI_Config:
    return self._ai_config

  @property
  def base_dir(self) -> str:
    return self._base_dir

  @property
  def base_path_to_prompts(self) -> str:
    return self._base_path_to_prompts


def get_config_return_AI_Config(obj: dict) -> AI_Config:
  """
  Generates a new AI_Config object based on the provided configuration dictionary.

  Parameters:
    config (dict): A dictionary containing the configuration for the AI_Config object.

  Returns:
    AI_Config: The newly generated AI_Config object.
  """
  return AI_Config(
      [AI_Entity(**architector)
       for architector in obj["architectors"]],
      [AI_Entity(**worker) for worker in obj["workers"]],
      [AI_Entity(**acceptance)
       for acceptance in obj["acceptance"]],
      obj["general_architector_system_prompt"],
      obj["general_worker_system_prompt"],
  )
