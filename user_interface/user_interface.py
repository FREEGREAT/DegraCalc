from ascii_art.ascii_art import AsciiArtGenerator
from color_utils.color_utils import Color
from file_manager.file_manager import FileManager
from error_handler.error_handler import ErrorHandler

class UserInterface:
    def __init__(self):
        self.generator = None

    def get_user_input(self):
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
        try:
            ascii_art = self.generator.generate_ascii_art()
            colored_art = Color.apply_color(ascii_art, color)
            print("\nПопередній перегляд ASCII-арту:\n")
            print(colored_art)
        except Exception as e:
            ErrorHandler.log_error(e)

    def save_ascii_art(self):
        try:
            filename = input("Введіть ім'я файлу для збереження (з .txt): ")
            content = self.generator.generate_ascii_art()
            FileManager.save_to_file(content, filename)
            print(f"ASCII-арт збережено у файлі {filename}.")
        except Exception as e:
            ErrorHandler.log_error(e)
