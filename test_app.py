import os
import unittest
from unittest.mock import patch
from app import app

class RoutesTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_catalog_without_key(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(self.client.get('/').status_code, 200)
            response = self.client.get('/?type=restaurant')
            self.assertIn(b'configure GOOGLE_MAPS_API_KEY', response.data)
    def test_invalid_type_redirects(self):
        self.assertEqual(self.client.get('/?type=invalid').status_code, 302)
    def test_configured_map(self):
        with patch.dict(os.environ, {'GOOGLE_MAPS_API_KEY': 'test-key'}):
            self.assertIn(b'key=test-key', self.client.get('/?type=restaurant').data)
    def test_unknown_route_redirects(self):
        self.assertEqual(self.client.get('/missing').status_code, 302)

if __name__ == '__main__':
    unittest.main()
