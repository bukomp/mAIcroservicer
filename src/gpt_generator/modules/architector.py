from gpt_generator.helpers.gpt_requests import create_chat_completion
from helpers.architecture_extractor import project_extractor
from helpers.config import config

from models.gpt_responses_interface import ArchitectorResponse


def gpt_architector(prompt: str) -> list[ArchitectorResponse | str]:
  """
  Generates a GPT-3 response for architectural design using a given prompt.

  Parameters:
  - prompt (str): The prompt for the GPT-3 model.

  Returns:
  - ArchitectorResponse: An object containing the generated architectural design project.

  Raises:
  - Exception: If an error occurs during the generation process.
  """
  try:
    response: str = create_chat_completion("architector", 0.4, [], [prompt])
    project = project_extractor(response)

    return [project, response]
  except Exception as e:
    print(f"An error occurred: {e}{__name__}")
    return []
