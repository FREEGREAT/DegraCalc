# main.py
from api.api_client import APIClient
from api.repository import DataRepository
from core.transaction import Transactions
from core.error_handler import ErrorHandler
from ui.user_interface import UserInterface

def main():
    """
    Головний модуль програми
    ------------------------

    Цей файл є точкою входу до програми, яка інтегрує взаємодію між API, базою даних, 
    користувацьким інтерфейсом, транзакціями та обробкою помилок.

    Імпортовані модулі:
    -------------------
    - api.api_client:
        Містить клас `APIClient` для взаємодії з API.
    - api.repository:
        Містить клас `DataRepository` для роботи з даними, отриманими через API.
    - core.transaction:
        Містить клас `Transactions` для обробки транзакцій.
    - ui.user_interface:
        Містить клас `UserInterface` для взаємодії з користувачем.
    - core.error_handler:
        Містить клас `ErrorHandler` для обробки помилок.

    Функції:
    --------

    - main():
        Основна функція програми. Ініціалізує основні компоненти:
        - `APIClient`: Підключається до заданого API.
        - `DataRepository`: Використовує `APIClient` для роботи з даними.
        - `Transactions`: Управляє історією транзакцій.
        - `UserInterface`: Забезпечує взаємодію з користувачем, використовуючи 
        репозиторій і транзакції.

        Основний процес:
        - Викликає метод `ui.start()` для запуску користувацького інтерфейсу.
        - Зберігає історію транзакцій через `transactions.save_history()`.

        У разі виникнення виключення обробляє його за допомогою `ErrorHandler.handle_error(e)`.

    Точка входу:
    ------------
    - if __name__ == "__main__":
        Викликає функцію `main()` для запуску програми.
    """

    try:
        api_client = APIClient("https://jsonplaceholder.typicode.com")
        repository = DataRepository(api_client)
        transactions = Transactions()
        ui = UserInterface(repository, transactions)
        
        ui.start()
        transactions.save_history()
    except Exception as e:
        ErrorHandler.handle_error(e)

if __name__ == "__main__":
    main()
