def format_version(version: int | str | float) -> str:
  """
  Format the given version number by joining its parts with an underscore and removing any dots.

  Parameters:
      version (int | str | float): The version number to be formatted.

  Returns:
      str: The formatted version number.
  """
  return "_".join(str(version).replace(".", ""))
