from exceptions.art_errors import ArtGenerationError

def generate_triangle(size):
    """
    Генерує трикутник ASCII.
    
    :param size: Розмір трикутника.
    :return: Список, що представляє трикутник (матриця 1 і 0).
    """
    try:
        if size <= 0:
            raise ArtGenerationError("Розмір трикутника повинен бути додатнім числом.")
        return [[1 if j >= size//2 - i and j <= size//2 + i else 0 for j in range(size)] for i in range(size//2 + 1)]
    except Exception as e:
        raise ArtGenerationError(f"Помилка під час генерації трикутника: {e}")
