import matplotlib.pyplot as plt  

from .base_plot import BasePlot

class Histogram(BasePlot):
    def plot(self, data):
        data['Humidity'].plot(kind='hist', bins=10)
        plt.title('Humidity Distribution')
        plt.xlabel('Humidity (%)')
        plt.ylabel('Frequency')
