import os
from helpers.read_user_input import read_user_input
from helpers.code_extractor import extract_files
from helpers.microservice_counter import microservice_count
from helpers.config import config
from gpt_generator.gpt_main import gpt_main
from helpers.file_writer import write_microservice_files


def main() -> None:

  # Define the base directory for microservices
  if not os.path.exists(config["BASE_DIR"]):
    os.makedirs(config["BASE_DIR"])

  # Define the new microservice name and directory
  microservice_name = 'microservice' + str(microservice_count())
  microservice_dir = os.path.join(config["BASE_DIR"], microservice_name)

  # Check if the directory exists, if not create it
  os.makedirs(microservice_dir, exist_ok=True)

  prompt = read_user_input()

  # Create and write to user_input.txt and response.txt in the microservice directory
  with open(os.path.join(microservice_dir, 'user_input.txt'), 'w') as user_input_file:
    user_input_file.write(prompt)

  # Extract the response content
  response = gpt_main(prompt)  # type: ignore

  with open(os.path.join(microservice_dir, 'response.txt'), 'w') as response_file:
    response_file.write(response)

  # Extract the files from the response
  file_contents = extract_files(response)

  # Write files
  write_microservice_files(microservice_dir, file_contents)


if __name__ == "__main__":
  main()
