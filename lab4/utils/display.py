"""
Модуль для відображення ASCII-арту з підтримкою кольорів, символів і вирівнювання.

Функція `display_ascii_art` забезпечує гнучке форматування ASCII-арту, включаючи вибір кольору, символу, 
вирівнювання тексту і обробку виводу залежно від розміру терміналу.

Functions:
    display_ascii_art(art, color="bw", symbol="@", alignment="left"): Виводить ASCII-арт на екран.

Dependencies:
    - shutil: Для отримання розмірів терміналу.
    - clear_console: Очищення консолі перед виведенням (модуль `utils.clear`).
"""
import shutil
from utils.clear import clear_console

def display_ascii_art(art, color="bw", symbol="@", alignment="left"):
    """
    Відображає ASCII-арт у терміналі з підтримкою кольорів і вирівнювання.

    Parameters:
        art (list[list[int]]): Матриця, що представляє ASCII-арт, де:
            - `1` вказує на позицію символу (`symbol`).
            - `0` вказує на порожній простір.
        color (str): Колір символу. Доступні варіанти:
            - "bw" (за замовчуванням): Чорно-білий (без кольору).
            - "purple", "green", "blue", "red": Відповідний колір тексту.
        symbol (str): Символ, який використовується для формування ASCII-арту (за замовчуванням "@").
        alignment (str): Вирівнювання тексту. Доступні варіанти:
            - "left" (за замовчуванням): Вирівнювання по лівому краю.
            - "center": Центрування тексту.
            - "right": Вирівнювання по правому краю.

    Workflow:
        1. Очищення консолі перед виведенням (використовує `clear_console`).
        2. Отримання ширини терміналу для обчислення вирівнювання.
        3. Встановлення кольору символу залежно від вибору користувача.
        4. Генерація рядків з матриці `art`, додаючи кольорові коди і вирівнюючи текст.
        5. Виведення ASCII-арту на екран.

    Raises:
        Exception: Виводить повідомлення про помилку у разі непередбаченого збою.

    Example:
        >>> art = [
        ...     [0, 1, 0],
        ...     [1, 1, 1],
        ...     [0, 1, 0]
        ... ]
        >>> display_ascii_art(art, color="green", symbol="#", alignment="center")

    Notes:
        - Кольори реалізовані через ANSI-коди.
        - Код адаптує текст до ширини терміналу.
        - Якщо ширина рядка більша за ширину терміналу, текст не буде обрізано.

    Terminal Behavior:
        - Під час виведення консолі попередній вміст очищується для чіткого відображення фігури.
    """
    try:
        clear_console()
        
        # Отримання розміру терміналу
        terminal_size = shutil.get_terminal_size()
        terminal_width = terminal_size.columns
        
        # Додавання кольору
        if color == "purple":
            color_code = '\033[35m'
        elif color == "green":
            color_code = '\033[32m'
        elif color == "blue":
            color_code = '\033[34m'
        elif color == "red":
            color_code = '\033[31m'
        else:
            color_code = ''
        
        reset_code = '\033[0m'
        symbol_colored = color_code + symbol + reset_code

        # Обчислення максимального рядка фігури
        max_width = max(len("".join([symbol if val == 1 else " " for val in row])) for row in art)

        for row in art:
            line = "".join([symbol_colored if val == 1 else " " for val in row])
            line_len = len(line.replace(color_code, '').replace(reset_code, ''))  # Довжина без кольорових кодів

            # Вирівнювання рядків залежно від ширини терміналу
            if alignment == "center":
                padding = (terminal_width - line_len) // 2
                line = " " * padding + line
            elif alignment == "right":
                padding = terminal_width - line_len
                line = " " * padding + line
            elif alignment == "left":
                line = line.ljust(max_width)

            # Виведення результату
            print(line)

    except Exception as e:
        print(f"Непередбачена помилка під час виведення ASCII-арту: {e}")
