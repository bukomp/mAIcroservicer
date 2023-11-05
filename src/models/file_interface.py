from validators.file_structure_validator import requirements_txt_validator


class File:
  def __init__(self, name: str, content: str, path: str = ""):
    self._name = name
    self._content = self.validate_content(name, content)
    self._path = path

  @property
  def name(self) -> str:
    return self._name

  @property
  def content(self) -> str:
    return self._content

  @property
  def path(self) -> str:
    return self._path

  def validate_content(self, name: str, content: str) -> str:
    validators = {"requirements.txt": requirements_txt_validator}
    if name in validators:
      return validators[name](content)
    return content


class FileCollection:
  def __init__(self, project_root: str):
    self._project_root = project_root
    self._collections: dict[str, list[File]] = {
        "raw_responses": [], "formatted_responses": []}

  @property
  def project_root(self) -> str:
    return self._project_root

  @property
  def collections(self) -> dict[str, list[File]]:
    return self._collections

  #! Unused function
  def add_file(self, collection_name: str, file: File) -> None:
    self.collections[collection_name].append(file)
