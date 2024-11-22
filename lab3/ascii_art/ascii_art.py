"""
Клас для генерації ASCII-арту за допомогою бібліотеки `pyfiglet`.

Клас дозволяє створювати ASCII-арт на основі заданого тексту, шрифту та символу для заміни символу `_`. Також передбачено можливість отримати список доступних шрифтів.

Attributes:
    text (str): Текст, який буде перетворено в ASCII-арт.
    font (str): Назва шрифту для генерації ASCII-арту (за замовчуванням 'slant').
    symbol (str): Символ, який замінить символ `_` у згенерованому ASCII-арті (за замовчуванням '_').

Methods:
    generate_ascii_art(): Генерує ASCII-арт на основі заданих параметрів.
    available_fonts(): Повертає список доступних шрифтів для ASCII-арту.
"""

import pyfiglet

class AsciiArtGenerator:
    """
    Клас для генерації ASCII-арту.
    """

    def __init__(self, text, font='slant', symbol='_'):
        """
        Ініціалізує об'єкт генератора ASCII-арту.

        Args:
            text (str): Текст для генерації ASCII-арту.
            font (str, optional): Назва шрифту для генерації (за замовчуванням 'slant').
            symbol (str, optional): Символ, який замінить `_` (за замовчуванням '_').
        """
        self.text = text
        self.font = font
        self.symbol = symbol

    def generate_ascii_art(self):
        """
        Генерує ASCII-арт на основі заданих параметрів.

        Returns:
            str: Згенерований ASCII-арт.

        Raises:
            ValueError: Якщо виникла помилка при генерації ASCII-арту.
        """
        try:
            ascii_art = pyfiglet.figlet_format(self.text, font=self.font)
            return ascii_art.replace('_', self.symbol)
        except Exception as e:
            raise ValueError("Помилка генерації ASCII-арту: " + str(e))

    def available_fonts(self):
        """
        Повертає список доступних шрифтів для ASCII-арту.

        Returns:
            list: Список назв доступних шрифтів.
        """
        return pyfiglet.FigletFont.getFonts()
