

class FileExplanation:
  def __init__(self, file_name: str, description: str):
    self._file_name = file_name
    self._description = description

  @property
  def file_name(self) -> str:
    return self._file_name

  @property
  def description(self) -> str:
    return self._description


class ArchitectorResponse:
  def __init__(self, name: str, structure: str, files: list[FileExplanation]):
    self._name = name
    self._structure = structure
    self._files = files

  @property
  def name(self) -> str:
    return self._name

  @property
  def structure(self) -> str:
    return self._structure

  @property
  def files(self) -> list[FileExplanation]:
    return self._files
