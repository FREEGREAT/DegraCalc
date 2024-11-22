"""
Модуль для отримання вводу від користувача для створення ASCII-фігур.

Цей модуль містить функції для вибору типу фігури, її параметрів, кольору, символу, вирівнювання та рішення про продовження роботи.

Functions:
    get_shape_choice() -> str: Повертає вибраний тип фігури.
    get_dimensions_for_rectangle() -> tuple[int, int]: Повертає ширину і висоту прямокутника.
    get_size_for_shape() -> int: Повертає розмір фігури.
    get_color_choice() -> str: Повертає вибраний колір.
    get_symbol_choice() -> str: Повертає символ для малювання.
    get_alignment_choice() -> str: Повертає вибране вирівнювання.
    ask_to_continue() -> bool: Повертає `True`, якщо користувач хоче продовжити роботу.
"""

def get_shape_choice():
    """
    Отримує вибір користувача щодо типу фігури.

    Returns:
        str: Тип фігури ("квадрат", "прямокутник", "трикутник", "ромб", "коло").

    Raises:
        ValueError: Якщо введене значення не відповідає допустимим варіантам.

    Example:
        >>> get_shape_choice()
        Виберіть фігуру (квадрат/прямокутник/трикутник/ромб/коло): квадрат
        'квадрат'
    """
    shape = input("Виберіть фігуру (квадрат/прямокутник/трикутник/ромб/коло): ").strip().lower()
    if shape not in ["квадрат", "прямокутник", "трикутник", "ромб", "коло"]:
        raise ValueError("Невірний тип фігури. Допустимі варіанти: квадрат, прямокутник, трикутник, ромб, коло.")
    return shape

def get_dimensions_for_rectangle():
    """
    Отримує параметри прямокутника: ширину і висоту.

    Returns:
        tuple[int, int]: Ширина і висота прямокутника.

    Example:
        >>> get_dimensions_for_rectangle()
        Введіть ширину прямокутника: 5
        Введіть висоту прямокутника: 3
        (5, 3)
    """
    width = int(input("Введіть ширину прямокутника: "))
    height = int(input("Введіть висоту прямокутника: "))
    return width, height

def get_size_for_shape():
    """
    Отримує розмір для фігур, які мають лише один параметр (наприклад, квадрат, ромб, трикутник).

    Returns:
        int: Розмір фігури.

    Example:
        >>> get_size_for_shape()
        Введіть розмір фігури: 4
        4
    """
    size = int(input("Введіть розмір фігури: "))
    return size

def get_color_choice():
    """
    Отримує вибір користувача щодо кольору.

    Returns:
        str: Колір ("purple", "green", "blue", "red", "bw").

    Example:
        >>> get_color_choice()
        Виберіть колір (purple/green/blue/red/bw): green
        'green'
    """
    color = input("Виберіть колір (purple/green/blue/red/bw): ").strip().lower()
    return color

def get_symbol_choice():
    """
    Отримує символ для малювання ASCII-фігури.

    Returns:
        str: Символ (один символ).

    Example:
        >>> get_symbol_choice()
        Введіть символ для малювання (один символ): #
        '#'
    """
    symbol = input("Введіть символ для малювання (один символ): ").strip()
    return symbol

def get_alignment_choice():
    """
    Отримує вибір користувача щодо вирівнювання тексту.

    Returns:
        str: Вирівнювання ("left", "center", "right").

    Example:
        >>> get_alignment_choice()
        Виберіть вирівнювання (left/center/right): center
        'center'
    """
    alignment = input("Виберіть вирівнювання (left/center/right): ").strip().lower()
    return alignment

def ask_to_continue():
    """
    Питає у користувача, чи хоче він створити ще одну фігуру.

    Returns:
        bool: `True`, якщо користувач відповів "так", інакше `False`.

    Example:
        >>> ask_to_continue()
        Бажаєте створити ще одну фігуру? (так/ні): так
        True
    """
    cont = input("Бажаєте створити ще одну фігуру? (так/ні): ").strip().lower()
    return cont == 'так'
