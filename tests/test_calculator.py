import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions"))

from calculator import Calculator, Memory
from ConvertNumberType import ConvertNumberType
from ErrorHandler import *

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.memory = Memory()

    # Завдання 1: Тестування Додавання
    def test_addition_positive_numbers(self):
        self.assertEqual(self.calculator.Add(3, 5), 8)
    
    def test_addition_negative_numbers(self):
        self.assertEqual(self.calculator.Add(-3, -5), -8)
    
    def test_addition_positive_and_negative(self):
        self.assertEqual(self.calculator.Add(-3, 5), 2)

    # Завдання 2: Тестування Віднімання
    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calculator.Subtract(10, 5), 5)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calculator.Subtract(5, 10), -5)

    # Завдання 3: Тестування Множення
    def test_multiplication_with_zero(self):
        self.assertEqual(self.calculator.Multiply(5, 0), 0)

    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calculator.Multiply(3, 5), 15)
    
    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calculator.Multiply(-3, -5), 15)

    # Завдання 4: Тестування Ділення
    def test_division_positive_numbers(self):
        self.assertEqual(self.calculator.Divide(10, 2), 5)

    def test_division_with_zero(self):
        self.assertEqual(self.calculator.Divide(10, 0), "Error: x/0")
    
    def test_division_negative_result(self):
        self.assertEqual(self.calculator.Divide(-10, 2), -5)

    # Завдання 5: Тестування Обробки Помилок
    def test_division_by_zero_error_handling(self):
        self.assertEqual(self.calculator.Divide(5, 0), "Error: x/0")

    def test_invalid_number_conversion(self):
        with self.assertRaises(ValueError):
            ConvertNumberType("invalid")

    # Тестування функцій історії
    def test_get_history(self):
        # Adding an entry to history
        self.calculator.Add(1, 1)
        with open("History.txt", "r") as file:
            self.assertIn("1 + 1 = 2", file.read())

    # Тести для Memory класу
    def test_memory_add(self):
        self.memory.Add(10)
        self.assertEqual(self.memory.Read(), 10)

    def test_memory_subtract(self):
        self.memory.Add(10)
        self.memory.Subtract(5)
        self.assertEqual(self.memory.Read(), 5)

    def test_memory_clear(self):
        self.memory.Add(10)
        self.memory.Clear()
        self.assertEqual(self.memory.Read(), 0)

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"✔️ Test '{test}' passed successfully.")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"❌ Test '{test}' failed. Error: {err}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"⚠️ Test '{test}' encountered an error. Error: {err}")

class CustomTextTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTextTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == '__main__':
    runner = CustomTextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)
