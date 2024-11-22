import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../lab2/classes')))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../lab2/functions"))
from calculator import Calculator, Memory
from ConvertNumberType import ConvertNumberType

class TestCalculator(unittest.TestCase):
    """
    Модуль тестування калькулятора

    Призначення:
        Цей модуль містить набір юніт-тестів для перевірки функціональності 
        класів `Calculator` та `Memory`, 
        а також функції `ConvertNumberType`. Використовується бібліотека `unittest`.

    Тестовані класи:
        - `Calculator`: Тести основних арифметичних операцій 
        (додавання, віднімання, множення, ділення).
        - `Memory`: Тести роботи з пам'яттю (додавання, віднімання, 
        очищення, читання пам'яті).
        - `ConvertNumberType`: Тест обробки некоректних даних.

    Тести:
        - Додавання:
            - test_addition_positive_numbers: Додавання двох додатних чисел.
            - test_addition_negative_numbers: Додавання двох від'ємних чисел.
            - test_addition_positive_and_negative: Додавання додатного і від'ємного числа.
        - Віднімання:
            - test_subtraction_positive_numbers: Віднімання двох додатних чисел.
            - test_subtraction_negative_result: Отримання від'ємного результату.
        - Множення:
            - test_multiplication_with_zero: Множення числа на нуль.
            - test_multiplication_positive_numbers: Множення двох додатних чисел.
            - test_multiplication_negative_numbers: Множення двох від'ємних чисел.
        - Ділення:
            - test_division_positive_numbers: Ділення двох додатних чисел.
            - test_division_with_zero: Перевірка ділення на нуль.
            - test_division_negative_result: Ділення додатного і від'ємного чисел.
            - test_division_by_zero_error_handling: Перевірка обробки помилки ділення на нуль.
        - Перетворення типів:
            - test_invalid_number_conversion: Перевірка некоректного вводу при перетворенні типів.
        - Історія обчислень:
            - test_get_history: Перевірка запису обчислень у файл історії.
        - Пам'ять:
            - test_memory_add: Перевірка додавання значення до пам'яті.
            - test_memory_subtract: Перевірка віднімання значення з пам'яті.
            - test_memory_clear: Перевірка очищення пам'яті.

    Кастомізація виводу:
        - Класи `CustomTextTestResult` і `CustomTextTestRunner` змінюють 
        стандартний вивід результатів тестування, 
        додаючи спеціальні повідомлення про успішні тести, помилки або збої.

    Запуск:
        - Запустіть файл для виконання тестів, використовуючи кастомний 
        тестовий раннер із підвищеною інформативністю.
        - Результати тестування будуть відображені в консолі.
    Приклад:
        $ python test_calculator.py
    """


    def setUp(self):
        self.calculator = Calculator()
        self.memory = Memory()

    def test_addition_positive_numbers(self):
        self.assertEqual(self.calculator.Add(3, 5), 8)
    
    def test_addition_negative_numbers(self):
        self.assertEqual(self.calculator.Add(-3, -5), -8)
    
    def test_addition_positive_and_negative(self):
        self.assertEqual(self.calculator.Add(-3, 5), 2)

    def test_subtraction_positive_numbers(self):
        self.assertEqual(self.calculator.Subtract(10, 5), 5)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calculator.Subtract(5, 10), -5)

    def test_multiplication_with_zero(self):
        self.assertEqual(self.calculator.Multiply(5, 0), 0)

    def test_multiplication_positive_numbers(self):
        self.assertEqual(self.calculator.Multiply(3, 5), 15)
    
    def test_multiplication_negative_numbers(self):
        self.assertEqual(self.calculator.Multiply(-3, -5), 15)

    def test_division_positive_numbers(self):
        self.assertEqual(self.calculator.Divide(10, 2), 5)

    def test_division_with_zero(self):
        self.assertEqual(self.calculator.Divide(10, 0), "Error: x/0")
    
    def test_division_negative_result(self):
        self.assertEqual(self.calculator.Divide(-10, 2), -5)

    def test_division_by_zero_error_handling(self):
        self.assertEqual(self.calculator.Divide(5, 0), "Error: x/0")

    def test_invalid_number_conversion(self):
        with self.assertRaises(ValueError):
            ConvertNumberType("invalid")

    def test_get_history(self):
        self.calculator.Add(1, 1)
        with open("History.txt", "r") as file:
            self.assertIn("1 + 1 = 2", file.read())
    
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
