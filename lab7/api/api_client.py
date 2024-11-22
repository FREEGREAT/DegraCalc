"""
api/api_client.py

Цей модуль реалізує клас APIClient, який відповідає за взаємодію з API через HTTP-запити.

Імпортовані модулі:
    import requests:
        Використовується для виконання HTTP-запитів.

    from core.error_handler import APIError, ErrorHandler:
        Забезпечує обробку помилок, що виникають під час запитів до API.

Класи:
    APIClient:
        Реалізує логіку роботи з API через базовий URL.
    
Методи:
    __init__(self, base_url):
        Ініціалізує клієнт з базовим URL для API.

    get_data(self, endpoint):
        Виконує GET-запит до API, обробляє відповіді та помилки.
"""
import requests
from core.error_handler import APIError, ErrorHandler

class APIClient:
    """
    Клас для взаємодії з API через HTTP-запити.
    """

    def __init__(self, base_url):
        """
        Ініціалізує APIClient з базовим URL.

        Параметри:
            base_url (str): Базовий URL API.
        """
        self.base_url = base_url

    def get_data(self, endpoint):
        """
        Виконує GET-запит до вказаного ендпоінту API.

        Параметри:
            endpoint (str): Шлях до ресурсу API відносно базового URL.

        Повертає:
            dict | None: JSON-відповідь від API у вигляді словника або None у разі помилки.

        Викликає:
            APIError: Якщо запит до API завершився помилкою.
        """
        try:
            response = requests.get(f"{self.base_url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            ErrorHandler.handle_error(APIError(f"API request failed: {e}"))
            return None
