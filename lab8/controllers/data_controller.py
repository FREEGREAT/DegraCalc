"""
Клас для керування завантаженням даних, їх аналізом та побудовою графіків.
"""
from models.data_loader import DataLoader
from models.data_analysis import DataAnalysis
from views.line_chart import LineChart
from views.scatter_plot import ScatterPlot
from views.histogram import Histogram

class DataController:
    """
    Клас для керування завантаженням даних, їх аналізом та побудовою графіків.
    Атрибути:
    ----------
    data_loader : DataLoader
        Екземпляр класу `DataLoader`, який використовується для завантаження даних з CSV файлу.
    data : pandas.DataFrame
        Дані, завантажені з файлу. Якщо дані не вдалося завантажити, буде виведено попередження.
    analysis : DataAnalysis
        Екземпляр класу `DataAnalysis`, який виконує аналіз даних, включаючи 
        обчислення екстремальних значень.
    Методи:
    --------
    __init__(file_path) :
        Ініціалізує клас, завантажуючи дані з CSV файлу за вказаним шляхом та здійснює їх 
        попередній аналіз.
    display_extremes() :
        Виводить мінімальні та максимальні значення для різних параметрів: 
        'Temperature', 'Humidity', 'WindSpeed', 'Rainfall'.
    get_plot_instance(plot_type) :
        Повертає екземпляр відповідного класу для побудови графіка 
        залежно від типу графіка:
        - "line" — `LineChart`
        - "scatter" — `ScatterPlot`
        - "histogram" — `Histogram`
    plot_chart(plot_type) :
        Створює графік за вказаним типом та відображає його.
    """
    def __init__(self, file_path):
        """
        Ініціалізує клас, завантажуючи дані з CSV файлу та здійснює їх попередню обробку.
        Параметри:
        -----------
        file_path : str
            Шлях до CSV файлу для завантаження даних.
        """
        self.data_loader = DataLoader(file_path)
        self.data = self.data_loader.load_data()
        if self.data.empty:
            print("Warning: The data is empty or could not be loaded correctly.")
        self.analysis = DataAnalysis(self.data)
    def display_extremes(self):
        """
        Виводить мінімальні та максимальні значення для таких параметрів, як:
        'Temperature', 'Humidity', 'WindSpeed', 'Rainfall'.
        """
        extremes = self.analysis.get_extreme_values()
        for key, value in extremes.items():
            print(f'{key}: Min={value[0]}, Max={value[1]}')

    def get_plot_instance(self, plot_type):
        """
        Повертає інстанс графіка відповідного типу.

        Параметри:
        -----------
        plot_type : str
            Тип графіка, який потрібно побудувати ("line", "scatter", "histogram").

        Повертає:
        --------
        object
            Інстанс відповідного класу для побудови графіка або `None`, 
            якщо тип графіка не підтримується.
        """
        if plot_type == "line":
            return LineChart()
        elif plot_type == "scatter":
            return ScatterPlot()
        elif plot_type == "histogram":
            return Histogram()
        else:
            return None
    def plot_chart(self, plot_type):
        """
        Створює графік за вказаним типом та відображає його.
        Параметри:
        -----------
        plot_type : str
            Тип графіка, який потрібно побудувати ("line", "scatter", "histogram").
        """
        plot_instance = self.get_plot_instance(plot_type)
        if plot_instance:
            plot_instance.plot(self.data)  
            plot_instance.show()
