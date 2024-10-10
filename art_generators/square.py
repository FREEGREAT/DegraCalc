from exceptions.art_errors import ArtGenerationError

def generate_square(size):
    """
    Генерує квадрат ASCII із заданим розміром.
    
    :param size: Розмір квадрата.
    :return: Список, що представляє квадрат (матриця 1 і 0).
    """
    try:
        if size <= 0:
            raise ArtGenerationError("Розмір квадрата повинен бути додатнім числом.")
        return [[1 if (i == 0 or i == size-1 or j == 0 or j == size-1) else 0 for j in range(size)] for i in range(size)]
    except Exception as e:
        raise ArtGenerationError(f"Помилка під час генерації квадрата: {e}")
