"""
Модуль для очищення консолі.

Функція `clear_console` забезпечує очищення консолі для більш чистого відображення нового контенту.

Functions:
    clear_console(): Очищає консоль відповідно до операційної системи.
"""
import os

def clear_console():
    """
    Очищає консоль на основі операційної системи.

    Працює як для Windows (`cls`), так і для Unix-подібних систем (`clear`).

    Usage:
        Використовується для очищення екрану перед відображенням нової інформації.

    Example:
        >>> clear_console()
        (консоль очищується)

    Notes:
        - Windows використовує команду `cls` для очищення.
        - MacOS/Linux використовують команду `clear`.

    Raises:
        None: Якщо команда системи не виконується, ніяких винятків не буде піднято, але консоль залишиться незмінною.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
