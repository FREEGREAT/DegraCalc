# core/user_input_parser.py
import re
from core.error_handler import UserInputError
"""
Модуль `user_input_parser`
--------------------------

Цей модуль реалізує клас `UserInputParser`, який забезпечує парсинг (розбір) 
введення користувача, 
включаючи дати у форматі `YYYY-MM-DD` та номери телефонів.

Імпортовані модулі:
-------------------
- `re`:
    Стандартний модуль для роботи з регулярними виразами.
- `core.error_handler.UserInputError`:
    Клас для обробки винятків, пов'язаних із некоректним введенням користувача.

Класи:
-----
"""

class UserInputParser:
    """
    Клас `UserInputParser`, який забезпечує парсинг (розбір) 
    введення користувача, 
    включаючи дати у форматі `YYYY-MM-DD` та номери телефонів.
    """
    DATE_PATTERN = r"\b\d{4}-\d{2}-\d{2}\b"  # YYYY-MM-DD
    PHONE_PATTERN = r"\b\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b"
    @staticmethod
    def parse_date(input_string):
        """
        Розбирає рядок, шукаючи дату у форматі `YYYY-MM-DD`.
        Параметри:
        - input_string (str): Рядок для перевірки.
        Повертає:
        - str: Знайдена дата.
        Викидає:
        - UserInputError: Якщо формат дати некоректний.
        """
        match = re.search(UserInputParser.DATE_PATTERN, input_string)
        if match:
            return match.group()
        raise UserInputError("Invalid date format. Please use YYYY-MM-DD.")

    @staticmethod
    def parse_phone(input_string):
        """
        Розбирає рядок, шукаючи телефонний номер у підтримуваному форматі.
        Параметри:
        - input_string (str): Рядок для перевірки.
        Повертає:
        - str: Знайдений номер телефону.
        Викидає:
        - UserInputError: Якщо формат номера телефону некоректний.
        """
        match = re.search(UserInputParser.PHONE_PATTERN, input_string)
        if match:
            return match.group()
        raise UserInputError("Invalid phone number format.")
