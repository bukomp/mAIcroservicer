# Function to extract files from the content
import re


def extract_files(content: str) -> list[dict[str, str]]:
  # Regular expression pattern to match file name and content
  pattern = r"---(.*?)---.*?`.*?\n(.*?)`"
  matches = re.findall(pattern, content, re.DOTALL)

  # List to store the extracted files
  files = []
  for match in matches:
    file_name = match[0].strip()
    file_content = match[1].strip()
    files.append({"name": file_name, "content": file_content})

  return files
