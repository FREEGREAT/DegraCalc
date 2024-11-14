import matplotlib.pyplot as plt  # Add this line at the top of scatter_plot.py

from .base_plot import BasePlot

class Histogram(BasePlot):
    def plot(self, data):
        data['Humidity'].plot(kind='hist', bins=10)
        plt.title('Humidity Distribution')
        plt.xlabel('Humidity (%)')
        plt.ylabel('Frequency')
