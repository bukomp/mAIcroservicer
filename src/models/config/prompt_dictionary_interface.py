import json
import os


class PromptDictionary:
  def __init__(self):
    with open('prompt_dictionary.json', encoding='utf-8') as f:
      self.prompt_dictionary = json.load(f)

  def get_prompt(self, path_or_version: str) -> str:

    if os.path.isfile(path_or_version):
      with open(path_or_version, 'r', encoding='utf-8') as file:
        return file.read()
    else:
      prompt_path = self._get_value_from_path(
          self.prompt_dictionary, path_or_version)
      if os.path.isfile(prompt_path):
        with open(prompt_path, 'r', encoding='utf-8') as file:
          return file.read()
      else:
        return "File not found"

  def _get_value_from_path(self, d, path_str):
    temp = d
    for key in path_str.split('.'):
      if key in temp:
        temp = temp[key]
      else:
        return "Key not found"
    return temp
