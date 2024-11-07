# ui/user_interface.py
from ui.console_view import ConsoleView
from api.repository import DataRepository
from core.transaction import Transactions
from core.user_input_parser import UserInputParser
from core.error_handler import ErrorHandler, APIError, UserInputError
from utils.data_saver import DataSaver

class UserInterface:
    def __init__(self, repository, transactions):
        self.repository = repository
        self.transactions = transactions
        self.view = ConsoleView()

    def start(self):
        print("Available resources: /posts, /comments, /albums, /photos, /todos, /users")
        query = input("Enter a resource name (e.g., 'posts') or type a date/phone number: ")

        try:
            if query in ["posts", "comments", "albums", "photos", "todos", "users"]:
                data = self.repository.fetch_data(query)
                if data:
                    self.view.display_data(data)
                    self.transactions.register_request(query, data)
                    self.save_data(data)
            elif UserInputParser.parse_phone(query):  # Перевірка введення як номер телефону
                data = self.repository.fetch_data("users")  # Завантажуємо всіх користувачів
                user = self.repository.find_user_by_phone(query, data)
                if user:
                    self.view.display_data([user])
                    self.transactions.register_request(query, [user])
                    self.save_data(user)
                else:
                    print("No user found with this phone number.")
            elif "date" in query:
                date = UserInputParser.parse_date(query)
                print(f"Parsed Date: {date}")
            else:
                raise UserInputError("Invalid input. Please enter a valid resource name or format.")
        except UserInputError as e:
            ErrorHandler.handle_error(e)
        except APIError as e:
            ErrorHandler.handle_error(e)
        except Exception as e:
            ErrorHandler.handle_error(e)

    def save_data(self, data):
        format_choice = input("Choose a format to save data (json, csv, txt): ").strip().lower()
        if format_choice == "json":
            DataSaver.save_to_json(data)
        elif format_choice == "csv":
            DataSaver.save_to_csv(data)
        elif format_choice == "txt":
            DataSaver.save_to_txt(data)
        else:
            print("Invalid choice. Data was not saved.")
