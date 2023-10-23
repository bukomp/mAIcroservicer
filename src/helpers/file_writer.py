import os
import re

from helpers.config import config
from models.file_interface import File_to_write
from models.gpt_responses_interface import ArchitectorResponse


def write_microservice_files(microservice_root_dir: str, file_contents: list[File_to_write]) -> None:
  # Write the extracted files to the new microservice directory
  for file in file_contents:
    file_name = file.name
    content = file.content
    path = file.path

    # Create the directory if it doesn't exist
    os.makedirs(os.path.join(
        os.getcwd(), microservice_root_dir, path), exist_ok=True)

    file_path = os.path.join(
        os.getcwd(), microservice_root_dir, path, file_name.strip())

    try:
      with open(file_path, 'x', encoding='utf-8') as file:
        file.write(content)
    except OSError as e:
      print(e)
