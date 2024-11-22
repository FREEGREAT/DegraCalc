"""
    Клас для завантаження та перевірки даних з CSV файлу.

    Атрибути:
    ----------
    file_path : str
        Шлях до CSV файлу, з якого будуть завантажуватися дані.

    Методи:
    --------
    load_data() :
        Завантажує дані з CSV файлу, перевіряє наявність 
        необхідних колонок та конвертує стовпець 'Date' 
        в формат datetime.
        Якщо файл не знайдено або відсутні необхідні колонки, 
        виводиться повідомлення про помилку.
        Повертає:
        --------
        pandas.DataFrame
            Завантажені дані, або порожній DataFrame у випадку помилки.
"""
import pandas as pd

class DataLoader:
    """
    Клас для завантаження та перевірки даних з CSV файлу.
    """
    def __init__(self, file_path):
        """
        Ініціалізує клас з шляхом до файлу.

        Параметри:
        -----------
        file_path : str
            Шлях до CSV файлу для завантаження даних.
        """
        self.file_path = file_path

    def load_data(self):
        """
        Завантажує дані з CSV файлу.

        Перевіряє наявність необхідних колонок: 
        'Date', 'Temperature', 'Humidity', 'WindSpeed', 'Rainfall'.
        Якщо хоча б одна колонка відсутня, 
        піднімається помилка ValueError.

        Також конвертує стовпець 'Date' в тип datetime, з обробкою помилок при конвертації.

        Повертає:
        --------
        pandas.DataFrame
            Завантажені та перевірені дані, або порожній DataFrame у разі помилки.
        """
        try:
            data = pd.read_csv(self.file_path)

            required_columns = {'Date', 'Temperature', 'Humidity', 'WindSpeed', 'Rainfall'}
            if not required_columns.issubset(data.columns):
                raise ValueError(f"CSV файл повинен містити колонки: {', '.join(required_columns)}")

            data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
            return data
        except FileNotFoundError:
            print(f"Файл {self.file_path} не знайдено.")
            return pd.DataFrame()
