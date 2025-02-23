import unittest
from src.app import app

class FlaskAppTestCase(unittest.TestCase):

    # Set up a test client for the Flask app
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test the '/' route to ensure it returns a 200 status code
    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Test the response content to ensure "Hello From Python!" is in the HTML output
    def test_index_content(self):
        response = self.app.get('/')
        self.assertIn(b"Hello From Python!", response.data)  # Make sure it contains "Hello From Python!"

if __name__ == "__main__":
    unittest.main()
