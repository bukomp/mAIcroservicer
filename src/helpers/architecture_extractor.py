# Function to extract files from the content
import re

from models.gpt_responses_interface import ArchitectorResponse, FileExplanation


def extract_file_description(content: str) -> list[FileExplanation]:
  pattern = r"---(.*?)---\n([\s\S]*?)(?=---|$)"
  matches = re.findall(pattern, content)
  file_list: list[FileExplanation] = []
  for match in matches:
    if match[0].strip() != "structure":
      file = FileExplanation(match[0].strip(), match[1].strip())
      file_list.append(file)
  return file_list


def extract_structure(content: str) -> str:
  pattern = r"---structure---(.*?)---"
  matches = re.findall(pattern, content, re.DOTALL)

  return matches[0].strip()


def project_extractor(content: str) -> ArchitectorResponse:
  project_name_match = re.search(r"---structure---\n(.*?)/", content)
  project_name: str = project_name_match.group(
      1) if project_name_match else "project"
  structure: str = extract_structure(content)
  files = extract_file_description(content)
  return ArchitectorResponse(project_name, structure, files)


# Re-run the function to exclude file names in the paths.
def structure_2_dict(file_structure: str) -> dict:
  lines = file_structure.strip().split("\n")
  stack = []
  file_path_dict = {}

  for line in lines:
    # Ignore lines with "..."
    if "..." in line:
      continue

    # Find the position of the first '─' to determine the depth
    depth = line.find('─') // 4
    name = line.split('─')[-1].strip()  # Get the name of the directory or file

    # Remove optional parameters from the file or folder name
    name = name.split(' ')[0]

    # Adjust stack to the current depth
    stack = stack[:depth]

    # Create full path
    full_path = '/'.join(stack)

    # If the name does not end with a '/', it is a file. Add it to the dictionary.
    if not name.endswith('/'):
      file_path_dict[name] = full_path if full_path else ''

    # Add the name to the stack for creating future full paths, remove trailing '/'
    stack.append(name.replace('/', '').strip())

  return file_path_dict
