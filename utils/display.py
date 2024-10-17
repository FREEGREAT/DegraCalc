import shutil
from utils.clear import clear_console

def display_ascii_art(art, color="bw", symbol="@", alignment="left"):
    try:
        clear_console()
        
        # Отримання розміру терміналу
        terminal_size = shutil.get_terminal_size()
        terminal_width = terminal_size.columns
        
        # Додавання кольору
        if color == "purple":
            color_code = '\033[35m'
        elif color == "green":
            color_code = '\033[32m'
        elif color == "blue":
            color_code = '\033[34m'
        elif color == "red":
            color_code = '\033[31m'
        else:
            color_code = ''
        
        reset_code = '\033[0m'
        symbol_colored = color_code + symbol + reset_code

        # Обчислення максимального рядка фігури
        max_width = max(len("".join([symbol if val == 1 else " " for val in row])) for row in art)

        for row in art:
            line = "".join([symbol_colored if val == 1 else " " for val in row])
            line_len = len(line.replace(color_code, '').replace(reset_code, ''))  # Довжина без кольорових кодів

            # Вирівнювання рядків залежно від ширини терміналу
            if alignment == "center":
                padding = (terminal_width - line_len) // 2
                line = " " * padding + line
            elif alignment == "right":
                padding = terminal_width - line_len
                line = " " * padding + line
            elif alignment == "left":
                line = line.ljust(max_width)

            # Виведення результату
            print(line)

    except Exception as e:
        print(f"Непередбачена помилка під час виведення ASCII-арту: {e}")
