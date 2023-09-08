import json
import os
import re
import openai
openai.organization = os.environ.get('GPT_ORG')
openai.api_key = os.environ.get('GPT_KEY')
openai.Model.list()

systemPrompt_under_constructions = """
Generate content that does not include any guides, tutorials, instructions, specific endpoint descriptions, or mentions of software setups and configurations.
"""

systemPrompt_codeSnippetExample = """
Here's an example of how to format code snippets:
---requirements.txt---
```
Flask
Flask-Testing
```
"""

systemPrompt_requiredFiles = """
The Dockerfile describes how to build a Docker image for the project. It installs the dependencies and starts the web server.

Web Server file (you must name this file accordingly) contains the web server application. It has several endpoints, including a home route, a test route, and a range route. The range route uses the CLI application to generate random numbers. API must be reachable from outside of the container.
Set Web Server to work on port 3000 and set it work on 0.0.0.0 ip address.

CLI application file (you must name this file accordingly) contains the CLI application. If the arguments are not provided, it prints an error message and exits.

The requirements.txt file lists the Python packages required by the project, include to this file packages that were used in this project.
"""

# add possible option
# on/off options
systemPrompt = """
  - Follow exactly this template when creating files: 
    ---{name of file}---
    ```{content}```
  - Do not give trivia. 
  - Give only pure code.
  - Do not decorate text in any other way.
  - Code must be runnable and must not contain errors. 
  - Python code must follow pep8.
  - Return answer to a prompt in a string format.
  

  Follow this instructions exactly.
"""

prompt = """
give me a Python project that includes a command-line interface (CLI) application and a web server. The CLI application generates a specified count of random numbers within a given range, while the web server provides several endpoints, including one that uses the CLI application.
Cli takes three arguments: the minimum and maximum values of the range, and the count of numbers to generate. 
"""

prompt2 = """
give me a Python project that includes a command-line interface (CLI) application and a web server. The CLI application context is 'while give me a joke of the day service'
"""


def extract_files(content):
  pattern = r"---(.*?)---.*?`.*?\n(.*?)`"
  matches = re.findall(pattern, content, re.DOTALL)

  files = []
  for match in matches:
    # Remove markdown code block delimiters from the content

    file_name = match[0].strip()
    file_content = match[1].strip()

    files.append({"name": file_name, "content": file_content})

  return files


# Create a chat completion with the user message "Hello, world!"
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": systemPrompt},
        {"role": "system", "content": systemPrompt_codeSnippetExample},
        {"role": "system", "content": systemPrompt_requiredFiles},
        {"role": "system", "content": systemPrompt_under_constructions},
        {"role": "user", "content": prompt},
    ],
    temperature=0.2
)


response = chat_completion.choices[0].message['content']  # type: ignore
print(response)
# This should be extracted from the context

base_dir = 'microservices'
if not os.path.exists(base_dir):
  os.makedirs(base_dir)
microservice_count = len([name for name in os.listdir(
    base_dir) if os.path.isdir(os.path.join(base_dir, name))])
microservice_name = 'microservice' + str(microservice_count)
microservice_dir = os.path.join(base_dir, microservice_name)

os.makedirs(microservice_dir, exist_ok=True)

file_contents = extract_files(response)


for file_content in file_contents:

  file_name = file_content['name']
  content = file_content['content']
  file_path = os.path.join(os.getcwd(), microservice_dir, file_name.strip())

  # Check if the directory exists, if not create it
  os.makedirs(os.path.dirname(file_path), exist_ok=True)
  try:
    with open(file_path, 'x') as file:
      file.write(content)
  except OSError as e:
    print(e)
