def GetOperator():
    while True:
        operator = input("Select operation ( + | - | * | / | √ (= sqrt) | % | ** (= ^) ): ").lower()
        try:
            if operator not in ["+", "-", "*", "/", "√", "sqrt", "%", "**"]:
                raise ValueError("Invalid operator")
            return operator
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid operator.")

def GetNumber():
    while True:
        num = input("Введіть число:")
        try:
            if num == "":
                raise ValueError("Field cannot be empty. Please enter a valid number.")
            return num
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")
            