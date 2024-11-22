from datetime import datetime
import os

"""
Модуль `transactions`
----------------------

Цей модуль реалізує клас `Transactions`, який відповідає за реєстрацію історії запитів 
та збереження її у лог-файл.

Імпортовані модулі:
-------------------
- `datetime.datetime`:
    Для отримання поточного часу запиту у форматі ISO.
- `os`:
    Для роботи з файловою системою, включаючи створення директорій.

Класи:
------
"""

class Transactions:
    """
           Клас для управління історією запитів і їх збереження у файл.

    Атрибути:
    ---------
    - history (list):
        Список для зберігання історії запитів. Кожен запис містить:
        - query (str): Назва запиту.
        - result: Результат запиту (будь-який тип).
        - timestamp (str): Час створення запиту у форматі ISO.

    Методи:
    -------
    - __init__():
        Ініціалізує об'єкт класу `Transactions` з порожньою історією.

    - register_request(query, result):
        Реєструє новий запит у історії.
        Параметри:
        - query (str): Назва або зміст запиту.
        - result: Результат виконання запиту.

    - save_history(filename="results/lab7/logs/history.log"):
        Зберігає всю історію у лог-файл і очищує список.
        Параметри:
        - filename (str): Шлях до файлу для збереження історії (за замовчуванням 
          "results/lab7/logs/history.log").
        - Якщо директорія у вказаному шляху не існує, вона створюється.
    """
    def __init__(self):
        """Ініціалізує історію запитів як порожній список."""
        self.history = []

    def register_request(self, query, result):
        """
        Реєструє запит у списку історії.

        Параметри:
        - query (str): Запит або ім'я ресурсу.
        - result: Результат виконання запиту (тип даних необмежений).

        Додає у `history` словник із полями `query`, `result` та поточним часом.
        """
        self.history.append({
            "query": query,
            "result": result,
            "timestamp": datetime.now().isoformat()
        })

    def save_history(self, filename="results/lab7/logs/history.log"):
        """
        Зберігає історію запитів у лог-файл.

        Параметри:
        - filename (str): Шлях до файлу, куди буде збережено історію (за замовчуванням 
          "results/lab7/logs/history.log").

        Опис:
        - Створює вказану директорію, якщо вона не існує.
        - Записує кожен елемент `history` у файл з форматованими даними (час, запит, результат).
        - Очищує список `history` після збереження.
        """
        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(filename, "a") as file:
            for entry in self.history:
                file.write(f"{entry['timestamp']} - Query: {entry['query']}, Result: {entry['result']}\n")
        
        self.history.clear()
