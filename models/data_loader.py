import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
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
