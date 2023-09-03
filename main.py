import os
import openai
openai.organization = ""
openai.api_key = ""
openai.Model.list()

systemPrompt = """
  file must start with ---{name of the file} and end with ---.
  do not decorate text in any other way.
  If answer is not complete you must ask if I want to continue at the end.
  Code must be runnable and must not contain errors. 
  Python code must follow pep8.
  Follow this instructions exactly.
"""

prompt = """
give me a Python project that includes a command-line interface (CLI) application and a web server. The CLI application generates a specified count of random numbers within a given range, while the web server provides several endpoints, including one that uses the CLI application.
The cli.py file contains the CLI application. It takes three arguments: the minimum and maximum values of the range, and the count of numbers to generate. If the arguments are not provided, it prints an error message and exits.
The cli_test.py file contains unit tests for the CLI application. It tests the generation of random numbers and the handling of insufficient arguments.
The web_server.py file contains the web server application. It has several endpoints, including a home route, a test route, and a range route. The range route uses the CLI application to generate random numbers. API must be reachable from outside of the container
The web_server_test.py file contains unit tests for the web server. It tests all the routes, including the handling of missing or out-of-range parameters in the range route.
The Dockerfile describes how to build a Docker image for the project. It installs the dependencies, runs the unit tests, compiles the CLI application to a binary using PyInstaller, adds the binary to the PATH, and starts the web server.
The requirements.txt file lists the Python packages required by the project, which are Flask and Flask_Testing.
return answer to a prompt in a string format.
"""

# Create a chat completion with the user message "Hello, world!"
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "user", "content": prompt},
    ]
)

print(chat_completion)  # type: ignore
