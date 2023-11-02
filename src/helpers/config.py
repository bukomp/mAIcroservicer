from dotenv import dotenv_values
import json

import os
import signal

from models.config.Secrets_interface import Secrets
from models.config.config_interface import Config

env = dict(dotenv_values(".env"))
if "GPT_KEY" not in env or "GPT_ORG" not in env:
  raise KeyError("GPT_KEY and/or GPT_ORG not found in .env.secret")
else:
  with open('config.json', 'r', encoding='utf-8') as f:
    config: Config = Config(
        dict(json.loads(f.read())), Secrets(env["GPT_ORG"], env["GPT_KEY"]))
