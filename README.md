# Microservice Generator

This project is a Python-based microservice generator. It uses OpenAI's GPT model to generate Python microservices based on given prompts. The generated microservices include a web server for handling API requests and a business logic component, which could be a command-line interface (CLI) application or other component.

## Table of Contents

1. [How it Works](#how-it-works)
2. [How to Run](#how-to-run)
3. [Dependencies](#dependencies)
4. [Configuration](#configuration)
5. [Note](#note)

## How it Works

The main function of the project is located in `main.py`. Here's a step-by-step guide on how it works:

1. It takes a prompt as input, which describes the Python project to be generated.
2. The prompt is passed to the `gpt_main` function in `gpt_generator/gpt_main.py`, which uses OpenAI's GPT model specified in `.env.secret` to generate the Python project.
3. The generated project is returned as a string, which is then passed to the `extract_files` function in `helpers/code_extractor.py`. This function extracts the individual files from the generated project.
4. The extracted files are then written to a new microservice directory by the `write_microservice_files` function in `helpers/file_writer.py`.
5. The name of the new microservice is determined by the `microservice_count` function in `helpers/microservice_counter.py`, which counts the existing microservices.

## How to Run

To run the project, follow these steps:

1. Navigate to the project directory in your terminal.
2. Depending on your operating system, run one of the following commands:
   - For Unix-based systems (like Linux or MacOS), run the command `./scripts/start_app.sh`.
   - For Windows systems, run the command `./scripts/start_app.ps1`.

## Dependencies

The project requires the following dependencies:

- Python 3.6 or higher
- OpenAI-API key
- The `dotenv`, `openai` Python packages

These dependencies can be installed by running the command `pip install -r requirements.txt` in your terminal.

## Configuration

The project uses environment variables for configuration. These are loaded from `.env.shared` and `.env.secret` files by the `config` dictionary in `helpers/config.py`. The `.env.shared` file contains shared development variables, while the `.env.secret` file contains sensitive variables.

Please ensure that these files exist in your project directory and that they contain the necessary variables. For example, you will need to provide your OpenAI organization and API key.

## Note

The generated Python projects are saved in a directory specified by the `BASE_DIR` environment variable. If this directory does not exist, it will be created.

