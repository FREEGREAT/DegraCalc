# views/base_plot.py

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from mpld3 import save_html  # For HTML export

class BasePlot:
    def show(self):
        plt.show()

    def save(self, filename, format="png"):
        plt.savefig(f"{filename}.{format}", format=format)

    def save_as_html(self, filename):
        save_html(plt.gcf(), f"{filename}.html")
