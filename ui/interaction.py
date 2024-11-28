"""
Цей модуль містить функції для взаємодії з користувачем, включаючи:
- Вибір лабораторної роботи для запуску.
- Запуск обраної лабораторної роботи.
"""

import os
import subprocess

def get_lab_choice():
    """
    Запитує користувача для вибору лабораторної роботи та повертає номер вибраної роботи.

    Виводить список доступних лабораторних робіт (lab1, lab2, ..., lab8) і запитує користувача
    ввести номер лабораторної роботи. Якщо введене значення коректне, повертає його як ціле число.

    Повертає:
    --------
    int or None
        Номер вибраної лабораторної роботи (1-8), або None, якщо введене значення некоректне.
    """
    print("Оберіть лабораторну роботу для запуску:")
    lab_dirs = [f"lab{i}" for i in range(1, 9)]  # Папки lab1, lab2, ..., lab8
    for i, lab in enumerate(lab_dirs, 1):
        print(f"{i}. {lab}")    
    choice = input("Введіть номер лабораторної роботи (1-8): ")
    return int(choice) if choice.isdigit() and 1 <= int(choice) <= 8 else None

def run_lab(lab_number):
    """
    Запускає Python скрипт лабораторної роботи на основі вибраного номера.

    Створює шлях до файлу `main.py` в папці відповідної 
    лабораторної роботи (lab1/main.py, lab2/main.py, ...).
    
    Якщо файл існує, виконує його за допомогою `subprocess.run`. 
    Якщо файл не знайдено або виникає помилка,
    виводить відповідне повідомлення.

    Параметри:
    -----------
    lab_number : int
        Номер лабораторної роботи, яку потрібно запустити (від 1 до 8).

    Викидає:
    --------
    subprocess.CalledProcessError
        Якщо виникає помилка під час виконання скрипта.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Поточний шлях до interaction.py
    lab_name = f"lab{lab_number}"
    lab_path = os.path.join(base_dir, "..", lab_name, "main.py")  # Шлях до lab1/main.py

    # Змінили ".." для переходу до кореневої директорії, де знаходяться папки lab1, lab2, ...
    if os.path.exists(lab_path):
        print(f"Запускаю {lab_name}...")
        try:
            subprocess.run(["python", lab_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Помилка при виконанні {lab_path}: {e}")
    else:
        print(f"Файл {lab_path} не знайдено!")
    

def interact():
    """
    Запускає інтерфейс взаємодії, дозволяючи запускати лабораторні роботи або тести.
    """
    print("Оберіть дію:")
    print("1. Запустити лабораторну роботу")
    print("2. Запустити всі тести (test_calculator.py і unit_test.py)")
    choice = input("Ваш вибір (1 або 2): ")

    if choice == "1":
        lab_choice = get_lab_choice()
        if lab_choice:
            run_lab(lab_choice)
        else:
            print("Невірний вибір. Будь ласка, введіть номер від 1 до 8.")
    elif choice == "2":
        run_tests()
    else:
        print("Невірний вибір. Введіть 1 або 2.")


def run_tests():
    """
    Запускає тести для модулів test_calculator.py (у папці tests) 
    і unit_test.py (у папці lab7/tests).
    Виводить результати з кастомним форматуванням.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__)) 

    test_calculator_path = os.path.join(base_dir, "..", "lab6", "tests", "test_calculator.py")
    unit_test_path = os.path.join(base_dir, "..", "lab7", "tests", "unit_test.py")

    for test_path in [test_calculator_path, unit_test_path]:
        if os.path.exists(test_path):
            print(f"Запускаю тести {os.path.basename(test_path)}...\n")
            try:
                subprocess.run(["python", test_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Помилка під час виконання тестів у {test_path}: {e}")
        else:
            print(f"Файл {test_path} не знайдено!")

