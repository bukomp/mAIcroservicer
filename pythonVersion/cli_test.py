import unittest
import subprocess


class TestCLI(unittest.TestCase):
  def test_generate_random_numbers(self):
    result = subprocess.run(
        ['python', 'cli.py', '1', '10', '5'], stdout=subprocess.PIPE)
    numbers = list(map(int, result.stdout.decode('utf-8').split(',')))
    self.assertEqual(len(numbers), 5)
    for number in numbers:
      self.assertTrue(1 <= number <= 10)

  def test_insufficient_arguments(self):
    result = subprocess.run(
        ['python', 'cli.py', '1', '10'], stdout=subprocess.PIPE)
    self.assertEqual(result.stdout.decode('utf-8'),
                     'Please provide min, max and count as arguments.\n')


if __name__ == "__main__":
  unittest.main()
