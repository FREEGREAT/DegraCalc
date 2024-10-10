import pyfiglet

class AsciiArtGenerator:
    def __init__(self, text, font='slant', symbol='*'):
        self.text = text
        self.font = font
        self.symbol = symbol

    def generate_ascii_art(self):
        try:
            ascii_art = pyfiglet.figlet_format(self.text, font=self.font)
            return ascii_art.replace('*', self.symbol)
        except Exception as e:
            raise ValueError("Помилка генерації ASCII-арту: " + str(e))

    def available_fonts(self):
        return pyfiglet.FigletFont.getFonts()
