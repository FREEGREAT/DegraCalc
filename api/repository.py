# api/repository.py
from api.api_client import APIClient
from core.error_handler import ErrorHandler, APIError

class DataRepository:
    def __init__(self, api_client):
        self.api_client = api_client

    def fetch_data(self, endpoint):
        data = self.api_client.get_data(endpoint)
        if data is None:
            ErrorHandler.handle_error(APIError(f"Failed to fetch data from endpoint: /{endpoint}"))
        return data

    def find_user_by_phone(self, phone, data):
        # Порівнюємо номер користувача з введеним телефоном
        for user in data:
            if user.get("phone") == phone:
                return user
        return None
