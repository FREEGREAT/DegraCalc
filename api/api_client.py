# api/api_client.py
import requests
from core.error_handler import APIError, ErrorHandler

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_data(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            ErrorHandler.handle_error(APIError(f"API request failed: {e}"))
            return None
