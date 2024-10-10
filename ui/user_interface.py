def get_shape_choice():
    shape = input("Виберіть фігуру (квадрат/прямокутник/трикутник/ромб/коло): ").strip().lower()
    if shape not in ["квадрат", "прямокутник", "трикутник", "ромб", "коло"]:
        raise ValueError("Невірний тип фігури. Допустимі варіанти: квадрат, прямокутник, трикутник, ромб, коло.")
    return shape

def get_dimensions_for_rectangle():
    width = int(input("Введіть ширину прямокутника: "))
    height = int(input("Введіть висоту прямокутника: "))
    return width, height

def get_size_for_shape():
    size = int(input("Введіть розмір фігури: "))
    return size

def get_color_choice():
    color = input("Виберіть колір (purple/green/blue/red/bw): ").strip().lower()
    return color

def get_symbol_choice():
    symbol = input("Введіть символ для малювання (один символ): ").strip()
    return symbol

def get_alignment_choice():
    alignment = input("Виберіть вирівнювання (left/center/right): ").strip().lower()
    return alignment

def ask_to_continue():
    cont = input("Бажаєте створити ще одну фігуру? (так/ні): ").strip().lower()
    return cont == 'так'
