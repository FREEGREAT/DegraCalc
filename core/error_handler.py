# core/error_handler.py

class APIError(Exception):
    """Exception raised for errors in API requests."""
    def __init__(self, message="An error occurred while accessing the API"):
        self.message = message
        super().__init__(self.message)


class UserInputError(Exception):
    """Exception raised for invalid user input."""
    def __init__(self, message="Invalid user input"):
        self.message = message
        super().__init__(self.message)


class ErrorHandler:
    @staticmethod
    def handle_error(error):
        """Logs and displays the error message."""
        print(f"Error: {error}")
