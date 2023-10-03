import os
from prompts.system import *
from helpers.code_extractor import extract_files
from helpers.microservice_counter import microservice_count
from helpers.config import config
from gpt_generator.gpt_main import gpt_main
from helpers.file_writer import write_microservice_files


prompt = """
give me a Python project that includes a command-line interface (CLI) application and a web server. The CLI application generates a specified count of random numbers within a given range, while the web server provides several endpoints, including one that uses the CLI application.
Cli takes three arguments: the minimum and maximum values of the range, and the count of numbers to generate. 
"""

prompt2 = """
give me a Python project that includes a command-line interface (CLI) application and a web server. The CLI application context is 'while give me a joke of the day service'
"""


def main() -> None:

  # Extract the response content
  response = gpt_main(prompt)  # type: ignore

  # Define the base directory for microservices
  if not os.path.exists(config["BASE_DIR"]):
    os.makedirs(config["BASE_DIR"])

  # Define the new microservice name and directory
  microservice_name = 'microservice' + str(microservice_count())
  microservice_dir = os.path.join(config["BASE_DIR"], microservice_name)

  # Extract the files from the response
  file_contents = extract_files(response)

  # Write files
  write_microservice_files(microservice_dir, file_contents)


if __name__ == "__main__":
  main()
