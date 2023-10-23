class File_to_write:
  def __init__(self, name: str, content: str, path: str = ""):
    self.name = name
    self.content = content
    self.path = path


class File_Collection:
  def __init__(self, project_root: str):
    self.project_root = project_root
    self.collections: dict[str, list[File_to_write]] = {
        "raw_responses": [], "formatted_responses": []}

  def add_file(self, collection_name: str, file: File_to_write):
    self.collections[collection_name].append(file)
