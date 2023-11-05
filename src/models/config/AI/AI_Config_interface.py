from .AI_Entity_interface import AI_Entity
from ..prompt_dictionary_interface import PromptDictionary


class AI_Config:
  def __init__(
      self,
      architectors: list[AI_Entity],
      workers: list[AI_Entity],
      acceptance: list[AI_Entity],
      general_architector_system_prompt: str,
      general_worker_system_prompt: str
  ):
    self._architectors = architectors
    self._workers = workers
    self._acceptance = acceptance
    self._general_architector_system_prompt = general_architector_system_prompt
    self._general_worker_system_prompt = general_worker_system_prompt

  @property
  def architectors(self) -> list[AI_Entity]:
    return self._architectors

  @property
  def workers(self) -> list[AI_Entity]:
    return self._workers

  @property
  def acceptance(self) -> list[AI_Entity]:
    return self._acceptance

  @property
  def general_architector_system_prompt(self) -> str:
    return PromptDictionary().get_prompt(self._general_architector_system_prompt)

  @property
  def general_worker_system_prompt(self) -> str:
    return PromptDictionary().get_prompt(self._general_worker_system_prompt)
