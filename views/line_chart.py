import matplotlib.pyplot as plt  # Add this line at the top of scatter_plot.py

from .base_plot import BasePlot

class LineChart(BasePlot):
    def plot(self, data):
        data.plot(x='Date', y='Temperature', kind='line')
        plt.title('Temperature Over Time')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
