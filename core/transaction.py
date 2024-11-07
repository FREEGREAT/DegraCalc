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

    def save_history(self, filename="logs/history.log"):
        with open(filename, "a") as file:
            for entry in self.history:
                file.write(f"{entry['timestamp']} - Query: {entry['query']}, Result: {entry['result']}\n")
        self.history.clear()
