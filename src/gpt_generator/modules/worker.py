
from gpt_generator.helpers.gpt_requests import create_chat_completion
from models.gpt_responses_interface import ArchitectorResponse


def gpt_worker(project: ArchitectorResponse, file_name: str, file_details: str) -> str:
  try:
    prompt = f"""
    File Name: {file_name} \n
    File Details: {file_details}
    """

    content: str = create_chat_completion(
        "worker", 0.1, [], [project.structure, prompt])

    return content
  except Exception as e:
    print(f"An error occurred: {e}{__file__}")
    return str(e)
