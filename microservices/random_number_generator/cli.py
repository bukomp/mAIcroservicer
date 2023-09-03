import random
import sys


def generate_random_numbers(minimum, maximum, count):
    if not all((minimum, maximum, count)):
        print("Error: Missing arguments")
        return []

    if minimum >= maximum or count <= 0:
        print("Error: Invalid arguments")
        return []

    return [random.randint(minimum, maximum) for _ in range(count)]


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: Missing arguments. Usage: python cli.py <minimum> <maximum> <count>")
        sys.exit(1)

    minimum = int(sys.argv[1])
    maximum = int(sys.argv[2])
    count = int(sys.argv[3])

    numbers = generate_random_numbers(minimum, maximum, count)
    print(numbers)