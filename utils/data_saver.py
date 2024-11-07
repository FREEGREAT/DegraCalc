# utils/data_saver.py
import json
import csv

class DataSaver:
    @staticmethod
    def save_to_json(data, filename="data.json"):
        with open(filename, "w") as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {filename}")

    @staticmethod
    def save_to_csv(data, filename="data.csv"):
        if not data:
            print("No data to save")
            return
        
        with open(filename, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0].keys())  # headers
            for row in data:
                writer.writerow(row.values())
        print(f"Data saved to {filename}")

    @staticmethod
    def save_to_txt(data, filename="data.txt"):
        with open(filename, "w") as txt_file:
            for row in data:
                txt_file.write(f"{row}\n")
        print(f"Data saved to {filename}")
