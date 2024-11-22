class UserInput:
    """
    Клас UserInput

    Призначення:
        Забезпечує взаємодію з користувачем для налаштування параметрів куба, таких як обертання, масштабування, колір, 
        початковий розмір і збереження у файл.

    Атрибути:
        cube (Cube): Об'єкт куба, з яким взаємодіє користувач.
        colors (dict): Словник доступних кольорів із ключами (номерами) та значеннями (назвами кольорів).

    Методи:
        get_next_action():
            Запитує у користувача наступну дію.

            Повертає:
                str: Вибір користувача (номер опції).

        get_rotation_input():
            Запитує у користувача кути обертання по осях X та Y і встановлює їх для куба.

        get_scale_input():
            Запитує у користувача коефіцієнт масштабування та встановлює його для куба.

        get_initial_size():
            Запитує у користувача початкові розміри куба по осях X, Y і Z.

            Повертає:
                tuple[float, float, float]: Початкові розміри куба (size_x, size_y, size_z).

        change_color():
            Дозволяє користувачеві змінити колір куба, вибравши його зі списку доступних кольорів.

    Обробка виключень:
        Усі методи обробляють можливі помилки, наприклад, некоректний ввід або проблеми під час виконання операцій, 
        і повертають відповідні повідомлення.

    Приклад використання:
        user_input = UserInput(cube)
        action = user_input.get_next_action()

        if action == "1":
            user_input.get_rotation_input()
        elif action == "2":
            user_input.change_color()
        elif action == "3":
            user_input.get_scale_input()
    """

    def __init__(self, cube):
        self.cube = cube
        self.colors = {"1": "Red", "2": "Green", "3": "Blue", "4": "Yellow", "5": "Cyan", 
            "6": "Magenta", "7": "White", "8": "Black", "9": "Gray", "10": "Orange"
        }

    def get_next_action(self):
        try:
            print("\nWhat do you want to do next?\n1 - Rotate\n2 - Change Color\n3 - Scale\n4 - Save to File\n5 - Exit")
            choice = input("Your choice: ")
            return choice
        except Exception as e:
            print(f"Error getting action input: {e}")
            return None

    def get_rotation_input(self):
        try:
            angle_x = float(input("Enter X rotation angle (between -360 and 360): "))
            angle_y = float(input("Enter Y rotation angle (between -360 and 360): "))
            self.cube.set_rotation(angle_x, angle_y)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error in rotation input: {e}")

    def get_scale_input(self):
        try:
            scale = float(input("Enter scale factor (between 1 and 100): "))
            if scale > 0:
                self.cube.set_scale(scale)
            else:
                print("Scale factor must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Error in scale input: {e}")

    def get_initial_size(self):
        try:
            size_x = float(input("Enter the cube size along X-axis (between 1 and 13): "))
            size_y = float(input("Enter the cube size along Y-axis (between 1 and 13): "))
            size_z = float(input("Enter the cube size along Z-axis (between 1 and 13): "))
            # Limit size between 1 and 100
            size_x = max(1, min(13, size_x))
            size_y = max(1, min(13, size_y))
            size_z = max(1, min(13, size_z))
            return size_x, size_y, size_z
        except ValueError:
            print("Invalid input. Default size 10x10x10 will be used.")
            return 10, 10, 10
        except Exception as e:
            print(f"Error getting initial size: {e}")
            return 10, 10, 10

    def change_color(self):
        try:
            print("Available colors: ")
            for key, color in self.colors.items():
                print(f"{key}: {color}")

            choice = input("Choose a color by entering a number: ")
            if choice in self.colors:
                self.cube.color = self.colors[choice]
                print(f"Color changed to {self.colors[choice]}")
            else:
                print("Invalid choice. Default color remains.")
        except Exception as e:
            print(f"Error changing color: {e}")
