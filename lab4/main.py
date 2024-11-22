"""
Модуль для генерації ASCII-арту різних геометричних фігур з можливістю налаштування кольору, символу, вирівнювання та збереження.

Ключові функції:
- Інтерактивний вибір параметрів для створення ASCII-арту.
- Генерація фігур: квадрат, прямокутник, трикутник, ромб, коло.
- Налаштування кольору, символу та вирівнювання.
- Попередній перегляд фігури та можливість збереження у файл.

Modules:
    user_interface: Отримання введення користувача.
    art_generators: Генерація ASCII-арту для фігур.
    utils: Відображення ASCII-арту та збереження у файл.
    exceptions: Обробка помилок під час генерації.

Functions:
    generate_ascii_art(): Основна функція для створення ASCII-арту.
"""

from ui.user_interface import (
    get_shape_choice, get_dimensions_for_rectangle, get_size_for_shape, 
    get_color_choice, get_symbol_choice, get_alignment_choice, ask_to_continue
)
from art_generators.square import generate_square
from art_generators.rectangle import generate_rectangle
from art_generators.triangle import generate_triangle
from art_generators.diamond import generate_diamond
from art_generators.circle import generate_circle
from utils.display import display_ascii_art
from utils.save_art import save_art_to_file
from exceptions.art_errors import ArtGenerationError

def generate_ascii_art():
    """
    Інтерактивно генерує ASCII-арт обраної користувачем фігури з налаштуванням кольору, символу та вирівнювання.

    Workflow:
        1. Отримання вибору користувача:
           - Тип фігури: квадрат, прямокутник, трикутник, ромб, коло.
           - Розмір або параметри (ширина та висота для прямокутника).
           - Колір, символ та вирівнювання.
        2. Генерація фігури за допомогою відповідної функції з `art_generators`.
        3. Відображення ASCII-арту з обраними налаштуваннями.
        4. Опціональне збереження у файл.

    Raises:
        ArtGenerationError: Якщо виникла помилка під час генерації фігури.
        ValueError: Якщо введені некоректні параметри.
        Exception: Інші непередбачені помилки.

    User Interaction:
        - Користувач обирає тип фігури, параметри, колір, символ та вирівнювання.
        - Пропонується зберегти фігуру у файл після перегляду.

    Example:
        >>> generate_ascii_art()
        Введіть тип фігури (квадрат/прямокутник/трикутник/ромб/коло): квадрат
        Введіть розмір: 5
        Введіть колір: red
        Введіть символ: #
        Введіть вирівнювання (left/center/right): center
        Попередній перегляд ASCII-арту...
        Бажаєте зберегти фігуру у файл? (так/ні): так
        Введіть ім'я файлу: square_art
        Файл збережено як square_art.txt
    """
    try:
        shape = get_shape_choice()

        if shape == "прямокутник":
            width, height = get_dimensions_for_rectangle()
        else:
            size = get_size_for_shape()

        color = get_color_choice()
        symbol = get_symbol_choice()
        alignment = get_alignment_choice()

        if shape == "квадрат":
            art = generate_square(size)
        elif shape == "прямокутник":
            art = generate_rectangle(width, height)
        elif shape == "трикутник":
            art = generate_triangle(size)
        elif shape == "ромб":
            art = generate_diamond(size)
        elif shape == "коло":
            art = generate_circle(size)
        else:
            raise ValueError("Невідомий тип фігури.")

        display_ascii_art(art, color, symbol, alignment)

        save_option = input("Бажаєте зберегти фігуру у файл? (так/ні): ").strip().lower()
        if save_option == 'так':
            file_name = input("Введіть ім'я файлу (без розширення): ").strip() + ".txt"
            save_art_to_file(art, file_name)

    except ArtGenerationError as e:
        print(f"Помилка генерації фігури: {e}")
    except ValueError as ve:
        print(f"Помилка: {ve}")
    except Exception as e:
        print(f"Непередбачена помилка: {e}")

if __name__ == "__main__":
    """
    Головний цикл програми.

    Виконує функцію `generate_ascii_art` у циклі, поки користувач не вирішить завершити програму.

    User Interaction:
        - Користувач може повторювати генерацію фігур, поки не обере вихід.

    Exceptions:
        - Обробляє будь-які помилки, що виникають під час виконання циклу.
    """
    try:
        while True:
            generate_ascii_art()
            if not ask_to_continue():
                break
    except Exception as e:
        print(f"Помилка у головному циклі програми: {e}")
    finally:
        print("Програма завершена.")
