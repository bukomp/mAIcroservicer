# Count the existing microservices
import os
from helpers.config import config


def microservice_count() -> int:
  return len([name for name in os.listdir(config.base_dir) if os.path.isdir(os.path.join(config.base_dir, name))])
