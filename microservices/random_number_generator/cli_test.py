import unittest
import cli


class CLITestCase(unittest.TestCase):

    def test_generate_random_numbers(self):
        # Test case 1: Valid arguments
        minimum = 1
        maximum = 10
        count = 5
        numbers = cli.generate_random_numbers(minimum, maximum, count)
        self.assertEqual(len(numbers), count)
        self.assertTrue(all(minimum <= number <= maximum for number in numbers))

        # Test case 2: Invalid arguments
        minimum = 10
        maximum = 1
        count = 0
        numbers = cli.generate_random_numbers(minimum, maximum, count)
        self.assertEqual(numbers, [])

        # Test case 3: Missing arguments
        numbers = cli.generate_random_numbers(None, None, None)
        self.assertEqual(numbers, [])


if __name__ == '__main__':
    unittest.main()