import math

class Calculator:
    """
    Клас Calculator для виконання базових математичних операцій, збереження результатів у пам'яті 
    та ведення історії обчислень.
    """

    def __init__(self):
        """
        Ініціалізує об'єкт калькулятора з початковими значеннями:
        - `a` та `b` (аргументи операцій) встановлені в 0.
        - `memory` (пам'ять) встановлена в 0.
        - `history` (історія операцій) ініціалізується як порожній список.
        """
        self.a = 0
        self.b = 0
        self.memory = 0
        self.history = []

    def Add(self, a, b):
        """
        Додає два числа.

        Args:
            a (float): Перше число.
            b (float): Друге число.

        Returns:
            float: Результат додавання.
        """
        result = a + b
        self.history.append(result)
        return result

    def Mul(self, a, b):
        """
        Множить два числа.

        Args:
            a (float): Перше число.
            b (float): Друге число.

        Returns:
            float: Результат множення.
        """
        result = a * b
        self.history.append(result)
        return result

    def Div(self, a, b):
        """
        Ділить два числа.

        Args:
            a (float): Ділене.
            b (float): Дільник.

        Returns:
            float: Результат ділення.

        Raises:
            ZeroDivisionError: Якщо дільник дорівнює нулю.
        """
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль заборонено.")
        result = a / b
        self.history.append(result)
        return result

    def Minus(self, a, b):
        """
        Віднімає друге число від першого.

        Args:
            a (float): Перше число.
            b (float): Друге число.

        Returns:
            float: Результат віднімання.
        """
        result = a - b
        self.history.append(result)
        return result

    def Mod(self, a, b):
        """
        Обчислює залишок від ділення.

        Args:
            a (int): Ділене.
            b (int): Дільник.

        Returns:
            int: Залишок від ділення.
        """
        result = a % b
        self.history.append(result)
        return result

    def Sqrt(self, number):
        """
        Обчислює квадратний корінь числа.

        Args:
            number (float): Число, для якого потрібно обчислити квадратний корінь.

        Returns:
            float: Квадратний корінь числа.

        Raises:
            ValueError: Якщо число від'ємне.
        """
        if number < 0:
            raise ValueError("Квадратний корінь від від'ємного числа не визначений.")
        return math.sqrt(number)

    def Exponentiation(self, a, b):
        """
        Підносить число `a` до степеня `b`.

        Args:
            a (float): Основа.
            b (float): Степінь.

        Returns:
            float: Результат піднесення до степеня.
        """
        result = a ** b
        self.history.append(result)
        return result

    def MemorySave(self, result):
        """
        Зберігає результат у пам'яті.

        Args:
            result (float): Значення для збереження в пам'яті.
        """
        self.memory = result

    def MemoryAdd(self, result):
        """
        Додає значення до пам'яті.

        Args:
            result (float): Значення для додавання до пам'яті.
        """
        self.memory += result

    def MemorySub(self, result):
        """
        Віднімає значення від пам'яті.

        Args:
            result (float): Значення для віднімання від пам'яті.
        """
        self.memory -= result

    def MemoryClear(self):
        """
        Очищає пам'ять, встановлюючи її значення в 0.
        """
        self.memory = 0

    def MemoryRead(self):
        """
        Зчитує поточне значення пам'яті.

        Returns:
            float: Значення, збережене в пам'яті.
        """
        return self.memory

    def GetHistory(self):
        """
        Повертає історію всіх операцій.

        Returns:
            list: Список результатів операцій.
        """
        return self.history
