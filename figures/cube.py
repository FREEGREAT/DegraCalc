from figures.figure import Figure
from utils.color import Color  # Import the Color class
from figures.figure import Figure

class Cube(Figure):
    def __init__(self, width: int, height: int, color: str):
        super().__init__(size=width, color=color)
        self.height = height

    def render(self):
        # Top part of the cube
        top = f"""
          {self.color}Cube (Width: {self.size}, Height: {self.height}){Color.COLORS['reset']}

           +{'-' * self.size}+
          /{' ' * self.size}/|
         /{' ' * self.size}/ |
        +{'-' * self.size}+  +
        """

        # Create the vertical height representation for all sides
        vertical_height = ""
        for _ in range(self.height):
            vertical_height += f"         |{' ' * self.size}|\n"

        # Bottom part of the cube with vertical lines
        bottom = f"""
        |{' ' * self.size}|  |
        |{' ' * self.size}|  |
        |{' ' * self.size}| /
        |{' ' * self.size}|/
        +{'-' * self.size}+
        """

        # Print the top part
        print(top)
        
        # Print the vertical height for left and right sides
        print(vertical_height.strip())
        
        # Print the bottom part
        print(bottom)

