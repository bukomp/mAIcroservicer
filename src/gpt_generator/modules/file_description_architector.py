import os
from gpt_generator.helpers.gpt_requests import create_chat_completion
from helpers.architecture_extractor import extract_file_description, strurcture_to_list_of_files
from helpers.config import config


from models.gpt_responses_interface import ArchitectorResponse


def gpt_file_description_architector(project: ArchitectorResponse, prompt: str) -> list[ArchitectorResponse | str]:

  try:
    project_structure = project.structure
    architector_config = next(
        (architector for architector
         in config.ai_config.architectors if architector.name == "file_architector"),
        None)

    if not architector_config:
      raise ValueError(
          "Architector 'file_architector' not found in config.")

    response: str = create_chat_completion(
        architector_config.model,
        float(architector_config.temperature),
        architector_config.system_prompts + [],
        architector_config.assistant_prompts + [],
        architector_config.user_prompts +
        [prompt, project_structure, str(
            strurcture_to_list_of_files(project_structure))]
    )

    project._files = extract_file_description(response)

    return [project, response]
  except Exception as e:
    print(f"An error occurred: {e} in {__name__}")
    return []
