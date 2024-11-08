# core/transaction.py
from datetime import datetime

class Transactions:
    def __init__(self):
        self.history = []

    def register_request(self, query, result):
        self.history.append({
            "query": query,
            "result": result,
            "timestamp": datetime.now().isoformat()
        })

    def log_save_action(self, phone, format, filename):
        """Log the saving action to a file with details."""
        entry = {
            "action": "save",
            "phone": phone,
            "format": format,
            "filename": filename,
            "timestamp": datetime.now().isoformat()
        }
        self.history.append(entry)
        self._write_log(entry)

    def _write_log(self, entry, filename="logs/history.log"):
        with open(filename, "a") as file:
            if "action" in entry:
                file.write(f"{entry['timestamp']} - Action: {entry['action']}, Phone: {entry['phone']}, Format: {entry['format']}, Filename: {entry['filename']}\n")
            else:
                file.write(f"{entry['timestamp']} - Query: {entry['query']}, Result Count: {len(entry['result'])}\n")

    def save_history(self, filename="logs/history.log"):
        with open(filename, "a") as file:
            for entry in self.history:
                self._write_log(entry, filename)
        self.history.clear()
