# utils/data_saver.py
import json
import csv
from datetime import datetime

class DataSaver:
    @staticmethod
    def _generate_filename(extension):
        """Генерує унікальну назву файлу з поточною датою і часом."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"data_{timestamp}.{extension}"

    @staticmethod
    def save_to_json(data):
        filename = DataSaver._generate_filename("json")
        try:
            with open(filename, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Data saved to {filename}")
            return filename
        except (IOError, OSError) as e:
            print("Failed to save data to JSON file.")
            raise e

    @staticmethod
    def save_to_csv(data):
        filename = DataSaver._generate_filename("csv")
        if not data:
            print("No data to save")
            return None
        
        try:
            with open(filename, "w", newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(data[0].keys())  # headers
                for row in data:
                    writer.writerow(row.values())
            print(f"Data saved to {filename}")
            return filename
        except (IOError, OSError) as e:
            print("Failed to save data to CSV file.")
            raise e

    @staticmethod
    def save_to_txt(data):
        filename = DataSaver._generate_filename("txt")
        try:
            with open(filename, "w") as txt_file:
                for row in data:
                    txt_file.write(f"{row}\n")
            print(f"Data saved to {filename}")
            return filename
        except (IOError, OSError) as e:
            print("Failed to save data to TXT file.")
            raise e
