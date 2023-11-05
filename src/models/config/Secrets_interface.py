class Secrets:
  def __init__(self, GPT_ORG: str | None, GPT_KEY: str | None, PATH_TO_CONFIG: str | None):
    if GPT_ORG is None or GPT_KEY is None:
      raise ValueError("GPT_ORG and/or GPT_KEY cannot be undefined")
    if PATH_TO_CONFIG is None:
      raise ValueError("PATH_TO_CONFIG cannot be undefined")
    self._GPT_ORG = GPT_ORG
    self._GPT_KEY = GPT_KEY
    self._PATH_TO_CONFIG = PATH_TO_CONFIG

  @property
  def GPT_ORG(self) -> str:
    return self._GPT_ORG

  @property
  def GPT_KEY(self) -> str:
    return self._GPT_KEY

  @property
  def PATH_TO_CONFIG(self) -> str:
    return self._PATH_TO_CONFIG
