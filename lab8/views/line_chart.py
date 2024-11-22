"""
line_chart.py

Цей модуль реалізує клас LineChart для побудови 
лінійних графіків, таких як зміна температури з часом.

Імпортовані модулі:
    import matplotlib.pyplot as plt:
        Використовується для побудови графіків.

    from .base_plot import BasePlot:
        Базовий клас для побудови графіків.

Класи:
    LineChart(BasePlot):
        Реалізує побудову лінійного графіка.

Методи:
    plot(self, data):
        Будує лінійний графік температури за часом.
"""
import matplotlib.pyplot as plt
from .base_plot import BasePlot

class LineChart(BasePlot):
    """
    Клас для створення лінійних графіків.

    Наслідує базовий функціонал з BasePlot і
    додає можливість побудови графіка зміни температури з часом.
    """

    def plot(self, data):
        """
        Побудова лінійного графіка на основі заданих даних.

        Перевіряє, чи дані не є порожніми. Якщо дані доступні, будує графік.

        Параметри:
            data (pandas.DataFrame): Табличні дані, 
            які повинні містити стовпці 'Date' та 'Temperature'.

        Графічні елементи:
            - Вісь X: Дата (Date).
            - Вісь Y: Температура (°C).
            - Заголовок: 'Temperature Over Time'.
        """
        if data.empty:
            print("No data available to plot.")
            return

        plt.figure()
        data.plot(x='Date', y='Temperature', kind='line')
        plt.title('Temperature Over Time')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
