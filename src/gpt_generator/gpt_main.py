from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Union

from gpt_generator.modules.architector import gpt_architector
from gpt_generator.modules.worker import gpt_worker
from helpers.architecture_extractor import structure_2_dict
from helpers.code_extractor import extract_code
from models.file_interface import File_Collection, File_to_write
from models.gpt_responses_interface import ArchitectorResponse

import logging

logging.basicConfig(level=logging.ERROR)


def gpt_main(prompt: str) -> File_Collection:
  try:
    # Generate initial project and response
    project, response = gpt_architector(prompt)

    # Assert project is of the correct type
    assert isinstance(project, ArchitectorResponse)

    # Initialize File_Collection
    file_collection = File_Collection(project.name)

    # Add initial response to collection
    file_collection.collections["raw_responses"].append(
        File_to_write("architector.txt", str(response))
    )

    structure_dictionary: dict[str, str] = structure_2_dict(project.structure)

    # Create a ThreadPool to execute gpt_worker on each file
    with ThreadPoolExecutor() as executor:
      future_to_file = {executor.submit(
          gpt_worker, project, file.file_name, file.description): file for file in project.files}

      for future in as_completed(future_to_file):
        try:
          # Obtain the completed future's corresponding file
          file = future_to_file[future]

          # Get the result from the future
          result = future.result()

          # Add results to the collection
          file_collection.collections["raw_responses"].append(
              File_to_write(f"raw_{file.file_name}.txt", result, "")
          )
          file_collection.collections["formatted_responses"].append(
              File_to_write(file.file_name, extract_code(result),
                            structure_dictionary[file.file_name])
          )
        except Exception as e:
          # Log any exceptions that occur within the thread
          logging.error(f"An error occurred in thread: {e}")

    return file_collection

  except Exception as e:
    # Log any other exceptions
    logging.error(f"An error occurred: {e}")
    return File_Collection("")
