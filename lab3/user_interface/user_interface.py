"""
Модуль `UserInterface` надає інтерфейс для взаємодії з користувачем, що дозволяє створювати, переглядати 
та зберігати ASCII-арт із кольоровим форматуванням. 

Клас використовує такі модулі:
- `AsciiArtGenerator` для генерації ASCII-арту.
- `Color` для застосування кольорового форматування.
- `FileManager` для збереження результатів у файл.
- `ErrorHandler` для обробки помилок.

Classes:
    UserInterface: Клас для взаємодії з користувачем.

Methods:
    get_user_input(): Отримує вхідні дані від користувача для створення ASCII-арту.
    preview_ascii_art(color): Відображає кольоровий ASCII-арт у консолі.
    save_ascii_art(): Зберігає ASCII-арт у файл.
"""
from ascii_art.ascii_art import AsciiArtGenerator
from color_utils.color_utils import Color
from file_manager.file_manager import FileManager
from error_handler.error_handler import ErrorHandler

class UserInterface:
    """
    Клас для взаємодії з користувачем, що дозволяє створювати, переглядати та зберігати ASCII-арт.
    """

    def __init__(self):
        """
        Ініціалізує об'єкт інтерфейсу користувача.

        Attributes:
            generator (AsciiArtGenerator): Об'єкт для генерації ASCII-арту (ініціалізується пізніше).
        """
        self.generator = None

    def get_user_input(self):
        """
        Отримує вхідні дані від користувача для створення ASCII-арту.

        Вхідні дані включають текст, шрифт, символ заміни та колір ASCII-арту.

        Returns:
            str: Колір ASCII-арту, обраний користувачем.

        Raises:
            Exception: Якщо виникає помилка під час отримання введення, вона логірується через `ErrorHandler`.
        """
        try:
            text = input("Введіть текст для ASCII-арту: ")
            font = input("Виберіть шрифт (або натисніть Enter для 'slant'): ") or 'slant'
            symbol = input("Введіть символ для ASCII-арту (або натисніть Enter для '*'): ") or '*'
            color = input("Введіть колір (red, green, yellow, blue, magenta, cyan): ")
            self.generator = AsciiArtGenerator(text, font, symbol)
            return color
        except Exception as e:
            ErrorHandler.log_error(e)

    def preview_ascii_art(self, color):
        """
        Відображає кольоровий ASCII-арт у консолі.

        Args:
            color (str): Колір, який буде застосовано до ASCII-арту.

        Raises:
            Exception: Якщо виникає помилка під час генерації або форматування, вона логірується через `ErrorHandler`.
        """
        try:
            ascii_art = self.generator.generate_ascii_art()
            colored_art = Color.apply_color(ascii_art, color)
            print("\nПопередній перегляд ASCII-арту:\n")
            print(colored_art)
        except Exception as e:
            ErrorHandler.log_error(e)

    def save_ascii_art(self):
        """
        Зберігає ASCII-арт у файл.

        Користувач вводить ім'я файлу, і результат зберігається у текстовий файл.

        Raises:
            Exception: Якщо виникає помилка під час збереження, вона логірується через `ErrorHandler`.
        """
        try:
            filename = input("Введіть ім'я файлу для збереження (з .txt): ")
            content = self.generator.generate_ascii_art()
            FileManager.save_to_file(content, filename)
            print(f"ASCII-арт збережено у файлі {filename}.")
        except Exception as e:
            ErrorHandler.log_error(e)
