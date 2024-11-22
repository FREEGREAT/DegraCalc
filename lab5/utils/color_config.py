class ColorConfig:
    COLORS = {
        "Red": "\033[31m",
        "Green": "\033[32m",
        "Blue": "\033[34m",
        "Yellow": "\033[33m",
        "Cyan": "\033[36m",
        "Magenta": "\033[35m",
        "White": "\033[37m",
        "Black": "\033[30m",
        "Gray": "\033[90m",
        "Orange": "\033[38;5;214m",
        "Reset": "\033[0m"
    }

    @staticmethod
    def get_color_code(color_name):
        return ColorConfig.COLORS.get(color_name, ColorConfig.COLORS["White"])
