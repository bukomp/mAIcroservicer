import unittest
from flask_testing import TestCase
from web_server import app


class TestWebServer(TestCase):
  def create_app(self):
    app.config['TESTING'] = True
    return app

  def test_home(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b"Welcome to the home page!")

  def test_test(self):
    response = self.client.get('/test')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, b"Test route is working!")

  def test_range(self):
    response = self.client.get('/range?min=1&max=100&count=5')
    self.assertEqual(response.status_code, 200)
    numbers = response.json['numbers']
    self.assertEqual(len(numbers), 5)
    for number in numbers:
      self.assertTrue(1 <= number <= 100)


if __name__ == "__main__":
  unittest.main()
