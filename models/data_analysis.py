class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def get_extreme_values(self):
        return {
            'Temperature': (self.data['Temperature'].min(), self.data['Temperature'].max()),
            'Humidity': (self.data['Humidity'].min(), self.data['Humidity'].max()),
            'WindSpeed': (self.data['WindSpeed'].min(), self.data['WindSpeed'].max()),
            'Rainfall': (self.data['Rainfall'].min(), self.data['Rainfall'].max())
        }
