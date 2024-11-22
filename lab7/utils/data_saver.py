"""
Клас для збереження даних у різних форматах 
(JSON, CSV, TXT).
"""
import os
import json
import csv

class DataSaver:
    """
    Клас для збереження даних у різних форматах 
    (JSON, CSV, TXT).
    Цей клас забезпечує функціональність для збереження 
    даних у файли різних форматів.
    Збереження відбувається в папку "results/lab7" (за замовчуванням), 
    або вказану користувачем підкаталог.
    Методи:
    --------
    save_to_json(data, filename="data.json") :
        Зберігає дані в форматі JSON.
    save_to_csv(data, filename="data.csv") :
        Зберігає дані в форматі CSV.
    save_to_txt(data, filename="data.txt") :
        Зберігає дані в текстовому форматі.
    """
    @staticmethod
    def _get_save_path(filename, subdir="results/lab7"):
        """
        Генерує повний шлях до файлу в заданій підпапці.
        Параметри:
        -----------
        filename : str
            Ім'я файлу для збереження.
        subdir : str
            Відносний шлях до папки для збереження файлів. 
            За замовчуванням це "results/lab7".
        Повертає:
        --------
        str
            Повний шлях до файлу.
        """
        directory = os.path.abspath(subdir)
        if not os.path.exists(directory):
            os.makedirs(directory)
        return os.path.join(directory, filename)

    @staticmethod
    def save_to_json(data, filename="data.json"):
        """
        Зберігає дані в форматі JSON.
        Параметри:
        -----------
        data : dict or list
            Дані для збереження.
        filename : str, optional
            Ім'я файлу для збереження даних. 
            За замовчуванням "data.json".
        Виводить:
        ---------
        str
            Повідомлення про успішне збереження файлу.
        """
        filepath = DataSaver._get_save_path(filename)
        with open(filepath, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {filepath}")

    @staticmethod
    def save_to_csv(data, filename="data.csv"):
        """
        Зберігає дані в форматі CSV.
        Параметри:
        -----------
        data : list of dict
            Дані для збереження, де кожен 
            елемент списку є словником.
        filename : str, optional
            Ім'я файлу для збереження даних. 
            За замовчуванням "data.csv".
        Виводить:
        ---------
        str
            Повідомлення про успішне збереження файлу, 
            або попередження, якщо дані відсутні.
        """
        if not data:
            print("No data to save")
            return

        filepath = DataSaver._get_save_path(filename)
        with open(filepath, "w", newline='', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0].keys())  # headers
            for row in data:
                writer.writerow(row.values())
        print(f"Data saved to {filepath}")

    @staticmethod
    def save_to_txt(data, filename="data.txt"):
        """
        Зберігає дані в текстовому форматі.
        Параметри:
        -----------
        data : list
            Дані для збереження у
            вигляді списку рядків.
        filename : str, optional
            Ім'я файлу для збереження даних. 
            За замовчуванням "data.txt".
        Виводить:
        ---------
        str
            Повідомлення про успішне збереження файлу.
        """
        filepath = DataSaver._get_save_path(filename)
        with open(filepath, "w", encoding="utf-8") as txt_file:
            for row in data:
                txt_file.write(f"{row}\n")
        print(f"Data saved to {filepath}")
