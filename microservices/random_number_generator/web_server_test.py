import unittest
from flask_testing import TestCase
from web_server import app


class WebServerTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Welcome to the CLI and Web Server project!')

    def test_test_route(self):
        response = self.client.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'This is a test route.')

    def test_generate_random_numbers_route(self):
        response = self.client.get('/range')
        self.assertEqual(response.status_code, 200)
        numbers = response.json
        self.assertGreater(len(numbers), 0)
        self.assertTrue(all(isinstance(number, int) for number in numbers))

        response = self.client.get('/range?minimum=10&maximum=1&count=0')
        self.assertEqual(response.status_code, 200)
        numbers = response.json
        self.assertEqual(numbers, [])

        response = self.client.get('/range?count=5')
        self.assertEqual(response.status_code, 200)
        numbers = response.json
        self.assertEqual(len(numbers), 5)


if __name__ == '__main__':
    unittest.main()