"""
main.py

Цей модуль є точкою входу для програми. Він забезпечує взаємодію користувача
 з даними через текстове меню.

Імпортовані модулі:
    from controllers.data_controller import DataController:
        Використовується для керування обробкою даних.

    from ui.menu import display_menu, handle_choice:
        Забезпечує відображення меню та обробку вибору користувача.

Функції:
    main():
        Основна функція програми. Відображає меню, обробляє вибір користувача 
        та координує роботу з даними.

Головний сценарій:
    Запускає програму, якщо модуль виконується безпосередньо.
"""
from controllers.data_controller import DataController
from ui.menu import display_menu, handle_choice

def main():
    """
    Основна функція програми.

    Ініціалізує DataController з шляхом до CSV-файлу, відображає меню та обробляє вибір користувача.

    Основна логіка:
        - Відображає текстове меню.
        - Приймає вибір користувача.
        - Передає вибір до відповідного обробника.
        - Завершує роботу програми, якщо користувач вводить 'q'.
    """
    file_path = 'lab8/data/weather_data.csv'
    controller = DataController(file_path)
    while True:
        display_menu()
        choice = input("Select an option (or 'q' to quit): ")        
        if choice.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        handle_choice(choice, controller) 
if __name__ == "__main__":
    main()
