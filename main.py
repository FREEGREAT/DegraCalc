# main.py
from api.api_client import APIClient
from api.repository import DataRepository
from core.transaction import Transactions
from ui.user_interface import UserInterface
from core.error_handler import ErrorHandler

def main():
    try:
        api_client = APIClient("https://jsonplaceholder.typicode.com")
        repository = DataRepository(api_client)
        transactions = Transactions()
        ui = UserInterface(repository, transactions)
        
        ui.start()
        transactions.save_history()
    except Exception as e:
        ErrorHandler.handle_error(e)

if __name__ == "__main__":
    main()
