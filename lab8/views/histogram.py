"""
histogram.py

Цей модуль реалізує клас Histogram для побудови гістограм, таких як розподіл вологості.

Імпортовані модулі:
    import matplotlib.pyplot as plt:
        Використовується для побудови графіків.

    from .base_plot import BasePlot:
        Базовий клас для побудови графіків.

Класи:
    Histogram(BasePlot):
        Реалізує побудову гістограми розподілу даних.

Методи:
    plot(self, data):
        Будує гістограму для заданих даних вологості.
"""
import matplotlib.pyplot as plt
from .base_plot import BasePlot

class Histogram(BasePlot):
    """
    Клас для створення гістограм.

    Наслідує базовий функціонал з BasePlot і додає можливість
    побудови гістограми для аналізу розподілу вологості.
    """

    def plot(self, data):
        """
        Побудова гістограми на основі заданих даних.

        Параметри:
            data (pandas.DataFrame): Табличні дані, які повинні містити стовпець 'Humidity'.

        Графічні елементи:
            - Вісь X: Вологість (%).
            - Вісь Y: Частота.
            - Заголовок: 'Humidity Distribution'.
        """
        data['Humidity'].plot(kind='hist', bins=10)
        plt.title('Humidity Distribution')
        plt.xlabel('Humidity (%)')
        plt.ylabel('Frequency')
