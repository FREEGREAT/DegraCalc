# core/user_input_parser.py
import re
from core.error_handler import UserInputError

class UserInputParser:
    DATE_PATTERN = r"\b\d{4}-\d{2}-\d{2}\b"  # YYYY-MM-DD
    PHONE_PATTERN = r"\b\+?\d{1,3}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b"

    @staticmethod
    def parse_date(input_string):
        match = re.search(UserInputParser.DATE_PATTERN, input_string)
        if match:
            return match.group()
        raise UserInputError("Invalid date format. Please use YYYY-MM-DD.")

    @staticmethod
    def parse_phone(input_string):
        match = re.search(UserInputParser.PHONE_PATTERN, input_string)
        if match:
            return match.group()
        raise UserInputError("Invalid phone number format.")
