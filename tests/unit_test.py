# tests/test_app.py
import unittest
from api.api_client import APIClient
from api.repository import DataRepository

class TestAPI(unittest.TestCase):
    def test_get_data(self):
        api_client = APIClient("https://jsonplaceholder.typicode.com")
        repository = DataRepository(api_client)
        data = repository.fetch_data("posts")
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
