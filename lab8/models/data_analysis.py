"""
    Модуль для аналізу даних, який дозволяє отримувати екстремальні значення для різних параметрів.
"""
class DataAnalysis:
    """
    Клас для аналізу даних, який дозволяє отримувати екстремальні значення для різних параметрів.

    Атрибути:
    ----------
    data : pandas.DataFrame
        Дані, які передаються в клас у вигляді DataFrame з інформацією про температуру, 
        вологість, швидкість вітру та опади.

    Методи:
    --------
    get_extreme_values() :
        Обчислює та повертає екстремальні значення (мінімальні та максимальні) 
        для кількох параметрів: 'Temperature', 'Humidity', 'WindSpeed', 'Rainfall'.
    """

    def __init__(self, data):
        """
        Ініціалізує клас з наданими даними.

        Параметри:
        -----------
        data : pandas.DataFrame
            Дані для аналізу, що містять стовпці 'Temperature', 
            'Humidity', 'WindSpeed' та 'Rainfall'.
        """
        self.data = data

    def get_extreme_values(self):
        """
        Повертає мінімальні та максимальні значення для різних параметрів.

        Повертає:
        --------
        dict
            Словник з мінімальними та максимальними значеннями для параметрів: 'Temperature', 
            'Humidity', 'WindSpeed' та 'Rainfall'.
        """
        return {
            'Temperature': (self.data['Temperature'].min(), self.data['Temperature'].max()),
            'Humidity': (self.data['Humidity'].min(), self.data['Humidity'].max()),
            'WindSpeed': (self.data['WindSpeed'].min(), self.data['WindSpeed'].max()),
            'Rainfall': (self.data['Rainfall'].min(), self.data['Rainfall'].max())
        }
