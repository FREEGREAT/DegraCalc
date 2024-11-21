from models.data_loader import DataLoader
from models.data_analysis import DataAnalysis
from views.line_chart import LineChart
from views.scatter_plot import ScatterPlot
from views.histogram import Histogram

class DataController:
    def __init__(self, file_path):
        self.data_loader = DataLoader(file_path)
        self.data = self.data_loader.load_data()
        if self.data.empty:
            print("Warning: The data is empty or could not be loaded correctly.")
        self.analysis = DataAnalysis(self.data)
    
    def display_extremes(self):
        extremes = self.analysis.get_extreme_values()
        for key, value in extremes.items():
            print(f'{key}: Min={value[0]}, Max={value[1]}')

    def get_plot_instance(self, plot_type):
        if plot_type == "line":
            return LineChart()
        elif plot_type == "scatter":
            return ScatterPlot()
        elif plot_type == "histogram":
            return Histogram()
        else:
            return None

    def plot_chart(self, plot_type):
        plot_instance = self.get_plot_instance(plot_type)
        if plot_instance:
            plot_instance.plot(self.data)  
            plot_instance.show() 
