import openai

from helpers.config import config
from models.gpt_requests_interface import Prompt


def create_chat_completion(
        LLM_model: str,
        temperature: float,
        system_prompts: list[str] = [],
        assistant_prompts: list[str] = [],
        user_prompts: list[str] = [],
        prompts_in_order: list[Prompt] = []
) -> str:
  """
  This function creates a chat completion using OpenAI's model.

  Args:
      LLM_model (str): The model to be used for generating the chat completion.
      temperature (float): The temperature of the model's output. Higher values result in more random completions, while lower values make the output more deterministic.
      system_prompts (list[str], optional): A list of system prompts to be included in the chat completion. Defaults to an empty list.
      assistant_prompts (list[str], optional): A list of assistant prompts to be included in the chat completion. Defaults to an empty list.
      user_prompts (list[str], optional): A list of user prompts to be included in the chat completion. Defaults to an empty list.
      prompts_in_order (list[Prompt], optional): A list of prompts in the order they should appear in the chat completion. Defaults to an empty list.

  Returns:
      str: The content of the message from the first choice in the chat completion.
  """
  try:
    openai.organization = config.secrets.GPT_ORG
    openai.api_key = config.secrets.GPT_KEY
    openai.Model.list()
    chat_completion = openai.ChatCompletion.create(
        model=LLM_model,
        messages=[
            * [{"role": "system", "content": system_prompt}
               for system_prompt in system_prompts],
            * [{"role": "system", "content": assistant_prompt}
               for assistant_prompt in assistant_prompts],
            * [{"role": "user", "content": user_prompt}
               for user_prompt in user_prompts],
            * [prompt_in_order
               for prompt_in_order in prompts_in_order],
        ],
        temperature=temperature
    )
    choise = chat_completion.choices[0]  # type: ignore
    content: str = choise.message['content']

    print(content)

    return content
  except Exception as e:
    print(f"An error occurred: {e} \n{__file__}")
    return str(e)
