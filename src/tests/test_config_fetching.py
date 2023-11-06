import pytest
from helpers.config import env, secrets, config
from models.config.config_interface import Config
from models.config.Secrets_interface import Secrets


@pytest.fixture
def setup():
  return {
      "env": env,
      "secrets": secrets,
      "config": config
  }


def test_env(setup):
  assert isinstance(setup["env"], dict)
  assert "GPT_KEY" in setup["env"]
  assert "GPT_ORG" in setup["env"]
  assert "PATH_TO_CONFIG" in setup["env"]


def test_secrets(setup):
  assert isinstance(setup["secrets"], Secrets)
  assert setup["secrets"].GPT_ORG == setup["env"]["GPT_ORG"]
  assert setup["secrets"].GPT_KEY == setup["env"]["GPT_KEY"]
  assert setup["secrets"].PATH_TO_CONFIG == setup["env"]["PATH_TO_CONFIG"]


def test_config(setup):
  assert isinstance(setup["config"], Config)
  assert setup["config"].secrets == setup["secrets"]
