class Prompt:
  def __init__(self, role: str, content: str):
    if role not in ["system", "user", "assistant"]:
      raise ValueError("Role is not 'system', 'user', or 'assistant'")
    self._role = role
    self._content = content

  @property
  def role(self) -> str:
    return self._role

  @property
  def content(self) -> str:
    return self._content
