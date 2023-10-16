
from helpers.config import config
import openai
from prompts.system_v0_4 import *
from prompts.libs.SuDoLang_Primer_T0_v1_07.prompt import *


def gpt_main(prompt: str) -> str:
  try:
    openai.organization = config['GPT_ORG']
    openai.api_key = config['GPT_KEY']
    openai.Model.list()
    # Create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model=config['GPT_MODEL'],
        messages=[
            {"role": "system", "content": systemPrompt},
            # {"role": "system", "content": systemPrompt_lib_SuDoLang_Primer_T0_v1_07},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1
    )
    return chat_completion.choices[0].message['content']  # type: ignore
  except Exception as e:
    print(f"An error occurred: {e}")
    return ""
