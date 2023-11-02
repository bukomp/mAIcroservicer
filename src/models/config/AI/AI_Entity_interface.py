from models.config.prompt_dictionary_interface import PromptDictionary


class AI_Entity:
  def __init__(self, name: str, description: str, system_prompts: list[str], assistant_prompts: list[str], user_prompts: list[str], ignore_general_system_prompts: bool, model: str, temperature: str):
    self._name = name
    self._description = description
    self._system_prompts = system_prompts
    self._assistant_prompts = assistant_prompts
    self._user_prompts = user_prompts
    self._ignore_general_system_prompts = ignore_general_system_prompts
    self._model = model
    self._temperature = temperature

  @property
  def name(self) -> str:
    return self._name

  @property
  def description(self) -> str:
    return self._description

  @property
  def system_prompts(self) -> list[str]:
    return [PromptDictionary().get_prompt(prompt) for prompt in self._system_prompts]

  @property
  def assistant_prompts(self) -> list[str]:
    return [PromptDictionary().get_prompt(prompt) for prompt in self._assistant_prompts]

  @property
  def user_prompts(self) -> list[str]:
    return [PromptDictionary().get_prompt(prompt) for prompt in self._user_prompts]

  @property
  def ignore_general_system_prompts(self) -> bool:
    return self._ignore_general_system_prompts

  @property
  def model(self) -> str:
    return self._model

  @property
  def temperature(self) -> str:
    return self._temperature
