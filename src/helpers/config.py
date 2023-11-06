import os
from dotenv import dotenv_values
import json

from models.config.Secrets_interface import Secrets
from models.config.config_interface import Config


env = dict(dotenv_values(".env"))
if "GPT_KEY" not in env or "GPT_ORG" not in env:
  raise KeyError("GPT_KEY and/or GPT_ORG not found in .env.secret")
else:
  secrets: Secrets = Secrets(
      env["GPT_ORG"], env["GPT_KEY"], env["PATH_TO_CONFIG"])
  with open(os.path.join(secrets.PATH_TO_CONFIG, "config.json"), 'r', encoding='utf-8') as f:
    config: Config = Config(
        dict(json.loads(f.read())),
        secrets
    )
