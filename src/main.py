import os

from helpers.read_user_input import read_user_input
from helpers.code_extractor import extract_files
from helpers.microservice_counter import microservice_count
from helpers.config import config
from gpt_generator.gpt_main import gpt_main
from helpers.file_writer import write_microservice_files
from models.file_interface import File_Collection


def main() -> None:
  try:
    if not os.path.exists(config["BASE_DIR"]):
      os.makedirs(config["BASE_DIR"])

    prompt = read_user_input()

    list_of_files: File_Collection = gpt_main(prompt)

    write_files(list_of_files)

  except Exception as e:
    print(f"An error occurred: {e}{__file__}")


def write_files(list_of_files: File_Collection):

  microservice_root_dir = os.path.join(
      config["BASE_DIR"], f"-{microservice_count()}--{list_of_files.project_root}")

  microservice_raw_files_root_dir = os.path.join(
      microservice_root_dir, "raw_responses")

  write_microservice_files(microservice_root_dir,
                           list_of_files.collections["formatted_responses"])

  write_microservice_files(microservice_raw_files_root_dir,
                           list_of_files.collections["raw_responses"])


if __name__ == "__main__":
  main()
