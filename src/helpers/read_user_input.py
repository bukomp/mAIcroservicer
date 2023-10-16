import argparse


def read_user_input() -> str:
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--prompt', help='User input prompt')
  args = parser.parse_args()
  if args.prompt:
    return args.prompt
  else:
    prompt = "Please enter your input: "
    return input(prompt)
