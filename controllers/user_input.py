import json

class UserInput:
    def __init__(self, cube):
        self.cube = cube
        self.colors = {
            "1": "Red",
            "2": "Green",
            "3": "Blue",
            "4": "Yellow",
            "5": "Cyan",
            "6": "Magenta",
            "7": "White",
            "8": "Black",
            "9": "Gray",
            "10": "Orange"
        }

    def get_next_action(self):
        print("\nWhat do you want to do next?")
        print("1 - Rotate")
        print("2 - Change Color")
        print("3 - Scale")
        print("4 - Save to File")
        print("5 - Exit")
        choice = input("Your choice: ")
        return choice

    def get_rotation_input(self):
        try:
            angle_x = float(input("Enter X rotation angle: "))
            angle_y = float(input("Enter Y rotation angle: "))
            self.cube.set_rotation(angle_x, angle_y)
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    def get_scale_input(self):
        try:
            scale = float(input("Enter scale factor (e.g., 1 for no scaling, 2 to double size, 0.5 to reduce size): "))
            if scale > 0:
                self.cube.set_scale(scale)
            else:
                print("Scale factor must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    def get_initial_size(self):
        try:
            size_x = float(input("Enter the cube size along X-axis: "))
            size_y = float(input("Enter the cube size along Y-axis: "))
            size_z = float(input("Enter the cube size along Z-axis: "))
            return size_x, size_y, size_z
        except ValueError:
            print("Invalid input. Default size 10x10x10 will be used.")
            return 10, 10, 10

    def change_color(self):
        print("Available colors: ")
        for key, color in self.colors.items():
            print(f"{key}: {color}")
        
        choice = input("Choose a color by entering a number: ")
        if choice in self.colors:
            self.cube.color = self.colors[choice]
            print(f"Color changed to {self.colors[choice]}")
        else:
            print("Invalid choice. Default color remains.")
    
    def save_colors_to_json(self, filename="colors.json"):
        with open(filename, 'w') as f:
            json.dump(self.colors, f)
        print(f"Colors saved to {filename}.txt")
