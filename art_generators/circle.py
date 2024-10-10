from exceptions.art_errors import ArtGenerationError

def generate_circle(radius):
    """
    Генерує коло ASCII із заданим радіусом.
    
    :param radius: Радіус кола.
    :return: Список, що представляє коло (матриця 1 і 0).
    """
    try:
        if radius <= 0:
            raise ArtGenerationError("Радіус повинен бути додатнім числом.")
        return [[1 if (i - radius) ** 2 + (j - radius) ** 2 <= radius ** 2 else 0 for j in range(2*radius+1)] for i in range(2*radius+1)]
    except Exception as e:
        raise ArtGenerationError(f"Помилка під час генерації кола: {e}")
