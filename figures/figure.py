from utils.color import Color  # Import the Color class

class Figure:
    def __init__(self, size: int, color: str):
        self.size = size
        self.color = Color.get_color(color)  # Use the Color class to get the color

    def render(self):
        raise NotImplementedError("Render method must be implemented by subclasses.")