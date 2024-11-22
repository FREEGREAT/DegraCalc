from exceptions.art_errors import ArtGenerationError

def generate_rectangle(width, height):
    """
    Генерує прямокутник ASCII із заданими шириною і висотою.
    
    :param width: Ширина прямокутника.
    :param height: Висота прямокутника.
    :return: Список, що представляє прямокутник (матриця 1 і 0).
    """
    try:
        if width <= 0 or height <= 0:
            raise ArtGenerationError("Ширина і висота повинні бути додатніми.")
        return [[1 if (i == 0 or i == height-1 or j == 0 or j == width-1) else 0 for j in range(width)] for i in range(height)]
    except Exception as e:
        raise ArtGenerationError(f"Помилка під час генерації прямокутника: {e}")
