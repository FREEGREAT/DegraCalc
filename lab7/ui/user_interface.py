# ui/user_interface.py
"""
    Модуль UserInterface
    ---------------------    
Цей модуль реалізує клас `UserInterface`, 
який забезпечує інтерактивну взаємодію з користувачем,
отримання даних із репозиторію, обробку введення 
користувача та збереження даних у різних форматах.
Імпортовані модулі
    -------------------
    - `ui.console_view.ConsoleView`:
        Для форматованого відображення даних у консолі.
    - `api.repository.DataRepository`:
        Для отримання та пошуку даних через API.
    - `core.transaction.Transactions`:
        Для реєстрації транзакцій і збереження історії.
    - `core.user_input_parser.UserInputParser`:
        Для перевірки та парсингу введення користувача 
        (наприклад, номер телефону чи дата).
    - `core.error_handler.ErrorHandler`, `APIError`, `UserInputError`:
        Для обробки загальних та специфічних помилок.
    - `utils.data_saver.DataSaver`:
        Для збереження даних у форматах JSON, CSV або TXT.
    Класи:
    ------
"""
from core.user_input_parser import UserInputParser
from core.error_handler import ErrorHandler, APIError, UserInputError
from utils.data_saver import DataSaver
from ui.console_view import ConsoleView

class UserInterface:
    """Клас для взаємодії з користувачем через консольний інтерфейс.

    Атрибути:
    ---------
    - repository (DataRepository):
        Репозиторій для отримання даних із API.
    - transactions (Transactions):
        Менеджер для реєстрації транзакцій.
    - view (ConsoleView):
        Інструмент для відображення даних у форматі таблиць.

    Методи:
    -------
    - __init__(repository, transactions):
        Ініціалізує об’єкт `UserInterface`.
        Параметри:
        - repository: Екземпляр `DataRepository` для роботи з API.
        - transactions: Екземпляр `Transactions` для обробки історії запитів.



    - save_data(data):
        Зберігає дані у вибраному користувачем форматі:
        - JSON, CSV або TXT.
        Якщо формат некоректний, дані не зберігаються.
"""

    def __init__(self, repository, transactions):
        self.repository = repository
        self.transactions = transactions
        self.view = ConsoleView()

    def start(self):
        """
        - start():
        Запускає головний цикл взаємодії з користувачем:
        - Отримує ресурс (наприклад, "posts", "users") або вводить інші дані.
        - Виконує запит до API для отримання даних.
        - Відображає дані через `ConsoleView`.
        - Реєструє транзакцію.
        - Дозволяє зберегти отримані дані у форматах JSON, CSV або TXT.

        Обробляє помилки введення користувача, API-запитів або інші винятки.
        """
        print("Available resources: /posts, /comments, /albums, /photos, /todos, /users")
        query = input("Enter a resource name (e.g., 'posts') or type a date/phone number: ")

        try:
            if query in ["posts", "comments", "albums", "photos", "todos", "users"]:
                data = self.repository.fetch_data(query)
                if data:
                    self.view.display_data(data)
                    self.transactions.register_request(query, data)
                    self.save_data(data)
            elif UserInputParser.parse_phone(query):  # Перевірка введення як номер телефону
                data = self.repository.fetch_data("users")  # Завантажуємо всіх користувачів
                user = self.repository.find_user_by_phone(query, data)
                if user:
                    self.view.display_data([user])
                    self.transactions.register_request(query, [user])
                    self.save_data(user)
                else:
                    print("No user found with this phone number.")
            elif "date" in query:
                date = UserInputParser.parse_date(query)
                print(f"Parsed Date: {date}")
            else:
                raise UserInputError("Invalid input. Please enter a valid resource name or format.")
        except UserInputError as e:
            ErrorHandler.handle_error(e)
        except APIError as e:
            ErrorHandler.handle_error(e)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def save_data(self, data):
        """
        Зберігає дані у файл, вибраний користувачем, 
        у одному з підтримуваних форматів: JSON, CSV або TXT.
        Користувач вибирає формат через введення з консолі.
        Параметри:
        -----------
        data : list of dict
            Дані для збереження, що передаються у 
            вигляді списку словників. 
            Кожен словник представляє один запис 
            (рядок) з даними.
        Виводить повідомлення про успішне збереження або помилку, 
        якщо формат вибраний некоректно.
        """
        format_choice = input("Choose a format to save data (json, csv, txt): ").strip().lower()
        if format_choice == "json":
            DataSaver.save_to_json(data)
        elif format_choice == "csv":
            DataSaver.save_to_csv(data)
        elif format_choice == "txt":
            DataSaver.save_to_txt(data)
        else:
            print("Invalid choice. Data was not saved.")
