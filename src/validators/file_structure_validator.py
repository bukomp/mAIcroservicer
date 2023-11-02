import re


def requirements_txt_validator(contents) -> str:
  """
  Validates the contents of a requirements.txt file.

  :param contents: The contents of the requirements.txt file as a string.
  :type contents: str
  :return: The validated contents of the requirements.txt file.
  :rtype: str
  """

  forbidden_packages = [
      "unittest"
  ]

  lines = contents.strip().split('\n')
  valid_lines = []
  for _i, line in enumerate(lines):
    # Ignore comments
    if line.startswith('#'):
      continue

    # Split package and version specifier
    parts = line.split('==')

    # Validate package name
    package_name = parts[0].strip()
    if not re.match('^[a-zA-Z0-9_-]+$', package_name):
      continue

    # Validate version specifier, if present
    if len(parts) > 1:
      version = parts[1].strip()
      if not re.match('^[0-9.]+$', version):
        continue

    # Remove forbidden packages
    if package_name not in forbidden_packages:
      valid_lines.append(line)

  contents = "\n".join(valid_lines)

  return contents
