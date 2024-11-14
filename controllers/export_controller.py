class ExportController:
    def export_plot(self, plot_instance, filename, format="png"):
        plot_instance.save(filename, format)
    
    def export_as_html(self, plot_instance, filename):
        plot_instance.save_as_html(filename)
    
    def prompt_and_export(self, plot_instance, filename_base, format="png"):
        save_choice = input("Do you want to save this chart? (y/n): ")
        if save_choice.lower() == 'y':
            filename = f"{filename_base}.{format}"
            self.export_plot(plot_instance, filename, format)
            print(f"Chart saved as {filename}.")
