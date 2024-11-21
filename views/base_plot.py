import matplotlib.pyplot as plt
class BasePlot:
    def show(self):
        plt.show()  
        plt.close()  

    def save(self, filename, format="png"):
        plt.savefig(f"{filename}.{format}", format=format)
        plt.close()  

