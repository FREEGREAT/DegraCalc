# tests/test_app.py
import unittest
import sys,os
from unittest.mock import patch, Mock, MagicMock
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.user_input_parser import UserInputParser, UserInputError
from utils.data_saver import DataSaver
from core.transaction import Transactions
from ui.user_interface import UserInterface
from api.repository import DataRepository
from ui.console_view import ConsoleView

class TestUserInputParser(unittest.TestCase):
    def test_parse_date_valid(self):
        date = UserInputParser.parse_date("2024-11-07")
        self.assertEqual(date, "2024-11-07")

    def test_parse_date_invalid(self):
        with self.assertRaises(UserInputError):
            UserInputParser.parse_date("07-11-2024")

    def test_parse_phone_valid(self):
        phone = UserInputParser.parse_phone("1-770-736-8031 x56442")
        self.assertEqual(phone, "1-770-736-8031 x56442")

    def test_parse_phone_invalid(self):
        with self.assertRaises(UserInputError):
            UserInputParser.parse_phone("not-a-phone-number")

class TestDataSaver(unittest.TestCase):
    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_save_to_json(self, mock_open):
        data = [{"key": "value"}]
        filename = DataSaver.save_to_json(data)
        self.assertTrue(filename.startswith("data_"))
        self.assertTrue(filename.endswith(".json"))
        mock_open.assert_called_once_with(filename, "w")

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_save_to_csv(self, mock_open):
        data = [{"key": "value"}]
        filename = DataSaver.save_to_csv(data)
        self.assertTrue(filename.startswith("data_"))
        self.assertTrue(filename.endswith(".csv"))
        mock_open.assert_called_once_with(filename, "w", newline='')

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_save_to_txt(self, mock_open):
        data = [{"key": "value"}]
        filename = DataSaver.save_to_txt(data)
        self.assertTrue(filename.startswith("data_"))
        self.assertTrue(filename.endswith(".txt"))
        mock_open.assert_called_once_with(filename, "w")

class TestTransactions(unittest.TestCase):
    def setUp(self):
        self.transactions = Transactions()

    def test_register_request(self):
        self.transactions.register_request("posts", [{"id": 1, "title": "Title"}])
        self.assertEqual(len(self.transactions.history), 1)
        self.assertEqual(self.transactions.history[0]["query"], "posts")

    @patch("builtins.open", new_callable=unittest.mock.mock_open)
    def test_log_save_action(self, mock_open):
        self.transactions.log_save_action("1-770-736-8031 x56442", "json", "data_20241107_121212.json")
        self.assertEqual(len(self.transactions.history), 1)
        self.assertEqual(self.transactions.history[0]["format"], "json")
        mock_open.assert_called_once()

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.repository = MagicMock(spec=DataRepository)
        self.transactions = MagicMock(spec=Transactions)
        self.console_view = MagicMock(spec=ConsoleView)
        self.interface = UserInterface(self.repository, self.transactions)
        self.interface.view = self.console_view  

    @patch("builtins.input", side_effect=["posts"])
    def test_start_with_resource(self, mock_input):
        self.repository.fetch_data.return_value = [{"id": 1, "title": "Test Post"}]
        self.interface.start()
        self.repository.fetch_data.assert_called_once_with("posts")
        self.console_view.display_data.assert_called_once()

    @patch("builtins.input", side_effect=["1-770-736-8031 x56442"])
    def test_start_with_phone_number(self, mock_input):
        self.repository.fetch_data.return_value = [
            {"id": 1, "name": "User", "phone": "1-770-736-8031 x56442"}
        ]
        self.interface.start()
        self.repository.fetch_data.assert_called_once_with("users")
        self.console_view.display_data.assert_called_once()

    @patch("builtins.input", side_effect=["json"])
    @patch("utils.data_saver.DataSaver.save_to_json", return_value="data_20241107_121212.json")
    def test_save_data_json(self, mock_save, mock_input):
        data = [{"id": 1, "title": "Test Post"}]
        self.interface.save_data(data, phone="1-770-736-8031 x56442")
        mock_save.assert_called_once_with(data)
        self.transactions.log_save_action.assert_called_once_with("1-770-736-8031 x56442", "json", "data_20241107_121212.json")

if __name__ == "__main__":
    unittest.main()