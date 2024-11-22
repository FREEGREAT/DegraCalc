# ui/console_view.py
"""
Модуль для відображення даних у консолі за допомогою бібліотеки `rich`.

Цей модуль містить клас `ConsoleView`, який надає можливість виводити дані у вигляді таблиці
у консоль з використанням бібліотеки `rich`, що дозволяє зробити виведення більш привабливим
і легким для сприйняття.

Модуль підтримує:
- Виведення таблиць з даними, де кожен стовпець може мати стилізований заголовок.
- Виведення повідомлення про відсутність даних, якщо переданий список порожній.
- Налаштування кольору для заголовка таблиці.

Приклад використання:
----------------------
from rich.console import Console
from rich.table import Table
from ui.console_view import ConsoleView

# Створення екземпляра ConsoleView з налаштованим кольором заголовка
view = ConsoleView(title_color="green")

# Приклад даних для відображення
data = [
    {"Name": "John", "Age": 30, "City": "New York"},
    {"Name": "Alice", "Age": 25, "City": "Los Angeles"},
    {"Name": "Bob", "Age": 35, "City": "Chicago"}
]

# Виклик методу для відображення таблиці
view.display_data(data)

"""

from rich.console import Console
from rich.table import Table

class ConsoleView:
    """
    Клас для відображення даних у вигляді таблиці у 
    консолі за допомогою бібліотеки `rich`.
    Атрибути:
    ----------
    console : rich.console.Console
        Екземпляр класу Console з бібліотеки `rich`,
        який використовується для виведення в консоль.
    title_color : str
        Колір для заголовка таблиці (за замовчуванням "blue").
    Методи:
    --------
    __init__(title_color="blue") :
        Ініціалізує ConsoleView з вказаним кольором 
        для заголовка таблиці.
    display_data(data) :
        Виводить дані у вигляді таблиці у консоль. 
        Якщо дані відсутні, виводиться повідомлення про помилку.
        Параметри:
        -----------
        data : list of dict
            Дані для відображення у вигляді списку словників, 
            де кожен словник представляє один рядок таблиці.
            Ключі словників використовуються як заголовки стовпців.
    """
    def __init__(self, title_color="blue"):
        self.console = Console()
        self.title_color = title_color

    def display_data(self, data):
        """
        Виводить дані у вигляді таблиці у консоль. 
        Якщо дані відсутні, виводиться повідомлення про помилку.
        Параметри:
        -----------
        data : list of dict
            Дані для відображення, де кожен елемент списку є 
            словником, що представляє один рядок.
        """
        if not data:
            self.console.print("[red]No data to display[/red]")
            return
        
        table = Table(title="Data", title_style=self.title_color)
        for key in data[0].keys():
            table.add_column(key.capitalize(), justify="left", style="bold " + self.title_color)

        for item in data:
            row = [str(value) for value in item.values()]
            table.add_row(*row)

        self.console.print(table)
