from controllers.data_controller import DataController
from views.subplots import plot_multiple_subplots

def display_menu():
    print("1. Display extreme values")
    print("2. Show Temperature Line Chart")
    print("3. Show Temperature vs Humidity Scatter Plot")
    print("4. Show Humidity Histogram")
    print("5. Show Multiple Subplots")
    print("6. Export Chart as PNG")

def handle_choice(choice, controller):
    if choice == '1':
        controller.display_extremes()
    elif choice == '2':
        controller.plot_chart("line") 
    elif choice == '3':
        controller.plot_chart("scatter")  
    elif choice == '4':
        controller.plot_chart("histogram")  
    elif choice == '5':
        from views.subplots import plot_multiple_subplots
        plot_multiple_subplots(controller.data)
    elif choice == '6':
        export_chart_as_png(controller) 
    else:
        print("Invalid choice")


def export_chart_as_png(controller):
    plot_type = input("Enter the type of chart to export (line, scatter, histogram): ").lower()
    plot_instance = controller.get_plot_instance(plot_type)
    
    if plot_instance:
        filename = input("Enter the filename (without extension): ")
        print("Exporting chart as PNG...")
        plot_instance.plot(controller.data)  
        plot_instance.save(filename, format="png")
        print(f"Chart exported as {filename}.png")
    else:
        print("Invalid chart type. Please try again.")
