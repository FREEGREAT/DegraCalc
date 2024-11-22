"""
scatter_plot.py

Цей модуль реалізує клас ScatterPlot, який використовується для 
створення графіків розсіювання (scatter plots)
 даних, таких як співвідношення температури та вологості.

Імпортовані модулі:
    import matplotlib.pyplot as plt:
        Використовується для візуалізації даних.

    from .base_plot import BasePlot:
        Базовий клас для різних типів графіків.

Класи:
    ScatterPlot(BasePlot):
        Наслідує функціональність BasePlot і додає метод для побудови графіків розсіювання.

Методи:
    plot(self, data):
        Будує графік розсіювання для заданих даних.
"""
import matplotlib.pyplot as plt
from .base_plot import BasePlot

class ScatterPlot(BasePlot):
    """
    Клас для створення графіків розсіювання.

    Наслідує базовий функціонал з BasePlot і додає можливість побудови 
    графіка розсіювання для співвідношення температури та вологості.
    """

    def plot(self, data):
        """
        Побудова графіка розсіювання на основі заданих даних.

        Параметри:
            data (pandas.DataFrame): Табличні дані, 
            які повинні містити стовпці 'Temperature' та 'Humidity'.

        Графічні елементи:
            - Вісь X: Температура (°C).
            - Вісь Y: Вологість (%).
            - Заголовок: 'Temperature vs Humidity'.
        """
        data.plot.scatter(x='Temperature', y='Humidity')
        plt.title('Temperature vs Humidity')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Humidity (%)')
