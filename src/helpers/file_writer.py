import os
import traceback


from helpers.config import config
from helpers.microservice_counter import microservice_count
from models.file_interface import FileCollection, File
from models.gpt_responses_interface import ArchitectorResponse


def _write_microservice_files(microservice_root_dir: str, file_contents: list[File]) -> None:
  try:
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
  except Exception as e:
    print(f"An error occurred in {__name__}: ")
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print("Traceback:")
    traceback.print_exc()


def write_files_from_collection(list_of_files: FileCollection) -> None:
  try:
    microservice_root_dir = os.path.join(
        config.base_dir, f"-{microservice_count()}--{list_of_files.project_root}")

    microservice_raw_files_root_dir = os.path.join(
        microservice_root_dir, "raw_responses")

    _write_microservice_files(microservice_root_dir,
                              list_of_files.collections["formatted_responses"])

    _write_microservice_files(microservice_raw_files_root_dir,
                              list_of_files.collections["raw_responses"])

  except Exception as e:
    print(f"An error occurred in {__name__}: ")
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {e}")
    print("Traceback:")
    traceback.print_exc()
