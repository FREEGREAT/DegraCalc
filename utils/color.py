class Color:
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }

    @staticmethod
    def get_color(color_name: str) -> str:
        return Color.COLORS.get(color_name, Color.COLORS['reset'])