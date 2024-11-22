from figures.figure import Figure
from utils.color import Color  # Імпортуємо клас Color
from figures.figure import Figure

class Cube(Figure):
    """
    Клас для створення куба з можливістю налаштування ширини, висоти та кольору.

    Наслідує:
        Figure: Базовий клас для геометричних фігур.

    Атрибути:
        size (int): Ширина куба (успадкований від Figure).
        height (int): Висота куба.
        color (str): Колір куба (успадкований від Figure).

    Методи:
        render(): Відображає куб у вигляді текстової візуалізації.
    """

    def __init__(self, width: int, height: int, color: str):
        """
        Ініціалізує об'єкт класу Cube.

        Параметри:
            width (int): Ширина куба.
            height (int): Висота куба.
            color (str): Назва кольору, який буде конвертовано у формат за допомогою класу Color.
        """
        super().__init__(size=width, color=color)
        self.height = height

    def render(self):
        """
        Відображає куб у вигляді текстової візуалізації.

        Створює тривимірний вигляд куба за допомогою символів ASCII.
        """
        # Верхня частина куба
        top = f"""
          {self.color}Cube (Width: {self.size}, Height: {self.height}){Color.COLORS['reset']}

           +{'-' * self.size}+
          /{' ' * self.size}/|
         /{' ' * self.size}/ |
        +{'-' * self.size}+  +
        """

        # Вертикальна частина куба
        vertical_height = ""
        for _ in range(self.height):
            vertical_height += f"         |{' ' * self.size}|\n"

        # Нижня частина куба
        bottom = f"""
        |{' ' * self.size}|  |
        |{' ' * self.size}|  |
        |{' ' * self.size}| /
        |{' ' * self.size}|/
        +{'-' * self.size}+
        """

        # Друк верхньої частини
        print(top)
        
        # Друк вертикальної частини
        print(vertical_height.strip())
        
        # Друк нижньої частини
        print(bottom)
