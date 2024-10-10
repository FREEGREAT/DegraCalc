def save_art_to_file(art, file_name="ascii_art.txt"):
    """
    Зберігає згенеровану ASCII-фігуру у файл.
    
    :param art: Список списків, що представляють фігуру (матриця 1 і 0).
    :param file_name: Ім'я файлу для збереження фігури.
    """
    try:
        with open(file_name, 'w') as file:
            for row in art:
                line = "".join(['@' if val == 1 else ' ' for val in row])  # Створення рядка з матриці
                file.write(line + '\n')  # Запис рядка у файл
        print(f"Фігуру збережено у файл: {file_name}")
    except Exception as e:
        print(f"Помилка під час збереження у файл: {e}")
