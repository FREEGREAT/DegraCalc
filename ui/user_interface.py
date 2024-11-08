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
        try:
            query = input("Enter a resource name (e.g., 'posts') or type a phone number: ")

            if query in ["posts", "comments", "albums", "photos", "todos", "users"]:
                data = self.repository.fetch_data(query)
                if data:
                    self.view.display_data(data)
                    self.transactions.register_request(query, data)
                    self.save_data(data)
            else:
                # Перевірка, чи введення є телефоном або датою
                try:
                    if UserInputParser.parse_phone(query):  # Перевірка введення як номер телефону
                        data = self.repository.fetch_data("users")  # Завантажуємо всіх користувачів
                        user = self.repository.find_user_by_phone(query, data)
                        if user:
                            self.view.display_data([user])
                            self.transactions.register_request(query, [user])
                            self.save_data([user], phone=query)  # Передаємо телефон для логування
                        else:
                            print("No user found with this phone number.")
                    elif UserInputParser.parse_date(query):  # Перевірка введення як дату
                        date = UserInputParser.parse_date(query)
                        print(f"Parsed Date: {date}")
                    else:
                        raise UserInputError("Invalid input format. Please enter a valid resource name, date, or phone number.")
                
                except UserInputError as e:
                    ErrorHandler.handle_error(e)
                    print("Invalid input. Please try again with a valid format.")

        except Exception as e:
            ErrorHandler.handle_error(e)

    def save_data(self, data, phone=None):
        try:
            format_choice = input("Choose a format to save data (json, csv, txt): ").strip().lower()
            
            if format_choice not in ["json", "csv", "txt"]:
                raise ValueError("Invalid choice. Data was not saved.")

            # Виконання збереження та отримання імені файлу
            filename = None
            if format_choice == "json":
                filename = DataSaver.save_to_json(data)
            elif format_choice == "csv":
                filename = DataSaver.save_to_csv(data)
            elif format_choice == "txt":
                filename = DataSaver.save_to_txt(data)
            
            if filename and phone:  # Логування збереження за номером телефону
                self.transactions.log_save_action(phone, format_choice, filename)
        
        except ValueError as e:
            print(e)
        except (IOError, OSError) as e:
            print("An error occurred while saving the file. Please try again.")
            ErrorHandler.handle_error(e)
