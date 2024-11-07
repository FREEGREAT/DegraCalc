# ui/console_view.py
from rich.console import Console
from rich.table import Table

class ConsoleView:
    def __init__(self, title_color="blue"):
        self.console = Console()
        self.title_color = title_color

    def display_data(self, data):
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
