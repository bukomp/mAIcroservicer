import os


def write_microservice_files(microservice_dir: str, file_contents: list[dict[str, str]]) -> None:
  # Write the extracted files to the new microservice directory
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
