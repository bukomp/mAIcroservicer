import argparse
import random
import json


def generate_numbers(min_value, max_value, count):
  return [random.randint(min_value, max_value) for _ in range(count)]


def main():
  parser = argparse.ArgumentParser(description='Generate random numbers.')
  parser.add_argument('--min', type=int, required=True, help='Minimum value')
  parser.add_argument('--max', type=int, required=True, help='Maximum value')
  parser.add_argument('--count', type=int, required=True,
                      help='Count of numbers to generate')

  args = parser.parse_args()

  numbers = generate_numbers(args.min, args.max, args.count)
  print(json.dumps(numbers))


if __name__ == "__main__":
  main()
