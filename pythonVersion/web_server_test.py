import unittest
from flask_testing import TestCase
from web_server import app


class TestFlaskRoutes(TestCase):
  def create_app(self):
    return app

  def test_home_route(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data.decode(), 'Hello, World!')

  def test_test_route(self):
    response = self.client.get('/api/test')
    self.assertEqual(response.status_code, 200)
    self.assertIn('Connection Test', response.json['message'])

  def test_range_route(self):
    response = self.client.get('/api/range?min=1&max=10&number=5')
    self.assertEqual(response.status_code, 200)

  def test_range_route_missing_parameters(self):
    response = self.client.get('/api/range?min=1&max=10')
    self.assertEqual(response.status_code, 400)
    self.assertEqual(
        response.json['error'], 'Please provide min, max and number parameters')

  def test_range_route_out_of_range(self):
    response = self.client.get('/api/range?min=1&max=10&number=15')
    self.assertEqual(response.status_code, 400)
    self.assertEqual(response.json['error'],
                     'Number is out of the provided range')


if __name__ == '__main__':
  unittest.main()
