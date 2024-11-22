class Color:
    COLORS = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'reset': '\033[0m'
    }

    @staticmethod
    def apply_color(text, color):
        if color not in Color.COLORS:
            raise ValueError(f"Недоступний колір: {color}. Доступні кольори: {', '.join(Color.COLORS.keys())}")
        return f"{Color.COLORS[color]}{text}{Color.COLORS['reset']}"
