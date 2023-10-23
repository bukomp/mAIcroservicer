

class FileExplanation:
  def __init__(self, file_name: str, description: str):
    self.file_name = file_name
    self.description = description

  def get(self):
    return {
        "file_name": self.file_name,
        "description": self.description,
    }


class ArchitectorResponse:
  def __init__(self, name: str, structure: str, files: list[FileExplanation]):
    self.name = name
    self.structure = structure
    self.files = files

  def get(self):
    return {
        "name": self.name,
        "structure": self.structure,
        "files": [file.get() for file in self.files],
    }
