"""
Модуль Тестування: test_app
---------------------------
Цей модуль реалізує тестування компонентів програми з використанням бібліотеки `unittest`.
Зокрема, перевіряється інтеграція між `APIClient` і `DataRepository`
для отримання даних із зовнішнього API.
Імпортовані модулі:
-------------------
- `unittest`:
    Стандартна бібліотека Python для написання тестів.
- `api.api_client.APIClient`:
    Клас для взаємодії з API.
- `api.repository.DataRepository`:
    Клас для отримання та роботи з даними через API.

Класи:
------
 """
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from api.api_client import APIClient
from api.repository import DataRepository

class TestAPI(unittest.TestCase):
    """Тестовий клас для перевірки роботи APIClient і DataRepository.

    Методи:
    -------
    - test_get_data():
        Перевіряє, чи метод `fetch_data` класу `DataRepository` повертає список 
        даних для заданого ресурсу (наприклад, "posts").
    """
    def test_get_data(self):
        """Тестує метод `fetch_data`:
        - Ініціалізує `APIClient` із базовим URL.
        - Створює екземпляр `DataRepository` із клієнтом API.
        - Викликає `fetch_data("posts")` для отримання даних.
        - Перевіряє, чи результат є списком (`list`).
        """
        api_client = APIClient("https://jsonplaceholder.typicode.com")
        repository = DataRepository(api_client)
        data = repository.fetch_data("posts")
        self.assertIsInstance(data, list)

if __name__ == "__main__":
    unittest.main()
