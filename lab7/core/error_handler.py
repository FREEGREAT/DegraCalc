"""
core/error_handler.py

Цей модуль забезпечує визначення користувацьких виключень 
та інструментів для обробки помилок у додатку.

Класи:
    APIError(Exception):
        Представляє помилки, які виникають під час запитів до API.

    UserInputError(Exception):
        Представляє помилки, викликані некоректним введенням користувача.

    ErrorHandler:
        Містить статичний метод для логування та відображення повідомлень про помилки.
"""

class APIError(Exception):
    """Виключення, що виникає у разі помилок під час запитів до API."""
    def __init__(self, message="An error occurred while accessing the API"):
        self.message = message
        super().__init__(self.message)


class UserInputError(Exception):
    """Виключення, що виникає через некоректне введення користувача."""
    def __init__(self, message="Invalid user input"):
        self.message = message
        super().__init__(self.message)


class ErrorHandler:
    @staticmethod
    def handle_error(error):
        """Логування та відображення повідомлення про помилку."""
        print(f"Error: {error}")
