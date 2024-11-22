"""
Головний модуль для запуску програм лабораторних робіт, включаючи генератор ASCII-арту.

Цей модуль забезпечує:
- Інтерактивний вибір лабораторних робіт для виконання.
- Запуск генератора ASCII-арту через клас `UserInterface`.

Functions:
    run_ascii_art_generator(): Запускає генератор ASCII-арту, взаємодіючи з користувачем.
    main(): Головна функція програми для вибору та запуску лабораторних робіт.
"""

import sys
import os

# Додаємо директорію з іншими модулями до шляху
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_interface.user_interface import UserInterface

def run_ascii_art_generator():
    """
    Запускає генератор ASCII-арту.

    Використовує `UserInterface` для отримання введення користувача, 
    попереднього перегляду ASCII-арту та його збереження у файл.

    Workflow:
        1. Отримання вхідних даних від користувача: текст, шрифт, символ і колір.
        2. Попередній перегляд згенерованого ASCII-арту з вибраним кольором.
        3. Пропозиція зберегти результат у файл.

    Exceptions:
        Виводить повідомлення про помилку, якщо виникає виключення під час виконання.
    """
    try:
        ui = UserInterface()
        color = ui.get_user_input()
        if color:
            ui.preview_ascii_art(color)
            save = input("Бажаєте зберегти ASCII-арт? (y/n): ").lower()
            if save == 'y':
                ui.save_ascii_art()

    except Exception as e:
        print(f"Сталася помилка під час виконання генератора ASCII-арту: {str(e)}")

def main():
    """
    Головна функція програми для вибору та запуску лабораторних робіт.

    Workflow:
        1. Відображає список доступних лабораторних робіт.
        2. Приймає вибір користувача.
        3. Виконує вибрану лабораторну роботу або завершує програму.

    Labs:
        - Генератор ASCII-арту (`run_ascii_art_generator`).
        - Можливість додавання інших лабораторних робіт у список `labs`.

    User Interaction:
        - Введення номера лабораторної роботи для запуску.
        - Введення даних для ASCII-арту під час запуску генератора.

    Exceptions:
        - Обробляє помилки вводу (неправильний номер або некоректне введення).
        - Виводить повідомлення про помилку, якщо виникає виключення під час виконання.
    """
    labs = [
        {"name": "Генератор ASCII-арту", "function": run_ascii_art_generator},
        # {"name": "Назва лабораторної", "function": ваша_функція}
    ]
     
    while True:
        print("\nВиберіть лабораторну роботу для запуску:")
        for i, lab in enumerate(labs, start=1):
            print(f"{i}. {lab['name']}")
        print(f"{len(labs) + 1}. Вихід")

        try:
            choice = int(input("Ваш вибір: "))

            if 1 <= choice <= len(labs):
                labs[choice - 1]["function"]()
            elif choice == len(labs) + 1:
                print("Вихід з програми.")
                break
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Будь ласка, введіть номер лабораторної роботи.")
        except Exception as e:
            print(f"Сталася помилка: {str(e)}")

if __name__ == "__main__":
    main()
