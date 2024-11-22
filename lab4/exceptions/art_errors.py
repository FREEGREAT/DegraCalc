class ArtGenerationError(Exception):
    """
    Виняток, який використовується для позначення помилок під час генерації ASCII-фігур.

    Атрибути:
        message (str): Повідомлення про помилку. За замовчуванням: "Помилка під час генерації фігури ASCII".

    Методи:
        __str__(): Повертає текстове представлення помилки.
    """

    def __init__(self, message="Помилка під час генерації фігури ASCII"):
        """
        Ініціалізує об'єкт ArtGenerationError.

        Параметри:
            message (str): Опис помилки.
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Повертає текстове представлення помилки.

        Повертає:
            str: Повідомлення про помилку у форматі "ArtGenerationError: <message>".
        """
        return f'ArtGenerationError: {self.message}'
