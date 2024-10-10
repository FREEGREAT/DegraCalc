import math

class Calculator:

    def Save(self, value):
        with open('History.txt', 'a') as file:
            file.write(f"{value}\n")

    def Add(self, a, b):
        result = a + b
        self.Save(f"{a} + {b} = {result}")
        return result

    def Subtract(self, a, b):
        result = a - b
        self.Save(f"{a} - {b} = {result}")
        return result

    def Multiply(self, a, b):
        result = a * b
        self.Save(f"{a} * {b} = {result}")
        return result

    def Divide(self, a, b):
        if b == 0:
            self.Save(f"{a} / {b} = Error: x/0")
            return "Error: x/0"
        else:
            result = a / b
            self.Save(f"{a} / {b} = {result}")
            return result

    def Mod(self, a, b):
        result = a % b
        self.Save(f"{a} % {b} = {result}")
        return result

    def SquareRoot(self, number):
        result = math.sqrt(number)
        self.Save(f"Square root of {number} = {result}")
        return result

    def Exponentiate(self, a, b):
        result = a ** b
        self.Save(f"{a}^{b} = {result}")
        return result

    def GetHistory(self):
        with open("History.txt", "r") as file:
            return print(file.read())


class Memory(Calculator):
    def __init__(self):
        super().__init__()
        self.value = 0

    def Add(self,value):
        self.value += value
        self.Save(f"Memory added: {self.value}")
        return self.value

    def Subtract(self,value):
        self.value -= value
        self.Save(f"Memory subtracted: {self.value}")
        return self.value

    def Clear(self):
        self.value = 0
        self.Save("Memory cleared")
        return self.value

    def Read(self):
    	return self.value
     
