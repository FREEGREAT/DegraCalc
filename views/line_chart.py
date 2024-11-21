import matplotlib.pyplot as plt
from .base_plot import BasePlot

class LineChart(BasePlot):
    def plot(self, data):
        if data.empty:
            print("No data available to plot.")
            return
        plt.figure()  
        data.plot(x='Date', y='Temperature', kind='line')
        plt.title('Temperature Over Time')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
