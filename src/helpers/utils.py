

import os

from models.config.prompt_dictionary_interface import PromptDictionary


# def format_version(version: int | str | float) -> str:
#  """
#  Format the given version number by joining its parts with an underscore and removing any dots.
#
#  Parameters:
#      version (int | str | float): The version number to be formatted.
#
#  Returns:
#      str: The formatted version number.
#  """
#  return "_".join(str(version).replace(".", ""))
#
#
# def get_architector_system_prompt() -> str:
#  with open(os.path.join('src', 'prompts', "architector",
#                         f"architector_system_v{format_version(config[f"ARCHITECTOR_SYSTEM_PROMPT_VERSION"])}.txt"), 'r') as file:
#    return file.read().replace('\n', '')
#
#
# def get_worker_system_prompt() -> str:
#  with open(os.path.join('src', 'prompts', "worker",
#                         f"worker_system_v{format_version(config[f"WORKER_SYSTEM_PROMPT_VERSION"])}.txt"), 'r') as file:
#    return file.read().replace('\n', '')
