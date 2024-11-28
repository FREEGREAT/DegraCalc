import matplotlib.pyplot as plt  

from .base_plot import BasePlot

class ScatterPlot(BasePlot):
    def plot(self, data):
        data.plot.scatter(x='Temperature', y='Humidity')
        plt.title('Temperature vs Humidity')
        plt.xlabel('Temperature (°C)')
        plt.ylabel('Humidity (%)')