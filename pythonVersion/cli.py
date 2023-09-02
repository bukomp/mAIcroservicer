import sys
import random


def generate_random_numbers(min, max, count):
    numbers = [random.randint(min, max) for _ in range(count)]
    return ','.join(map(str, numbers))


def main():
    args = sys.argv[1:]
    if len(args) < 3:
        print('Please provide min, max and count as arguments.')
        sys.exit(1)
    min, max, count = map(int, args)
    print(generate_random_numbers(min, max, count))


if __name__ == "__main__":
    main()
