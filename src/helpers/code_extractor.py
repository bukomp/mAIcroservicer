# Function to extract files from the content
import re


def extract_code(raw_string: str) -> str:

  return re.sub(r'^```.*?\n|```$', '',
                raw_string, flags=re.MULTILINE)
