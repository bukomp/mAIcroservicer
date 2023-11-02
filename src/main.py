import os

from helpers.read_user_input import read_user_input
from helpers.config import config
from gpt_generator.gpt_main import gpt_main
from helpers.file_writer import write_files_from_collection
from models.file_interface import FileCollection


def main() -> None:
  try:
    if not os.path.exists(config.base_dir):
      os.makedirs(config.base_dir)

    prompt = read_user_input()

    list_of_files_to_write: FileCollection = gpt_main(prompt)

    write_files_from_collection(list_of_files_to_write)

  except Exception as e:
    print(f"An error occurred: {e} in {__name__}")


if __name__ == "__main__":
  main()
