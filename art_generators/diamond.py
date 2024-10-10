from exceptions.art_errors import ArtGenerationError

def generate_diamond(size):
    """
    Генерує ромб ASCII із заданим розміром.
    
    :param size: Розмір ромба.
    :return: Список, що представляє ромб (матриця 1 і 0).
    """
    try:
        if size <= 0:
            raise ArtGenerationError("Розмір ромба повинен бути додатнім числом.")
        return [[1 if abs(size//2 - i) + abs(size//2 - j) <= size//2 else 0 for j in range(size)] for i in range(size)]
    except Exception as e:
        raise ArtGenerationError(f"Помилка під час генерації ромба: {e}")
