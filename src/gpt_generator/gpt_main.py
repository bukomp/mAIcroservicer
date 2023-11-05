from gpt_generator.helpers.file_collection import a_create_file_collection

from gpt_generator.modules.file_description_architector import gpt_file_description_architector
from gpt_generator.modules.structure_architector import gpt_project_structure_architector

from models.file_interface import FileCollection, File
from models.gpt_responses_interface import ArchitectorResponse

import logging
import asyncio


logging.basicConfig(level=logging.ERROR)


async def a_gpt_main(prompt: str) -> FileCollection:
  try:
    # Generate initial project and response
    project, response = await gpt_project_structure_architector(prompt)

    # Assert project is of the correct type
    assert isinstance(project, ArchitectorResponse)

    project, response = await gpt_file_description_architector(project, prompt)

    # Assert project is of the correct type
    assert isinstance(project, ArchitectorResponse)

    # Assert response is of the correct type
    assert isinstance(response, str)

    return await a_create_file_collection(
        project,
        response
    )

  except Exception as e:
    # Log any other exceptions
    logging.error(f"An error occurred: {e}")
    return FileCollection("")


def gpt_main(prompt: str) -> FileCollection:
  return asyncio.run(a_gpt_main(prompt))
