class ArtGenerationError(Exception):
    
    def __init__(self, message="Помилка під час генерації фігури ASCII"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'ArtGenerationError: {self.message}'
