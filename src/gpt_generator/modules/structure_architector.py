import os
from gpt_generator.helpers.gpt_requests import create_chat_completion
from helpers.architecture_extractor import project_extractor
from helpers.config import config


from models.gpt_responses_interface import ArchitectorResponse


async def gpt_project_structure_architector(prompt: str) -> list[ArchitectorResponse | str]:

  try:
    architector_config = next(
        (architector for architector
         in config.ai_config.architectors if architector.name == "structure_architector"),
        None)

    if not architector_config:
      raise ValueError(
          "Architector 'structure_architector' not found in config.")

    response: str = await create_chat_completion(
        architector_config.model,
        float(architector_config.temperature),
        architector_config.system_prompts + [],
        architector_config.assistant_prompts + [],
        architector_config.user_prompts + [prompt]
    )

    project = project_extractor(response)

    return [project, response]
  except Exception as e:
    print(f"An error occurred: {e} in {__name__}")
    return []
