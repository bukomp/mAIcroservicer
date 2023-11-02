import json
import os

# Define the base directory where the prompts are stored
base_dir = 'src/prompts'

# Initialize an empty dictionary to store the data
data = {}

# Function to create a multilevel object based on folder structure
def create_object(path):
    obj = {}
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            # Ignore .pyc and __pycache__ files
            if name.endswith('.pyc') or name == '__pycache__' or name == 'README.md':
                continue
            # Extract the version from the filename
            version = name.split('_v')[-1].replace('.txt', '')
            # Create a dictionary entry for each file
            obj[version] = os.path.join(path, name)
        else:
            if name.endswith('.pyc') or name == '__pycache__' or name == 'README.md':
                continue
            obj[name] = create_object(os.path.join(path, name))
    return obj

# Create the multilevel object
data = create_object(base_dir)

# Convert the dictionary to a JSON string
json_data = json.dumps(data, indent=4)

# Print the JSON data
print(json_data)