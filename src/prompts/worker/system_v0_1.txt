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
