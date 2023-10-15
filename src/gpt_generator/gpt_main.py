
from helpers.config import config
import openai
from prompts.system_v0_2 import *


def gpt_main(prompt: str) -> str:
  openai.organization = config['GPT_ORG']
  openai.api_key = config['GPT_KEY']
  openai.Model.list()
  # Create a chat completion
  chat_completion = openai.ChatCompletion.create(
      model=config['GPT_MODEL'],
      messages=[
          {"role": "system", "content": systemPrompt},
          {"role": "user", "content": prompt},
      ],
      temperature=0.2
  )
  return chat_completion.choices[0].message['content']  # type: ignore
