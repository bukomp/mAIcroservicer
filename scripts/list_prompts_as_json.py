import json
import os

# Define the base directory where the prompts are stored
base_dir = 'src/prompts'

# Initialize an empty dictionary to store the data
data = {}

# Function to create a multilevel object based on folder structure


def create_object(path: str) -> dict:
  obj: dict = {}
  for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
      # Ignore .pyc and __pycache__ files
      if name.endswith('.pyc') or name == '__pycache__' or name == 'README.md':
        continue
      # Extract the name and version from the filename
      file_name: str
      version: str
      file_name, version = name.split('_v')
      version = version.replace('.txt', '')
      # Create a dictionary entry for each file, grouped by name
      if file_name not in obj:
        obj[file_name] = {}
      obj[file_name][version] = os.path.join(path, name).replace('\\', '/')
    else:
      if name.endswith('.pyc') or name == '__pycache__' or name == 'README.md':
        continue
      obj[name] = create_object(os.path.join(path, name))
  return obj


# Create the multilevel object
data: dict = create_object(base_dir)

# Convert the dictionary to a JSON string
json_data: str = json.dumps(data, indent=4)

# Write the JSON data to the prompt_dictionary.json file
with open('prompt_dictionary.json', 'w') as json_file:
  json_file.write(json_data)
