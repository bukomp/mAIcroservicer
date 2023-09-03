import unittest
import subprocess
import json


class TestCli(unittest.TestCase):
  def test_generate_numbers(self):
    result = subprocess.run(['python', 'cli.py', '--min', '1',
                            '--max', '100', '--count', '5'], stdout=subprocess.PIPE)
    numbers = json.loads(result.stdout)
    self.assertEqual(len(numbers), 5)
    for number in numbers:
      self.assertTrue(1 <= number <= 100)

  def test_missing_arguments(self):
    result = subprocess.run(['python', 'cli.py'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
  unittest.main()
