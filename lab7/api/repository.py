"""
api/repository.py

Цей модуль реалізує клас DataRepository, який відповідає за доступ 
до даних через API та маніпуляції з отриманою інформацією.

Імпортовані модулі:
    from api.api_client import APIClient:
        Використовується для виконання запитів до API.

    from core.error_handler import ErrorHandler, APIError:
        Забезпечує обробку помилок, що виникають під час роботи з API.

Класи:
    DataRepository:
        Відповідає за доступ до даних через API та їх обробку.

Методи:
    __init__(self, api_client):
        Ініціалізує екземпляр класу з переданим клієнтом API.

    fetch_data(self, endpoint):
        Отримує дані з вказаного API-ендпоінту. У разі невдачі викликає обробник помилок.

    find_user_by_phone(self, phone, data):
        Знаходить користувача за номером телефону в отриманих даних.
"""
from core.error_handler import ErrorHandler, APIError

class DataRepository:
    """
    Клас для роботи з даними, отриманими через API.
    """

    def __init__(self, api_client):
        """
        Ініціалізує DataRepository з клієнтом API.

        Параметри:
            api_client (APIClient): Екземпляр клієнта для виконання запитів до API.
        """
        self.api_client = api_client

    def fetch_data(self, endpoint):
        """
        Отримує дані з вказаного API-ендпоінту.

        Параметри:
            endpoint (str): Шлях до ресурсу API.

        Повертає:
            dict: Дані, отримані з API.

        Викликає:
            APIError: Якщо дані не вдалося отримати.
        """
        data = self.api_client.get_data(endpoint)
        if data is None:
            ErrorHandler.handle_error(APIError(f"Failed to fetch data from endpoint: /{endpoint}"))
        return data

    def find_user_by_phone(self, phone, data):
        """
        Шукає користувача за номером телефону.

        Параметри:
            phone (str): Номер телефону для пошуку.
            data (list[dict]): Список даних користувачів.

        Повертає:
            dict | None: Дані користувача, якщо знайдено, або None, якщо користувач не знайдений.
        """
        for user in data:
            if user.get("phone") == phone:
                return user
        return None
