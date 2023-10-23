import openai
import os

from helpers.config import config
from helpers.utils import format_version


def create_chat_completion(prompt_mode: str, temperature: float, system_prompts: list[str], user_prompts: list[str]) -> str:
  """
  Create a chat completion using OpenAI GPT-3.

  Args:
      prompt_mode (str): The mode in which the prompt is generated. Must be either 'architector' or 'worker'.
      temperature (float): The temperature of the model's output. Higher values result in more random completions, while lower values make the output more focused.
      system_prompts (list[str]): The list of system prompts to be included in the chat completion.
      user_prompts (list[str]): The list of user prompts to be included in the chat completion.

  Returns:
      dict: The response from the OpenAI ChatCompletion.create() API.

  Raises:
      AssertionError: If the prompt_mode is not 'architector' or 'worker'.

  """
  assert prompt_mode in [
      "architector", "worker"], "Invalid prompt_mode. Expected 'architector' or 'worker'"

  openai.organization = config['GPT_ORG']
  openai.api_key = config['GPT_KEY']
  openai.Model.list()
  chat_completion = openai.ChatCompletion.create(
      model=config[f"GPT_{prompt_mode.upper()}_MODEL"],
      messages=[
          {"role": "system", "content": get_system_prompt(prompt_mode)},
          * [{"role": "system", "content": system_prompt}
             for system_prompt in system_prompts],
          * [{"role": "user", "content": user_prompt}
             for user_prompt in user_prompts],
      ],
      temperature=temperature
  )
  choise = chat_completion.choices[0]  # type: ignore
  content: str = choise.message['content']
  return content


def get_system_prompt(prompt_mode: str) -> str:
  with open(os.path.join('src', 'prompts', prompt_mode,
                         f"{prompt_mode}_system_v{format_version(config[f"{prompt_mode.upper()}_PROMPT_VERSION"])}.txt"), 'r') as file:
    return file.read().replace('\n', '')
