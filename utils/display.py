from utils.clear import clear_console

def display_ascii_art(art, color="bw", symbol="@", alignment="left"):
    try:
        clear_console() 

        if color == "purple":
            symbol = '\033[35m' + symbol + '\033[0m'
        elif color == "green":
            symbol = '\033[32m' + symbol + '\033[0m'
        elif color == "blue":
            symbol = '\033[34m' + symbol + '\033[0m'
        elif color == "red":
            symbol = '\033[31m' + symbol + '\033[0m'

        max_width = len(art[0])  

        for row in art:
            line = "".join([symbol if val == 1 else " " for val in row])
            line_len = len(line)

            if alignment == "center":
                padding = (max_width - line_len) // 2
                line = " " * padding + line
            elif alignment == "right":
                padding = max_width - line_len
                line = " " * padding + line
            print(line)

    except Exception as e:
        print(f"Непередбачена помилка під час виведення ASCII-арту: {e}")
